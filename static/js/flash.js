// script to hide the login status message after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const msg = document.getElementById('login-status');
    if (msg) {
        setTimeout(() => {
            msg.classList.add("flash-hide");
            setTimeout(() => msg.remove(), 1000);
        }, 5000);
    }
});

// script to hide the logout status message after 20 seconds
document.addEventListener('DOMContentLoaded', function() {
    const msg = document.getElementById('logout-status');
    if (msg) {
        setTimeout(() => {
            msg.classList.add("flash-hide");
            setTimeout(() => msg.remove(), 1000);
        }, 5000);
    }
});
