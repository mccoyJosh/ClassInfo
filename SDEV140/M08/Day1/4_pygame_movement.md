# Pygame Movement

## Properly Updating the screen

So this is shown in the last example but this is a good way to 
make sure your game does not draw over previous assets.

We do this by simply:
1. refilling screen to be blank
2. DRAWING WHATEVER WE WANT
3. Commit it to the screen

### General Use:

```
# Creates loop so our game will run until we want it to close
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: # if the "X" on the window is pressed
         pygame.quit()
    # Clears screen to be nothing
    screen.fill((0, 0, 0))
    

    # Draw whatever you want on your screen!
    

    # Draws screen
    pygame.display.flip()
```



With that, lets actually properly put our little character on the screen:

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


# Loads in image "Player"
player : pygame.surface.Surface = pygame.image.load("assets/test_guy.png").convert()
player = pygame.transform.scale(player, (40, 50))
start_x = (WIDTH/2) - (player.get_width() / 2)
start_y = (HEIGHT/2) - (player.get_height() / 2)
player_pos = [start_x, start_y] # Should start in center of screen


# Creates loop so our game will run until we want it to close
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: # if the "X" on the window is pressed
         pygame.quit()
    # Clears screen to be nothing
    screen.fill((0, 0, 0))
    
    # Draw whatever you want on your screen!
    screen.blit(player, player_pos)

    # Draws screen
    pygame.display.flip()
```

ALSO, we made the picture slightly smaller because the image was too big for our little screen!
This code here accomplishes this task:
```
player = pygame.transform.scale(player, (40, 50))
```

Now, do note, the order in which we place these object on the screen is very important.

We are basically stacking them in the layer we present, 1 at a time.

So, perhaps, if I draw to the screen a red rectangle after my player on the same place as my player, 
then it will appear above them.

Replace the previous while loop with this piece of code to see this:

```
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: # if the "X" on the window is pressed
         pygame.quit()
    # Clears screen to be nothing
    screen.fill((0, 0, 0))
    
    # Draw whatever you want on your screen!
    screen.blit(player, player_pos)

    red = (255, 0, 0)
    pygame.draw.rect(screen, red, pygame.Rect(WIDTH/2, 0, 10, 450))

    # Draws screen
    pygame.display.flip()

```

## Moving... anything

With a little guy on the screen, we can finally make him move.

Basically, we have the position of the character being saved to
"player_pos" and it is redrawing it each frame of the game.

Therefore, all we need to do to make them move is update this position, and 
python will draw this at the new position!

Doing this is relatively simple:

```
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: # if the "X" on the window is pressed
         pygame.quit()

    player_pos[0] += 0.1
    
    # Clears screen to be nothing
    screen.fill((0, 0, 0))
    
    # Draw whatever you want on your screen!
    screen.blit(player, player_pos)


    # Draws screen
    pygame.display.flip()
```

This does get the person to move, but, probably not as intended. We really want to be able to control this character.

So, lets talk about actually getting input from the user to control this guy!


## Getting Input and Badly Moving Character

We have kinda already been getting input from the game... actually.

So, the way that pygame interprets inputs is by labeling anything that can happen as an **event**.

One such even is pressing the CLOSE button on the window of the pygame game.
This event is "pygame.QUIT"; we trigger the game to quit in this instance;
this snippet of code has been in our code a bit now.

Another event type is "KEYDOWN"; this is pressing a key on our keyboard.
What we can do is add on to our existing loop to detect events to also do
specific actions when keys are pressed.

Look at the code below. We have added 1 check to see
if the KEYDOWN event occurred to know if we should check
what key was pressed.

Once we have a key, we can do specific actions
on their press. Here, we are using the directional arrow keys to control the character, so when any of them
are pressed, they change the position of the character variable.


```
# Creates loop so our game will run until we want it to close
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the "X" on the window is pressed
            pygame.quit()
        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_LEFT:     # Press "left" button
                player_pos[0] -= 5
            elif event.key == pygame.K_RIGHT:  # Press "right" button
                player_pos[0] += 5
            elif event.key == pygame.K_UP:     # Press "up" button
                player_pos[1] -= 5
            elif event.key == pygame.K_DOWN:   # Press "down" button
                player_pos[1] += 5
    
    # Clears screen to be nothing
    screen.fill((0, 0, 0))
    
    # Draw whatever you want on your screen!
    screen.blit(player, player_pos)

    # Draws screen
    pygame.display.flip()
```

This "works", although, pygame only detects the initial press of the movement.
Normally, we want our character to keep moving once they press and hold down the key.

To fix this, we need to add a bit more code.

## Moving A Character

To keep our character moving, we basically just need to ensure we ALWAYS, are recording the key inputs.
So, we take it out of our for loop.

We have also implemented a `speed` variable so that
we can easily change how fast our character moves.

We have also made a function to update our position, but this will make more sense in just a moment.

Otherwise though, our character is now moving around properly and everything is chill.

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
player : pygame.surface.Surface = pygame.image.load("assets/test_guy.png").convert()
player = pygame.transform.scale(player, (40, 50))


x_pos = (WIDTH/2) - (player.get_width() / 2)
y_pos = (WIDTH/2) - (player.get_width() / 2)
player_pos = [x_pos, y_pos] # Should start in center of screen
speed = 0.3

def update_position():
    player_pos[0] = x_pos
    player_pos[1] = y_pos

# Creates loop so our game will run until we want it to close
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the "X" on the window is pressed
            pygame.quit()

    # Gets user key inputs continuously
    key_pressed_is = pygame.key.get_pressed() 
    if key_pressed_is[pygame.K_LEFT]:
        x_pos -= speed
    if key_pressed_is[pygame.K_RIGHT]:
        x_pos += speed
    if key_pressed_is[pygame.K_UP]:
        y_pos -= speed
    if key_pressed_is[pygame.K_DOWN]:
        y_pos += speed
    
    update_position()
    
    # Clears screen to be nothing
    screen.fill((0, 0, 0))
    
    # Draw whatever you want on your screen!
    screen.blit(player, player_pos)

    # Draws screen
    pygame.display.flip()



```

## Collision

The simplest collision we need to ensure is to make our user stays on the screen.
This is honestly pretty easy to code.

The position of the edges of the window shouldn't change, so, we can just add a bit of code to our "update" position
function where if we were to fall outside the range of the screen, we are just prevented from moving that direction:

```
def update_position():
    global x_pos
    global y_pos
    # Ensures player stays on the screen
    if x_pos < 0 or x_pos > WIDTH - player.get_width():
        x_pos = player_pos[0]
    if y_pos < 0 or y_pos > HEIGHT - player.get_height():
        y_pos = player_pos[1]
    player_pos[0] = x_pos
    player_pos[1] = y_pos
```

This is pretty simple. We have another issue though: colliding with objects.

Now, this is a way in which pygame can kinda deal with this for us, but we are going to instead
implement this ourselves.

To make this work, we are going to add a few things.

First, we are going to create a function to create rectangle objects for us so we can
also have it add it to a list.

We want a list of objects so we can walk through it and make sure we are not colliding with any of them.

We are also creating a `declare_objects` function to have a single place for all of our objects.

Once we have these objects, we want to include in our game loop
to actually draw these objects.

Finally, once this is all in place, we actually have some objects to collide with.

```python
import pygame
from pygame.locals import *

def create_rectangle(left, top, width, height):
    global objects
    objects.append(pygame.Rect(left, top, width, height))
    
def declare_objects():
    global objects 
    objects = []
    create_rectangle(0, 0, 20, 100)
    create_rectangle(380, 0, 20, 100)
    create_rectangle(195, 300, 20, 200)
    create_rectangle(100, 150, 200, 20)


def main():
    # Initializes the game and gives our window a name
    pygame.init()
    pygame.display.set_caption("My Game")
    declare_objects()


    # Creates the dimensions for what will be our game
    HEIGHT = 450
    WIDTH = 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))


    # Loads in image
    player : pygame.surface.Surface = pygame.image.load("assets/test_guy.png").convert()
    player = pygame.transform.scale(player, (40, 50))

    global x_pos, y_pos
    x_pos = (WIDTH/2) - (player.get_width() / 2)
    y_pos = (HEIGHT/2) - (player.get_height() / 2)
    player_pos = [x_pos, y_pos] # Should start in center of screen
    speed = 0.3

    def update_position():
        global x_pos, y_pos, objects
        # Ensures player stays on the screen
        if x_pos < 0 or x_pos > WIDTH - player.get_width():
            x_pos = player_pos[0]
        if y_pos < 0 or y_pos > HEIGHT - player.get_height():
            y_pos = player_pos[1]

        obj : pygame.rect.Rect
        
        for obj in objects:
            p_left__o_right = x_pos < obj.right                         # Player Left side moves past object right side
            p_right__o_left = x_pos + player.get_width() > obj.left     # Player Right side moves past object left side
            p_top__o_bottom = y_pos < obj.bottom                        # Player Top side moves past bottom of object
            p_bottom__o_top = y_pos + player.get_height() > obj.top     # Player Bottom moves pass past top of object

            if p_left__o_right and p_right__o_left and p_top__o_bottom and p_bottom__o_top:
                x_pos = player_pos[0]
                y_pos = player_pos[1]

            

            
        player_pos[0] = x_pos
        player_pos[1] = y_pos
    
    def draw_objects():
        global objects
        for obj in objects:
            color = (0, 255, 0) # This is green
            pygame.draw.rect(screen, color, obj)


    # Creates loop so our game will run until we want it to close
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if the "X" on the window is pressed
                pygame.quit()

        # Gets user key inputs continuously
        key_pressed_is = pygame.key.get_pressed() 
        if key_pressed_is[pygame.K_LEFT]:
            x_pos -= speed
        if key_pressed_is[pygame.K_RIGHT]:
            x_pos += speed
        if key_pressed_is[pygame.K_UP]:
            y_pos -= speed
        if key_pressed_is[pygame.K_DOWN]:
            y_pos += speed
        
        update_position()
        
        # Clears screen to be nothing
        screen.fill((0, 0, 0))
        
        # Draw whatever you want on your screen!
        draw_objects()
        screen.blit(player, player_pos)

        # Draws screen
        pygame.display.flip()


if __name__ == "__main__":
    main() 
```


The way we check for collisions is by comparing the bounds of the character to each object.
Here is the code chunk which does this in particular:
```
        for obj in objects:
            p_left__o_right = x_pos < obj.right                         # Player Left side moves past object right side
            p_right__o_left = x_pos + player.get_width() > obj.left     # Player Right side moves past object left side
            p_top__o_bottom = y_pos < obj.bottom                        # Player Top side moves past bottom of object
            p_bottom__o_top = y_pos + player.get_height() > obj.top     # Player Bottom moves pass past top of object

            if p_left__o_right and p_right__o_left and p_top__o_bottom and p_bottom__o_top:
                x_pos = player_pos[0]
                y_pos = player_pos[1]

```

What we find is that we are REALLY only doing 4 comparisons, those being:
- does Player's Left side move past object's right side
- does Player's Right side move past object's left side
- does Player's Top side move past bottom of the object
- does Player's Bottom move pass past top of the object

If all of these are true, then that means their bounds are colliding!


Think about it: if any one of these were false, it would just mean the character is just off somewhere no-where near the object.

![bound_conditions.png](assets/bound_conditions.png)

This is a very basic example, but this is how it works!