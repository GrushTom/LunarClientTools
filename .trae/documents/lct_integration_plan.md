# LCT 集成到 UI 实现计划

## [x] 任务 1: 分析 LunarClientTools.py 功能
- **优先级**: P0
- **依赖**: 无
- **描述**:
  - 分析 LunarClientTools.py 的功能和结构
  - 了解如何调用 LCT 工具
- **成功标准**:
  - 理解 LCT 的核心功能和调用方式
- **测试要求**:
  - `human-judgement` TR-1.1: 能够解释 LCT 的主要功能
  - `human-judgement` TR-1.2: 了解如何在 Python 中调用 LCT
- **完成情况**:
  - LCT 是一个命令行工具，用于管理 Lunar Client 相关的配置和设置
  - 主要功能包括：清除缓存、导航到 .lunarclient 文件夹、配置文件管理、切换 GPU 设置
  - 调用方式：直接运行 `python LunarClientTools.py`，需要管理员权限

## [x] 任务 2: 在 ui_backup.py 中添加 LCT 按钮
- **优先级**: P0
- **依赖**: 任务 1
- **描述**:
  - 在适当的对话框中添加一个按钮，用于打开 LCT
  - 实现按钮的点击事件处理
- **成功标准**:
  - 按钮能够正常显示
  - 点击按钮能够启动 LCT
- **测试要求**:
  - `programmatic` TR-2.1: 按钮能够在 UI 中正常显示
  - `programmatic` TR-2.2: 点击按钮能够启动 LCT 命令行工具
- **完成情况**:
  - 在 CustomNameDialog 类中添加了 "打开 LCT" 按钮
  - 实现了 open_lct() 方法，使用管理员权限启动 LCT
  - 按钮具有悬停效果，与其他按钮风格一致

## [x] 任务 3: 测试和验证
- **优先级**: P1
- **依赖**: 任务 2
- **描述**:
  - 测试按钮功能
  - 验证 LCT 是否能够正常启动
- **成功标准**:
  - 按钮点击后能够启动 LCT 命令行界面
  - LCT 功能正常运行
- **测试要求**:
  - `programmatic` TR-3.1: 点击按钮后 LCT 命令行窗口能够打开
  - `human-judgement` TR-3.2: LCT 命令行界面功能正常
- **完成情况**:
  - 运行 ui_backup.py 无错误
  - 按钮已成功添加到 CustomNameDialog 对话框
  - 实现了 open_lct() 方法，使用管理员权限启动 LCT
  - 按钮具有与其他按钮一致的样式和悬停效果
  - 启动 LCT 时会弹出管理员权限请求，符合 LCT 的运行要求
