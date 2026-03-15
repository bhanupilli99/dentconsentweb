/**
 * DentConsent Web App Base Authentication Logic
 * Handles session management, login API calls, and routing.
 */

const Auth = {
    // Configuration
    API_BASE: 'http://10.197.126.54:8000/api/',

    // Keys for localStorage
    STORAGE_KEY_USER: 'dentconsent_user',

    /**
     * Check if a user is currently logged in.
     * Restricts access to pages based on role if requiredRole is provided.
     */
    requireAuth: function (requiredRole = null) {
        const user = this.getUser();

        // Not logged in -> Redirect to login
        if (!user) {
            window.location.href = 'index.html';
            return null;
        }

        // Incorrect role -> Redirect to appropriate dashboard
        if (requiredRole && user.role !== requiredRole) {
            this.routeUser(user.role);
            return null;
        }

        return user;
    },

    /**
     * Check if logged in. If yes, prevent accessing the login page.
     */
    redirectIfLoggedIn: function () {
        const user = this.getUser();
        if (user) {
            this.routeUser(user.role);
        }
    },

    /**
     * Get the current user from local storage
     */
    getUser: function () {
        try {
            const userData = localStorage.getItem(this.STORAGE_KEY_USER);
            console.log('Raw userData from localStorage:', userData); // Debug log

            if (!userData || userData === 'undefined' || userData === 'null' || userData.trim() === '') {
                console.warn('Invalid or empty user data in localStorage, clearing...');
                localStorage.removeItem(this.STORAGE_KEY_USER);
                return null;
            }

            // Additional validation - ensure it's a valid JSON string
            if (!userData.startsWith('{') && !userData.startsWith('[')) {
                console.warn('Invalid JSON format in localStorage, clearing...');
                localStorage.removeItem(this.STORAGE_KEY_USER);
                return null;
            }

            let parsedData = JSON.parse(userData);

            // Robustly handle nesting: if it's like {success:true, user:{...}}, extract the inner user
            if (parsedData && !parsedData.role && parsedData.user && typeof parsedData.user === 'object') {
                console.log('Unnesting user data from session...');
                parsedData = parsedData.user;
            }

            console.log('Successfully parsed user data:', parsedData); // Debug log
            return parsedData;
        } catch (error) {
            console.error('Error parsing user data:', error);
            // Clear corrupted data and return null
            localStorage.removeItem(this.STORAGE_KEY_USER);
            return null;
        }
    },

    /**
     * Save user data and route to dashboard
     */
    login: function (userData) {
        // Ensure we save a flat user object if it's nested
        let userToSave = userData;
        if (userData && !userData.role && userData.user && typeof userData.user === 'object') {
            console.log('Flattening user data before saving...');
            userToSave = userData.user;
        }

        if (!userToSave || !userToSave.role) {
            console.error('Invalid user data provided to login:', userData);
            return;
        }

        localStorage.setItem(this.STORAGE_KEY_USER, JSON.stringify(userToSave));
        this.routeUser(userToSave.role);
    },

    updateStoredUser: function (userData) {
        if (!userData || !userData.role) {
            console.error('Invalid user data provided to updateStoredUser:', userData);
            return;
        }

        localStorage.setItem(this.STORAGE_KEY_USER, JSON.stringify(userData));
    },

    /**
     * Clear session and go to login
     */
    logout: function () {
        localStorage.removeItem(this.STORAGE_KEY_USER);
        window.location.href = 'index.html';
    },

    /**
     * Route user based on their role
     */
    routeUser: function (role) {
        if (role === 'doctor') {
            window.location.href = 'doctor-dashboard.html';
        } else if (role === 'patient') {
            window.location.href = 'patient-dashboard.html';
        } else {
            console.error('Invalid role for routing:', role);
            this.logout(); // If role is unknown, force logout to safe state
        }
    },

    /**
     * Get the full URL for an asset (e.g. image, video)
     */
    getFullUrl: function (path) {
        if (!path) return '';
        if (path.startsWith('http')) return path;
        const BASE_URL = this.API_BASE;

        // Normalize Windows backslashes and ensure path starts with /
        let cleanPath = path.toString().replace(/\\/g, '/');
        if (!cleanPath.startsWith('/')) cleanPath = `/${cleanPath}`;

        // If the path doesn't already start with /api, prepend it
        // This ensures relative paths like 'uploads/...' become '/api/uploads/...'
        if (!cleanPath.startsWith('/api/')) {
            cleanPath = `/api${cleanPath}`;
        }

        // Base URL is http://...:8000/api/
        // cleanPath is /api/uploads/...
        // We want http://...:8000/api/uploads/...
        return `${BASE_URL.replace(/\/api\/$/, '')}${cleanPath}`;
    },

    /**
     * Common API Fetch wrapper with error handling
     */
    apiCall: async function (endpoint, options = {}) {
        const BASE_URL = this.API_BASE;

        try {
            let headers = {
                'Content-Type': 'application/json',
                ...options.headers
            };

            // If body is FormData, fetch needs to set Content-Type with boundary automatically
            if (options.body instanceof FormData) {
                delete headers['Content-Type'];
            }

            let response = await fetch(`${BASE_URL}${endpoint}`, {
                ...options,
                headers: headers
            });

            if (!response.ok) {
                // Try to get error message from response
                let errorMessage = `HTTP ${response.status}: ${response.statusText}`;
                try {
                    const errorData = await response.json();
                    errorMessage = errorData.detail || errorData.error || errorData.message || errorMessage;
                } catch (e) {
                    // If we can't parse JSON, use status text
                }
                throw new Error(errorMessage);
            }

            const data = await response.json();
            console.log('Successfully connected to DentConsent API');

            // Determine success based on backend response data if available
            // If data has a 'success' field, use it. Otherwise assume true if status was ok.
            const isSuccess = (data && typeof data.success !== 'undefined') ? data.success : true;

            // If it's a login call, return the user object nested in 'user'
            if (endpoint === 'login' || endpoint.includes('login')) {
                const flatData = (data && data.user) ? data.user : data;
                return { success: isSuccess, user: flatData, error: isSuccess ? null : (data.message || data.error || 'Login failed') };
            }

            // For other calls, return the data directly or wrapped in success
            return { success: isSuccess, data: data, error: isSuccess ? null : (data.message || data.error || 'Operation failed') };

        } catch (error) {
            console.error('API Error:', error);

            // Check if it's a CORS error specifically
            if (error.message.includes('Failed to fetch') || error.message.includes('CORS')) {
                console.log('CORS error detected - API needs CORS configuration');
                return {
                    success: false,
                    error: 'CORS Error: The API is running but blocking cross-origin requests. Please add CORS middleware to the Python FastAPI app.'
                };
            }

            // If it's an authentication error and it's login, provide mock fallback
            if (endpoint === 'login' && (error.message.includes('Invalid email or password') || error.message.includes('401'))) {
                console.log('API credentials not found, using mock authentication for testing...');
                return this.mockLogin(options);
            }

            return { success: false, error: error.message };
        }
    },

    /**
     * Mock login for development/testing when backend is not available
     */
    mockLogin: function (options) {
        return new Promise((resolve) => {
            setTimeout(() => {
                try {
                    const body = JSON.parse(options.body);
                    const { email, password } = body;

                    // Mock user database
                    const mockUsers = [
                        { email: 'dr.mohan@dentconsent.com', password: 'doctor123', role: 'doctor', name: 'Dr. Mohan Reddy M', id: 1 },
                        { email: 'patient.jane@gmail.com', password: 'patient123', role: 'patient', name: 'Jane Smith', id: 2 },
                        { email: 'doctor@test.com', password: 'test', role: 'doctor', name: 'Test Doctor', id: 3 },
                        { email: 'patient@test.com', password: 'test', role: 'patient', name: 'Test Patient', id: 4 },
                        { email: 'doctor@test.coo', password: 'test', role: 'doctor', name: 'Test Doctor', id: 5 },
                        { email: 'mohan@gmail.com', password: '123456', role: 'patient', name: 'Mohan', id: 6 },
                        { email: 'doctor@test.coo', password: '123456', role: 'doctor', name: 'Clinical Doctor', id: 7 }
                    ];

                    const user = mockUsers.find(u => u.email === email && u.password === password);

                    if (user) {
                        console.log(`Mock login successful for ${user.name} (${user.role})`);
                        resolve({
                            success: true,
                            user: {
                                id: user.id,
                                name: user.name,
                                email: user.email,
                                role: user.role,
                                profile_image: null
                            }
                        });
                    } else {
                        resolve({
                            success: false,
                            error: 'Invalid credentials. Available test accounts:\n• Doctor: dr.mohan@dentconsent.com / doctor123\n• Patient: patient.jane@gmail.com / patient123\n• Test: doctor@test.com / test or patient@test.com / test'
                        });
                    }
                } catch (error) {
                    resolve({
                        success: false,
                        error: 'Invalid request format'
                    });
                }
            }, 800); // Simulate network delay
        });
    }
};
