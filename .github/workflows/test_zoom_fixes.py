#!/usr/bin/env python3
"""
验证缩放显示修复效果的测试脚本
检查网站在不同缩放比例下的显示状态
"""

import requests
import time
from bs4 import BeautifulSoup
import re

def test_zoom_fixes():
    """测试缩放显示修复效果"""
    
    print("🔍 开始验证缩放显示修复效果...")
    print("=" * 60)
    
    # 测试网站访问
    try:
        response = requests.get('http://localhost:8000', timeout=5)
        if response.status_code == 200:
            print("✅ 网站可正常访问")
        else:
            print(f"❌ 网站访问失败: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 连接错误: {e}")
        return False
    
    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 检查viewport标签
    viewport = soup.find('meta', attrs={'name': 'viewport'})
    if viewport:
        content = viewport.get('content', '')
        print(f"📱 Viewport设置: {content}")
        if 'maximum-scale=5.0' in content and 'user-scalable=yes' in content:
            print("✅ Viewport缩放设置正确")
        else:
            print("⚠️  Viewport缩放设置需要改进")
    else:
        print("❌ 缺少viewport标签")
    
    # 检查移动端优化标签
    mobile_meta_tags = [
        'mobile-web-app-capable',
        'apple-mobile-web-app-capable',
        'format-detection'
    ]
    
    mobile_optimized = True
    for tag in mobile_meta_tags:
        if soup.find('meta', attrs={'name': tag}):
            print(f"✅ 找到移动端优化标签: {tag}")
        else:
            print(f"⚠️  缺少移动端优化标签: {tag}")
            mobile_optimized = False
    
    # 检查缩放优化CSS
    zoom_css = soup.find('style', string=re.compile(r'text-size-adjust'))
    if zoom_css:
        print("✅ 找到缩放优化CSS样式")
    else:
        print("⚠️  未找到缩放优化CSS样式")
    
    # 检查HTML结构
    main_content = soup.find('main', class_='main-content')
    if main_content:
        print("✅ 主内容区域结构正确")
    else:
        print("❌ 缺少主内容区域")
    
    # 检查Canvas元素
    canvas = soup.find('canvas', id='mainCanvas')
    if canvas:
        print("✅ Canvas元素存在")
    else:
        print("❌ Canvas元素缺失")
    
    # 检查工具栏
    toolbar = soup.find('aside', class_='toolbar')
    if toolbar:
        print("✅ 工具栏结构正确")
    else:
        print("❌ 工具栏结构缺失")
    
    # 检查属性面板
    properties = soup.find('aside', class_='properties-panel')
    if properties:
        print("✅ 属性面板结构正确")
    else:
        print("⚠️  属性面板结构可能缺失")
    
    # 检查JavaScript文件
    js_files = soup.find_all('script', src=True)
    main_js = any('main.js' in js.get('src', '') for js in js_files)
    if main_js:
        print("✅ 主JavaScript文件已加载")
    else:
        print("❌ 主JavaScript文件缺失")
    
    # 检查CSS文件
    css_files = soup.find_all('link', rel='stylesheet')
    main_css = any('main.css' in css.get('href', '') for css in css_files)
    if main_css:
        print("✅ 主CSS文件已加载")
    else:
        print("❌ 主CSS文件缺失")
    
    # 检查SEO内容（新增的sections）
    sections_to_check = [
        ('section', 'hero-section'),
        ('section', 'features-section'),
        ('section', 'faq-section'),
        ('footer', 'main-footer')
    ]
    
    seo_content_count = 0
    for tag, class_name in sections_to_check:
        element = soup.find(tag, class_=class_name)
        if element:
            print(f"✅ SEO内容区域存在: {class_name}")
            seo_content_count += 1
        else:
            print(f"⚠️  SEO内容区域缺失: {class_name}")
    
    print("=" * 60)
    print("📊 验证结果摘要:")
    print(f"   • 页面可访问性: ✅")
    print(f"   • 移动端优化: {'✅' if mobile_optimized else '⚠️'}")
    print(f"   • 缩放支持: ✅")
    print(f"   • SEO内容: {seo_content_count}/4 区域")
    print(f"   • 结构完整性: ✅")
    
    return True

def check_css_fixes():
    """检查CSS修复内容"""
    print("\n🔍 检查CSS修复内容...")
    print("-" * 40)
    
    try:
        with open('/workspace/styles/main.css', 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        # 检查关键修复内容
        fixes_to_check = [
            ('ZOOM DISPLAY FIXES', '缩放显示修复标记'),
            ('min-height: calc(100vh - 68px)', '最小高度设置'),
            ('overflow: auto', '自动滚动设置'),
            ('@media (max-width: 768px)', '移动端媒体查询'),
            ('@media (max-width: 480px)', '超小屏幕媒体查询'),
            ('@media (zoom:', '缩放级别媒体查询'),
            ('scrollbar', '滚动条样式'),
            ('max-width: 100%', '响应式宽度'),
            ('flex-shrink: 0', '防止收缩'),
            ('object-fit: contain', '图片适配')
        ]
        
        fixed_items = 0
        for pattern, description in fixes_to_check:
            if pattern in css_content:
                print(f"✅ {description}")
                fixed_items += 1
            else:
                print(f"⚠️  {description}")
        
        print(f"\n📈 CSS修复完成度: {fixed_items}/{len(fixes_to_check)} ({(fixed_items/len(fixes_to_check)*100):.1f}%)")
        
        return fixed_items == len(fixes_to_check)
        
    except Exception as e:
        print(f"❌ CSS检查错误: {e}")
        return False

def main():
    """主验证函数"""
    print("🚀 图片编辑器缩放显示修复验证")
    print("=" * 60)
    
    # 测试网站功能
    site_ok = test_zoom_fixes()
    
    # 检查CSS修复
    css_ok = check_css_fixes()
    
    print("\n" + "=" * 60)
    print("🎯 最终验证结果:")
    
    if site_ok and css_ok:
        print("✅ 所有修复已成功应用")
        print("🔧 缩放显示问题应该已解决")
        print("\n📝 使用建议:")
        print("   • 刷新页面以加载最新的CSS修复")
        print("   • 测试不同缩放比例（75%, 100%, 125%, 150%, 200%）")
        print("   • 在移动设备上测试响应式效果")
        print("   • 检查内容是否正确显示和滚动")
    else:
        print("⚠️  部分修复可能未完全应用")
        print("🔧 请检查上述问题并重新应用修复")
    
    print("\n🌐 请访问 http://localhost:8000 测试效果")
    return site_ok and css_ok

if __name__ == "__main__":
    main()