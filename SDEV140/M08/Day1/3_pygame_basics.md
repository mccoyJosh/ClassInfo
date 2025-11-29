# Pygame

## What is it?

Pygame is a
- open source (community made)
  - https://github.com/pygame/pygame
- cross-platform (works on most operating systems)
- "game engine" (library for the development of multimedia appliacations like videos games)
- USES PYTHON

It's a python game engine.

So, we can use it to make games!

## Where to get?

Pygame is already part of the pypi repository of packages, so we can easily install pygame with pip:

```
pip install pygame
```

Now, all we need to do is import into the files we are going to use!

```python
import pygame

# run code!
```

-----------------------------

# How to use

So, there are lots and lots of things that are in pygame...
so we can not possibly talk about all the things,
so we will talk about lots of the important details

## Starting Off (MAKING A WINDOW)

So, with it installed, lets do something really simple: make a window!

Here is 
```python
import pygame
from pygame.locals import *


# Initializes the game and gives our window a name
pygame.init()
pygame.display.set_caption("My Game")


# Creates the dimensions for what will be our game
HEIGHT = 450
WIDTH = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))



# Creates loop so our game will run until we want it to close... instead of closing immediately
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # if the "X" on the window is pressed
      pygame.quit()
```

If you want your game to be fullscreen, you can create your window with this alternative line:
```
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
```

## Surfaces

So, the way in which pygame organizes its objects to display is by surfaces.

Basically, **everything is a "surface"** which we can attach things to/draw on to.

This includes the **game screen itself**... i.e. the window we made!

This guy:
```
screen = pygame.display.set_mode((WIDTH, HEIGHT))
```

So, the other things we want to display on the screen are also going to be surfaces.

The simplest of these surfaces is the rectangle.

### Creating a rectangle

Here is how we create a rectangle

```
color = (255,255,0)
pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
pygame.display.flip()
```

A few things are happening here.

First, we are creating a color. This color is actually just a tuple with 3 values which pygame which will evaluate as a color.
This, obviously is going to be the color of our rectangle. The three values are representing it's Red, Green, and Blue values.

color = (red, green, blue)

Each of these 3 values go from 0 to 255

- Red would be (255, 0, 0)
- Yellow would be (255, 255, 0)
- Black would be (0, 0, 0)
- White would be (255, 255, 255)

So, you can create a range of colors pretty easily with some loops!
````python
import pygame
from pygame.locals import *


# Initializes the game and gives our window a name
pygame.init()
pygame.display.set_caption("My Game")


# Creates the dimensions for what will be our game
HEIGHT = 600
WIDTH = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def limiter(va):
  if va >= 256:
    return 255
  elif va < 0:
    return 0
  return va

for c in range(768):
  red = 0
  green = 0
  blue = 0

  if c <= 256: # red green
    c_offset = c
    red = limiter(256 - c_offset)
    green = limiter(c_offset)
  elif c <= 512: # green blue
    c_offset = c - 256
    green = limiter(256 - c_offset)
    blue = limiter(c_offset)
  else: # blue red 
    c_offset = c - 512
    blue = limiter(256 - c_offset)
    red = limiter(c_offset)
  for i in range(-300, 300):
    color = (limiter(red + i), limiter(green + i), limiter(blue + i))
    pygame.draw.rect(screen, color, pygame.Rect(c, i+300, 1, 1))


pygame.display.flip()




# Creates loop so our game will run until we want it to close
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # if the "X" on the window is pressed
      pygame.quit()
````

Next, the rectangle takes a few more values other than colors:

```
pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
```

We see:
- takes the surface it is being placed on; in this example it is the screen itself, but it can be future made surfaces as well
- it then takes the rectangle object itself, pygame.Rect(); this takes 4 values, in this order:
  - **left**: how many pixels away from the left side of the surface it needs to be
  - **top**: how many pixels away from the top side of the surface it needs to be
  - **width**: from that point, how wide is it (in pixels); this "extends" towards the right
  - **height**: from that point, how tall is it (in pixels); this "extends" down
  - ###### **ESSENTIALLY, you designate a point with the left and top parameters, and then tell how big you want the object there**


Once you tell pygame to draw the object, it technically is not on your screen yet.
Basically, the game knows it is there, but has NOT displayed it to the player yet.

No change actually occurs until we update the screen.


So, to do that, we can use:
```
pygame.display.flip()
```


```python
import pygame
from pygame.locals import *


# Initializes the game and gives our window a name
pygame.init()
pygame.display.set_caption("My Game")


# Creates the dimensions for what will be our game
HEIGHT = 450
WIDTH = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Waits 1 second
pygame.time.delay(1000)

# Inits and draws shape to screen
color = (255,255,0)
pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
pygame.display.flip()

# Inits shape to screen
color = (255,0,0)
pygame.draw.rect(screen, color, pygame.Rect(180, 30, 60, 60))

# Waits 1 second
pygame.time.delay(1000)

# Draws the new screen
pygame.display.flip()


# Creates loop so our game will run until we want it to close
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT: # if the "X" on the window is pressed
         pygame.quit()

```



## Importing an image

Importing an image is another example of creating  new surface,

Doing it is really only involves 2 new functions

pygame.image.load
and
screen (or whatever surface you want) .blit

```
# Loads in image
imp = pygame.image.load("assets/test_guy.png").convert()


# Using blit to copy content from one surface to other
screen.blit(imp, (0, 0))

# paint screen one time
pygame.display.flip()
```

Here is an example of putting it on the screen:
```python
import pygame
from pygame.locals import *


# Initializes the game and gives our window a name
pygame.init()
pygame.display.set_caption("My Game")


# Creates the dimensions for what will be our game
HEIGHT = 450
WIDTH = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# Loads in image
imp = pygame.image.load("assets/test_guy.png").convert()


# Using blit to copy content from one surface to other
screen.blit(imp, (140, 120))

# paint screen one time
pygame.display.flip()


# Creates loop so our game will run until we want it to close
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT: # if the "X" on the window is pressed
         pygame.quit()

```

Do note: 

trying to move the "player" by just changing the position and redrawing does not work.
As shown in this next example, just drawing the player in different positions will
leave the last copies on the screen still:

```python
import pygame
from pygame.locals import *


# Initializes the game and gives our window a name
pygame.init()
pygame.display.set_caption("My Game")


# Creates the dimensions for what will be our game
HEIGHT = 450
WIDTH = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# Loads in image
imp = pygame.image.load("assets/test_guy.png").convert()


# Using blit to copy content from one surface to other
screen.blit(imp, (140, 120))

# paint screen one time
pygame.display.flip()

step_n = 4
for w in range (0, WIDTH - imp.get_width(), step_n):
   for h in range (0, HEIGHT - imp.get_height(), step_n):
      screen.blit(imp, (w, h))
      pygame.display.flip()


# Creates loop so our game will run until we want it to close
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT: # if the "X" on the window is pressed
         pygame.quit()


```

The problem of the previous iteration of the screen can be solved with using `screen.fill((0,0,0))`
```
step_n = 4
for w in range (0, WIDTH - imp.get_width(), step_n):
   for h in range (0, HEIGHT - imp.get_height(), step_n):
      pygame.time.delay(1)
      screen.fill((0, 0, 0))
      screen.blit(imp, (w, h))
      pygame.display.flip()

```

This essentially clears the previous screen.... although we will look more into this later when we start adding "movement"
to the character.


## Adding sounds/music

So, adding sounds or music is actually 2 different things.

Technically, you could use sound objects for your music too, but you probably don't want to do that!

So, for music, this is going to be your general, background music.

As long as you have a audio file, this should be relatively simple:

```
pygame.mixer.init()

# Loading the song
pygame.mixer.music.load("assets/TinyTavern.mp3")

# Setting the volume
pygame.mixer.music.set_volume(0.7)

# Start playing the song
pygame.mixer.music.play()
```

This will start the song and keep playing it.

Notice also the set_volume method... this sets the volume.

Now, since you only normally have 1 track play in the background, you don't need to set it as its own object.

YOU DO NEED TO CREATE SOUND OBJECTS SINCE YOU PROBABLY WILL HAVE MULTIPLE SOURCES OF NOISE.

This is how you create a sound object:

```
sound_effect = pygame.mixer.Sound("assets/Buzz.mp3")
sound_effect.set_volume(0.5)
sound_effect.play()
```

This also has the same set_volume method, to, well, set audio.

Otherwise, it just plays the sound.

In this example, I turn on the music and tie the noise to pressing the b key.
We will get more into this later!


```python
import pygame
from pygame.locals import *


# Initializes the game and gives our window a name
pygame.init()
pygame.display.set_caption("My Game")


# Creates the dimensions for what will be our game
HEIGHT = 450
WIDTH = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.mixer.init()

# Loading the song
pygame.mixer.music.load("assets/TinyTavern.mp3")

# Setting the volume
pygame.mixer.music.set_volume(0.7)

# Start playing the song
pygame.mixer.music.play()


sound_effect = pygame.mixer.Sound("assets/Buzz.mp3")
sound_effect.set_volume(0.5)

# Creates loop so our game will run until we want it to close
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the "X" on the window is pressed
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_b:
                sound_effect.play()



```


## Displaying Text

Displaying text is yet just another method we need to call. 

Really, it is a combination of making a font object and describing what text it should
display in that font.

```

# Set up text object
font = pygame.font.Font(None, 50)
color = (255, 255, 255)
text = font.render("Hello, BRO!", True, color)


# Display it on the screen
screen.blit(text, (20, 20))
pygame.display.flip()

```

Here it is being used in a larger example:

```python
import pygame
from pygame.locals import *


# Initializes the game and gives our window a name
pygame.init()
pygame.display.set_caption("My Game")


# Creates the dimensions for what will be our game
HEIGHT = 450
WIDTH = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))



font = pygame.font.Font(None, 50)
color = (255, 255, 255)
text = font.render("Hello, BRO!", True, color)

# Creates loop so our game will run until we want it to close
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the "X" on the window is pressed
            pygame.quit()

    screen.fill((0, 0, 0))
    screen.blit(text, (20, 20))
    pygame.display.flip()


```


