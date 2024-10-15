from database import create_table
from gui import UserManagementApp
import tkinter as tk

if __name__ == "__main__":
    create_table()
    root = tk.Tk()
    app = UserManagementApp(root)
    root.mainloop()
