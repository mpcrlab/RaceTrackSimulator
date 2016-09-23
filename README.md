# RaceTrackSimulator
Simulation of RaceTrackRover, to be able to train the neural network offline

## Libraries you may need

PyGame 

## Worlds
To swap a world, simply create an .txt file and replace world.txt with your world version

writing an <b>"o"</b> creates a WALL

writing a <b>"x"</b> positions the ROVER

writing <b>anything</b> else gets ignored

###Example World:
```
###################################
#.................................#
#.................................#
#.........ooooooooooooooooooo.....#
#.........o.................o.....#
#.........o.................o.....#
#.........o.................o.....#
#.........o.................o.....#
#.........o.................o.....#
#.........o......oooooo.....o.....#
#.........o......o....o.....o.....#
#.........o......oooo.o.....o.....#
#.........o.........o.o.....o.....#
#.........o.........o.o.....o.....#
#.........o.........o.o.....o.....#
#.........o.........o.o.....o.....#
#.........ooooo.....o.o.....o.....#
#.............o.....o.o.....o.....#
#.............o.....o.o.....o.....#
#.............o.....o.o.....o.....#
#.............o.....ooo.....o.....#
#.............o.............o.....#
#.............o.............o.....#
#.............o...x.........o.....#
#.............o.............o.....#
#.............o.............o.....#
#.............ooooooooooooooo.....#
#.................................#
#.................................#
###################################
```

## Information
Control with arrow keys

Image of car comes licence-free from: https://pixabay.com/en/racing-car-ferrari-red-top-view-296772/

###TODO
-Add a "FOV"

-States, rewards, etc (for learning)

-Add AI contorls
