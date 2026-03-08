<h1 align="center">
    Lunar Client 工具
</h1>
<p align="center">
    <strong>用于自动化 LunarClient 简单任务的 Python 工具</strong></br>
    <a href="https://github.com/GrushTom/LunarClientTools/releases">查看发布</a>
    ·
    <a href="https://github.com/GrushTom/LunarClientTools/issues">报告问题</a>
    ·
    <a href="https://github.com/GrushTom/LunarClientTools/issues">请求功能</a>

</p>
<p align="center">
    <a href=https://github.com/GrushTom/LunarClientTools/releases><img align=center src="https://img.grushtom.com/file/1772988153163_lct_banner.png" width="900" alt="banner"></a></br>
</p>
<div align="center" style="background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin: 20px 0;">
    <strong>声明：</strong>您同样可以通过<a href="https://github.com/Vaption/LunarClientTools">https://github.com/Vaption/LunarClientTools</a>来获取此文件，我只是在此基础上修改为了中文版并重构为 Python 实现，请支持原作者。
</div>

## 💭 什么是 LCT？

**LunarClientTools** 是一个用 Python 编写的工具，用于自动化与 LunarClient 相关的一些任务，这些任务你也可以手动完成（通过浏览文件）。当前版本的 LCT 提供以下功能：</br>

- [x] 配置文件管理选项
  - [x] 从 <a href=https://github.com/Vaption/LunarClientProfiles>存档</a> 导入配置文件
  - [x] 导出你的配置文件到桌面
  - [x] 列出目录中所有现有的配置文件
  - [x] 自动检测并生成 profile_manager.json
  - [x] 使用给定值手动生成 profile_manager.json
- [x] 清除缓存文件
- [x] 导航到 .lunarclient 文件夹
- [x] 切换 LunarClient 的 GPU 到独立/集成显卡

## 📚 使用方法

LCT 必须以管理员身份运行才能正常工作。这是因为工具的整个目的是复制、删除或写入文件，或修改 Windows 注册表值，这些操作需要管理员权限。该工具是开源的，这意味着你可以在使用前检查代码。

**免责声明：** LunarClientTools 是一个 Windows 工具，这意味着它**仅在 Windows** 上工作，并且随着 LunarClient 启动器的更新（仅允许 Windows 10 及以上版本），该工具也遵循相同的路径。

**LCT 与 LunarClient 无关。**

## 🔧 功能

### 1. 清除缓存文件

- 从 LunarClient 的缓存目录中删除缓存文件
- 这些文件将在 LunarClient 启动时自动重新创建

### 2. 导航到 .lunarclient

- 在 Windows 资源管理器中打开 .lunarclient 文件夹，方便访问客户端文件

### 3. 配置文件管理选项

- **从存档导入配置文件**：从 LunarClientProfiles 仓库下载并安装配置文件
- **列出所有现有配置文件**：显示当前在 LunarClient 设置中可用的所有配置文件
- **自动检测并生成 profile_manager.json**：自动扫描你的配置文件文件夹并生成新的 profile_manager.json 文件
- **手动生成 profile_manager.json**：允许你使用指定的值创建自定义的 profile_manager.json 文件
- **导出你的配置文件到桌面**：将你的配置文件备份到桌面上的文件夹

### 4. 切换 LunarClient 的 GPU

- **独立显卡**：将 LunarClient 设置为使用独立显卡以获得更好的性能
- **集成显卡**：将 LunarClient 设置为使用集成显卡以节省电量

## 📝 许可证

LunarClientTools 使用 <a href="https://github.com/GrushTom/LunarClientTools/blob/main/LICENSE">MIT 许可证</a>。

## 👨‍💻 贡献

该项目是从批处理脚本重构为 Python 实现的，代码结构更加清晰和可维护。只要你在提交拉取请求时提供有效的描述，你就可以为这个项目做出贡献。

## 📖 如何运行

### 方法 1：运行可执行文件（推荐）

1. 从 [发布](https://github.com/GrushTom/LunarClientTools/releases) 页面下载最新版本
2. 解压下载的 zip 文件
3. 右键单击 `LunarClientTools.exe` 并选择"以管理员身份运行"
4. 按照屏幕上的说明选择所需的选项

### 方法 2：直接运行 Python 脚本

1. 确保你的系统已安装 Python 3.7 或更高版本
2. 下载项目文件
3. 右键单击 `LunarClientTools.py` 并选择"以管理员身份运行"
4. 按照屏幕上的说明选择所需的选项

## ⚠️ 重要说明

- 此工具需要管理员权限才能正常运行
- 它仅在 Windows 10 及以上版本上工作
- 在进行任何更改之前，请始终备份你的配置文件
- 工具按原样提供，不提供任何担保

## 🤝 支持

如果你遇到任何问题或有任何疑问，请在 [GitHub 仓库](https://github.com/GrushTom/LunarClientTools/issues) 上打开一个 issue。
