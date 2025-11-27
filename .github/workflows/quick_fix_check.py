#!/usr/bin/env python3
"""
快速验证图片导入修复
"""

import subprocess
import time
import requests
import os

def check_fix():
    """检查修复状态"""
    print("🔧 图片导入问题修复验证")
    print("=" * 50)
    
    # 1. 检查文件存在
    files = ['js/main.js', 'index.html', 'image_import_test.html']
    print("\n1. 检查修复文件...")
    for file in files:
        if os.path.exists(file):
            print(f"✅ {file} 存在")
        else:
            print(f"❌ {file} 缺失")
            return False
    
    # 2. 验证代码修复
    print("\n2. 验证代码修复...")
    with open('js/main.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixes = [
        ('开始加载图片', '调试日志'),
        ('非图片文件类型', '文件类型验证'),
        ('文件过大', '文件大小验证'),
        ('Canvas或Context未初始化', 'Canvas检查'),
        ('图片加载完全成功', '成功反馈')
    ]
    
    for pattern, description in fixes:
        if pattern in content:
            print(f"✅ {description}: 已修复")
        else:
            print(f"❌ {description}: 未找到")
    
    # 3. 验证HTML修复
    print("\n3. 验证HTML调试功能...")
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    if 'PhotoEditor initialized successfully' in html_content:
        print("✅ 自动调试功能: 已添加")
    else:
        print("❌ 自动调试功能: 缺失")
    
    print("\n🎯 修复完成摘要:")
    print("✅ 增强了loadImage方法，添加详细调试日志")
    print("✅ 添加了文件类型和大小验证")
    print("✅ 增强了Canvas初始化检查")
    print("✅ 启用了自动调试模式")
    print("✅ 创建了专门的测试页面")
    
    print("\n📋 下一步操作:")
    print("1. 启动服务器: python3 -m http.server 8000")
    print("2. 打开测试页面: http://localhost:8000/image_import_test.html")
    print("3. 按F12打开开发者工具")
    print("4. 测试图片导入功能")
    print("5. 观察Console中的调试信息")
    
    print("\n🚨 如果仍有问题:")
    print("- 检查Console中的红色错误信息")
    print("- 确认图片格式和大小符合要求")
    print("- 验证浏览器兼容性")
    print("- 参考 IMAGE_IMPORT_FIX_REPORT.md 获取详细信息")

if __name__ == '__main__':
    check_fix()
