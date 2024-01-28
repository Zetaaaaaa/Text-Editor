import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")

        self.text_widget = tk.Text(self.root, wrap="word", undo=True)
        self.text_widget.pack(expand="yes", fill="both")

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)

    def new_file(self):
        self.text_widget.delete(1.0, tk.END)
        self.root.title("Text Editor")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                file_content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, file_content)
            self.root.title(f"Text Editor - {file_path}")

    def save_file(self):
        if self.root.title() == "Text Editor":
            self.save_file_as()
        else:
            file_path = self.root.title()[len("Text Editor - "):]
            with open(file_path, "w") as file:
                file.write(self.text_widget.get(1.0, tk.END))

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_widget.get(1.0, tk.END))
            self.root.title(f"Text Editor - {file_path}")

    def exit_editor(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
