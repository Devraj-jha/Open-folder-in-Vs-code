import os
import subprocess
import sys
import tkinter as tk
from tkinter import scrolledtext
from tkinter import PhotoImage

def create_project(event=None):
    project_name = entry.get().strip()
    if not project_name:
        output.config(state=tk.NORMAL)
        output.insert(tk.END, "Please enter a project name.\n")
        output.see(tk.END)
        output.config(state=tk.DISABLED)
        return

    project_name_clean = project_name.replace(" ", "_")
    
    # ============================================================
    # SET YOUR PROJECT FOLDER PATH HERE
    # ============================================================
    # Example for Windows:
    # programming_folder = os.path.join(os.path.expanduser("~"), "Documents", "Programming")
    #
    # Example for macOS:
    # programming_folder = os.path.join(os.path.expanduser("~"), "Documents", "Programming")
    #
    # Please set your desired folder path below:
    programming_folder = os.path.join(os.path.expanduser("~"), "Documents", "Programming")
    # ============================================================
    
    new_folder_path = os.path.join(programming_folder, project_name_clean)

    try:
        os.makedirs(new_folder_path, exist_ok=True)
        output.config(state=tk.NORMAL)
        output.insert(tk.END, f"✅ Folder created at: {new_folder_path}\n")
        output.see(tk.END)
        output.config(state=tk.DISABLED)

        # Open VS Code in the new folder (works for both Windows and macOS)
        if sys.platform == "win32":
            # For Windows
            subprocess.run(["code", new_folder_path], shell=True)
        else:
            # For macOS and Linux
            subprocess.run(["code", new_folder_path])
            
        output.config(state=tk.NORMAL)
        output.insert(tk.END, f"VS Code opened in {new_folder_path}\n")
        output.see(tk.END)
        output.config(state=tk.DISABLED)
    except Exception as e:
        output.config(state=tk.NORMAL)
        output.insert(tk.END, f"❌ Error: {e}\n")
        output.see(tk.END)
        output.config(state=tk.DISABLED)

    entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Open folder in VS Code")
root.geometry("700x450")
root.minsize(500, 300)
root.configure(bg="#2b2b2b")

# Optional background image
try:
    bg_image = PhotoImage(file="1.png")
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)
except:
    pass

# =====================
# Create output area (expands)
# =====================
output_frame = tk.Frame(root, bg="#2b2b2b")
output_frame.pack(fill=tk.BOTH, expand=True, side=tk.TOP, padx=10, pady=(10,0))

output = scrolledtext.ScrolledText(output_frame, bg="#1e1e1e", fg="#ffd700",
                                   insertbackground="#ffd700", font=("Courier", 12))
output.pack(fill=tk.BOTH, expand=True)
output.insert(tk.END, "Enter your project name below and hit Create or press Enter:\n")
output.config(state=tk.DISABLED)  # Read-only

# =====================
# Create input area (fixed at bottom)
# =====================
input_frame = tk.Frame(root, bg="#2b2b2b")
input_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=10)  # Always at bottom

entry = tk.Entry(input_frame, bg="#1e1e1e", fg="#ffd700", insertbackground="#ffd700",
                 font=("Courier", 14))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry.focus()
entry.bind("<Return>", create_project)

button = tk.Button(input_frame, text="Create Project", bg="#000000", fg="black",
                   font=("Courier", 12), command=create_project)
button.pack(side=tk.LEFT, padx=(10,0))

root.mainloop()