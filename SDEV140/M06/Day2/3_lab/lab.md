# Lab

----

## File Editor

> Make a file text editor 

```python
import tkinter as tk
from tkinter import filedialog as fd


class ExampleProject(tk.Tk):

    def set_up_intro_page(self):
        self.clear_content()
        tk.Label(self.content, text=f"Welcome to my text editor!").grid(row=0, column=0, columnspan = 3, sticky="NSEW")
        tk.Label(self.content, image=self.my_editor_pic).grid(row=1, column=0, columnspan=3, sticky="NSEW")

        # New File Buttons
        tk.Label(self.content, text='File Name:').grid(row=4, column=0, sticky="NSEW")
        self.potential_file_name_en = tk.Entry(self.content)
        self.potential_file_name_en.grid(row=4, column=1, sticky="NSEW")
        tk.Button(self.content, text='New File', command=lambda:self.open_file(self.potential_file_name_en.get(), True)).grid(row=3, column=0, columnspan=2, sticky="NSEW")


        # Open Existing Files
        tk.Button(self.content, text='Open Existing File', command=lambda:self.open_file(fd.askopenfilename(), False)).grid(row=3, column=2, sticky="NSEW")


    def save_file(self, new_content):
        try:
            f = open(self.file_name, 'w')
            f.write(new_content)
            f.close()
        except Exception:
            print("ERROR: FAILED TO WRITE TO FILE")

    def set_up_edit_page(self, initial_page_content):
        self.clear_content()
        tk.Label(self.content, image=self.file_pic).grid(row=0, column=0)
        tk.Button(self.content, text='Back', command=self.set_up_intro_page).grid(row=0, column=1, sticky="NSEW")
        tk.Label(self.content, text=f"File: {self.file_name}").grid(row=0, column=2, sticky="NSEW")

        self.text_area = tk.Text(self.content)
        self.text_area.grid(column=0, row=1, columnspan=4)
        self.text_area.insert(1.0, initial_page_content)

        tk.Button(self.content, text='Save', command=lambda : self.save_file(self.text_area.get("1.0", "end-1c") )).grid(row=0, column=3, sticky="NSEW")




    def open_file(self, file_path, is_new_file):
        if is_new_file:
            self.file_name = file_path
            self.set_up_edit_page("")
            return

        try:
            # Actually reads file found
            file_reader = open(file_path, 'r')
            text_found = file_reader.read()
            file_reader.close()


            # Gets just the filename out of the file path and updates header
            # file_path_split_up = file_path.split('/')
            # self.file_name = file_path_split_up[len(file_path_split_up) - 1]
            self.file_name = file_path
            self.set_up_edit_page(text_found)
        except Exception:
            print("FAILURE TO OPEN FILE:", file_path)

    def clear_content(self):
        # Goes through every component of content frame to clear it
        for widget in self.content.winfo_children():
            widget.destroy()

    def __init__(self):
        super().__init__()
        self.title("EXMP PROGRAM")

        # initializes image objects
        self.file_pic = tk.PhotoImage(file='Day2/assets/file.png')
        self.file_pic = self.file_pic.subsample(13,13)
        self.my_editor_pic = tk.PhotoImage(file='Day2/assets/myTextEditor.png')

        # Initializes other used variables
        self.file_name = ''
        self.text_area = None
        self.potential_file_name_en = None

        self.content = tk.Frame(self)
        self.content.grid(row=0, column=0, sticky="NSEW")

        self.set_up_intro_page()



def main():
    ExampleProject().mainloop()


if __name__ == "__main__":
    main()
```