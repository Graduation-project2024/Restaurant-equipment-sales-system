var swiper = new Swiper(".reviews-slider", {
    loop:true,
    spaceBetween: 20,
    pagination: {
       el: ".swiper-pagination",
       clickable:true,
    },
    breakpoints: {
       0: {
          slidesPerView:1,
       },
       768: {
          slidesPerView: 2,
       },
       991: {
          slidesPerView: 3,
       },
    },
 });