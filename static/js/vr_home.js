window.onload = function () {
  window.addEventListener("scroll", function (e) {
    let s = this.scrollY;
    let w = this.outerWidth;
    let h = document.getElementsByClassName("paralax")[0].clientWidth;
    let h_b = document.getElementsByClassName("container")[0].clientWidth;
    let p = (s / h) * 100;
    let p_b = (s / h_b) * 100;
    let opas = 1 - (1 / 100) * p_b;
    let z_1 = 1 + (w / 10000) * p_b;


    document.getElementsByClassName(
      "p-item4"
    )[0].style = `transform: scale(${z_1});opacity: ${opas}`;


    let z_2 = 1 + (w / 5000000) * p;


    document.getElementsByClassName(
      "p-item1"
    )[0].style = `transform: scale(${z_2})`;


    let hr = (w / 2000) * p_b;
    let z_3 = 1 + w * 0.000005 * p_b;


    document.getElementsByClassName(
      "p-item2"
    )[0].style = `transform: translate3d(${hr}px,0,0) scale(${z_3})`;


    let hr_2 = (w / 1500) * p_b;
    let z_4 = 1 + w * 0.00001 * p_b;
    document.getElementsByClassName(
      "p-item3"
    )[0].style = `transform: translate3d(${hr_2}px,0,0) scale(${z_4})`;
  });
};










const imgSlider = document.querySelector(".img-slider");
const imgFruits = document.querySelectorAll(".img-item.fruit");
const infoSlider = document.querySelector(".info-slider");
const infoItems = document.querySelectorAll(".info-item");
const bgs = document.querySelectorAll(".bg");
const carousel = document.querySelector(".carousel");

const nextBtn = document.querySelector(".next-btn");
const prevBtn = document.querySelector(".prev-btn");

let index = 0;
let direction = 0;

function updateActiveItems() {
  imgFruits.forEach((item, i) => {
    item.classList.toggle("active", i === index);
  });

  bgs.forEach((bg, i) => {
    bg.classList.toggle("active", i === index);
  });

  infoItems.forEach((item, i) => {
    if (i === index) {
      item.style.opacity = 0;
      item.style.display = "flex";

      item.offsetHeight;
      item.style.transition = "opacity 0.5s ease-in-out";
      item.style.opacity = 1;
    } else {
      item.style.opacity = 0;
      setTimeout(() => {
        item.style.display = "none";
      }, 500);
    }
  });

  const activeBg = bgs[index];
  const activeBgStyle = getComputedStyle(activeBg);
  carousel.style.backgroundImage = activeBgStyle.backgroundImage;
}

function handleTransition() {
  const infoSlider = document.querySelector('.info-slider'); // Assuming you need to select the slider element

  // Set the transition and transform styles
  infoSlider.style.transition = "transform 0.5s cubic-bezier(0.645, 0.045, 0.355, 1)";
  infoSlider.style.transform = `translateY(${direction * 25}%)`;

  // Reset the transition and transform styles after the transition ends
  setTimeout(() => {
    infoSlider.style.transition = "none";
    infoSlider.style.transform = "translateY(0%)";
  }, 500);
}


function updateCarousel() {
  const imgSlider = document.querySelector('.img-slider'); // Assuming you need to select the imgSlider element

  // Apply the rotation and update styles
  imgSlider.style.transform = `rotate(${index * -90}deg)`;

  // Call other functions to update the carousel
  updateActiveItems();
  handleTransition();
}


function changeIndex(step) {
  index += step;
  if (index < 0) {
    index = imgFruits.length - 1;
  } else if (index >= imgFruits.length) {
    index = 0;
  }

  updateCarousel();
}

nextBtn.addEventListener("click", () => {
  changeIndex(1);
});

prevBtn.addEventListener("click", () => {
  changeIndex(-1);
});

updateCarousel();

infoSlider.addEventListener("transitionend", () => {
  if (direction === -1) {
    infoSlider.appendChild(infoSlider.firstElementChild);
  } else if (direction === 1) {
    infoSlider.prepend(infoSlider.lastElementChild);
  }
});
