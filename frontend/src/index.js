import EnemyController from "./EnemyController.js";
import Player from "./Player.js";
import BulletController from "./BulletController.js";

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
canvas.width = 1000;
canvas.height = 600;

let background,
  playerBulletController,
  enemyBulletController,
  enemyController,
  player;

let scene = "menu";
let isSceneInitilized = false;

function gameLoop() {
  switch (scene) {
    case "menu":
      if (!isSceneInitilized) initMenu();
      return sceneMenu();
    case "level1":
      if (!isSceneInitilized) initLevel1();
      return sceneLevel1();
    // case "level2":
    //   if (!isSceneInitilized) initLevel2();
    //   return level2();
    case "lose":
      return sceneGameOver();
    case "win":
      return sceneVictory();
  }
}
function initMenu() {
  background = new Image();
  background.src = "images/topographic-pattern.png";
  background.onload = function () {
    isSceneInitilized = true;
  };
}
function initLevel1() {
  background = new Image();
  background.src = "images/topographic-pattern.png";
  playerBulletController = new BulletController({
    canvas,
    maxBulletsAtATime: 10,
    bulletColor: "#96FA9D",
    soundEnabled: true,
  });
  enemyBulletController = new BulletController({
    canvas,
    maxBulletsAtATime: 4,
    bulletColor: "#FFFFFF",
    soundEnabled: false,
  });
  enemyController = new EnemyController({
    canvas,
    enemyBulletController,
    playerBulletController,
    moveDownTimerDefault: 30,
    fireBulletTimerDefault: 10,
    velocityX: 1,
    velocityY: 1,
  });
  player = new Player({
    canvas,
    velocity: 3,
    playerBulletController,
  });
  isSceneInitilized = true;
}

function sceneMenu() {
  ctx.drawImage(background, 0, 0, canvas.width, canvas.height);
  ctx.font = "30px Arial";
  ctx.fillStyle = "#96FA9D";
  ctx.textBaseline = "middle";
  ctx.textAlign = "center";
  ctx.fillText("Queen Invaders", canvas.width / 2, canvas.height / 2 - 40);
  ctx.font = "16px Arial";
  ctx.fillText("touch to start.", canvas.width / 2, canvas.height / 2);

  function startGame() {
    canvas.removeEventListener("click", startGame);
    isSceneInitilized = false;
    scene = "level1";
  }

  canvas.addEventListener("click", startGame);
}

function sceneLevel1() {
  ctx.drawImage(background, 0, 0, canvas.width, canvas.height);
  enemyController.draw(ctx);
  player.draw(ctx);
  playerBulletController.draw(ctx);
  enemyBulletController.draw(ctx);
  if (enemyBulletController.collideWith(player)) scene = "lose";
  if (enemyController.collideWith(player)) scene = "lose";
  if (enemyController.enemyRows.length === 0) scene = "win";
}

function sceneGameOver() {
  ctx.drawImage(background, 0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "white";
  ctx.font = "70px Arial";
  ctx.textBaseline = "middle";
  ctx.textAlign = "center";
  ctx.fillText("Game Over", game.width / 2, game.height / 2);
}

function sceneVictory() {
  ctx.drawImage(background, 0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "white";
  ctx.font = "70px Arial";
  ctx.textBaseline = "middle";
  ctx.textAlign = "center";
  ctx.fillText("You Win!", game.width / 2, game.height / 2);
}

// use setInterval to update the game state
setInterval(gameLoop, 1000 / 60);
