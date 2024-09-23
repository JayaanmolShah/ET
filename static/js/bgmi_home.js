var textWrapper = document.querySelector(".title");
textWrapper.innerHTML = textWrapper.textContent.replace(
  /\S/g,
  "<span class='letter'>$&</span>"
);



TweenMax.to(".box", 2.4, {
  y: "-100%",
  ease: Expo.easeInOut,
  delay: 1,
});

TweenMax.from("img", 0, {
  scale: "2",
  ease: Expo.easeInOut,
  delay: 0,
});

TweenMax.to(".wrapper-img", 2.4, {
  width: "400",
  height: "500",
  ease: Expo.easeInOut,
  delay: 3.6,
});

TweenMax.from(".img", 0.4, {
  opacity: 0,
  ease: Expo.easeInOut,
  delay: 3.4,
});

TweenMax.to(".left", 2, {
  x: "-400",
  rotation: -10,
  ease: Expo.easeInOut,
  delay: 3.8,
});

TweenMax.to(".right", 2, {
  x: "100",
  rotation: 10,
  ease: Expo.easeInOut,
  delay: 3.8,
});

/*CAROUSEL CODE*/

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
  infoSlider.style.transition =
    "transform 0.5s cubic-bezier(0.645, 0.045, 0.355, 1)";
  infoSlider.style.transform = `translateY(${direction * 25}%)`;

  setTimeout(() => {
    infoSlider.style.transition = "none";
    infoSlider.style.transform = "translateY(0%)";
  }, 500);
}

function updateCarousel() {
  imgSlider.style.transform = `rotate(${index * -90}deg)`;
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

/*MENU CODE*/

document.addEventListener("DOMContentLoaded", function () {
  let tl = gsap.timeline({ paused: true });
  tl.to(".menu-overlay", {
    duration: 1,
    clipPath: "polygon(0 0, 100% 0, 100% 100%, 0 100%)",
    ease: "power2.out",
  });

  tl.from(
    ".menu-link, .btn",
    {
      opacity: 0,
      y: 60,
      stagger: 0.05,
      duration: 0.75,
      ease: "power1.inOut",
    },
    "<"
  );

  tl.to(
    ".video-preview",
    {
      duration: 1,
      height: "200px",
      ease: "power2.out",
    },
    "<"
  );

  tl.to(
    ".menu-divider",
    {
      duration: 2,
      width: "100%",
      ease: "power4.out",
    },
    "<"
  );

  function openMenu() {
    document.querySelector(".menu-overlay").style.pointerEvents = "all";
    tl.play();
  }

  function closeMenu() {
    document.querySelector(".menu-overlay").style.pointerEvents = "none";
    tl.reverse();
  }

  document.querySelector(".menu-open-btn").addEventListener("click", openMenu);

  document
    .querySelector(".menu-close-btn")
    .addEventListener("click", closeMenu);

  tl.reverse();
});

/*RULEBOOK CODE*/

const allcontainer = gsap.utils.toArray(".container-item");
const venueImageWrap = document.querySelector(".container-img-wrap");
const venueImage = document.querySelector(".container-img");

function initcontainer() {
  allcontainer.forEach((link) => {
    link.addEventListener("mouseenter", venueHover);
    link.addEventListener("mouseleave", venueHover);
    link.addEventListener("mousemove", moveVenueImage);
  });
}

function moveVenueImage(e) {
  let xpos = e.clientX;
  let ypos = e.clientY;
  const tl = gsap.timeline();
  tl.to(venueImageWrap, {
    x: xpos,
    y: ypos,
  });
}

function venueHover(e) {
  if (e.type === "mouseenter") {
    const targetImage = e.target.dataset.img;

    const tl = gsap.timeline();
    tl.set(venueImage, {
      backgroundImage: `url(${targetImage})`,
    }).to(venueImageWrap, {
      duration: 0.5,
      autoAlpha: 1,
    });
  } else if (e.type === "mouseleave") {
    const tl = gsap.timeline();
    tl.to(venueImageWrap, {
      duration: 0.5,
      autoAlpha: 0,
    });
  }
}

function init() {
  initcontainer();
}

window.addEventListener("load", function () {
  init();
});

tl = new TimelineMax();

tl.from(".navbar > div", 1.6, {
  opacity: 0,
  y: 60,
  ease: Expo.easeInOut,
  delay: 0.6,
});

tl.from(
  ".site-logo",
  1.6,
  {
    opacity: 0,
    y: 40,
    ease: Expo.easeInOut,
  },
  "-=1.6"
);

tl.staggerFrom(
  ".site-menu > div",
  1,
  {
    opacity: 0,
    y: 60,
    ease: Power2.easeOut,
  },
  0.2
);

tl.staggerFrom(
  ".header > div",
  1,
  {
    opacity: 0,
    y: 60,
    ease: Power2.easeOut,
    delay: -1.4,
  },
  0.2
);
