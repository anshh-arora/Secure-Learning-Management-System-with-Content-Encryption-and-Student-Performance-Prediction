//-- ----- Swiper JS ----- -
var swiper = new Swiper(".mySwiper", {
  slidesPerView: 2,
  grabCursor: true,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});

//-- ----- Scroll Reveal JS ----- -
ScrollReveal().reveal('#courses', { delay: 200 });
ScrollReveal().reveal('#features', { delay: 200 });
ScrollReveal().reveal('#reviews', { delay: 200 });
