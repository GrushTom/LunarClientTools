#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LunarClientTools v1.9 Python 版本
https://github.com/GrushTom/LunarClientTools

MIT License
Copyright (c) 2024 GrushTom ✨

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import ctypes
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

class Color:
    GREEN = "\033[92m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    END = "\033[0m"

class LunarClientTools:
    def __init__(self):
        self.home_dir = Path.home()
        self.lunar_dir = self.home_dir / ".lunarclient"
        self.settings_dir = self.lunar_dir / "settings" / "game"
        self.cache_dir = self.lunar_dir / ".lct-cache"
    
    def is_admin(self):
        """检查是否以管理员权限运行"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    
    def run_as_admin(self):
        """以管理员权限重新运行"""
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
    
    def clear_screen(self):
        """清屏函数"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def pause(self):
        """等待用户输入"""
        input("按回车键继续...")
    
    def print_header(self):
        """打印头部信息"""
        print(f"{Color.CYAN}###################################################################{Color.END}")
        print(f"{Color.CYAN}##                  Lunar Client Tools                           ##{Color.END}")
        print(f"{Color.CYAN}##          https://github.com/GrushTom/LunarClientTools         ##{Color.END}")
        print(f"{Color.CYAN}###################################################################{Color.END}")
        print()
    
    def main_menu(self):
        """主菜单"""
        while True:
            self.clear_screen()
            self.print_header()
            print(f"{Color.YELLOW}您想要做什么？{Color.END}")
            print()
            print(f"{Color.RED}1.{Color.END} 清除缓存文件")
            print(f"{Color.RED}2.{Color.END} 导航到 .lunarclient 文件夹")
            print(f"{Color.RED}3.{Color.END} 配置文件管理选项")
            print(f"{Color.RED}4.{Color.END} 切换 LunarClient 的 GPU 为独立/集成显卡")
            print(f"{Color.RED}5.{Color.END} 退出")
            print()
            
            choice = input(f"{Color.CYAN}请输入 1-5 然后按回车键:{Color.END} ")
            
            if choice == "1":
                self.clear_cache()
            elif choice == "2":
                self.open_lunar_folder()
            elif choice == "3":
                self.json_menu()
            elif choice == "4":
                self.gpu_switch()
            elif choice == "5":
                exit()
            else:
                print("无效的选择，请重新输入")
                self.pause()
    
    def json_menu(self):
        """配置文件管理菜单"""
        while True:
            self.clear_screen()
            self.print_header()
            print(f"{Color.YELLOW}配置文件管理选项{Color.END}")
            print()
            print(f"{Color.RED}1.{Color.END} 从存档导入配置文件")
            print(f"{Color.RED}2.{Color.END} 列出目录中所有现有的配置文件")
            print(f"{Color.RED}3.{Color.END} 自动检测配置文件并替换当前配置文件管理器")
            print(f"{Color.RED}4.{Color.END} 手动配置文件管理器生成器")
            print(f"{Color.RED}5.{Color.END} 导出当前配置文件到桌面")
            print(f"{Color.RED}6.{Color.END} 取消")
            print()
            
            choice = input(f"{Color.CYAN}请输入 1-6 然后按回车键:{Color.END} ")
            
            if choice == "1":
                self.import_profile_from_archive()
            elif choice == "2":
                self.list_profiles()
            elif choice == "3":
                self.auto_generate_profile_manager()
            elif choice == "4":
                self.manual_generate_profile_manager()
            elif choice == "5":
                self.export_profiles_to_desktop()
            elif choice == "6":
                break
            else:
                print("无效的选择，请重新输入")
                self.pause()
    
    def clear_cache(self):
        """清除缓存文件"""
        self.clear_screen()
        print()
        print()
        print()
        confirm = input("确定要继续吗？按 Y 继续，按 C 取消: ")
        
        if confirm.lower() == "y":
            cache_path = self.lunar_dir / "offline" / "multiver" / "cache"
            if cache_path.exists():
                for file in cache_path.iterdir():
                    if file.is_file():
                        try:
                            file.unlink()
                        except Exception as e:
                            print(f"{Color.RED}删除文件时出错: {e}{Color.END}")
                print(f"{Color.GREEN}成功删除 LunarClient 游戏缓存。{Color.END}")
            else:
                print(f"{Color.YELLOW}缓存文件夹不存在。{Color.END}")
        
        print()
        print()
        print()
        self.pause()
    
    def open_lunar_folder(self):
        """导航到 .lunarclient 文件夹"""
        self.clear_screen()
        print()
        print()
        print()
        if self.lunar_dir.exists():
            subprocess.run(["explorer.exe", str(self.lunar_dir)])
            print(f"{Color.GREEN}成功在新窗口中打开 .lunarclient。{Color.END}")
        else:
            print(f"{Color.RED}.lunarclient 文件夹不存在。{Color.END}")
        
        print()
        print()
        print()
        self.pause()
    
    def import_profile_from_archive(self):
        """从存档导入配置文件"""
        self.clear_screen()
        
        # 清理缓存目录
        if self.cache_dir.exists():
            for file in self.cache_dir.iterdir():
                try:
                    if file.is_file():
                        file.unlink()
                except Exception as e:
                    print(f"删除缓存文件时出错: {e}")
            try:
                self.cache_dir.rmdir()
            except Exception as e:
                print(f"删除缓存目录时出错: {e}")
        
        # 创建缓存目录
        try:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"创建缓存目录时出错: {e}")
            self.pause()
            return
        
        # 下载 data.json 文件
        print(f"{Color.CYAN}正在从存档下载配置文件信息...{Color.END}")
        try:
            import urllib.request
            url = "https://raw.githubusercontent.com/Vaption/LunarClientProfiles/main/profiles/data.json"
            filename = self.cache_dir / "data.json"
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            print(f"{Color.RED}下载配置文件信息时出错: {e}{Color.END}")
            self.pause()
            return
        
        # 解析 data.json 文件并下载链接
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            profiles = data.get('profiles', [])
            for profile in profiles:
                name = profile.get('name')
                link = profile.get('link')
                if name and link:
                    link_file = self.cache_dir / f"{name}.txt"
                    with open(link_file, 'w', encoding='utf-8') as f:
                        f.write(link)
        except Exception as e:
            print(f"{Color.RED}解析配置文件信息时出错: {e}{Color.END}")
            self.pause()
            return
        
        self.clear_screen()
        self.print_header()
        print(f"{Color.CYAN}正在扫描当前可用的配置文件...{Color.END}")
        
        # 检查配置文件数量
        if self.settings_dir.exists():
            profiles = [d for d in self.settings_dir.iterdir() if d.is_dir()]
            total_profiles = len(profiles)
            
            if total_profiles > 7:
                print(f"{Color.RED}错误：存在超过七个配置文件！{Color.END}")
                print(f"{Color.RED}允许的最大配置文件数量为八个，无法导入配置文件。{Color.END}")
                print(f"{Color.RED}请导航到 .lunarclient\settings\game 并在运行命令前删除一些配置文件。{Color.END}")
                self.pause()
                return
        else:
            print(f"{Color.RED}.lunarclient 中不存在设置文件夹{Color.END}")
            self.pause()
            return
        
        # 显示可用的配置文件
        print(f"{Color.CYAN}存档中可用的配置文件：{Color.END}")
        profile_files = [f for f in self.cache_dir.iterdir() if f.suffix == '.txt' and f.name != 'linkDisplay.txt']
        profile_names = [f.stem for f in profile_files]
        
        for i, name in enumerate(profile_names, 1):
            print(f"{Color.RED}{i}.{Color.END} {name}")
        
        # 选择配置文件
        choice = input(f"{Color.CYAN}请输入您要导入的配置文件编号: {Color.END}")
        
        try:
            index = int(choice) - 1
            if 0 <= index < len(profile_files):
                selected_file = profile_files[index]
                
                # 读取下载链接
                with open(selected_file, 'r', encoding='utf-8') as f:
                    download_link = f.read().strip()
                
                # 下载并解压配置文件
                print(f"{Color.CYAN}尝试从存档下载配置文件...{Color.END}")
                try:
                    import zipfile
                    import io
                    
                    # 下载文件
                    response = urllib.request.urlopen(download_link)
                    zip_data = io.BytesIO(response.read())
                    
                    # 解压到设置文件夹
                    with zipfile.ZipFile(zip_data, 'r') as zip_ref:
                        # 获取文件名（不含扩展名）作为文件夹名
                        import os.path
                        filename = os.path.basename(download_link)
                        folder_name = os.path.splitext(filename)[0]
                        extract_path = self.settings_dir / folder_name
                        
                        # 确保目标文件夹不存在
                        if extract_path.exists():
                            shutil.rmtree(extract_path)
                        
                        zip_ref.extractall(extract_path)
                    
                    print(f"{Color.GREEN}配置文件导入成功，尝试生成新的 profile_manager.json...{Color.END}")
                    self.auto_generate_profile_manager()
                except Exception as e:
                    print(f"{Color.RED}下载或解压配置文件时出错: {e}{Color.END}")
                    self.pause()
                    return
            else:
                print(f"{Color.RED}所选配置文件不存在。正在退出...{Color.END}")
                self.pause()
                return
        except ValueError:
            print(f"{Color.RED}无效的输入。正在退出...{Color.END}")
            self.pause()
            return
    
    def list_profiles(self):
        """列出目录中所有现有的配置文件"""
        self.clear_screen()
        print()
        print(f"{Color.CYAN}正在扫描您的配置文件目录...{Color.END}")
        
        if self.settings_dir.exists():
            profiles = [d.name for d in self.settings_dir.iterdir() if d.is_dir()]
            count = len(profiles)
            print(f"{Color.YELLOW}您总共有 {count}/8 个配置文件：{Color.END}")
            print()
            for profile in profiles:
                print(f"- {profile}")
        else:
            print(f"{Color.RED}.lunarclient 中不存在设置文件夹{Color.END}")
        
        print()
        print()
        print()
        self.pause()
    
    def auto_generate_profile_manager(self):
        """自动检测配置文件并替换当前配置文件管理器"""
        self.clear_screen()
        
        if not self.settings_dir.exists():
            print(f"{Color.RED}.lunarclient 中不存在设置文件夹{Color.END}")
            print(f"{Color.RED}LCT 无法在您的设置目录中检测到任何配置文件。{Color.END}")
            self.pause()
            return
        
        print(f"{Color.CYAN}正在扫描设置文件夹...{Color.END}")
        
        # 统计配置文件数量
        profiles = [d for d in self.settings_dir.iterdir() if d.is_dir()]
        total_profiles = len(profiles)
        
        # 检查配置文件数量是否超过8个
        if total_profiles > 8:
            print(f"{Color.RED}错误：存在超过八个配置文件！{Color.END}")
            print(f"{Color.RED}请导航到 .lunarclient\settings\game 并在运行命令前删除一些配置文件。{Color.END}")
            # 清理缓存
            self._clean_cache()
            self.pause()
            return
        
        print(f"{Color.YELLOW}在设置文件夹中找到 {total_profiles} 个配置文件。{Color.END}")
        print(f"{Color.CYAN}正在终止启动器进程...{Color.END}")
        
        # 终止 Lunar Client 进程
        try:
            subprocess.run(["taskkill", "/im", "Lunar Client.exe", "/f"], capture_output=True, text=True)
        except Exception as e:
            print(f"{Color.RED}终止进程时出错: {e}{Color.END}")
        
        print(f"{Color.GREEN}任务完成。{Color.END}")
        print(f"{Color.CYAN}正在生成配置文件...{Color.END}")
        
        # 生成 profile_manager.json
        profiles_data = []
        for profile in profiles:
            profile_name = profile.name
            profile_data = {
                "name": profile_name,
                "displayName": profile_name,
                "default": False,
                "active": False,
                "iconName": "",
                "server": ""
            }
            profiles_data.append(profile_data)
        
        # 保存到文件
        profile_manager_path = self.settings_dir / "profile_manager.json"
        try:
            with open(profile_manager_path, 'w', encoding='utf-8') as f:
                json.dump(profiles_data, f, indent=2, ensure_ascii=False)
            print(f"{Color.GREEN}成功生成并替换 profile_manager.json{Color.END}")
            print(f"{Color.GREEN}操作成功。{Color.END}")
        except Exception as e:
            print(f"{Color.RED}生成配置文件时出错: {e}{Color.END}")
        
        # 清理缓存
        self._clean_cache()
        self.pause()
    
    def manual_generate_profile_manager(self):
        """手动配置文件管理器生成器"""
        self.clear_screen()
        
        print(f"{Color.CYAN}请输入要添加的配置文件总数（最大=8）：{Color.END}")
        total_profiles_input = input()
        
        try:
            total_profiles = int(total_profiles_input)
            if total_profiles > 8:
                print(f"{Color.RED}错误：超过最大配置文件数量。请输入 1 到 8 之间的数字。{Color.END}")
                self.pause()
                return
            elif total_profiles < 1:
                print(f"{Color.RED}错误：配置文件数量必须至少为 1。{Color.END}")
                self.pause()
                return
        except ValueError:
            print(f"{Color.RED}错误：无效的输入。请输入一个数字。{Color.END}")
            self.pause()
            return
        
        print(f"{Color.CYAN}正在生成配置文件...{Color.END}")
        print()
        
        # 收集配置文件信息
        profiles_data = []
        for i in range(1, total_profiles + 1):
            print(f"{Color.YELLOW}配置文件 {i}{Color.END}")
            profile_name = input(f"{Color.CYAN}请输入配置文件 %i 的名称：{Color.END} " % i)
            display_name = input(f"{Color.CYAN}请输入配置文件 %i 的显示名称：{Color.END} " % i)
            
            profile_data = {
                "name": profile_name,
                "displayName": display_name,
                "default": (i == 1),
                "active": (i == 1),
                "iconName": "",
                "server": ""
            }
            profiles_data.append(profile_data)
        
        # 保存到桌面
        desktop_path = self.home_dir / "Desktop" / "profile_manager.json"
        try:
            with open(desktop_path, 'w', encoding='utf-8') as f:
                json.dump(profiles_data, f, indent=2, ensure_ascii=False)
            print()
            print(f"{Color.GREEN}成功在您的桌面上生成 profile_manager.json。{Color.END}")
        except Exception as e:
            print(f"{Color.RED}生成配置文件时出错: {e}{Color.END}")
        
        print()
        print()
        self.pause()
    
    def export_profiles_to_desktop(self):
        """导出当前配置文件到桌面"""
        self.clear_screen()
        print()
        print()
        print()
        
        confirm = input(f"{Color.CYAN}确定要继续吗？按 Y 继续，按 C 取消: {Color.END}")
        if confirm.lower() != "y":
            return
        
        # 创建桌面文件夹
        desktop_folder = self.home_dir / "Desktop" / "LCT-Profiles"
        try:
            if desktop_folder.exists():
                shutil.rmtree(desktop_folder)
            desktop_folder.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"{Color.RED}创建文件夹时出错: {e}{Color.END}")
            self.pause()
            return
        
        # 复制配置文件
        if self.settings_dir.exists():
            try:
                # 复制所有文件和文件夹
                for item in self.settings_dir.iterdir():
                    if item.is_dir():
                        shutil.copytree(item, desktop_folder / item.name)
                    else:
                        shutil.copy2(item, desktop_folder)
                
                # 删除不需要的文件
                files_to_delete = [
                    "accounts.json",
                    "alert_manager.json",
                    "features.json",
                    "global_options.json",
                    "internal.json",
                    "knownServers.json",
                    "language.json",
                    "main_menu_theme_manager.json",
                    "metadata_fallback.json",
                    "muted_users.json",
                    "rule-features.json",
                    "statistics.json",
                    "version"
                ]
                
                for file_name in files_to_delete:
                    file_path = desktop_folder / file_name
                    if file_path.exists():
                        try:
                            file_path.unlink()
                        except Exception as e:
                            pass
                
                print(f"{Color.GREEN}成功将您的配置文件复制到桌面。{Color.END}")
                print(f"{Color.YELLOW}文件路径：{desktop_folder}{Color.END}")
                
                # 打开文件夹
                subprocess.run(["explorer.exe", str(desktop_folder)])
            except Exception as e:
                print(f"{Color.RED}复制文件时出错: {e}{Color.END}")
        else:
            print(f"{Color.RED}.lunarclient 中不存在设置文件夹{Color.END}")
        
        print()
        print()
        print()
        self.pause()
    
    def gpu_switch(self):
        """切换 LunarClient 的 GPU"""
        self.clear_screen()
        print()
        print()
        print()
        
        choice = input(f"{Color.CYAN}您想切换到哪种图形处理器？按 D 选择独立显卡，按 I 选择集成显卡: {Color.END}")
        
        if choice.upper() == "D":
            # 切换到独立显卡
            confirm = input(f"{Color.CYAN}确定要继续吗？按 Y 继续，按 C 取消: {Color.END}")
            if confirm.lower() == "y":
                self.set_gpu_preference(2, "高性能模式")
        elif choice.upper() == "I":
            # 切换到集成显卡
            confirm = input(f"{Color.CYAN}确定要继续吗？按 Y 继续，按 C 取消: {Color.END}")
            if confirm.lower() == "y":
                self.set_gpu_preference(1, "节能模式")
        else:
            print(f"{Color.RED}无效的选择。{Color.END}")
            self.pause()
    
    def set_gpu_preference(self, preference, mode_name):
        """设置 GPU 偏好"""
        # 查找 javaw.exe 文件
        javaw_path = self.find_javaw()
        
        if javaw_path:
            try:
                # 修改注册表
                import winreg
                key_path = r"SOFTWARE\Microsoft\DirectX\UserGpuPreferences"
                
                # 打开或创建注册表键
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(key, str(javaw_path), 0, winreg.REG_SZ, f"GpuPreference={preference};")
                winreg.CloseKey(key)
                
                print(f"{Color.GREEN}成功将 LunarClient 的 GPU 切换到{mode_name}。{Color.END}")
            except Exception as e:
                print(f"{Color.RED}修改注册表时出错: {e}{Color.END}")
        else:
            print(f"{Color.RED}LCT 无法找到 javaw.exe，请重新启动游戏以下载该文件。{Color.END}")
        
        print()
        print()
        self.pause()
    
    def find_javaw(self):
        """查找 javaw.exe 文件"""
        root_directory = self.lunar_dir / "jre"
        return self._find_javaw_recursive(root_directory)
    
    def _find_javaw_recursive(self, directory):
        """递归查找 javaw.exe 文件"""
        if not directory.exists() or not directory.is_dir():
            return None
        
        # 检查当前目录
        javaw_path = directory / "bin" / "javaw.exe"
        if javaw_path.exists():
            return javaw_path
        
        # 递归检查子目录
        for subdir in directory.iterdir():
            if subdir.is_dir():
                result = self._find_javaw_recursive(subdir)
                if result:
                    return result
        
        return None
    
    def _clean_cache(self):
        """清理缓存目录"""
        if self.cache_dir.exists():
            for file in self.cache_dir.iterdir():
                try:
                    if file.is_file():
                        file.unlink()
                except Exception as e:
                    pass
            try:
                self.cache_dir.rmdir()
            except Exception as e:
                pass

if __name__ == "__main__":
    # 创建工具实例
    lct = LunarClientTools()
    
    # 检查是否以管理员权限运行
    if not lct.is_admin():
        print("请以管理员身份运行此脚本。")
        lct.run_as_admin()
        sys.exit()
    
    print("成功以管理员身份运行。")
    lct.main_menu()