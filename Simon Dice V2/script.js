const colors = {
    ArrowUp: "up",
    ArrowLeft: "left",
    ArrowRight: "right",
    ArrowDown: "down"
};

let sequence = [];
let playerSequence = [];
let level = 0;
let isPlaying = false;

const startButton = document.getElementById("start-button");
const message = document.getElementById("message");
const gameBoard = document.getElementById("game-board");

startButton.addEventListener("click", startGame);
document.addEventListener("keydown", handleKeyPress);

function startGame() {
    sequence = [];
    playerSequence = [];
    level = 0;
    isPlaying = true;
    message.textContent = "Observa la secuencia...";
    nextLevel();
}

function nextLevel() {
    playerSequence = [];
    level++;
    message.textContent = `Nivel ${level}`;
    
    const randomColor = Object.values(colors)[Math.floor(Math.random() * 4)];
    sequence.push(randomColor);

    playSequence();
}

function playSequence() {
    let i = 0;
    isPlaying = false;

    const interval = setInterval(() => {
        flashColor(sequence[i]);
        i++;

        if (i >= sequence.length) {
            clearInterval(interval);
            isPlaying = true;
            message.textContent = "Tu turno";
        }
    }, 800);
}

function flashColor(color) {
    const element = document.getElementById(color);
    element.classList.add("flash");
    setTimeout(() => element.classList.remove("flash"), 400);
}

function handleKeyPress(event) {
    if (!isPlaying || !colors[event.key]) return;

    const selectedColor = colors[event.key];
    flashColor(selectedColor);
    playerSequence.push(selectedColor);

    if (playerSequence[playerSequence.length - 1] !== sequence[playerSequence.length - 1]) {
        message.textContent = "¡Perdiste! Inténtalo de nuevo.";
        isPlaying = false;
        return;
    }

    if (playerSequence.length === sequence.length) {
        message.textContent = "¡Bien hecho! Siguiente nivel...";
        setTimeout(nextLevel, 1000);
    }
}
