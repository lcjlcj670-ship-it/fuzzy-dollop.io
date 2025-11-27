#!/usr/bin/env python3
"""
详细的图片导入功能诊断脚本
"""

import os
import re
from bs4 import BeautifulSoup

def check_html_structure():
    """检查HTML结构和元素"""
    print("🔍 检查HTML结构...")
    
    with open('/workspace/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 检查关键元素
    required_elements = {
        'mainCanvas': 'Canvas元素',
        'fileInput': '文件输入元素',
        'dropZone': '拖拽区域元素'
    }
    
    missing_elements = []
    found_elements = []
    
    for element_id, description in required_elements.items():
        element = soup.find(id=element_id)
        if element:
            found_elements.append(f"✅ {description} ({element_id})")
        else:
            missing_elements.append(f"❌ {description} ({element_id})")
    
    for item in found_elements:
        print(f"  {item}")
    
    for item in missing_elements:
        print(f"  {item}")
    
    return len(missing_elements) == 0

def check_script_loading():
    """检查脚本加载顺序"""
    print("\n🔍 检查脚本加载...")
    
    with open('/workspace/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 检查脚本标签
    script_patterns = [
        (r'<script src="js/notifications\.js"></script>', 'notifications.js'),
        (r'<script src="js/user\.js"></script>', 'user.js'),
        (r'<script src="js/main\.js"></script>', 'main.js'),
        (r'<script>', '内联脚本')
    ]
    
    for pattern, script_name in script_patterns:
        if re.search(pattern, html_content):
            print(f"  ✅ {script_name} 已加载")
        else:
            print(f"  ❌ {script_name} 未找到")
    
    # 检查初始化代码
    init_patterns = [
        r'new PhotoEditor\(\)',
        r'window\.photoEditor',
        r'DOMContentLoaded'
    ]
    
    for pattern in init_patterns:
        if re.search(pattern, html_content, re.DOTALL):
            print(f"  ✅ 找到初始化代码: {pattern}")
        else:
            print(f"  ❌ 未找到初始化代码: {pattern}")

def check_debugging_features():
    """检查调试功能"""
    print("\n🔍 检查调试功能...")
    
    with open('/workspace/js/main.js', 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    # 检查调试日志
    debug_checks = [
        ('console\.log.*🔄.*开始加载图片', 'loadImage调试日志'),
        ('console\.log.*📖.*文件读取成功', '文件读取成功日志'),
        ('console\.log.*🖼️.*图片加载成功', '图片加载成功日志'),
        ('console\.log.*✏️.*正在绘制图片', '图片绘制日志'),
        ('console\.log.*✅.*图片绘制完成', '图片完成日志')
    ]
    
    for pattern, description in debug_checks:
        if re.search(pattern, js_content):
            print(f"  ✅ {description}")
        else:
            print(f"  ❌ {description}")

def check_file_validation():
    """检查文件验证逻辑"""
    print("\n🔍 检查文件验证...")
    
    with open('/workspace/js/main.js', 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    validation_checks = [
        (r'file\.type\.startsWith.*image/', '文件类型验证'),
        (r'file\.size.*10.*1024.*1024', '文件大小限制'),
        ('notificationManager.show', '用户通知')
    ]
    
    for pattern, description in validation_checks:
        if re.search(pattern, js_content):
            print(f"  ✅ {description}")
        else:
            print(f"  ❌ {description}")

def check_photoeditor_methods():
    """检查PhotoEditor方法"""
    print("\n🔍 检查PhotoEditor方法...")
    
    with open('/workspace/js/main.js', 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    method_checks = [
        ('loadImage(', 'loadImage方法'),
        ('handleFileSelect(', 'handleFileSelect方法'),
        ('setupDragAndDrop(', 'setupDragAndDrop方法'),
        ('preventDefaults(', 'preventDefaults方法')
    ]
    
    for method, description in method_checks:
        if method in js_content:
            print(f"  ✅ {description}")
        else:
            print(f"  ❌ {description}")

def generate_test_script():
    """生成详细的测试脚本"""
    print("\n📝 生成测试脚本...")
    
    test_html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>图片导入详细诊断</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .test-section {
            background: white;
            margin: 20px 0;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .test-result {
            margin: 10px 0;
            padding: 10px;
            border-radius: 4px;
        }
        .success { background: #d4edda; border: 1px solid #c3e6cb; color: #155724; }
        .error { background: #f8d7da; border: 1px solid #f5c6cb; color: #721c24; }
        .info { background: #d1ecf1; border: 1px solid #bee5eb; color: #0c5460; }
        canvas {
            border: 2px solid #ddd;
            background: white;
            margin: 10px 0;
        }
        #dropZone {
            border: 2px dashed #ccc;
            padding: 20px;
            text-align: center;
            margin: 10px 0;
            background: #f9f9f9;
            cursor: pointer;
        }
        #dropZone.drag-over {
            background: #e3f2fd;
            border-color: #2196F3;
        }
    </style>
</head>
<body>
    <h1>🖼️ 图片导入详细诊断测试</h1>
    
    <div class="test-section">
        <h2>1. 系统初始化检查</h2>
        <div id="initCheck"></div>
    </div>
    
    <div class="test-section">
        <h2>2. Canvas功能测试</h2>
        <canvas id="testCanvas" width="400" height="300"></canvas>
        <div id="canvasCheck"></div>
    </div>
    
    <div class="test-section">
        <h2>3. 文件输入测试</h2>
        <input type="file" id="fileInput" accept="image/*">
        <div id="fileInputCheck"></div>
    </div>
    
    <div class="test-section">
        <h2>4. 拖拽区域测试</h2>
        <div id="dropZone">
            <p>拖拽图片文件到这里或点击选择文件</p>
            <input type="file" id="fileInput2" accept="image*" style="display: none;">
        </div>
        <div id="dropZoneCheck"></div>
    </div>
    
    <div class="test-section">
        <h2>5. 加载日志监控</h2>
        <div id="consoleLog" style="background: #f8f9fa; padding: 10px; border: 1px solid #dee2e6; height: 200px; overflow-y: auto; font-family: monospace; font-size: 12px;"></div>
    </div>

    <script src="js/notifications.js"></script>
    <script src="js/user.js"></script>
    <script src="js/main.js"></script>
    
    <script>
        // 重写console.log以显示在页面上
        const originalLog = console.log;
        console.log = function(...args) {
            originalLog.apply(console, args);
            const logDiv = document.getElementById('consoleLog');
            const timestamp = new Date().toLocaleTimeString();
            logDiv.innerHTML += `[${timestamp}] ${args.join(' ')}<br>`;
            logDiv.scrollTop = logDiv.scrollHeight;
        };
        
        console.error = function(...args) {
            console.log('❌ ERROR:', ...args);
        };
        
        function checkInit() {
            const results = [];
            
            // 检查PhotoEditor类
            if (typeof PhotoEditor === 'function') {
                results.push('<div class="test-result success">✅ PhotoEditor类已定义</div>');
            } else {
                results.push('<div class="test-result error">❌ PhotoEditor类未找到</div>');
            }
            
            // 检查全局变量
            if (window.photoEditor) {
                results.push('<div class="test-result success">✅ window.photoEditor 已初始化</div>');
            } else {
                results.push('<div class="test-result error">❌ window.photoEditor 未初始化</div>');
            }
            
            // 检查Canvas元素
            const canvas = document.getElementById('mainCanvas');
            if (canvas) {
                results.push('<div class="test-result success">✅ mainCanvas 元素存在</div>');
                if (canvas.width && canvas.height) {
                    results.push(`<div class="test-result info">📐 Canvas尺寸: ${canvas.width}x${canvas.height}</div>`);
                }
            } else {
                results.push('<div class="test-result error">❌ mainCanvas 元素不存在</div>');
            }
            
            // 检查fileInput元素
            const fileInput = document.getElementById('fileInput');
            if (fileInput) {
                results.push('<div class="test-result success">✅ fileInput 元素存在</div>');
            } else {
                results.push('<div class="test-result error">❌ fileInput 元素不存在</div>');
            }
            
            // 检查dropZone元素
            const dropZone = document.getElementById('dropZone');
            if (dropZone) {
                results.push('<div class="test-result success">✅ dropZone 元素存在</div>');
            } else {
                results.push('<div class="test-result error">❌ dropZone 元素不存在</div>');
            }
            
            document.getElementById('initCheck').innerHTML = results.join('');
        }
        
        function testCanvas() {
            const canvas = document.getElementById('testCanvas');
            const ctx = canvas.getContext('2d');
            
            // 绘制测试
            ctx.fillStyle = '#ff0000';
            ctx.fillRect(50, 50, 100, 100);
            ctx.fillStyle = '#00ff00';
            ctx.fillRect(100, 100, 100, 100);
            ctx.fillStyle = '#0000ff';
            ctx.fillText('Canvas测试', 20, 20);
            
            console.log('🎨 Canvas测试完成');
            
            const results = [];
            if (ctx) {
                results.push('<div class="test-result success">✅ Canvas上下文获取成功</div>');
            } else {
                results.push('<div class="test-result error">❌ Canvas上下文获取失败</div>');
            }
            
            document.getElementById('canvasCheck').innerHTML = results.join('');
        }
        
        function testFileInput() {
            const fileInput = document.getElementById('fileInput');
            const results = [];
            
            if (fileInput) {
                fileInput.addEventListener('change', function(e) {
                    const file = e.target.files[0];
                    if (file) {
                        console.log('📁 文件选择:', file.name, file.type, file.size);
                        
                        if (window.photoEditor && typeof window.photoEditor.loadImage === 'function') {
                            console.log('📦 调用loadImage方法');
                            window.photoEditor.loadImage(file);
                        } else {
                            console.error('❌ loadImage方法不可用');
                        }
                    }
                });
                
                results.push('<div class="test-result success">✅ 文件输入事件监听已设置</div>');
                results.push('<div class="test-result info">ℹ️ 请选择一个图片文件进行测试</div>');
            } else {
                results.push('<div class="test-result error">❌ 文件输入元素不存在</div>');
            }
            
            document.getElementById('fileInputCheck').innerHTML = results.join('');
        }
        
        function testDropZone() {
            const dropZone = document.getElementById('dropZone');
            const fileInput2 = document.getElementById('fileInput2');
            const results = [];
            
            if (dropZone) {
                // 拖拽事件
                ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
                    dropZone.addEventListener(eventName, (e) => {
                        e.preventDefault();
                        e.stopPropagation();
                        console.log(`🖱️ ${eventName} 事件触发`);
                    });
                });
                
                dropZone.addEventListener('dragover', () => {
                    dropZone.classList.add('drag-over');
                });
                
                dropZone.addEventListener('dragleave', () => {
                    dropZone.classList.remove('drag-over');
                });
                
                dropZone.addEventListener('drop', (e) => {
                    dropZone.classList.remove('drag-over');
                    const files = e.dataTransfer.files;
                    if (files.length > 0) {
                        const file = files[0];
                        console.log('📂 拖拽文件:', file.name, file.type, file.size);
                        
                        if (window.photoEditor && typeof window.photoEditor.loadImage === 'function') {
                            console.log('📦 调用loadImage方法');
                            window.photoEditor.loadImage(file);
                        } else {
                            console.error('❌ loadImage方法不可用');
                        }
                    }
                });
                
                // 点击事件
                dropZone.addEventListener('click', () => {
                    fileInput2.click();
                });
                
                fileInput2.addEventListener('change', function(e) {
                    const file = e.target.files[0];
                    if (file) {
                        console.log('📁 点击选择文件:', file.name, file.type, file.size);
                        
                        if (window.photoEditor && typeof window.photoEditor.loadImage === 'function') {
                            console.log('📦 调用loadImage方法');
                            window.photoEditor.loadImage(file);
                        } else {
                            console.error('❌ loadImage方法不可用');
                        }
                    }
                });
                
                results.push('<div class="test-result success">✅ 拖拽区域事件监听已设置</div>');
                results.push('<div class="test-result info">ℹ️ 拖拽或点击拖拽区域进行测试</div>');
            } else {
                results.push('<div class="test-result error">❌ 拖拽区域不存在</div>');
            }
            
            document.getElementById('dropZoneCheck').innerHTML = results.join('');
        }
        
        // 等待DOM加载完成
        document.addEventListener('DOMContentLoaded', function() {
            console.log('🚀 DOM加载完成，开始检查...');
            
            setTimeout(() => {
                checkInit();
                testCanvas();
                testFileInput();
                testDropZone();
                console.log('✅ 所有检查完成');
            }, 100);
        });
    </script>
</body>
</html>'''
    
    with open('/workspace/detailed_image_test.html', 'w', encoding='utf-8') as f:
        f.write(test_html)
    
    print("  ✅ 详细测试页面已生成: detailed_image_test.html")

def main():
    print("🖼️ 图片导入功能详细诊断")
    print("=" * 50)
    
    # 运行所有检查
    html_ok = check_html_structure()
    check_script_loading()
    check_debugging_features()
    check_file_validation()
    check_photoeditor_methods()
    generate_test_script()
    
    print("\n" + "=" * 50)
    print("📋 诊断总结:")
    if html_ok:
        print("✅ HTML结构检查通过")
    else:
        print("❌ HTML结构有问题，请检查缺失的元素")
    
    print("📄 测试页面已生成: detailed_image_test.html")
    print("🌐 请在浏览器中访问: http://localhost:8000/detailed_image_test.html")
    print("🔍 打开F12查看Console日志进行详细调试")

if __name__ == "__main__":
    main()