// Show back-to-top button on scroll
window.onscroll = function () {
    const backToTop = document.querySelector('.back-to-top');
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        backToTop.style.display = "flex";
    } else {
        backToTop.style.display = "none";
    }
};

// Smooth scroll for navigation and back-to-top button
document.querySelectorAll("a[href^='#']").forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});
