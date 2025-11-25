# Change Page (or state, or window, however you may think of it)

So there comes a time when you may want to change the entirety of the window you have.
Maybe you want to display a different page. Maybe you need to display like a settings menu.
Regardless, you need to transfer to a new page and there are a few ways to go about this!


----

# Easiest Option

First off, there is the easiest* option. This is to destroy all the assets
and then re-add the assets you want.

This is the easiest option only because it doesn't require you to store all the assets
necessarily. When you go about bringing up a new page, you cannot just
add the elements you want, because the old components start overlapping each other.
So, you need to remove the old components. To remove components, you need to call
the widget.destroy() method on them, and if you didn't create a variable for said widget,
then getting access to it may prove difficult.

So, it can be easy to just have a loop go through all the components and
delete them all, and just re-add the items you want.

This has some downsides though, especially if you have components you want to consist for all pages:
- inefficient: you are probably re-adding the same component over and over again
  which, takes time to do.
- repeated code: if you have something like a header, you are going to need to re-add it after
  everytime you want a new page, which if you forget to add this piece of code, then your header is just gone too.

```python
import tkinter as tk


class ExampleProject(tk.Tk):

    def clear_window(self):
        # Goes through every component of root window to clear it
        for widget in self.winfo_children():
            widget.destroy()

    def exit(self):
        # Destroys everything and exits program
        self.destroy()
        exit(0)

    def show_header(self):
        # Adds elements to header
        frame = tk.Frame(self, bg="gray")
        tk.Button(frame, text="Exit", command=self.exit, padx=40, pady=3).grid(row=0, column=0, sticky="NSEW")
        tk.Button(frame, text="Main", command=self.show_main_window, padx=40, pady=3).grid(row=0, column=1, sticky="NSEW")
        tk.Button(frame, text="Other Window", command=self.show_other_window, padx=10, pady=3).grid(row=0, column=2, sticky="NSEW")
        frame.grid(row=0, column=0, columnspan=3, sticky="NSEW")


    def show_main_window(self):
        # Clear old window and reset header
        self.clear_window()
        self.show_header()

        # Add Content for this window (main window)
        tk.Label(image=self.cat_picture).grid(row=1, column=1, sticky="NSEW", padx=5, pady=5)


    def show_other_window(self):
        # Clear old window and reset header
        self.clear_window()
        self.show_header()

        # Add Content for this window (other window)
        tk.Label(text="Hey here is the other window!").grid(row=1, column=1, sticky="NSEW", padx=5, pady=5)


    def __init__(self):
        # Initializes root
        super().__init__()

        # Sets up window
        self.title("EXMP PRGM")

        # Initializes window which will appear first
        self.cat_picture = tk.PhotoImage(file="old_mod7_day1/assets/cat.png")
        self.cat_picture = self.cat_picture.subsample(2)
        self.show_main_window()


def main():
    ExampleProject().mainloop()


if __name__ == "__main__":
    main()
```


------

# Better Option

A better option to avoid both of the cons in the previous example is to 
set up some frame to store your content in.

A frame is a component which can be used to group together other components.
You can use a frame to add a bunch of components to and design the layout specifically
within the frame.

By creating a 'content' frame for our GUI, we can simply add the components on your new page
on to it, and whenever we change pages, we can just clear the content frame without needing to worry about
the header!

BTW, THIS IS WHAT I WOULD RECOMMEND

Note, it does offset the content inside the frame to its own grid, so, in our example,
the cat picture is no longer in the center of the screen because its now positioned
inside the frame.

```python
import tkinter as tk


class ExampleProject(tk.Tk):

    def clear_content(self):
        # Goes through every component of content frame to clear it
        for widget in self.content.winfo_children():
            widget.destroy()

    def exit(self):
        # Destroys everything and exits program
        self.destroy()
        exit(0)

    def show_header(self):
        # Adds elements to header
        frame = tk.Frame(self, bg="gray")
        tk.Button(frame, text="Exit", command=self.exit, padx=40, pady=3).grid(row=0, column=0, sticky="NSEW")
        tk.Button(frame, text="Main", command=self.show_main_window, padx=40, pady=3).grid(row=0, column=1, sticky="NSEW")
        tk.Button(frame, text="Other Window", command=self.show_other_window, padx=10, pady=3).grid(row=0, column=2, sticky="NSEW")
        frame.grid(row=0, column=0, columnspan=3, sticky="NSEW")


    def show_main_window(self):
        # Clear old window and reset header
        self.clear_content()

        # Add Content for this window (main window)
        tk.Label(self.content, image=self.cat_picture).grid(row=0, column=0, sticky="NSEW", padx=5, pady=5)


    def show_other_window(self):
        # Clear old window and reset header
        self.clear_content()

        # Add Content for this window (other window)
        tk.Label(self.content, text="Hey here is the other window!").grid(row=0, column=0, sticky="NSEW", padx=5, pady=5)


    def __init__(self):
        # Initializes root
        super().__init__()

        # Sets up window
        self.title("EXMP PRGM")

        # Initializes cat picture
        self.cat_picture = tk.PhotoImage(file="old_mod7_day1/assets/cat.png")
        self.cat_picture = self.cat_picture.subsample(2)

        # Displays header
        self.show_header()

        # Sets up content frame
        self.content = tk.Frame(self)
        self.content.grid(row=1, column=0, columnspan=3, sticky="NSEW")

        # Displays main page
        self.show_main_window()


def main():
    ExampleProject().mainloop()


if __name__ == "__main__":
    main()
```


------

# Alternative Option

One final solution is to use the tkinter built in notebook widget.

The tkinter notebook widget has built in tabs to transfer to multiple pages.
All you need to do is create a page and add it to the notebook.

This also utilizes frames, as you just create a frame for a page, add the page content
to it, then add it to the notebook.

The notebook deals with going from one page to the next.

The only downside is that the notebook's tab-buttons are not really under
our control, so we cannot simply add an exit tab to quit the program.

What we have to do it bind the tab change event to a method, where if it detects
that the Exit tab was pressed, it can then call our exit function.

See the example below:


```python
import tkinter as tk
from tkinter import ttk


class ExampleProject(tk.Tk):


    def exit(self):
        # Destroys everything and exits program
        self.destroy()
        exit(0)


    def main_page(self):
        page = tk.Frame(self.notebook)
        tk.Label(page, image=self.cat_picture).grid(row=0, column=0, sticky="NSEW", padx=5, pady=5)
        self.notebook.add(page, text="Main")

    def other_page(self):
        page = tk.Frame(self.notebook)
        tk.Label(page, text="Hey here is the other window!").grid(row=0, column=0, sticky="NSEW", padx=5, pady=5)
        self.notebook.add(page, text="Other Page")


    def __init__(self):
        # Initializes root
        super().__init__()

        # Sets up window
        self.title("EXMP PRGM")

        # Initializes cat picture
        self.cat_picture = tk.PhotoImage(file="old_mod7_day1/assets/cat.png")
        self.cat_picture = self.cat_picture.subsample(2)

        # Initializes tkinter notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Adds pages
        self.main_page()
        self.other_page()

        # Adds an empty frame to the exit page and bind function to event when
        # widget it changed
        self.notebook.add(tk.Frame(), text="Exit")
        self.bind('<<NotebookTabChanged>>', self.on_tab_change)

    def on_tab_change(self, event):
        # This method occurs when a tab changes
        tab = event.widget.tab('current')['text']
        if tab == 'Main':
            # Currently prints 1 when main tab is used
            print("1")
        elif tab == 'Other Page':
            # Currently prints 2 when other tab is used
            print("2")
        elif tab == 'Exit':
            # Exits program when exit tab is used
            self.exit()






def main():
    ExampleProject().mainloop()


if __name__ == "__main__":
    main()
```


