// const imgSlider = document.querySelector(".img-slider");
// const imgFruits = document.querySelectorAll(".img-item.fruit");
// const infoSlider = document.querySelector(".info-slider");
// const infoItems = document.querySelectorAll(".info-item");
// const bgs = document.querySelectorAll(".bg");
// const carousel = document.querySelector(".carousel");

// const nextBtn = document.querySelector(".next-btn");
// const prevBtn = document.querySelector(".prev-btn");
// let currentSlide = 0;
// let index =0;
// const slides = document.querySelectorAll('.img-item.fruit');
// const totalSlides = slides.length;

// document.querySelector('.next-btn').addEventListener('click', () => {
//     changeSlide(1);
// });

// document.querySelector('.prev-btn').addEventListener('click', () => {
//     changeSlide(-1);
// });

// function changeSlide(direction) {
//     slides[currentSlide].classList.remove('active');
//     currentSlide = (currentSlide + direction + totalSlides) % totalSlides;
//     slides[currentSlide].classList.add('active');
// }


// let index = 0;
// let direction = 0;

// function updateActiveItems() {
//   imgFruits.forEach((item, i) => {
//     item.classList.toggle("active", i === index);
//   });

//   bgs.forEach((bg, i) => {
//     bg.classList.toggle("active", i === index);
//   });

//   infoItems.forEach((item, i) => {
//     if (i === index) {
//       item.style.opacity = 0;
//       item.style.display = "flex";

//       item.offsetHeight;
//       item.style.transition = "opacity 0.5s ease-in-out";
//       item.style.opacity = 1;
//     } else {
//       item.style.opacity = 0;
//       setTimeout(() => {
//         item.style.display = "none";
//       }, 500);
//     }
//   });

//   const activeBg = bgs[index];
//   const activeBgStyle = getComputedStyle(activeBg);
//   carousel.style.backgroundImage = activeBgStyle.backgroundImage;
// }

// function handleTransition() {
//   infoSlider.style.transition =
//     "transform 0.5s cubic-bezier(0.645, 0.045, 0.355, 1)";
//   infoSlider.style.transform = `translateY(${direction * 25}%)`;

//   setTimeout(() => {
//     infoSlider.style.transition = "none";
//     infoSlider.style.transform = "translateY(0%)";
//   }, 500);
// }

// function updateCarousel() {
//   imgSlider.style.transform = `rotate(${index * -90}deg)`;
//   updateActiveItems();
//   handleTransition();
// }

// function changeIndex(step) {
//   index += step;
//   if (index < 0) {
//     index = imgFruits.length - 1;
//   } else if (index >= imgFruits.length) {
//     index = 0;
//   }

//   updateCarousel();
// }

// nextBtn.addEventListener("click", () => {
//   changeIndex(1);
// });

// prevBtn.addEventListener("click", () => {
//   changeIndex(-1);
// });

// updateCarousel();

// infoSlider.addEventListener("transitionend", () => {
//   if (direction === -1) {
//     infoSlider.appendChild(infoSlider.firstElementChild);
//   } else if (direction === 1) {
//     infoSlider.prepend(infoSlider.lastElementChild);
//   }
// });




// Function to update the slide position
function updateSliderPosition() {
  const sliderWidth = imgFruits[0].clientWidth;
  imgSlider.style.transform = `translateX(${-currentSlide * sliderWidth}px)`;
}

// Event listener for next button
nextBtn.addEventListener('click', () => {
  currentSlide = (currentSlide + 1) % totalSlides; // Loop back to the first slide
  updateSliderPosition();
});

// Event listener for previous button
prevBtn.addEventListener('click', () => {
  currentSlide = (currentSlide - 1 + totalSlides) % totalSlides; // Loop to the last slide
  updateSliderPosition();
});

// Initial setup
updateSliderPosition();


const imgSlider = document.querySelector(".img-slider");
const imgFruits = document.querySelectorAll(".img-item.fruit");
const infoSlider = document.querySelector(".info-slider");
const infoItems = document.querySelectorAll(".info-item");
const bgs = document.querySelectorAll(".bg");
const carousel = document.querySelector(".carousel");

const nextBtn = document.querySelector(".next-btn");
const prevBtn = document.querySelector(".prev-btn");
let currentSlide = 0;
let index = 0;
const totalSlides = imgFruits.length;

// Consolidate both changeSlide and changeIndex into one function
function changeSlide(step) {
  currentSlide = (currentSlide + step + totalSlides) % totalSlides;
  index = currentSlide;
  updateCarousel(step);
}

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

      // Trigger reflow for transition
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

function handleTransition(step) {
  const direction = step > 0 ? -1 : 1; // Adjust direction based on step
  infoSlider.style.transition = "transform 0.5s cubic-bezier(0.645, 0.045, 0.355, 1)";
  infoSlider.style.transform = `translateY(${direction * 25}%)`;

  setTimeout(() => {
    infoSlider.style.transition = "none";
    infoSlider.style.transform = "translateY(0%)";
  }, 500);
}

function updateCarousel(step) {
  imgSlider.style.transform = `rotate(${index * -90}deg)`; // Rotate the slider for visual effect
  updateActiveItems();
  handleTransition(step);
}

// Event listeners for buttons
nextBtn.addEventListener("click", () => {
  changeSlide(1);
});

prevBtn.addEventListener("click", () => {
  changeSlide(-1);
});

// Initialize the carousel
updateCarousel(0);

infoSlider.addEventListener("transitionend", () => {
  if (direction === -1) {
    infoSlider.appendChild(infoSlider.firstElementChild);
  } else if (direction === 1) {
    infoSlider.prepend(infoSlider.lastElementChild);
  }
});






// const imgSlider = document.querySelector(".img-slider");
// const imgFruits = document.querySelectorAll(".img-item.fruit");
// const infoSlider = document.querySelector(".info-slider");
// const infoItems = document.querySelectorAll(".info-item");
// const bgs = document.querySelectorAll(".bg");
// const carousel = document.querySelector(".carousel");

// const nextBtn = document.querySelector(".next-btn");
// const prevBtn = document.querySelector(".prev-btn");

// let index = 0;
// let direction = 0;

// function updateActiveItems() {
//   imgFruits.forEach((item, i) => {
//     item.classList.toggle("active", i === index);
//   });

//   bgs.forEach((bg, i) => {
//     bg.classList.toggle("active", i === index);
//   });

//   infoItems.forEach((item, i) => {
//     if (i === index) {
//       item.style.opacity = 0;
//       item.style.display = "flex";

//       item.offsetHeight;
//       item.style.transition = "opacity 0.5s ease-in-out";
//       item.style.opacity = 1;
//     } else {
//       item.style.opacity = 0;
//       setTimeout(() => {
//         item.style.display = "none";
//       }, 500);
//     }
//   });

//   const activeBg = bgs[index];
//   const activeBgStyle = getComputedStyle(activeBg);
//   carousel.style.backgroundImage = activeBgStyle.backgroundImage;
// }

// function handleTransition() {
//   infoSlider.style.transition =
//     "transform 0.5s cubic-bezier(0.645, 0.045, 0.355, 1)";
//   infoSlider.style.transform = `translateY(${direction * 25}%)`;

//   setTimeout(() => {
//     infoSlider.style.transition = "none";
//     infoSlider.style.transform = "translateY(0%)";
//   }, 500);
// }

// function updateCarousel() {
//   imgSlider.style.transform = `rotate(${index * -90}deg)`;
//   updateActiveItems();
//   handleTransition();
// }

// function changeIndex(step) {
//   index += step;
//   if (index < 0) {
//     index = imgFruits.length - 1;
//   } else if (index >= imgFruits.length) {
//     index = 0;
//   }

//   updateCarousel();
// }

// nextBtn.addEventListener("click", () => {
//   changeIndex(1);
// });

// prevBtn.addEventListener("click", () => {
//   changeIndex(-1);
// });

// updateCarousel();

// infoSlider.addEventListener("transitionend", () => {
//   if (direction === -1) {
//     infoSlider.appendChild(infoSlider.firstElementChild);
//   } else if (direction === 1) {
//     infoSlider.prepend(infoSlider.lastElementChild);
//   }
// });