import tkinter as tk


class ExampleProject(tk.Tk):

    def init_window(self):
        #self.geometry("500x500")
        self.title("EXAMPLE PROGRAM")
        self.resizable(width=True, height=True)
        self.configure(background="black")

    def add_text_message(self):
        message = ""
        try:
            message = f"Here is what you typed added by one: {int(self.input_obj.get()) + 1}"
        except ValueError:
            message = "Please enter an integer."
        for widget in self.grid_slaves(3, 0):
            widget.destroy()
        tk.Label(self, text=message).grid(row=3, column=0, padx=20, pady=20)

    def __init__(self):
        super().__init__()
        self.init_window()

        self.input_obj = tk.Entry(self)
        self.input_obj.grid(row=0, column=0, padx=20, pady=20)

        tk.Button(self, text="Submit", command=self.add_text_message).grid(row=1, column=0, padx=20, pady=20)


def main():
    ExampleProject().mainloop()


if __name__ == "__main__":
    main()
