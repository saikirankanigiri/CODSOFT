import tkinter as tk
from tkinter import messagebox, simpledialog


class Contact:
    def __init__(self, name, phone, email, address):
        self.name, self.phone, self.email, self.address = name, phone, email, address


class ContactManagerApp:
    def __init__(self, root):
        self.root, self.contacts = root, []
        self.root.title("Contact Manager")
        self.create_widgets()

    def create_widgets(self):
        labels_and_entries = [("Name:", 0), ("Phone:", 1), ("Email:", 2), ("Address:", 3)]
        for label, row in labels_and_entries:
            lbl = tk.Label(self.root, text=label)
            lbl.grid(row=row, column=0, padx=10, pady=5)
            entry = tk.Entry(self.root)
            entry.grid(row=row, column=1, padx=10, pady=5)
            setattr(self, label.lower().split(":")[0] + "_entry", entry)

        buttons = [("Add Contact", self.add_contact), ("View Contacts", self.view_contacts),
                   ("Search Contact", self.search_contact), ("Update Contact", self.update_contact),
                   ("Delete Contact", self.delete_contact)]
        for txt, cmd in buttons:
            button = tk.Button(self.root, text=txt, command=cmd)
            button.grid(row=4 + buttons.index((txt, cmd)), columnspan=2, padx=10, pady=5, sticky="we")

        self.view_shell = tk.Text(self.root, width=40, height=10)
        self.view_shell.grid(row=0, column=2, rowspan=9, padx=10, pady=5, sticky="ns")

    def add_contact(self):
        name, phone, email, address = (getattr(self, label.lower().split(":")[0] + "_entry").get()
                                       for label, _ in [("Name:", 0), ("Phone:", 1), ("Email:", 2), ("Address:", 3)])
        if name and phone:
            contact = Contact(name, phone, email, address)
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        self.view_shell.delete(1.0, tk.END)
        self.view_shell.insert(tk.END, "\n\n".join(f"Name: {c.name}\nPhone: {c.phone}\nEmail: {c.email}\nAddress: {c.address}"
                                                   for c in self.contacts) or "No contacts found.")

    def search_contact(self):
        search_query = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_query:
            self.view_shell.delete(1.0, tk.END)
            found_contacts = [c for c in self.contacts if search_query.lower() in c.name.lower() or search_query in c.phone]
            self.view_shell.insert(tk.END, "\n\n".join(f"Name: {c.name}\nPhone: {c.phone}\nEmail: {c.email}\nAddress: {c.address}"
                                                       for c in found_contacts) or "No contacts found.")

    def update_contact(self):
        search_query = simpledialog.askstring("Update Contact", "Enter name or phone number:")
        if search_query:
            found_contacts = [c for c in self.contacts if search_query.lower() in c.name.lower() or search_query in c.phone]
            if found_contacts:
                contact = found_contacts[0]
                attrs = [("name", "Enter new name:"), ("phone", "Enter new phone number:"),
                         ("email", "Enter new email:"), ("address", "Enter new address:")]
                for attr, prompt in attrs:
                    updated_value = simpledialog.askstring("Update Contact", prompt, initialvalue=getattr(contact, attr))
                    setattr(contact, attr, updated_value if updated_value else getattr(contact, attr))
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showinfo("Error", "Contact not found.")

    def delete_contact(self):
        search_query = simpledialog.askstring("Delete Contact", "Enter name or phone number:")
        if search_query:
            found_contacts = [c for c in self.contacts if search_query.lower() in c.name.lower() or search_query in c.phone]
            if found_contacts:
                self.contacts.remove(found_contacts[0])
                messagebox.showinfo("Success", "Contact deleted successfully!")
            else:
                messagebox.showinfo("Error", "Contact not found.")

    def clear_entries(self):
        for entry in (self.name_entry, self.phone_entry, self.email_entry, self.address_entry):
            entry.delete(0, tk.END)


root = tk.Tk()
app = ContactManagerApp(root)
root.mainloop()
