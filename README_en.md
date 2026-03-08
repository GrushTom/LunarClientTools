<h1 align="center">
    Lunar Client Tools
</h1>
<p align="center">
    <strong>Python Tool to Automate Simple <a href="https://lunarclient.com">LunarClient</a> Tasks</strong></br>
    <a href="https://github.com/GrushTom/LunarClientTools/releases">View Releases</a>
    ·
    <a href="https://github.com/GrushTom/LunarClientTools/issues">Report a Bug</a>
    ·
    <a href="https://github.com/GrushTom/LunarClientTools/issues">Request Feature</a>

</p>

<p align="center">
    <a href=https://github.com/GrushTom/LunarClientTools/releases><img align=center src=".github/lct_banner.png" width="900" alt="banner"></a></br>
</p>

<div align="center" style="background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin: 20px 0;">
    <strong>Declaration:</strong> You can also get this file through <a href="https://github.com/Vaption/LunarClientTools">https://github.com/Vaption/LunarClientTools</a>, I just modified it to be in Chinese and refactored it to Python implementation, support the original author.
</div>

## 💭 What is LCT?

**LunarClientTools** is a Python-based tool to automate tasks related to LunarClient, which you are already able to do manually (by going through the files). The current release of LCT provides the following: </br>

- [x] Profile Management Options
  - [x] Import Profiles From <a href=https://github.com/Vaption/LunarClientProfiles>the Archive</a>
  - [x] Export Your Profiles to Your Desktop
  - [x] List All Present Profiles in the Directory
  - [x] Auto-Detect and Generate profile_manager.json
  - [x] Manually Generate profile_manager.json with Given Values
- [x] Clear Cached Files
- [x] Navigate to .lunarclient
- [x] Switch LunarClient's GPU to Dedicated/Integrated

## 📚 Usage

LCT has to be ran as administrator for it to work properly. This is because the entire purpose of the tool is to either copy, delete, or write files, or modify Windows registry values, which require administrative privileges. The tool is open-source, which means you can check the code before using it.

**Disclaimer:** LunarClientTools is a Windows tool, which means it works **only on Windows**, and as of LunarClient's launcher update (which only allows Windows 10 or above), the tool also follows the same path.

**LCT is not affiliated with LunarClient.**

## 🔧 Features

### 1. Clear Cached Files

- Removes cached files from LunarClient's cache directory
- These files will be automatically recreated when LunarClient is launched

### 2. Navigate to .lunarclient

- Opens the .lunarclient folder in Windows Explorer for easy access to client files

### 3. Profile Management Options

- **Import Profiles From Archive**: Downloads and installs profiles from the LunarClientProfiles repository
- **List All Present Profiles**: Displays all profiles currently available in your LunarClient settings
- **Auto-Detect and Generate profile_manager.json**: Automatically scans your profiles folder and generates a new profile_manager.json file
- **Manually Generate profile_manager.json**: Allows you to create a custom profile_manager.json file with your specified values
- **Export Your Profiles to Desktop**: Backs up your profiles to a folder on your desktop

### 4. Switch LunarClient's GPU

- **Dedicated GPU**: Sets LunarClient to use your dedicated graphics card for better performance
- **Integrated GPU**: Sets LunarClient to use your integrated graphics card for power savings

## 📝 License

LunarClientTools is licensed under the <a href="https://github.com/GrushTom/LunarClientTools/blob/main/LICENSE">MIT license</a>.

## 👨‍💻 Contributing

This project has been refactored from a batch script to a Python implementation, resulting in a more structured and maintainable codebase. You're allowed to contribute to this project as long as you provide a valid description while submitting your pull request.

## 📖 How to Run

### Method 1: Run the Executable (Recommended)

1. Download the latest release from the [Releases](https://github.com/GrushTom/LunarClientTools/releases) page
2. Extract the downloaded zip file
3. Right-click on `LunarClientTools.exe` and select "Run as administrator"
4. Follow the on-screen instructions to select the desired option

### Method 2: Run the Python Script Directly

1. Ensure your system has Python 3.7 or higher installed
2. Download the project files
3. Right-click on `LunarClientTools.py` and select "Run as administrator"
4. Follow the on-screen instructions to select the desired option

## ⚠️ Important Notes

- This tool requires administrative privileges to function correctly
- It only works on Windows 10 and above
- Always make a backup of your profiles before making any changes
- The tool is provided as-is, without any warranty

## 🤝 Support

If you encounter any issues or have any questions, please open an issue on the [GitHub repository](https://github.com/GrushTom/LunarClientTools/issues).
