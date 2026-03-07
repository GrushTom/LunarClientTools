⚠️ 提示：当前文件有且只能在C盘环境下运行 ⚠️

<h1 align="center">
    Lunar Client Tools
</h1>
<p align="center">
    <strong>Simple Batch Script to Automate Simple <a href="https://lunarclient.com">LunarClient</a> Tasks</strong></br>
    <a href="https://github.com/GrushTom/LunarClientTools/releases">View Releases</a>
    ·
    <a href="https://github.com/GrushTom/LunarClientTools/issues">Report a Bug</a>
    ·
    <a href="https://github.com/GrushTom/LunarClientTools/issues">Request Feature</a>

</p>
<div align="center" style="background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin: 20px 0;">
    <strong>声明：</strong>您同样可以通过<a href="https://github.com/Vaption/LunarClientTools">https://github.com/Vaption/LunarClientTools</a>来获取此文件，我只是在此基础上修改为了中文版，支持原作者。
</div>

## 💭 What is LCT?

**LunarClientTools** is a simple batch script to automate few tasks related to the client, which </br>you are already able to do manually (by going through the files). The current release of LCT provides the following: </br>

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

LCT has to be ran as administrator for it to work properly. This is because the entire purpose of the script is to either copy, delete, or write files, or modify Windows registry values, which require administrative privileges. The script is open-source, which means you can check the code before using it.

**Disclaimer:** LunarClientTools is a batch script, which means it works **only on Windows**, and as of LunarClient's launcher update (which only allows Windows 10 or above), the script also follows the same path.

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

  LunarClientTools is licensed under the <a href="https://github.com/Vaption/LunarClientTools/blob/main/LICENSE">MIT license</a>.

  ## 👨‍💻 Contributing

  I made LunarClientTools without _any_ coding knowledge, based on my findings on how batch works, on Google or with the help of AI. You're allowed to contribute to this project as long as you provide a valid description while submitting your pull request.

  ## 📖 How to Run

1. Download the latest release from the [Releases](https://github.com/GrushTom/LunarClientTools/releases) page
2. Extract the downloaded zip file
3. Right-click on `LunarClientTools.bat` and select "Run as administrator"
4. Follow the on-screen instructions to select the desired option

## ⚠️ Important Notes

- This script requires administrative privileges to function correctly
- It only works on Windows 10 and above
- Always make a backup of your profiles before making any changes
- The script is provided as-is, without any warranty

  ## 🤝 Support

  If you encounter any issues or have any questions, please open an issue on the [GitHub repository](https://github.com/GrushTom/LunarClientTools/issues).
