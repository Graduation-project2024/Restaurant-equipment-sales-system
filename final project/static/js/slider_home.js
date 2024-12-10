// خاص بتمرير الاعلان
var swiper = new Swiper(".home-slider", {
  loop:true,
  spaceBetween: 20,
    pagination: {
    el: ".swiper-pagination",
    clickable:true,
    },
  });

// خاص بتمرير التصنيفات
var swiper = new Swiper(".category-slider", {
  loop:true,
  spaceBetween: 20,
  pagination: {
  el: ".swiper-pagination",
  clickable:true,
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
  var swiper = new Swiper(".products-slider", {
loop:true,
spaceBetween: 20,
pagination: {
  el: ".swiper-pagination",
  clickable:true,
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