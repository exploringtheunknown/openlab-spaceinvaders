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

let scene = "level1";
let isSceneInitilized = false;

function gameLoop() {
  if (isSceneInitilized) {
    checkGamestate();
  }

  switch (scene) {
    // case menu: return sceneMenu();
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

function initLevel1() {
  background = new Image();
  background.src = "images/topographic-pattern.png";

  playerBulletController = new BulletController(canvas, 10, "#96FA9D", true);
  enemyBulletController = new BulletController(canvas, 4, "#FFFFFF", false);
  enemyController = new EnemyController(
    canvas,
    enemyBulletController,
    playerBulletController,
    30,
    10,
    1,
    1
  );
  player = new Player(canvas, 3, playerBulletController);
  isSceneInitilized = true;
}

function sceneLevel1() {
  ctx.drawImage(background, 0, 0, canvas.width, canvas.height);
  enemyController.draw(ctx);
  player.draw(ctx);
  playerBulletController.draw(ctx);
  enemyBulletController.draw(ctx);
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

function checkGamestate() {
  if (enemyBulletController.collideWith(player)) scene = "lose";
  if (enemyController.collideWith(player)) scene = "lose";
  if (enemyController.enemyRows.length === 0) scene = "win";
}

setInterval(gameLoop, 1000 / 60);
