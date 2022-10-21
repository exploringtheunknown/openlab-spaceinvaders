import EnemyController from "./EnemyController.js";
import Player from "./Player.js";
import BulletController from "./BulletController.js";

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

canvas.width = 1000;
canvas.height = 600;

const background = new Image();
background.src = "images/topographic-pattern.png";
// background.onload = drawBackground

// function drawBackground() {
//   ctx.drawImage(this, 0, 0, canvas.width, canvas.height);
// }

const playerBulletController = new BulletController(canvas, 10, "#96FA9D", true);
const enemyBulletController = new BulletController(canvas, 4, "#FFFFFF", false);
const enemyController = new EnemyController(
  canvas,
  enemyBulletController,
  playerBulletController
);
const player = new Player(canvas, 3, playerBulletController);

let isGameOver = false;
let didWin = false;

function game() {
  checkGameOver();
  ctx.drawImage(background, 0, 0, canvas.width, canvas.height);
  displayGameOver();
  if (!isGameOver) {
    enemyController.draw(ctx);
    player.draw(ctx);
    playerBulletController.draw(ctx);
    enemyBulletController.draw(ctx);
  }
}

function displayGameOver() {
  if (isGameOver) {
    const text = didWin ? "You Win" : "Game Over";
    ctx.fillStyle = '#96FA9D';
    ctx.font = "70px Arial";
    ctx.textBaseline = "middle";
    ctx.textAlign = "center";
    ctx.fillText(text, canvas.width / 2, canvas.height / 2);
  }
}

function checkGameOver() {
  if (isGameOver) {
    return;
  }

  if (enemyBulletController.collideWith(player)) {
    isGameOver = true;
  }

  if (enemyController.collideWith(player)) {
    isGameOver = true;
  }

  if (enemyController.enemyRows.length === 0) {
    didWin = true;
    isGameOver = true;
  }
}

function drawMenu() {
  ctx.drawImage(this, 0, 0, canvas.width, canvas.height);
  ctx.font = "30px Arial";
  ctx.fillStyle = '#96FA9D';
  ctx.textBaseline = "middle";
  ctx.textAlign = "center";
  ctx.fillText("Queen Invaders", canvas.width / 2, canvas.height / 2 - 40);
  ctx.font = "16px Arial";
  ctx.fillText("Press 'Space' or touch to start.", canvas.width / 2, canvas.height / 2);
  canvas.addEventListener('click', function () {
    console.log("click1")
  }, false);
  onkeydown = function (e) {
    if (e.code === 'Space') { 
      console.log("click3", e)
    }
  }

}


let showMenu = true;

if (showMenu) {
  background.onload = drawMenu

} else {
  setInterval(game, 1000 / 60);
}

