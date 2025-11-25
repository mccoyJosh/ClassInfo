
# Using a bunch of different aspects of GUI:

-----

# Pop Up Boxes

A pop-up box is exactly what you think it is... a window which pops up.
To make one, it is relatively easy... because it's nearly the same as 
making a window, which we have already done!

The only difference is we call TopLevel() instead of Tk().
Making a window and putting text on it would look like this:
```
popup = tk.Toplevel(root)
tk.Label(popup, text="Please enter an integer.").pack(side=tk.LEFT)
```
Making a popup window like this will tie it to the root, so if you close the root
window, all the popups go away as well.

By making a window in this fashion, it also will automatically make the window run
without the need to run mainloop()

Here is an example using this to inform the user they did not put in an integer:

```python
import tkinter as tk


class ExampleProject(tk.Tk):

    def add_text_message(self):
        message = ""
        try:
            message = f"Here is what you typed added by one: {int(self.input_obj.get()) + 1}"
        except ValueError:
            x = tk.Toplevel(self)
            x.title("Error")
            tk.Label(x, text="Please enter an integer.").pack(side=tk.LEFT)
            return
        for widget in self.grid_slaves(3, 0):
            widget.destroy()
        tk.Label(self, text=message).grid(row=3, column=0, padx=20, pady=20)

    def __init__(self):
        super().__init__()
        self.title("EXAMPLE PROGRAM")

        self.input_obj = tk.Entry(self)
        self.input_obj.grid(row=0, column=0, padx=20, pady=20)

        tk.Button(self, text="Submit", command=self.add_text_message).grid(row=1, column=0, padx=20, pady=20)


def main():
    ExampleProject().mainloop()


if __name__ == "__main__":
    main()
```


### Little Fun Program :)

This makes lots of cat pages
```python
import tkinter as tk


class ExampleProject(tk.Tk):
    def create_pop_up(self):
        x = tk.Toplevel(self)
        x.title("Cat")
        tk.Label(x, image=self.cat_pic).grid(row=0, column=0, sticky="NSEW")
        tk.Label(x, text="Cat.").grid(row=1, column=0, sticky="NSEW")

    def __init__(self):
        super().__init__()
        self.title("CAT PROGRAM")

        self.cat_pic =tk.PhotoImage(file="old_mod7_day1/assets/cat.png")
        self.cat_pic = self.cat_pic.subsample(3, 3)
        for i in range(100):
            self.create_pop_up()


def main():
    ExampleProject().mainloop()


if __name__ == "__main__":
    main()
```

-----

# Nested Frames

A good way to make components and organize them is with layers of 
frames.

For instance, if you needed a window which needed age and name, we can simply
the problem by making a method which creates for us a label + entry object,
and just calling that instead of creating NEARLY same thing twice. Putting these
components in a frame makes this possible.

```python
import tkinter as tk


class ExampleProject(tk.Tk):

    def create_input(self, root, msg="Please input: "):
        f = tk.Frame(root)
        tk.Label(f, text=msg).grid(row=0, column=0, sticky=tk.W)
        input_obj = tk.Entry(f, textvariable=tk.StringVar())
        input_obj.grid(row=0, column=1, sticky=tk.W)
        f.pack(side=tk.TOP)
        return input_obj

    def create_output(self):
        for widget in self.output.winfo_children():
            widget.destroy()
        tk.Label(self.output, text=f"Output: {self.name.get()} is {self.age.get()}").pack()


    def __init__(self):
        super().__init__()
        self.title("EXMP PROGRAM")
        self.content = tk.Frame(self)
        self.output = tk.Frame(self)

        self.name = self.create_input(self.content, "Name: ")
        self.age = self.create_input(self.content, "Age: ")
        tk.Button(self.content, text="Submit", command=self.create_output).pack(side=tk.TOP)

        self.content.pack(side=tk.TOP)
        self.output.pack(side=tk.TOP)





def main():
    ExampleProject().mainloop()


if __name__ == "__main__":
    main()
```

----

# Multiline Text Areas

So up to this point we have been using the tk.Entry() object
which is a single line of input. Sometimes, we may want to have more area to type!

This is actually super easy. Instead of .Entry(), we just use:
tk.Text()

Here is a simple example:

```python
import tkinter as tk

class ExampleProject(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EXMP PROGRAM")

        tk.Label(self, text="Hey here is a big place to type", font=("Helvetica", 40)).grid(row=0, column=0)

        text_area = tk.Text(self)
        text_area.grid(column=0, row=1)


def main():
    ExampleProject().mainloop()


if __name__ == "__main__":
    main()
```

-----

# File Dialogs

Sometimes you need access to the file system on your computer, like selecting
a file to import into your program.

To do this, we can use tkinter's built in filedialog functionality. This 
uses your system's directories to browse through your files. All it
does is give you the location of the file, but that is really
all you need.

Here is an example piece of code which is able to read a file and allow you to edit
it (it does not save it).

```python
import tkinter as tk
from tkinter import filedialog as fd


class ExampleProject(tk.Tk):

    def update_file_info(self, file_name='NONE'):
        # Removes previous header
        for widget in self.file_info.winfo_children():
            widget.destroy()
        
        # Creates label for file name and button to run open_file method
        tk.Label(self.file_info, text=f"File: {file_name}").pack(side=tk.LEFT)
        tk.Button(self.file_info, text='Open New File', command=self.open_file).pack(side=tk.LEFT)

    def open_file(self):
        # Calls tkinter filedialog menu
        file_path = fd.askopenfilename()

        # Actually reads file found
        file_reader = open(file_path, 'r')
        text_found = file_reader.read()
        file_reader.close()

        # Removes previous text and places new text
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(1.0, text_found)

        
        # Gets just the filename out of the file path and updates header
        file_path_split_up = file_path.split('/')
        self.update_file_info(file_path_split_up[len(file_path_split_up) - 1])

    def __init__(self):
        super().__init__()
        self.title("EXMP PROGRAM")
        
        # Set up file info header
        self.file_info = tk.Frame(self)
        self.file_info.grid(column=0, row=0)
        
        # Creates header
        self.update_file_info()

        # Create Editable text area
        self.text_area = tk.Text(self)
        self.text_area.grid(column=0, row=1)


def main():
    ExampleProject().mainloop()


if __name__ == "__main__":
    main()
```


-----

# Extra Buttons
- Check Boxes
  - Check boxes are exactly what they sound like. They are boxes you can select and they become 'true'
      and if not selected they are false.



- Radio Buttons
  - Radio buttons are used in situations like a multiple choice test where there
    is only one option. Selecting any one of the options will make the other
    options become unselected.


Here is an example using both:
```python
import tkinter as tk


class ExampleProject(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("EXMP PROGRAM")

        checked = tk.BooleanVar()
        tk.Checkbutton(self, text="Here is an example check button", variable=checked, onvalue=True, offvalue=False).pack()
        tk.Button(self, text='Print Check Bool', command=lambda: print(checked.get())).pack()

        selected = tk.StringVar()
        tk.Radiobutton(self, text='Btn 1', variable=selected, value='btn1').pack()
        tk.Radiobutton(self, text='Btn 2', variable=selected, value='btn2').pack()
        tk.Button(self, text='Print Radio Selection', command=lambda: print(selected.get())).pack()





def main():
    ExampleProject().mainloop()


if __name__ == "__main__":
    main()
```

----
# Keyboard Events

The final thing we are going to talk about in terms of GUI is keyboard inputs.
So, when someone is within your GUI, you have access to the buttons they are pressing
and you have a choice as to what occurs when they are typed. Getting access to these buttons
is actually relativley simple. ALl you need to do is use the bind method on the window you want the inputs
from:

```
window.bind("<KEY TYPED>", <function to occur if key is pressed>)
```

Here is an example of that in action:

```python
import tkinter as tk


class ExampleProject(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("EXMP PROGRAM")

        self.bind('<F>', lambda event: print('Hey you typed F!!!'))
        self.bind('<Escape>', lambda event: self.quit())



def main():
    ExampleProject().mainloop()


if __name__ == "__main__":
    main()

```

