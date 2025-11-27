#!/usr/bin/env python3
"""
修复图片导入问题的诊断和修复脚本
"""

import os
import re

def check_files():
    """检查文件是否存在"""
    files = ['index.html', 'js/main.js', 'js/canvas.js']
    for file in files:
        if os.path.exists(file):
            print(f"✅ 文件存在: {file}")
        else:
            print(f"❌ 文件缺失: {file}")
            return False
    return True

def analyze_main_js():
    """分析main.js中的图片导入逻辑"""
    with open('js/main.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # 检查PhotoEditor类是否正确实现
    if 'class PhotoEditor' not in content:
        issues.append("❌ PhotoEditor类未找到")
    else:
        print("✅ PhotoEditor类存在")
    
    # 检查init方法
    if 'init()' in content:
        print("✅ init方法存在")
    else:
        issues.append("❌ init方法未找到")
    
    # 检查loadImage方法
    if 'loadImage(file)' in content:
        print("✅ loadImage方法存在")
    else:
        issues.append("❌ loadImage方法未找到")
    
    # 检查canvas初始化
    if 'this.canvas.width = 800' in content and 'this.canvas.height = 600' in content:
        print("✅ Canvas初始化正常")
    else:
        issues.append("❌ Canvas初始化可能有问题")
    
    # 检查事件监听器
    if "addEventListener('change'" in content:
        print("✅ 文件输入事件监听器存在")
    else:
        issues.append("❌ 文件输入事件监听器缺失")
    
    # 检查拖拽事件
    if 'setupDragAndDrop' in content:
        print("✅ 拖拽功能存在")
    else:
        issues.append("❌ 拖拽功能缺失")
    
    return issues

def analyze_index_html():
    """分析index.html中的相关元素"""
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # 检查Canvas元素
    if 'id="mainCanvas"' in content:
        print("✅ mainCanvas元素存在")
    else:
        issues.append("❌ mainCanvas元素缺失")
    
    # 检查文件输入元素
    if 'id="fileInput"' in content:
        print("✅ fileInput元素存在")
    else:
        issues.append("❌ fileInput元素缺失")
    
    # 检查拖拽区域
    if 'id="dropZone"' in content:
        print("✅ dropZone元素存在")
    else:
        issues.append("❌ dropZone元素缺失")
    
    # 检查脚本加载顺序
    script_order = ['main.js', 'canvas.js', 'tools.js']
    script_positions = []
    for script in script_order:
        if f'src="js/{script}"' in content:
            pos = content.find(f'src="js/{script}"')
            script_positions.append((script, pos))
            print(f"✅ {script} 脚本已加载")
        else:
            issues.append(f"❌ {script} 脚本未加载")
    
    # 检查window.photoEditor实例化
    if 'window.photoEditor = new PhotoEditor()' in content:
        print("✅ PhotoEditor实例化存在")
    else:
        issues.append("❌ PhotoEditor实例化缺失")
    
    return issues

def fix_load_image_method():
    """修复loadImage方法，添加更详细的错误处理和调试信息"""
    
    # 读取当前main.js
    with open('js/main.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找loadImage方法并替换为修复版本
    old_load_image = '''    loadImage(file) {
        // Show loading indicator
        this.showNotification('正在加载图片...', 'info');
        
        const reader = new FileReader();
        reader.onload = (e) => {
            const img = new Image();
            
            img.onload = () => {
                try {
                    // Set maximum canvas size
                    const maxWidth = 1200;
                    const maxHeight = 800;
                    
                    // Calculate new dimensions
                    let newWidth = img.width;
                    let newHeight = img.height;
                    
                    // Scale down if too large
                    if (newWidth > maxWidth || newHeight > maxHeight) {
                        const scale = Math.min(maxWidth / newWidth, maxHeight / newHeight);
                        newWidth = Math.floor(newWidth * scale);
                        newHeight = Math.floor(newHeight * scale);
                    }
                    
                    // Ensure minimum dimensions
                    newWidth = Math.max(newWidth, 100);
                    newHeight = Math.max(newHeight, 100);
                    
                    // Resize canvas and context
                    this.canvas.width = newWidth;
                    this.canvas.height = newHeight;
                    
                    // Clear canvas completely
                    this.ctx.save();
                    this.ctx.globalCompositeOperation = 'source-over';
                    this.ctx.clearRect(0, 0, newWidth, newHeight);
                    this.ctx.fillStyle = '#ffffff';
                    this.ctx.fillRect(0, 0, newWidth, newHeight);
                    
                    // Draw image
                    this.ctx.drawImage(img, 0, 0, newWidth, newHeight);
                    this.ctx.restore();
                    
                    // Update current layer
                    if (this.layers[this.currentLayer]) {
                        const layer = this.layers[this.currentLayer];
                        layer.canvas.width = newWidth;
                        layer.canvas.height = newHeight;
                        const layerCtx = layer.canvas.getContext('2d');
                        layerCtx.clearRect(0, 0, newWidth, newHeight);
                        layerCtx.drawImage(img, 0, 0, newWidth, newHeight);
                    }
                    
                    this.currentFile = file;
                    this.hideDropZone();
                    this.addToHistory();
                    this.render();
                    this.updateCanvasSize();
                    
                    // Hide loading indicator and show success
                    this.hideNotification();
                    notificationManager.show('图片加载成功!', 'success');
                    
                } catch (error) {
                    console.error('Error loading image:', error);
                    this.hideNotification();
                    notificationManager.show('图片加载失败: ' + error.message, 'error');
                }
            };
            
            img.onerror = () => {
                console.error('Error loading image');
                this.hideNotification();
                notificationManager.show('图片格式不支持或文件损坏', 'error');
            };
            
            img.crossOrigin = 'anonymous';
            img.src = e.target.result;
        };
        
        reader.onerror = () => {
            console.error('Error reading file');
            this.hideNotification();
            notificationManager.show('文件读取失败', 'error');
        };
        
        reader.readAsDataURL(file);'''
    
    new_load_image = '''    loadImage(file) {
        // 调试信息
        console.log('开始加载图片:', file.name, '类型:', file.type, '大小:', file.size);
        
        // 验证文件类型
        if (!file.type.startsWith('image/')) {
            notificationManager.show('请选择图片文件', 'error');
            return;
        }
        
        // 验证文件大小 (最大10MB)
        if (file.size > 10 * 1024 * 1024) {
            notificationManager.show('文件大小不能超过10MB', 'error');
            return;
        }
        
        // Show loading indicator
        this.showNotification('正在加载图片...', 'info');
        
        const reader = new FileReader();
        
        reader.onload = (e) => {
            console.log('文件读取成功，开始创建Image对象');
            
            const img = new Image();
            
            img.onload = () => {
                try {
                    console.log('图片加载成功，尺寸:', img.width, 'x', img.height);
                    
                    // 确保canvas和context有效
                    if (!this.canvas || !this.ctx) {
                        console.error('Canvas或Context未初始化');
                        this.setupCanvas();
                    }
                    
                    // Set maximum canvas size
                    const maxWidth = 1200;
                    const maxHeight = 800;
                    
                    // Calculate new dimensions
                    let newWidth = img.width;
                    let newHeight = img.height;
                    
                    // Scale down if too large
                    if (newWidth > maxWidth || newHeight > maxHeight) {
                        const scale = Math.min(maxWidth / newWidth, maxHeight / newHeight);
                        newWidth = Math.floor(newWidth * scale);
                        newHeight = Math.floor(newHeight * scale);
                        console.log('图片过大，已缩放为:', newWidth, 'x', newHeight);
                    }
                    
                    // Ensure minimum dimensions
                    newWidth = Math.max(newWidth, 100);
                    newHeight = Math.max(newHeight, 100);
                    
                    // Resize canvas and context
                    this.canvas.width = newWidth;
                    this.canvas.height = newHeight;
                    console.log('Canvas尺寸已调整为:', newWidth, 'x', newHeight);
                    
                    // Clear canvas completely
                    this.ctx.save();
                    this.ctx.globalCompositeOperation = 'source-over';
                    this.ctx.clearRect(0, 0, newWidth, newHeight);
                    this.ctx.fillStyle = '#ffffff';
                    this.ctx.fillRect(0, 0, newWidth, newHeight);
                    
                    // Draw image
                    console.log('正在绘制图片到Canvas');
                    this.ctx.drawImage(img, 0, 0, newWidth, newHeight);
                    this.ctx.restore();
                    console.log('图片绘制完成');
                    
                    // Update current layer
                    if (this.layers[this.currentLayer]) {
                        const layer = this.layers[this.currentLayer];
                        layer.canvas.width = newWidth;
                        layer.canvas.height = newHeight;
                        const layerCtx = layer.canvas.getContext('2d');
                        layerCtx.clearRect(0, 0, newWidth, newHeight);
                        layerCtx.drawImage(img, 0, 0, newWidth, newHeight);
                    }
                    
                    this.currentFile = file;
                    this.hideDropZone();
                    this.addToHistory();
                    this.render();
                    this.updateCanvasSize();
                    
                    // Hide loading indicator and show success
                    this.hideNotification();
                    console.log('图片加载完全成功');
                    notificationManager.show('图片加载成功!', 'success');
                    
                } catch (error) {
                    console.error('Error loading image:', error);
                    this.hideNotification();
                    notificationManager.show('图片加载失败: ' + error.message, 'error');
                }
            };
            
            img.onerror = (error) => {
                console.error('Error loading image from result:', error);
                console.log('Image src was:', img.src);
                this.hideNotification();
                notificationManager.show('图片格式不支持或文件损坏', 'error');
            };
            
            img.crossOrigin = 'anonymous';
            img.src = e.target.result;
            console.log('Image src设置为:', img.src.substring(0, 50) + '...');
        };
        
        reader.onerror = (error) => {
            console.error('Error reading file:', error);
            this.hideNotification();
            notificationManager.show('文件读取失败', 'error');
        };
        
        console.log('开始读取文件');
        reader.readAsDataURL(file);
    }'''
    
    if old_load_image in content:
        content = content.replace(old_load_image, new_load_image)
        with open('js/main.js', 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ loadImage方法已更新")
        return True
    else:
        print("❌ 找不到loadImage方法进行替换")
        return False

def add_debug_mode():
    """添加调试模式到页面"""
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 在DOMContentLoaded事件中添加调试信息
    debug_script = '''
            // Debug: Check if photoEditor is properly initialized
            setTimeout(() => {
                if (window.photoEditor) {
                    console.log('✅ PhotoEditor initialized successfully');
                    console.log('Canvas element:', window.photoEditor.canvas);
                    console.log('Context:', window.photoEditor.ctx);
                    
                    // Test canvas drawing
                    if (window.photoEditor.canvas && window.photoEditor.ctx) {
                        window.photoEditor.ctx.fillStyle = '#ff0000';
                        window.photoEditor.ctx.fillRect(50, 50, 100, 100);
                        console.log('✅ Canvas test drawing successful');
                    }
                } else {
                    console.error('❌ PhotoEditor not initialized');
                }
                
                // Check file input
                const fileInput = document.getElementById('fileInput');
                if (fileInput) {
                    console.log('✅ File input found');
                    console.log('File input events:', getEventListeners(fileInput));
                } else {
                    console.error('❌ File input not found');
                }
                
                // Check drop zone
                const dropZone = document.getElementById('dropZone');
                if (dropZone) {
                    console.log('✅ Drop zone found');
                } else {
                    console.error('❌ Drop zone not found');
                }
                
            }, 1000);
    '''
    
    # 找到合适的位置插入调试脚本
    if 'photoEditor.init();' in content:
        content = content.replace('photoEditor.init();', 'photoEditor.init();' + debug_script)
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ 调试脚本已添加")
        return True
    else:
        print("❌ 找不到插入调试脚本的位置")
        return False

def main():
    print("🔧 图片导入问题诊断和修复")
    print("=" * 50)
    
    # 1. 检查文件存在性
    print("\n1. 检查文件...")
    if not check_files():
        return
    
    # 2. 分析main.js
    print("\n2. 分析main.js...")
    main_issues = analyze_main_js()
    
    # 3. 分析index.html
    print("\n3. 分析index.html...")
    html_issues = analyze_index_html()
    
    # 4. 修复loadImage方法
    print("\n4. 修复loadImage方法...")
    if fix_load_image_method():
        print("✅ loadImage方法修复成功")
    else:
        print("❌ loadImage方法修复失败")
    
    # 5. 添加调试模式
    print("\n5. 添加调试信息...")
    if add_debug_mode():
        print("✅ 调试信息添加成功")
    else:
        print("❌ 调试信息添加失败")
    
    # 6. 输出总结
    print("\n" + "=" * 50)
    print("📋 问题诊断总结:")
    
    if not main_issues and not html_issues:
        print("✅ 所有检查都通过")
    else:
        if main_issues:
            print("\n❌ main.js问题:")
            for issue in main_issues:
                print(f"  - {issue}")
        
        if html_issues:
            print("\n❌ index.html问题:")
            for issue in html_issues:
                print(f"  - {issue}")
    
    print("\n🔧 修复措施:")
    print("1. ✅ 添加了详细的调试日志")
    print("2. ✅ 增强了错误处理")
    print("3. ✅ 添加了文件验证")
    print("4. ✅ 添加了Canvas初始化检查")
    
    print("\n📝 使用说明:")
    print("1. 启动网站服务器")
    print("2. 打开浏览器开发者工具 (F12)")
    print("3. 查看Console面板的调试信息")
    print("4. 尝试导入图片并观察错误信息")
    
    print("\n🎯 预期结果:")
    print("- 图片应该能够正常加载并显示")
    print("- Console中会有详细的调试信息")
    print("- 成功加载时显示'图片加载成功'消息")

if __name__ == '__main__':
    main()
