document.addEventListener("DOMContentLoaded", () => {
    const dismissToast = (toast) => {
        if (!toast || toast.classList.contains("is-dismissing")) return;
        toast.classList.add("is-dismissing");
        window.setTimeout(() => toast.remove(), 260);
    };

    document.querySelectorAll(".toast").forEach((toast) => {
        toast.querySelector(".toast-close")?.addEventListener("click", () => {
            dismissToast(toast);
        });

        if (toast.dataset.autohide === "true") {
            window.setTimeout(() => dismissToast(toast), 5000);
        }
    });
});
