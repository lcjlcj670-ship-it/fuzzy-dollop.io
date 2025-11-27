#!/usr/bin/env python3
"""
修复图片编辑器缩放显示不全问题
专门解决在不同缩放比例下内容被截断的问题
"""

import re

def fix_zoom_display_issues():
    """修复缩放显示问题的CSS代码"""
    
    # 读取现有CSS文件
    with open('/workspace/styles/main.css', 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # 创建改进的CSS样式
    zoom_fixes = """
/* ===== ZOOM DISPLAY FIXES ===== */
/* 修复缩放显示不全问题 */

/* 基础布局优化 */
html, body {
  height: auto;
  min-height: 100vh;
  overflow-x: auto;
  overflow-y: auto;
  zoom: reset; /* 重置缩放 */
}

body {
  zoom: inherit; /* 继承浏览器缩放设置 */
  -webkit-text-size-adjust: 100%; /* iOS缩放修复 */
  -ms-text-size-adjust: 100%;
  text-size-adjust: 100%;
}

/* 主内容区域改进 */
.main-content {
  display: flex;
  min-height: calc(100vh - 68px); /* 最小高度 */
  height: auto; /* 自动高度 */
  max-height: none; /* 无最大高度限制 */
  overflow: visible; /* 允许内容显示 */
  position: relative;
  z-index: 1;
}

/* 编辑器区域 */
.editor-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: auto;
  min-width: 0; /* 防止flex子元素溢出 */
  background-color: var(--neutral-900);
  position: relative;
}

/* Canvas容器改进 */
.canvas-container {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: auto;
  position: relative;
  min-height: 400px; /* 最小高度 */
  padding: 1rem;
}

/* Canvas响应式 */
#mainCanvas {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  border-radius: var(--radius-sm);
  background-color: var(--neutral-800);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

/* 工具栏改进 */
.toolbar {
  width: 56px;
  min-height: calc(100vh - 68px);
  background-color: var(--neutral-900);
  border-right: 1px solid var(--neutral-700);
  display: flex;
  flex-direction: column;
  padding: var(--space-sm) 0;
  gap: var(--space-sm);
  overflow-y: auto;
  flex-shrink: 0; /* 防止收缩 */
}

/* 属性面板改进 */
.properties-panel {
  width: 280px;
  min-width: 280px;
  background-color: var(--neutral-900);
  border-left: 1px solid var(--neutral-700);
  overflow-y: auto;
  flex-shrink: 0;
  max-height: calc(100vh - 68px);
}

/* 容器改进 */
.container {
  max-width: 100%;
  width: 100%;
  margin: 0 auto;
  padding: 0 1rem;
  box-sizing: border-box;
}

/* 移动端缩放优化 */
@media (max-width: 768px) {
  .main-content {
    flex-direction: column;
    height: auto;
    min-height: calc(100vh - 60px);
  }
  
  .toolbar {
    width: 100%;
    height: 60px;
    flex-direction: row;
    padding: var(--space-xs) var(--space-sm);
    overflow-x: auto;
    overflow-y: hidden;
  }
  
  .tool-group {
    flex-direction: row;
    gap: var(--space-xs);
  }
  
  .tool-button {
    width: 36px;
    height: 36px;
    min-width: 36px;
    min-height: 36px;
  }
  
  .properties-panel {
    width: 100%;
    height: auto;
    max-height: 300px;
  }
  
  .canvas-container {
    min-height: 300px;
    padding: 0.5rem;
  }
  
  #mainCanvas {
    max-width: calc(100vw - 2rem);
    max-height: 50vh;
  }
}

/* 超小屏幕优化 */
@media (max-width: 480px) {
  .main-content {
    min-height: calc(100vh - 50px);
  }
  
  .toolbar {
    height: 50px;
  }
  
  .tool-button {
    width: 32px;
    height: 32px;
    min-width: 32px;
    min-height: 32px;
  }
  
  .canvas-container {
    min-height: 250px;
    padding: 0.25rem;
  }
  
  #mainCanvas {
    max-width: calc(100vw - 1rem);
    max-height: 40vh;
  }
}

/* 高DPI屏幕优化 */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  #mainCanvas {
    image-rendering: -webkit-optimize-contrast;
    image-rendering: crisp-edges;
  }
}

/* 缩放级别优化 */
@media (zoom: 0.75) {
  .main-content {
    min-height: calc(100vh - 51px); /* 调整 */
  }
  
  .toolbar {
    min-height: calc(100vh - 51px);
  }
}

@media (zoom: 1.25) {
  .main-content {
    min-height: calc(100vh - 85px); /* 调整 */
  }
  
  .toolbar {
    min-height: calc(100vh - 85px);
  }
}

@media (zoom: 1.5) {
  .main-content {
    min-height: calc(100vh - 102px); /* 调整 */
  }
  
  .toolbar {
    min-height: calc(100vh - 102px);
  }
}

@media (zoom: 2) {
  .main-content {
    min-height: calc(100vh - 136px); /* 调整 */
  }
  
  .toolbar {
    min-height: calc(100vh - 136px);
  }
}

/* 滚动条优化 */
* {
  scrollbar-width: thin;
  scrollbar-color: var(--neutral-600) var(--neutral-900);
}

*::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

*::-webkit-scrollbar-track {
  background: var(--neutral-900);
}

*::-webkit-scrollbar-thumb {
  background-color: var(--neutral-600);
  border-radius: 4px;
}

*::-webkit-scrollbar-thumb:hover {
  background-color: var(--neutral-500);
}

/* 防止水平滚动 */
body, html {
  overflow-x: hidden;
}

/* 但允许内容区域水平滚动 */
.editor-area, .toolbar, .properties-panel {
  overflow-x: visible;
}

.canvas-container {
  overflow-x: auto;
  overflow-y: auto;
}

/* ===== END ZOOM DISPLAY FIXES ===== */

"""
    
    # 将修复代码添加到CSS文件末尾
    updated_css = css_content + zoom_fixes
    
    # 写入更新的CSS文件
    with open('/workspace/styles/main.css', 'w', encoding='utf-8') as f:
        f.write(updated_css)
    
    print("✅ 缩放显示修复CSS已添加到 styles/main.css")
    
    # 创建一个改进的HTML头部来优化缩放
    html_head_improvements = """
    <!-- Improved Zoom Support -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <meta name="format-detection" content="telephone=no">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="Photo Editor">
    
    <!-- Zoom and Scaling Optimizations -->
    <style>
        html {
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
            text-size-adjust: 100%;
        }
        
        @media (max-width: 768px) {
            html {
                -webkit-text-size-adjust: 120%;
                -ms-text-size-adjust: 120%;
                text-size-adjust: 120%;
            }
        }
    </style>
    """
    
    print("✅ HTML缩放优化代码已生成")
    print("🔧 修复内容:")
    print("   • 改善了主内容区域的缩放支持")
    print("   • 添加了overflow处理防止内容截断")
    print("   • 优化了移动端和超小屏幕的显示")
    print("   • 添加了高DPI屏幕支持")
    print("   • 支持不同缩放级别的自适应")
    print("   • 改进了滚动条样式")
    
    return True

if __name__ == "__main__":
    fix_zoom_display_issues()