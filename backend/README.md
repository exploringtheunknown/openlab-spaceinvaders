# BACKEND

### Get started 

Run the following commands to create a virtual environment: 

```
python3 -m venv .venv
source .venv/bin/activate
```

Then install the following: 

```
pip install -r requirements.txt

pre-commit install

```

To run the program:

```
sudo -E python3 -m uvicorn src.app:app
```


### Instructions

Familiarize yourself with Pythons FastAPI and the provided post-requests. You may alter the functions or add as many as you want. Out of ideas? Visit adafruits CircuitPython LED Animations documentation for some inspiration: https://learn.adafruit.com/circuitpython-led-animations


### The example code

There are 4 premade functions that will display light effects on the LED grid 'rectangle'. Feel free to modify these as you wish, see examples below for some ideas to implement.


### Example tasks / how to gather points

- Create displays of game animations: 2-5 p

Examples: 

Displaying each enemy sprite as a pixel on the grid, which then disappears upon enemy death
Displaying the movement of the player or bullets on the grid
Displaying the current score of the player 
Displaying animations when firing or when hit

- Complexity and responsiveness: 2-10 p

You can earn points depending on the complexity of the light effects you create and based on their timing with the gameplay.  
