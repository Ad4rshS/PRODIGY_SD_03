import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, 'r') as file:
                contacts = json.load(file)
                if isinstance(contacts, list):
                    return contacts
                else:
                    return list(contacts.values())
        except Exception as e:
            print(f"Error loading contacts: {e}")
            return []
    return []

def save_contacts(contacts):
    try:
        with open(CONTACTS_FILE, 'w') as file:
            json.dump(contacts, file, indent=4)
    except Exception as e:
        print(f"Error saving contacts: {e}")

def add_contact():
    name = simpledialog.askstring("Input", "Enter name:")
    if not name:
        return
    phone = simpledialog.askstring("Input", "Enter phone number:")
    if not phone:
        return
    email = simpledialog.askstring("Input", "Enter email address:")
    if not email:
        return
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    update_contact_list()
    messagebox.showinfo("Success", "Contact added.")

def view_contacts():
    contact_list.delete(0, tk.END)
    if not contacts:
        contact_list.insert(tk.END, "No contacts available.")
    for serial, info in enumerate(contacts, start=1):
        contact_list.insert(tk.END, f"Serial: {serial}, Name: {info['name']}, Phone: {info['phone']}, Email: {info['email']}")

def edit_contact():
    selected_serial = simpledialog.askinteger("Input", "Enter the serial number of the contact you want to edit:")
    if not selected_serial or selected_serial < 1 or selected_serial > len(contacts):
        messagebox.showerror("Error", "Invalid serial number.")
        return
    index = selected_serial - 1
    name = simpledialog.askstring("Input", "Enter new name:", initialvalue=contacts[index]['name'])
    if not name:
        return
    phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=contacts[index]['phone'])
    if not phone:
        return
    email = simpledialog.askstring("Input", "Enter new email address:", initialvalue=contacts[index]['email'])
    if not email:
        return
    contacts[index] = {'name': name, 'phone': phone, 'email': email}
    save_contacts(contacts)
    update_contact_list()
    messagebox.showinfo("Success", "Contact updated.")

def delete_contact():
    selected_serial = simpledialog.askinteger("Input", "Enter the serial number of the contact you want to delete:")
    if not selected_serial or selected_serial < 1 or selected_serial > len(contacts):
        messagebox.showerror("Error", "Invalid serial number.")
        return
    index = selected_serial - 1
    del contacts[index]
    save_contacts(contacts)
    update_contact_list()
    messagebox.showinfo("Success", "Contact deleted.")

def update_contact_list():
    contact_list.delete(0, tk.END)
    if not contacts:
        contact_list.insert(tk.END, "No contacts available.")
    else:
        for serial, info in enumerate(contacts, start=1):
            contact_list.insert(tk.END, f"Serial: {serial}, Name: {info['name']}, Phone: {info['phone']}, Email: {info['email']}")

# Debugging: Print contacts to verify correct loading
contacts = load_contacts()  # Initialize contacts list
print(f"Loaded contacts: {contacts}")

root = tk.Tk()
root.title("Contact Manager")

frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

contact_list = tk.Listbox(frame, width=55)
contact_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame, orient="vertical")
scrollbar.config(command=contact_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

contact_list.config(yscrollcommand=scrollbar.set)

update_contact_list()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact)
add_button.grid(row=0, column=0, padx=5)

view_button = tk.Button(button_frame, text="View Contacts", command=view_contacts)
view_button.grid(row=0, column=1, padx=5)

edit_button = tk.Button(button_frame, text="Edit Contact", command=edit_contact)
edit_button.grid(row=0, column=2, padx=5)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact)
delete_button.grid(row=0, column=3, padx=5)

root.mainloop()
