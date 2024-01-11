import tkinter as tk

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
    print("DNS Server 1:", dns_server1)
    print("DNS Server 2:", dns_server2)
    # Add further processing or configurations with the obtained values

def setup_IPv4(parent):
    # IPv4 Configuration Dialog
    ip_dialog = tk.Toplevel(parent)

    # Labels
    tk.Label(ip_dialog, text="IP Address:").grid(row=0, column=0)
    tk.Label(ip_dialog, text="Subnet Mask:").grid(row=1, column=0)
    tk.Label(ip_dialog, text="Default Gateway:").grid(row=2, column=0)
    tk.Label(ip_dialog, text="DNS Server 1:").grid(row=3, column=0)
    tk.Label(ip_dialog, text="DNS Server 2:").grid(row=4, column=0)

    # Entry boxes
    ip_entry = tk.Entry(ip_dialog)
    subnet_entry = tk.Entry(ip_dialog)
    gateway_entry = tk.Entry(ip_dialog)
    dns1_entry = tk.Entry(ip_dialog)
    dns2_entry = tk.Entry(ip_dialog)

    ip_entry.grid(row=0, column=1)
    subnet_entry.grid(row=1, column=1)
    gateway_entry.grid(row=2, column=1)
    dns1_entry.grid(row=3, column=1)
    dns2_entry.grid(row=4, column=1)

    # Submit button
    submit_button = tk.Button(ip_dialog, text="Submit", command=lambda: submit_values(ip_entry, subnet_entry, gateway_entry, dns1_entry, dns2_entry))
    submit_button.grid(row=5, columnspan=2)
