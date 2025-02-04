import tkinter as tk
from tkinter import messagebox
from database import add_user, delete_user, update_user, get_users
from user import hash_password
from system_info import get_system_info


class UserManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des utilisateurs")
        self.create_widgets()

    def create_widgets(self):
        self.create_user_form()
        self.create_user_list()
        self.create_system_info()
        self.load_users()

    def create_user_form(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Nom d'utilisateur:").grid(row=0, column=0)
        self.username_entry = tk.Entry(frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(frame, text="Mot de passe:").grid(row=1, column=0)
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Label(frame, text="Email:").grid(row=2, column=0)
        self.email_entry = tk.Entry(frame)
        self.email_entry.grid(row=2, column=1)

        tk.Label(frame, text="Rôle:").grid(row=3, column=0)
        self.role_entry = tk.Entry(frame)
        self.role_entry.grid(row=3, column=1)

        tk.Button(frame, text="Ajouter", command=self.add_user).grid(row=4, column=0, pady=10)
        tk.Button(frame, text="Mettre à jour", command=self.update_user).grid(row=4, column=1, pady=10)
        tk.Button(frame, text="Supprimer", command=self.delete_user).grid(row=5, column=0, columnspan=2, pady=10)

    def create_user_list(self):
        self.user_list = tk.Listbox(self.root, width=50)
        self.user_list.pack(pady=20)
        self.user_list.bind('<<ListboxSelect>>', self.load_selected_user)

    def create_system_info(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Informations Système").grid(row=0, column=0, columnspan=2)

        self.system_info_text = tk.Text(frame, height=10, width=50)
        self.system_info_text.grid(row=1, column=0, columnspan=2)

        self.update_system_info()

    def update_system_info(self):
        info = get_system_info()
        info_text = f"Utilisation CPU: {info['cpu_percent']}%\n"
        info_text += f"Utilisation Mémoire: {info['memory_percent']}%\n"
        info_text += f"Utilisation Disque: {info['disk_usage']}%\n"
        info_text += f"Adresse IP: {info['ip_address']}\n"
        self.system_info_text.delete(1.0, tk.END)
        self.system_info_text.insert(tk.END, info_text)
        self.root.after(5000, self.update_system_info)  # Mise à jour toutes les 5 secondes

    def add_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        role = self.role_entry.get()

        if username and password and email and role:
            hashed_password = hash_password(password)
            add_user(username, hashed_password, email, role)
            self.load_users()
        else:
            messagebox.showerror("Erreur", "Tous les champs sont requis")

    def update_user(self):
        selected_user = self.user_list.curselection()
        if not selected_user:
            messagebox.showerror("Erreur", "Sélectionnez un utilisateur à mettre à jour")
            return

        user_id = self.user_list.get(selected_user).split()[0]
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        role = self.role_entry.get()

        if username and password and email and role:
            hashed_password = hash_password(password)
            update_user(user_id, username, hashed_password, email, role)
            self.load_users()
        else:
            messagebox.showerror("Erreur", "Tous les champs sont requis")

    def delete_user(self):
        selected_user = self.user_list.curselection()
        if not selected_user:
            messagebox.showerror("Erreur", "Sélectionnez un utilisateur à supprimer")
            return

        user_id = self.user_list.get(selected_user).split()[0]
        delete_user(user_id)
        self.load_users()

    def load_users(self):
        self.user_list.delete(0, tk.END)
        users = get_users()
        for user in users:
            self.user_list.insert(tk.END, f"{user[0]} {user[1]}")

    def load_selected_user(self, event):
        selected_user = self.user_list.curselection()
        if not selected_user:
            return

        user_id = self.user_list.get(selected_user).split()[0]
        users = get_users()
        for user in users:
            if str(user[0]) == user_id:
                self.username_entry.delete(0, tk.END)
                self.username_entry.insert(0, user[1])
                self.password_entry.delete(0, tk.END)
                self.password_entry.insert(0, '')
                self.email_entry.delete(0, tk.END)
                self.email_entry.insert(0, user[3])
                self.role_entry.delete(0, tk.END)
                self.role_entry.insert(0, user[4])


if __name__ == "__main__":
    root = tk.Tk()
    app = UserManagementApp(root)
    root.mainloop()
