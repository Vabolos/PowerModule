import tkinter as tk
from tkinter import font

def submit_values(ip_entry, subnet_entry, gateway_entry, dns1_entry, dns2_entry):
    ip_address = ip_entry.get()
    subnet_mask = subnet_entry.get()
    default_gateway = gateway_entry.get()
    dns_server1 = dns1_entry.get()
    dns_server2 = dns2_entry.get()

    # You can perform actions with the entered values here
    print("IP Address:", ip_address)
    print("Subnet Mask:", subnet_mask)
    print("Default Gateway:", default_gateway)
    print("Preferred DNS server:", dns_server1)
    print("Alternate DNS server:", dns_server2)
    # Add further processing or configurations with the obtained values

def setup_IPv4(parent):
    # IPv4 Configuration Dialog
    ip_dialog = tk.Toplevel(parent)
    ip_dialog.configure(bg='#242424')  # Set background color to black
    ip_dialog.title("IPv4 Configuration")  # Set the title of the window
    ip_dialog.geometry('400x250')  # Set the initial size of the window

    # Font settings
    custom_font = font.Font(family='Helvetica', size=12)

    # Labels
    tk.Label(ip_dialog, text="IP Address:", fg='white', font=custom_font).grid(row=0, column=0)
    tk.Label(ip_dialog, text="Subnet Mask:", fg='white', font=custom_font).grid(row=1, column=0)
    tk.Label(ip_dialog, text="Default Gateway:", fg='white', font=custom_font).grid(row=2, column=0)
    tk.Label(ip_dialog, text="Preferred DNS server:", fg='white', font=custom_font).grid(row=3, column=0)
    tk.Label(ip_dialog, text="Alternate DNS server:", fg='white', font=custom_font).grid(row=4, column=0)

    # Entry boxes
    ip_entry = tk.Entry(ip_dialog, font=custom_font)
    subnet_entry = tk.Entry(ip_dialog, font=custom_font)
    gateway_entry = tk.Entry(ip_dialog, font=custom_font)
    dns1_entry = tk.Entry(ip_dialog, font=custom_font)
    dns2_entry = tk.Entry(ip_dialog, font=custom_font)

    ip_entry.grid(row=0, column=1)
    subnet_entry.grid(row=1, column=1)
    gateway_entry.grid(row=2, column=1)
    dns1_entry.grid(row=3, column=1)
    dns2_entry.grid(row=4, column=1)

    # Submit button
    submit_button = tk.Button(ip_dialog, text="Submit", command=lambda: submit_values(ip_entry, subnet_entry, gateway_entry, dns1_entry, dns2_entry), bg='darkgreen', fg='white', font=custom_font)
    submit_button.grid(row=5, columnspan=2)
    # close window on submit and print values
    submit_button.bind('<Return>', lambda event: submit_values(ip_entry, subnet_entry, gateway_entry, dns1_entry, dns2_entry))