# Computer Graphics - Project 3

## Members
- Artur de Vlieger Lima [13671574]
- Gabriel da Costa Merlin [12544420]

## Scene
Our scene contains a ground plane covered by a spherical Skybox. In this dome, we have a house that divides the internal and the external parts. The internal one is the inside of the house, containing a bed, a drawer, a vase with a rose flower and a magic crystal ball above the bed. The external one have a character (Shrek) holding a lantern, two types of ramdomized placed plants, a flying bird and an outside house bathroom.

The difference between this project and the Project 2 is that in this one we introduce the concepts of lighting. The internal lights are the
lamp and the crystal ball, while the external ones are the sun and the Shrek lantern.

It is possible to interact with the scene by pressing some buttons:
- 'w': camera forward movement
- 'a': camera backward movement
- 's': camera left movement
- 'd': camera right movement
- mouse: change camera view
- '↑': Scale up rose
- '↓': Scale down rose
- '←': Slow down bird (decreases rotation speed)
- '→': Speed up  bird (increases rotation speed)
- 'i': Shrek forward movement
- 'k': Shrek backward movement
- 'j': Shrek left movement
- 'l': Shrek right movement
- '1': Decreases ambient light
- '2': Increases ambient light
- '3': Decreases diffuse light
- '4': Increases diffuse light 
- '5': Decreases specular light
- '6': Increases specular liight
- 'z': Turn on/off lamp light
- 'x': Turn on/off crystall ball light
- 'c': Turn on/off Shrek lantern light
- 'v': Turn on/off sunlight
 
## Dependencies:

- Python 3.9
- NumPy (pip install numpy==2.0.1)
- GLFW (pip install glfw==2.7.0)
- OPENGL (pip install pyopengl==3.1.7)

## How to run:
- python3 main.py