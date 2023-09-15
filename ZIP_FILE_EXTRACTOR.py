import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import zipfile
import lzma
# import py7zr

def show_tooltip(widget, message):
    # Create a tooltip balloon with the given message
    tooltip = tk.Toplevel()
    tooltip.wm_overrideredirect(True)
    tooltip.wm_geometry(f"+{widget.winfo_rootx()+ -30}+{widget.winfo_rooty() + 25}")
    label = tk.Label(tooltip, text=message, background="yellow")
    label.pack()
    tooltip.after(2000, tooltip.destroy) # Hide the tooltip after 2 seconds

# def show_tool(widget, message):
#     # Create a tooltip balloon with the given message
#     tooltip = tk.Toplevel()
#     tooltip.wm_overrideredirect(True)
#     tooltip.wm_geometry(f"+{widget.winfo_rootx()+25}+{widget.winfo_rooty() + 25}")
#     label = tk.Label(tooltip, text=message, background="yellow")
#     label.pack()
#     tooltip.after(2000, tooltip.destroy)


def browse_file():
    # Open a file dialog for browsing and get the selected file path
    file_path = filedialog.askopenfilename()
    zip_file_entry.delete(0, tk.END)
    zip_file_entry.insert(0, file_path)

def browse_folder():
    # Open a file dialog for browsing and get the selected folder path
    folder_path = filedialog.askdirectory()
    dest_folder_entry.delete(0, tk.END)
    dest_folder_entry.insert(0, folder_path)

def extract_zip_file():
    # Get the zip file path and destination folder from input fields
    zip_file_path = zip_file_entry.get()
    destination_folder = dest_folder_entry.get()

    # Check if the zip file path is empty
    if not zip_file_path:
        show_tooltip(browse_zip_file_button, "Please insert zip file")
        return
    #result_label.config(text="Extraction Started...")
    # # Open the zip file in read mode
    # with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    #     # Extract all files and folders to the destination folder
    #     zip_ref.extractall(destination_folder)
    #     messagebox.showinfo("Result",f"Zip file Extracted Successfully")
        # Extract .zip file
    if zip_file_path.endswith(".zip"):
        # Open the zip file in read mode
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            
            # zip_file = tk.Label(root,text = "Zip Extraction Started")
            # zip_file.place(relx=0.6,rely=0.6)
            # Extract all files and folders to the destination folder
            zip_ref.extractall(destination_folder)
            messagebox.showinfo("Result",f"Zip file Extracted Successfully")
            # result_label.config(text="Zip file Extration Started.")
        
        with lzma.open(zip_file_path) as f_in:
            with open(destination_folder, 'wb') as f_out:
                f_out.write(f_in.read())

    # # Extract .7z file
    # elif zip_file_path.endswith(".7z"):
    #     # Open the .7z file in read mode
    #     with py7zr.SevenZipFile(zip_file_path, mode='r') as szf:
    #         # Extract all files and folders to the destination folder
    #         szf.extractall(path=destination_folder)
    #         result_label.config(text=".7z file extracted successfully.")
    else:
        messagebox.showerror("Error", "Invalid file format. Please select .zip or .7z file.")
    
    

# Create the main window
root = tk.Tk()
root.title("Zip File Extractor")

root.minsize(width=300,height=200)

# Create labels and input fields for zip file and destination folder
zip_file_label = tk.Label(root, text="Zip File Path:")
zip_file_label.grid(row=0, column=0, padx=10, pady=10)


zip_file_entry = tk.Entry(root, width=50)
zip_file_entry.grid(row=0, column=1, padx=10, pady=10)


browse_zip_file_button = tk.Button(root, text="Browse", command=browse_file)
browse_zip_file_button.grid(row=0, column=2, padx=10, pady=10)
browse_zip_file_button.bind("<Enter>", lambda event: show_tooltip(browse_zip_file_button, "Please insert zip file"))

dest_folder_label = tk.Label(root, text="Destination Folder:")
dest_folder_label.grid(row=1, column=0, padx=10, pady=10)


dest_folder_entry = tk.Entry(root, width=50)
dest_folder_entry.grid(row=1, column=1, padx=10, pady=10)


browse_dest_folder_button = tk.Button(root, text="Browse", command=browse_folder)
browse_dest_folder_button.grid(row=1, column=2, padx=10, pady=10)
browse_dest_folder_button.bind("<Enter>", lambda event: show_tooltip(browse_dest_folder_button, "Please select Destination Folder "))

# zip_file = tk.Label(root,text = "Zip Extraction Started")
# zip_file.place(relx=0.6,rely=0.6)


# Create OK and Cancel buttons
ok_button = tk.Button(root, text="Submit", command=extract_zip_file)
ok_button.place(relx=0.35,rely=0.7,relwidth=0.17,relheight=0.17)




cancel_button = tk.Button(root, text="Cancel", command=root.quit)
cancel_button.place(relx=0.6,rely=0.7,relwidth=0.17,relheight=0.17)

# Create a label for displaying the result
result_label = tk.Label(root, text="")
result_label.place(relx=0.6,rely=0.7)

root.mainloop()

