// خاص بتمرير الاعلان
var homeSlider = new Swiper(".home-slider", {
  loop: true,
  spaceBetween: 20,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  autoplay: {
    delay: 3500,
    disableOnInteraction: false,
  }
});

// خاص بتمرير التصنيفات
var categorySlider = new Swiper(".category-slider", {
  loop: true,
  spaceBetween: 20,
  pagination: {
  el: ".swiper-pagination",
  clickable: true,
},
breakpoints: {
  0: {
    slidesPerView: 2,
  },
    650: {
  slidesPerView: 3,
  },
  768: {
  slidesPerView: 4,
  },
  1024: {
  slidesPerView: 5,
  },
},
});

// خاص بتمرير الاصناف
var productsSlider = new Swiper(".products-slider", {
loop: true,
spaceBetween: 20,
pagination: {
  el: ".swiper-pagination",
  clickable: true,
},
  breakpoints: {
550: {
  slidesPerView: 2,
  },
  768: {
  slidesPerView: 2,
  },
  1024: {
  slidesPerView: 3,
},
},
});
