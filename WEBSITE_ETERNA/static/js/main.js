let navbar = document.querySelector('.header .flex .navbar');
let profile = document.querySelector('.header .flex .profile');

// Add smooth transition for navbar and profile
navbar.style.transition = 'all 0.3s ease';
profile.style.transition = 'all 0.3s ease';

document.querySelector('#menu-btn').onclick = () =>{
  navbar.classList.toggle('active');
  profile.classList.remove('active');
}

document.querySelector('#user-btn').onclick = () =>{
  profile.classList.toggle('active');
  navbar.classList.remove('active');
}

window.onscroll = () =>{
  navbar.classList.remove('active');
  profile.classList.remove('active');
}

let mainImage = document.querySelector('.quick-view .box .row .image-container .main-image img');
let subImages = document.querySelectorAll('.quick-view .box .row .image-container .sub-image img');

// Add fade effect for image switching
subImages.forEach(images =>{
  images.onclick = () =>{
    mainImage.style.opacity = 0;
    setTimeout(() => {
        src = images.getAttribute('src');
        mainImage.src = src;
        mainImage.style.opacity = 1;
    }, 300);
  }
});