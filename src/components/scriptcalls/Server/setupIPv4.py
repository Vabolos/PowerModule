import tkinter as tk
from tkinter import ttk

def submit_values(ip_entry, subnet_entry, gateway_entry, dns1_entry, dns2_entry):
    ip_address = ip_entry.get()
    subnet_mask = subnet_entry.get()
    default_gateway = gateway_entry.get()
    dns_server1 = dns1_entry.get()
    dns_server2 = dns2_entry.get()

    # You can perform actions with the entered values here
    print("IP Address:          ", ip_address)
    print("Subnet Mask:         ", subnet_mask)
    print("Default Gateway:     ", default_gateway)
    print("Preferred DNS server:", dns_server1)
    print("Alternate DNS server:", dns_server2)

def calculate_subnet(ip_address):
    # Calculate subnet mask based on the network class of the IP address
    octets = list(map(int, ip_address.split('.')))

    if 1 <= octets[0] <= 126:
        subnet_mask = '255.0.0.0'
    elif 128 <= octets[0] <= 191:
        subnet_mask = '255.255.0.0'
    elif 192 <= octets[0] <= 223:
        subnet_mask = '255.255.255.0'
    else:
        subnet_mask = 'Invalid IP'

    return subnet_mask

def update_subnet_mask(ip_entry, subnet_entry):
    ip_address = ip_entry.get()
    subnet_mask = calculate_subnet(ip_address)
    subnet_entry.delete(0, tk.END)  # Clear the existing value
    subnet_entry.insert(0, subnet_mask)  # Set the calculated subnet mask

def setup_IPv4(parent):
    # IPv4 Configuration Dialog
    ip_dialog = tk.Toplevel(parent)
    ip_dialog.title("IPv4 Configuration")
    ip_dialog.geometry('400x250')
    ip_dialog.configure(bg='#242424')  # Set the background color to dark gray
    ip_dialog.iconbitmap("powermodule.ico")  # Set the icon to the powermodule icon
    ip_dialog.resizable(False, False)  # Disable resizing of the window
    ip_dialog.focus_force()  # Set focus to the dialog window

    # Style configuration
    style = ttk.Style()
    # remove label hightlighting
    style.map('TLabel', background=[('!active', '#242424')])
    style.configure('TLabel', font=('Helvetica', 12, 'bold'), foreground='#ffffff')
    style.configure('TFrame', background='#242424')  # Set the background color of frames
    style.configure('TEntry', font=('Helvetica', 12), fieldbackground='#1d1e1e', foreground='#1d1e1e', highlightthickness=0)  # Set entry box colors and remove border
    style.configure('TButton', font=('Helvetica', 12), background='#242424', foreground='#1d1e1e', highlightthickness=0)  # Set button colors and remove border

    # Labels
    ttk.Label(ip_dialog, text="IP Address:          ").grid(row=0, column=0, padx=10, pady=5, sticky='w')
    ttk.Label(ip_dialog, text="Subnet Mask:         ").grid(row=1, column=0, padx=10, pady=5, sticky='w')
    ttk.Label(ip_dialog, text="Default Gateway:     ").grid(row=2, column=0, padx=10, pady=5, sticky='w')
    ttk.Label(ip_dialog, text="Preferred DNS server:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
    ttk.Label(ip_dialog, text="Alternate DNS server:").grid(row=4, column=0, padx=10, pady=5, sticky='w')

    # Entry boxes
    ip_entry = ttk.Entry(ip_dialog, font=('Helvetica', 12))
    subnet_entry = ttk.Entry(ip_dialog, font=('Helvetica', 12))
    gateway_entry = ttk.Entry(ip_dialog, font=('Helvetica', 12))
    dns1_entry = ttk.Entry(ip_dialog, font=('Helvetica', 12))
    dns2_entry = ttk.Entry(ip_dialog, font=('Helvetica', 12))

    ip_entry.grid(row=0, column=1, padx=10, pady=5)
    subnet_entry.grid(row=1, column=1, padx=10, pady=5)
    gateway_entry.grid(row=2, column=1, padx=10, pady=5)
    dns1_entry.grid(row=3, column=1, padx=10, pady=5)
    dns2_entry.grid(row=4, column=1, padx=10, pady=5)

    # Bind an event to update the subnet mask when the IP address changes
    ip_entry.bind('<KeyRelease>', lambda event: update_subnet_mask(ip_entry, subnet_entry))


    # Submit button
    submit_button = ttk.Button(ip_dialog, text="Submit", command=lambda: submit_values(ip_entry, subnet_entry, gateway_entry, dns1_entry, dns2_entry))
    submit_button.grid(row=5, columnspan=2, pady=10)
    
    # Close dialog on enter key press
    ip_dialog.bind('<Return>', lambda event: submit_values(ip_entry, subnet_entry, gateway_entry, dns1_entry, dns2_entry))
