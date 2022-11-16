# Space Invaders - Game Dev

## Running the project locally

```bash
# install dependencies
pnpm i
# or
npm i

# run project
pnpm dev
# or
npm dev
```

## Instructions

Never played Space Invaders before? Now’s your chance to try. Run the game and consider what you would change if you were its creator. Faster bullets? Bouncing bullets? Explosions? Tweak whatever you want, as long as the finished product is still playable and fun!
You can also collect points by adding a start- and highscore menu and a HP display.

## The code

Some stuff to look at if you're unsure of where to start:

- The gameLoop switch could perhaps be expanded with more states?
- The enemyController accepts a object with customizable values. Perhaps the same thing can be done with bullet controllers?

## Example tasks / how to gather points

- Implement and use the controller: 2 p

You can implement the controller that is provided, docs can be found here ([Gamepad API](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API)).

- Add highscore: 1 p

Add a highscore menu to keep track of the points you scored within the game! Compare with your friends

- Menu: 2 p

Add a start and/or game over menu

- Tweaks: 2-8 p

Examples:

Adding multiplayer functionality
Increasing the speed or shooting pattern of the bullets
Creating new sound effects
Explosions
Implementing an HP bar or multiple lives
Adding new scenes
Adding parallax background
Adding new movement patterns for the enemies
