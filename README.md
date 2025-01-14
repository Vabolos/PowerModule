# 🎉 PowerModule 🎉

Welcome to **PowerModule**! This is a powerful and versatile PowerShell module designed to make your automation tasks a breeze. Whether you're running on Windows Servers or regular Windows machines, PowerModule has got you covered.

And guess what? We've recently added an **ADM (Active Directory Manager)** feature that allows you to effortlessly manage Active Directory components! 🎉

## 🚀 Installation

To get started with PowerModule, simply run the following command in your PowerShell terminal:

```powershell
Install-Module -Name PowerModule
```

(Note: This module is still in development, so it might not be available on PowerShell Gallery yet. Stay tuned for updates!)

In the meantime, if you want to contribute or make changes to the code, you can install the dependencies by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

## 🛠️ Usage

Using PowerModule is as easy as pie! Just import the module into your PowerShell session with the following command:

```powershell
Import-Module -Name PowerModule
```

And you're ready to automate! Check out the examples below to see how you can leverage the power of PowerModule.

### Example: Active Directory Management

Want to manage your Active Directory components? No problem! With our new ADM feature, you can do it effortlessly.

```powershell
# Example usage of ADM feature to get all users
Get-ADMUsers

# Example usage of ADM feature to add a new user
Add-ADMUser -Name "John Doe" -Department "IT"
```

Feel the power of automation right at your fingertips! 💪

## 🤝 Contributing

We love contributions! If you have ideas or improvements, feel free to open a pull request. For major changes, please open an issue first to discuss what you'd like to change.

Here's how you can contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

Let's build something amazing together! 🚀

## 📚 Documentation

For more detailed information and advanced usage, check out our [documentation](https://github.com/Vabolos/powermodule/wiki).

## 🌟 Support

If you like PowerModule, please give us a ⭐ on [GitHub](https://github.com/vabolos/powermodule)! Your support means a lot to us.
