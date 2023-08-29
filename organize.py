import os
import shutil
import  customtkinter as tk
from tkinter import filedialog

def move_files_by_extension(src_folder):
    for filename in os.listdir(src_folder):
        if os.path.isfile(os.path.join(src_folder, filename)):
            _, extension = os.path.splitext(filename)
            if extension:
                extension = extension[1:]  # Remove the dot from extension
                dest_folder = os.path.join(src_folder, extension)
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                shutil.move(os.path.join(src_folder, filename), os.path.join(dest_folder, filename))

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        move_files_by_extension(folder_path)
        status_label.config(text="Files moved successfully.")

# Create the main window
root = tk.CTk()
root.title("Mike's File Organizer by Extension")
# Create GUI elements
label = tk.CTkLabel(root, text=" This will move all files to folders by extension \n Use with caution! ", text_color= "yellow", bg_color="black")
label.pack(pady=10)
browse_button = tk.CTkButton(root, text="Organize Folder by extention", command=browse_folder)
browse_button.pack(pady=5)
status_label = tk.CTkLabel(root, text="")
status_label.pack(pady=10)

# Set the window size and position centered
root.update_idletasks()
width = 800
height = 400
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Set the application icon
icon_path = "C://Users//muken//OneDrive//Escritorio//ICO//file3.ico"  # Replace with the actual path to your .ico file
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

# Start the GUI event loop
root.mainloop()
