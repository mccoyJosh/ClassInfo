# Obstacles

## Health

Creating health (and many, many other things) are as simple as creating a new variables.

In the instance for health, this can be 1 simple variable called "health".

Otherwise, all we would really want to do for the user is make it so that
they can see it and the game ends when it hits 0.

In the following code, we have made those adjustments:

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


def create_health_text(health_score):
    font = pygame.font.Font(None, 50)
    color = (255, 0, 0)
    return font.render(f"Health: {health_score}", True, color)




def main():
    # Initializes the game and gives our window a name
    pygame.init()
    pygame.display.set_caption("My Game")
    declare_objects()


    # Creates the dimensions for what will be our game
    HEIGHT = 450
    WIDTH = 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # PLAYER INFO

    # Loads in image
    player : pygame.surface.Surface = pygame.image.load("assets/test_guy.png").convert()
    player = pygame.transform.scale(player, (40, 50))

    # Player attributes
    global health
    health = 100

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
        if health <= 0:
            # Prints out game over screen and then waits to close game
            screen.fill((0, 0, 0))
            screen.blit(pygame.font.Font(None, 50).render("GAME OVER", True, (255, 0, 0)), (100, 200))
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.quit()

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
        screen.blit(create_health_text(health), (0,0))

        # Draws screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
```

If we wanted to have a little bit of fun, we can also change the color of the health text as the health changes by 
implementing a bit more code to our constructor for the health text, seen below:

```
def create_health_text(health_score):
    font = pygame.font.Font(None, 50)
    
    color_equiv = 0
    if health_score > 0:
        color_equiv = int(255 * (health_score/100))

    color = (255 - color_equiv, 0, color_equiv)
    return font.render(f"Health: {health_score}", True, color)
```


## "Spikes"

So, if you think about it, we already have objects, and
all spikes are ARE objects which hurt you.

SO, we can implement spikes or any other dangerous object by simply 
adding a bit more code to our object piece of code!

First, we can change our object things to have a second parameter, that being their type (represented by
a second value in a tuple). We then specify some objects are spikes:

```
def create_rectangle(left, top, width, height):
    global objects
    objects.append((pygame.Rect(left, top, width, height), 'obj'))


def create_spike(left, top, width, height):
    global objects
    objects.append((pygame.Rect(left, top, width, height), 'spike'))
    
def declare_objects():
    global objects 
    objects = []
    create_rectangle(0, 0, 20, 100)
    create_rectangle(380, 0, 20, 100)
    create_rectangle(195, 300, 20, 200)
    create_spike(100, 150, 200, 20)
```

THEN, we need the drawer of the objects **to account for the tuple** and **CHANGE THE COLOR of a spike** vs a non-spike.

```
    def draw_objects():
        global objects
        for (obj, typ) in objects:
            if typ == "spike":
                color = (255, 0, 0) # red
                pygame.draw.rect(screen, color, obj)
            else:
                color = (0, 255, 0) # green
                pygame.draw.rect(screen, color, obj)

```


The collision detector also needs to account for this tuple as well!

```
        for (obj, typ) in objects:  ## JUST THIS LINE HERE GOT CHANGED... FOR NOW
            p_left__o_right = x_pos < obj.right                         # Player Left side moves past object right side
            p_right__o_left = x_pos + player.get_width() > obj.left     # Player Right side moves past object left side
            p_top__o_bottom = y_pos < obj.bottom                        # Player Top side moves past bottom of object
            p_bottom__o_top = y_pos + player.get_height() > obj.top     # Player Bottom moves pass past top of object

            if p_left__o_right and p_right__o_left and p_top__o_bottom and p_bottom__o_top:
                x_pos = player_pos[0]
                y_pos = player_pos[1]
```

Finally, with everything being accounted for, we now just need to damage the player when they collide with 
the spike.

We already have code to account for the spike colliding... we can just add some code to
also decrease the health in this instance!

With the collision method updated, we get a final result of this, where touching this call will hurt out player:

```python
import pygame
from pygame.locals import *

def create_rectangle(left, top, width, height):
    global objects
    objects.append((pygame.Rect(left, top, width, height), 'obj'))


def create_spike(left, top, width, height):
    global objects
    objects.append((pygame.Rect(left, top, width, height), 'spike'))
    
def declare_objects():
    global objects 
    objects = []
    create_rectangle(0, 0, 20, 100)
    create_rectangle(380, 0, 20, 100)
    create_rectangle(195, 300, 20, 200)
    create_spike(100, 150, 200, 20)


def create_health_text(health_score):
    font = pygame.font.Font(None, 50)
    
    color_equiv = 0
    if health_score > 0:
        color_equiv = int(255 * (health_score/100))

    color = (255 - color_equiv, 0, color_equiv)
    return font.render(f"Health: {health_score}", True, color)


    

def main():
    # Initializes the game and gives our window a name
    pygame.init()
    pygame.display.set_caption("My Game")
    declare_objects()


    # Creates the dimensions for what will be our game
    HEIGHT = 450
    WIDTH = 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # PLAYER INFO

    # Loads in image
    player : pygame.surface.Surface = pygame.image.load("assets/test_guy.png").convert()
    player = pygame.transform.scale(player, (40, 50))

    # Player attributes
    global health
    health = 100

    global x_pos, y_pos
    x_pos = (WIDTH/2) - (player.get_width() / 2)
    y_pos = (HEIGHT/2) - (player.get_height() / 2)
    player_pos = [x_pos, y_pos] # Should start in center of screen
    speed = 0.3

    def update_position():
        global x_pos, y_pos, objects, health
        # Ensures player stays on the screen
        if x_pos < 0 or x_pos > WIDTH - player.get_width():
            x_pos = player_pos[0]
        if y_pos < 0 or y_pos > HEIGHT - player.get_height():
            y_pos = player_pos[1]

        obj : pygame.rect.Rect
        
        for (obj, typ) in objects:
            p_left__o_right = x_pos < obj.right                         # Player Left side moves past object right side
            p_right__o_left = x_pos + player.get_width() > obj.left     # Player Right side moves past object left side
            p_top__o_bottom = y_pos < obj.bottom                        # Player Top side moves past bottom of object
            p_bottom__o_top = y_pos + player.get_height() > obj.top     # Player Bottom moves pass past top of object

            if p_left__o_right and p_right__o_left and p_top__o_bottom and p_bottom__o_top:
                x_pos = player_pos[0]
                y_pos = player_pos[1]
                if typ == "spike":
                    health -= 1

            

            
        player_pos[0] = x_pos
        player_pos[1] = y_pos
    
    def draw_objects():
        global objects
        for (obj, typ) in objects:
            if typ == "spike":
                color = (255, 0, 0) # red
                pygame.draw.rect(screen, color, obj)
            else:
                color = (0, 255, 0) # green
                pygame.draw.rect(screen, color, obj)


    # Creates loop so our game will run until we want it to close
    while True:
        if health <= 0:
            # Prints out game over screen and then waits to close game
            screen.fill((0, 0, 0))
            screen.blit(pygame.font.Font(None, 50).render("GAME OVER", True, (255, 0, 0)), (100, 200))
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.quit()

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
        screen.blit(create_health_text(health), (0,0))

        # Draws screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
```


## Enemies

So, all an enemy is IS basically another player.

Honestly, you could think of it as a moving spike too, but either way works.

So, what we do is implement many of the same attributes we have for the player and add them into the game.

We are also not putting any restrictions on the enemy to allow them always move closer to the player.
To make it follow the player, all de need to do is find the difference in the x and y coordinates from each other. With
that, the enemy just needs to move in that direction. We make divide it by itself to make sure it results in either -1 or
1 just so we know what cardinal direction / quadrant to move. We then add speed on top of this so we are in control
of how quickly it moves in our game.

 
#### FPS

Without adding FPS, the game is going to go as fast as it can.
With the implementation of the enemy, they move FAR to fast to avoid normally, and it is inconsistent 
on different systems.
To account for this, we use pygame's built in FPS controls to always ensure the game runs at the same speed, giving us,
the control we need.

This does mean that the player now moves slower, so we can update their speed and make everything run as intended!

We finally end up with a pretty simple game!

From here, we can maybe add a score to display to the user to see how high they can get it, but
that's all we are really going to do for this game.



```python
import pygame
from pygame.locals import *

def create_rectangle(left, top, width, height):
    global objects
    objects.append((pygame.Rect(left, top, width, height), 'obj'))


def create_spike(left, top, width, height):
    global objects
    objects.append((pygame.Rect(left, top, width, height), 'spike'))
    
def declare_objects():
    global objects 
    objects = []
    create_rectangle(0, 0, 20, 100)
    create_rectangle(380, 0, 20, 100)
    create_rectangle(195, 300, 20, 200)
    create_spike(100, 150, 200, 20)


def create_health_text(health_score):
    font = pygame.font.Font(None, 50)
    
    color_equiv = 0
    if health_score > 0:
        color_equiv = int(255 * (health_score/100))

    color = (255 - color_equiv, 0, color_equiv)
    return font.render(f"Health: {health_score}", True, color)


    

def main():
    # Initializes the game and gives our window a name
    pygame.init()
    pygame.display.set_caption("My Game")
    declare_objects()


    # Creates the dimensions for what will be our game
    HEIGHT = 450
    WIDTH = 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # PLAYER INFO

    # Loads in image
    player : pygame.surface.Surface = pygame.image.load("assets/test_guy.png").convert()
    player = pygame.transform.scale(player, (40, 50))

    # Player attributes
    global health
    health = 100
    score = 0


    global x_pos, y_pos
    x_pos = (WIDTH/2) - (player.get_width() / 2)
    y_pos = (HEIGHT/2) - (player.get_height() / 2)
    player_pos = [x_pos, y_pos] # Should start in center of screen
    speed = 1.5

    def update_position():
        global x_pos, y_pos, objects, health
        # Ensures player stays on the screen
        if x_pos < 0 or x_pos > WIDTH - player.get_width():
            x_pos = player_pos[0]
        if y_pos < 0 or y_pos > HEIGHT - player.get_height():
            y_pos = player_pos[1]

        obj : pygame.rect.Rect
        
        for (obj, typ) in objects:
            p_left__o_right = x_pos < obj.right                         # Player Left side moves past object right side
            p_right__o_left = x_pos + player.get_width() > obj.left     # Player Right side moves past object left side
            p_top__o_bottom = y_pos < obj.bottom                        # Player Top side moves past bottom of object
            p_bottom__o_top = y_pos + player.get_height() > obj.top     # Player Bottom moves pass past top of object

            if p_left__o_right and p_right__o_left and p_top__o_bottom and p_bottom__o_top:
                x_pos = player_pos[0]
                y_pos = player_pos[1]
                if typ == "spike":
                    health -= 1

            

            
        player_pos[0] = x_pos
        player_pos[1] = y_pos
    

    # ENEMY INFO
    # Loads in image
    enemy : pygame.surface.Surface = pygame.image.load("assets/super_scary_creature.png").convert()
    enemy = pygame.transform.scale(enemy, (40, 50))

    # Enemy attributes
    global evil_health
    evil_health = 100
    global enemy_pos
    enemy_pos = [WIDTH - enemy.get_width(), HEIGHT - enemy.get_height()]
    enemy_speed = 1

    def update_enemy_position():
        global x_pos, y_pos, enemy_pos, health
        # Get difference from positions of player and enemy
        x_dif = x_pos - enemy_pos[0]
        y_dif = y_pos - enemy_pos[1]


        # Reduce to 1
        if x_dif != 0:
            x_dif_pow = x_dif / abs(x_dif)
        else:
            x_dif_pow = 0
        if y_dif != 0:
            y_dif_pow = y_dif / abs(y_dif)
        else: 
            y_dif_pow = 0
        
        enemy_pos = ((enemy_pos[0] + x_dif_pow) * enemy_speed, (enemy_pos[1] + y_dif_pow) * enemy_speed)


        # See if collides with player:
        # Here we are not AS worried with absolute collision, so we are just seeing if they are close (we already have their differences)!
        distance = (x_dif**2 + y_dif**2) ** 0.5
        if distance < 10:
            health -= 1




    
    def draw_objects():
        global objects
        for (obj, typ) in objects:
            if typ == "spike":
                color = (255, 0, 0) # red
                pygame.draw.rect(screen, color, obj)
            else:
                color = (0, 255, 0) # green
                pygame.draw.rect(screen, color, obj)




    FPS = 60
    FramePerSec = pygame.time.Clock()

    # Creates loop so our game will run until we want it to close
    while True:
        if health <= 0:
            # Prints out game over screen and then waits to close game
            screen.fill((0, 0, 0))
            screen.blit(pygame.font.Font(None, 50).render("GAME OVER", True, (255, 0, 0)), (100, 200))
            screen.blit(pygame.font.Font(None, 25).render(f"SCORE: {score}", True, (255, 255, 255)), (25, 300))
            pygame.display.flip()
            pygame.time.wait(5000)
            pygame.quit()

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
        update_enemy_position()
        
        # Clears screen to be nothing
        screen.fill((0, 0, 0))
        
        # Draw whatever you want on your screen!
        draw_objects()
        screen.blit(player, player_pos)
        screen.blit(enemy, enemy_pos)
        screen.blit(create_health_text(health), (0,0))

        # Draws screen
        pygame.display.flip()
        score += 1
        FramePerSec.tick(FPS)


if __name__ == "__main__":
    main()
```


