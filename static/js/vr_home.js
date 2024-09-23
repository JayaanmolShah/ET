const spotlight = document.querySelector(".spotlight");
const overlay = document.querySelector(".overlay");
const toggleButton = document.getElementById("toggleOverlay");

let scrollAmmount = 0;
let yPos = 0;
let xPos = 0;

spotlight.addEventListener("mousemove", handleMoveEvent);
spotlight.addEventListener("touchmove", handleMoveEvent);
toggleButton.addEventListener("click", toggleOverlayVisibility);

window.addEventListener('scroll', (event) => {
    if (window.scrollY >= 250) {
        toggleButton.classList.add('lights-hidden');
        toggleButton.classList.remove('lights');
    } else {
        toggleButton.classList.remove('lights-hidden');
        toggleButton.classList.add('lights');
    }
})

function handleMoveEvent(e) {
    // if (!overlayVisible) return; // Prevent movement if overlay is hidden

    const clientX = e.clientX || e.touches[0].clientX;
    const clientY = e.clientY || e.touches[0].clientY;

    setTimeout(() => {
        yPos = clientY - overlay.offsetHeight / 2;
        xPos = clientX - overlay.offsetWidth / 2;

        // If you want to use scroll position, ensure it's handled correctly
        scrollAmmount = overlay.scrollTop + yPos;

        // Use backticks for string interpolation
        overlay.style.top = `${scrollAmmount}px`;
        overlay.style.left = `${xPos}px`;
    }, 100);
}

function toggleOverlayVisibility() {
    if (overlay.classList.contains("hidden")) {
        overlay.classList.remove("hidden");
    } else {
        overlay.classList.add("hidden");
    }
}


const output = document.querySelector(".output");

// Define colors array to match the words array
const colors = [
    "#0c1c34", // Color for "Full Stack Developer"
    "#0c1c34", // Color for "Full Stack Developer"
    "#0c1c34", // Color for "Full Stack Developer"
];

let typeSpeed = 100; // Speed of typing
let removeSpeed = 100; // Speed of removing

let id = 0; // Index of the current word
let charCount = 0; // Number of characters typed/removed

function type() {
    let res = words[id].substr(0, charCount);
    output.style.color = colors[id]; // Set color based on current word

    if (charCount >= words[id].length + 3) { // +3 for pause before removing
        clearInterval(time);
        charCount = 1;
        time = setInterval(remove, removeSpeed); // Start removing
    }
    output.innerHTML = res;
    charCount++;
}

function remove() {
    let res = words[id].substr(0, words[id].length - charCount);

    if (res.length <= 0) { // If the word is fully removed
        id = (id >= words.length - 1) ? 0 : id + 1; // Move to the next word or loop back to start
        clearInterval(time);
        charCount = 0;
        time = setInterval(type, typeSpeed); // Start typing the new word
    }
    output.innerHTML = res;
    charCount++;
}

// Define words array
const words = [
    "IMMERSE\xa0VR",
    "EXPLORE\xa0VR",
    "EXPERIENCE\xa0VR",
];

// Start typing animation
let time = setInterval(type, typeSpeed);


const panels = document.querySelectorAll(".panel");
const panelsContainer = document.querySelector(".panels");
const descriptions = document.querySelectorAll(".description > div");
const backBtn = document.querySelector(".back-btn");

// Add mouse enter and leave events to panels
panels.forEach(panel => {
    panel.addEventListener("mouseenter", () => {
        panels.forEach(p => p.classList.add("panel-inactive"));
        panel.classList.remove("panel-inactive");
    });

    panel.addEventListener("mouseleave", () => {
        panels.forEach(p => p.classList.remove("panel-inactive"));
    });
});

// Add click events to panels
panels.forEach((panel, i) => {
    panel.addEventListener("click", () => {
        panels.forEach(p => {
            p.classList.add("panel-hidden");
        });

        setTimeout(() => {
            panels.forEach(p => {
                p.style.display = "none";
            });

            panel.classList.remove("panel-hidden");
            panel.style.display = "flex";
            panel.classList.add("panel-active");
            panelsContainer.style.display = "block";

            descriptions.forEach(d => d.classList.remove("description-active"));
            descriptions[i].classList.add("description-active");
            backBtn.style.display = "block";
        }, 400);
    });
});

// Add click event to back button
backBtn.addEventListener("click", () => {
    panels.forEach(panel => {
        panel.classList.remove("panel-hidden");
        panel.classList.remove("panel-active");
        panel.style.display = "flex"; // Show all panels

        descriptions.forEach(description => description.classList.remove("description-active"));
        backBtn.style.display = "none";
    });

    panelsContainer.style.display = "grid"; // Adjust container display if needed
});


















ScrollTrigger.create({
    animation: gsap.from(".logo",{
        y:"50vh",
        scale: 6,
        yPercent:-50,
    }),
    scrub: true,
    trigger: ".pages",
    start: "top bottom",
    endTrigger: ".pages",
    end:"top center",
});






const bgAnimation = document.getElementById('bgAnimation');

const numberOfColorBoxes = 400;

for (let i = 0; i < numberOfColorBoxes; i++) {
    const colorBox = document.createElement('div');
    colorBox.classList.add('colorBox');
    bgAnimation.append(colorBox)
}

