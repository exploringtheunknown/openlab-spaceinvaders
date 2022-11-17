import EnemyController from "./EnemyController.js";
import Player from "./Player.js";
import BulletController from "./BulletController.js";
import EnemyBulletController from "./EnemyBulletController.js"
import { postLightFill, postLightScrollingText } from "./ledApi.js";

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

let hasSentStartRequest = false
async function gameLoop() {
  // reset LED grid
  if (!hasSentStartRequest) {
    await postLightFill({ color: { r: 0, g: 0, b: 0 } })
    hasSentStartRequest = true
  }
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
  background.src = "images/startpage.png";
  background.onload = function () {
    isSceneInitilized = true;
  };
}
function initLevel1() {
  background = new Image();
  background.src = "images/background.png";
  playerBulletController = new BulletController({
    canvas,
    maxBulletsAtATime: 10,
    bulletColor: "#96FA9D",
    soundEnabled: true,
    isEnemy: false
  });
  enemyBulletController = new EnemyBulletController({
    canvas,
    maxBulletsAtATime: 4,
    bulletColor: "#FFFFFF",
    soundEnabled: false,
    isEnemy: true
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

let isGameOverRun = false
async function sceneGameOver() {
  background = new Image();
  background.src = "images/gameover.png";
  if (!isGameOverRun) {
    await postLightScrollingText({
      text: "GAME OVER",
      text_speed: 0.12,
      color: {
        r: 255, g: 100, b: 0
      }
    })
    isGameOverRun = true
  }
  ctx.drawImage(background, 0, 0, canvas.width, canvas.height);
}
let isGameWon = false
async function sceneVictory() {
  if (!isGameWon) {
    await postLightScrollingText({
      text: "WINNER",
      text_speed: 0.12,
      color: {
        r: 255, g: 100, b: 0
      }
    })
    isGameWon = true
  }
  ctx.drawImage(background, 0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "white";
  ctx.font = "70px Arial";
  ctx.textBaseline = "middle";
  ctx.textAlign = "center";
  ctx.fillText("You Win!", game.width / 2, game.height / 2);
}

// use setInterval to update the game state
setInterval(gameLoop, 1000 / 60);
