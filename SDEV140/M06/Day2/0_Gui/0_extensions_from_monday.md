# Extensions From Monday

Things which were half covered monday:

## Place Method?

Another way to get your widgets on the screen other than Grid and Pack
is with the Place method.

This can be used to place a frame or widget on the screen in an
absolute position or relative position on the screen from another window/frame.

In this example, it keeps our `l` label in the top right hand corner of the screen
by making the anchor point 'ne' for Northeast
and sets the relx and rely to 1 and 0.

Now, these values are kind of initially confusing.

### Anchor

This value does NOT represent from what position we are basing our distance off of. This
instead tells tkinter from what side of our widget/frame we are placing on the window/frame
to calculate the relative distance to. So, by setting the anchor to center, it will determine
where to place the item based off of the center point of the widget/frame.

### relx and rely

These values tell tkinter where to place our widget/frame from relative positions 
in the x direction (left and right) and the y direction (up and down); they are shortened from
relative x to relx and relative y to rely

The relative x value is based off of the distance from the left hand side of the window 
to the right hand side of the window; so if you wanted something to stick to the right
hand side of the window, you would set this value to 1, i.e. 100%, as it would always be 100%
on the right hand side of the screen.

The relative y value is based off the distance from the top of the screen to the bottom. So, if you
wanted some to appear at the top of the screen, you would set this value to 0 (i.e. 0%) to indicate
you want it no distance away from the top of the screen compared to bottom.

```python
import tkinter as tk


class ExampleProject(tk.Tk):

    def init_window(root):
        #root.geometry("500x500")
        root.title("EXAMPLE PROGRAM")
        root.resizable(width=True, height=True)
        root.configure(background="black")

    def __init__(root):
        super().__init__()
        root.init_window()
        root.cat_picture = tk.PhotoImage(file='cat.png')  # DOING root. BEFORE THIS IS VERY IMPORTANT
        tk.Label(root, image=root.cat_picture).grid(row=0, column=0, sticky="NSEW")
        tk.Label(root, text="Here is a cat", font=("Helvetica", 20)).grid(row=1, column=0, sticky="NSEW")

        l = tk.Label(root, text= "TEXT AHH", font=("Helvetica", 20), )
        l.config(fg='red')
        l.place(relx = 1, rely = 0, anchor = 'ne')




def main():
    ExampleProject().mainloop()


if __name__ == "__main__":
    main()
```

If we wanted to change the l label to appear in the upper left hand corner, we would want to change it to this:
```python
        l = tk.Label(root, text= "TEXT AHH", font=("Helvetica", 20), )
        l.config(fg='red')
        l.place(relx = 0, rely = 0, anchor = 'nw')
```

If we wanted to change it to the center, we would want to change it to this:

```python
        l = tk.Label(root, text= "TEXT AHH", font=("Helvetica", 20), )
        l.config(fg='red')
        l.place(relx = 0.5, rely = 0.5, anchor = 'center')
```



## Sounds in Tkinter?

Tkinter does not support sound, so we will need to use a third party 
item to make this work... such as pygame

First install it:
```
pip install pygame
```


This should work
(untested)
```python
import pygame


pygame.mixer.init()
pygame.mixer.music.load("sound.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(loops=0)
```


## JPEG/JPG not supported natively in Tkinter???

By default, JPEGs are not supported in tkinter. So, you get around this
by just converting your image to PNG, or we can use this other
package to fix our problem!

Do it like this instead!
(untested)

```python
import tkinter as tk
from PIL import Image


class ExampleProject(tk.Tk):

    def init_window(root):
        #root.geometry("500x500")
        root.title("EXAMPLE PROGRAM")
        root.resizable(width=True, height=True)
        root.configure(background="black")

    def __init__(root):
        super().__init__()
        root.init_window()

        root.dog_image = ImageTk.PhotoImage(Image.open("dog.jpg"))

        tk.Label(root, image=root.dog_image).grid(row=0, column=0, sticky="NSEW")
        tk.Label(root, text="Here is a cat", font=("Helvetica", 20)).grid(row=1, column=0, sticky="NSEW")






def main():
    ExampleProject().mainloop()


if __name__ == "__main__":
    main()
```