(function () {
    if (window.showToast) return;

    let container = null;

    function ensureContainer() {
        if (container) return container;

        const style = document.createElement('style');
        style.textContent = `
            .dc-toast-wrap {
                position: fixed;
                right: 16px;
                top: 16px;
                z-index: 10000;
                display: flex;
                flex-direction: column;
                gap: 10px;
                max-width: min(92vw, 420px);
            }
            .dc-toast {
                display: flex;
                align-items: center;
                gap: 10px;
                padding: 12px 14px;
                border-radius: 12px;
                border: 1px solid rgba(0, 0, 0, 0.08);
                background: #ffffff;
                color: #1c1c1e;
                font-family: 'Plus Jakarta Sans', sans-serif;
                font-size: 13px;
                line-height: 1.45;
                box-shadow: 0 10px 24px rgba(0, 0, 0, 0.12);
                transform: translateY(-8px);
                opacity: 0;
                animation: dcToastIn 200ms ease forwards;
            }
            .dc-toast--success { border-left: 4px solid #30b55a; }
            .dc-toast--error { border-left: 4px solid #ff453a; }
            .dc-toast--warning { border-left: 4px solid #ff9f0a; }
            .dc-toast--info { border-left: 4px solid #0a84ff; }
            .dc-toast__dot {
                width: 8px;
                height: 8px;
                border-radius: 50%;
                flex-shrink: 0;
                background: currentColor;
            }
            .dc-toast--success .dc-toast__dot { color: #30b55a; }
            .dc-toast--error .dc-toast__dot { color: #ff453a; }
            .dc-toast--warning .dc-toast__dot { color: #ff9f0a; }
            .dc-toast--info .dc-toast__dot { color: #0a84ff; }
            .dc-toast--exit {
                animation: dcToastOut 180ms ease forwards;
            }
            @keyframes dcToastIn {
                to { transform: translateY(0); opacity: 1; }
            }
            @keyframes dcToastOut {
                to { transform: translateY(-6px); opacity: 0; }
            }
        `;
        document.head.appendChild(style);

        container = document.createElement('div');
        container.className = 'dc-toast-wrap';
        document.body.appendChild(container);
        return container;
    }

    window.showToast = function (message, type = 'info', duration = 3000) {
        const host = ensureContainer();
        const toast = document.createElement('div');
        const safeType = ['success', 'error', 'warning', 'info'].includes(type) ? type : 'info';

        toast.className = `dc-toast dc-toast--${safeType}`;
        toast.innerHTML = `<span class="dc-toast__dot"></span><span>${String(message || '')}</span>`;
        host.appendChild(toast);

        const dismiss = () => {
            toast.classList.add('dc-toast--exit');
            setTimeout(() => toast.remove(), 180);
        };

        const timeout = setTimeout(dismiss, Math.max(1500, duration));
        toast.addEventListener('click', () => {
            clearTimeout(timeout);
            dismiss();
        });
    };
})();