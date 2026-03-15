# Doctor Role API Documentation

This document outlines the primary API endpoints used by the **Doctor** role within the DentConsent platform, including example `curl` commands.

> [!NOTE]
> All endpoints assume the base URL is `http://localhost:8000/api` (or your specific backend host).

---

## 1. Authentication

### Login
Doctors use this to authenticate and retrieve their profile data.

```bash
curl -X POST http://localhost:8000/api/login \
     -H "Content-Type: application/json" \
     -d '{
       "email": "doctor@example.com",
       "password": "securepassword123"
     }'
```

---

## 2. Patient & Treatment Management

### Get Doctor's Treatments
Retrieves all treatments associated with the logged-in doctor. This is the endpoint the web app should use to build the doctor's consent report list.

```bash
curl -X GET "http://localhost:8000/api/get_treatments?user_id=123&role=doctor"
```

Frontend usage:

```js
const res = await Auth.apiCall(`get_treatments?user_id=${currentUser.id}&role=doctor`);

const treatments = Array.isArray(res.data)
  ? res.data
  : Array.isArray(res.data?.treatments)
    ? res.data.treatments
    : [];

const consentReports = treatments.filter((treatment) => {
  const status = (treatment.status || '').toLowerCase();
  return !!treatment.consent_pdf_url || status === 'completed' || status === 'consent_signed' || status === 'signed';
});
```

Notes:

- Required query params: `user_id`, `role=doctor`
- Use the returned treatment list as the doctor report source
- Treat any item with `consent_pdf_url` or a signed/completed status as a consent report entry

### Create New Treatment
Assigns a procedure to a specific patient.

```bash
curl -X POST http://localhost:8000/api/create_treatment \
     -H "Content-Type: application/json" \
     -d '{
       "doctor_id": 123,
       "patient_id": 456,
       "operation_type_id": 1,
       "clinical_notes": "Patient requires localized anesthesia.",
       "anesthesia_required": true
     }'
```

### Update Treatment
Modifies clinical notes or requirements for an existing treatment.

```bash
curl -X POST http://localhost:8000/api/update_treatment \
     -H "Content-Type: application/json" \
     -d '{
       "treatment_id": 789,
       "clinical_notes": "Updated: Patient also has minor gingivitis.",
       "anesthesia_required": true
     }'
```

### Delete Treatment
Removes a treatment record.

```bash
curl -X POST http://localhost:8000/api/delete_treatment \
     -H "Content-Type: application/json" \
     -d '{
       "treatment_id": 789
     }'
```

---

## 3. Clinical Procedures

### Get Operation Types
Fetch all available specializations and their respective procedures.

```bash
curl -X GET http://localhost:8000/api/get_operation_types
```

### Create Custom Treatment (Procedure)
Allows a doctor to define a new procedure type with educational content, risks, and verification quizzes. This endpoint accepts `multipart/form-data` to handle optional video uploads.

```bash
curl -X POST http://localhost:8000/api/create_custom_treatment \
     -F 'data={
       "specialization_id": 1,
       "name": "Advanced Dental Implant",
       "description": "Premium implant procedure with 3D mapping.",
       "success_rate": 99.5,
       "procedure_steps": [
         {"title": "Initial Scan", "description": "3D imaging of the jaw."},
         {"title": "Placement", "description": "Surgical insertion of the post."}
       ],
       "risks": [
         {"title": "Minor Swelling", "description": "Expected for 2-3 days.", "risk_percentage": 5}
       ],
       "quizzes": [
         {
           "language": "en",
           "question_text": "How long does the scan take?",
           "options": ["5 mins", "1 hour", "1 day"],
           "correct_option_index": 0
         }
       ]
     }' \
     -F 'video=@/path/to/intro_video.mp4'
```

---

## 4. Consent & Clinical Records

### View Signed Consent (PDF)
Fetches the generated PDF for a completed treatment.

```bash
curl -X GET http://localhost:8000/api/serve_consent_pdf.php?treatment_id=789 \
     --output signed_consent.pdf
```
