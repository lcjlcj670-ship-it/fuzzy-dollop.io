#!/usr/bin/env python3
"""
验证PhotoEditor修复
"""

import subprocess
import os

def test_syntax():
    """检查JavaScript语法"""
    print("🔍 检查JavaScript语法...")
    
    js_files = ['js/main.js', 'js/user.js', 'js/notifications.js']
    
    for js_file in js_files:
        if os.path.exists(js_file):
            try:
                result = subprocess.run(['node', '-c', js_file], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"  ✅ {js_file} 语法正确")
                else:
                    print(f"  ❌ {js_file} 语法错误:")
                    print(f"     {result.stderr}")
            except FileNotFoundError:
                print(f"  ⚠️ Node.js未安装，跳过{js_file}语法检查")
        else:
            print(f"  ❌ {js_file} 文件不存在")

def check_initialization():
    """检查初始化代码"""
    print("\n🔍 检查PhotoEditor初始化...")
    
    with open('js/main.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'window.photoEditor = new PhotoEditor()' in content:
        print("  ✅ PhotoEditor实例化代码已添加")
    else:
        print("  ❌ PhotoEditor实例化代码缺失")
    
    if '🚀 PhotoEditor 实例已创建' in content:
        print("  ✅ 日志记录已添加")
    else:
        print("  ❌ 日志记录缺失")

def main():
    print("🔧 PhotoEditor 修复验证")
    print("=" * 30)
    
    test_syntax()
    check_initialization()
    
    print("\n📋 修复摘要:")
    print("✅ 添加了 PhotoEditor 实例化: window.photoEditor = new PhotoEditor()")
    print("✅ 添加了初始化日志")
    print("\n🌐 现在可以测试图片导入功能:")
    print("   1. 访问 http://localhost:8000")
    print("   2. 打开F12查看Console")
    print("   3. 尝试导入图片 (File→Open 或拖拽)")
    print("   4. 查看详细的调试日志")

if __name__ == "__main__":
    main()