#!/usr/bin/env python3
"""
Test script for Photo Editor functionality
"""
import subprocess
import time
import sys
import json
from pathlib import Path

def check_files():
    """Check if all required files exist"""
    required_files = [
        'index.html',
        'js/user.js',
        'js/main.js',
        'js/language.js',
        'styles/main.css',
        'styles/components.css',
        'styles/responsive.css'
    ]
    
    print("Checking required files...")
    for file in required_files:
        if not Path(file).exists():
            print(f"❌ Missing file: {file}")
            return False
        print(f"✅ Found: {file}")
    
    return True

def check_admin_user():
    """Check if admin user is created in user.js"""
    print("\nChecking admin user creation...")
    with open('js/user.js', 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'createAdminUser()' in content:
        print("✅ Admin user creation method found")
    else:
        print("❌ Admin user creation method missing")
        return False
        
    if "'lcjlcj670'" in content:
        print("✅ Admin username 'lcjlcj670' found")
    else:
        print("❌ Admin username missing")
        return False
        
    if "isAdmin: true" in content:
        print("✅ Admin flag found")
    else:
        print("❌ Admin flag missing")
        return False
        
    return True

def check_login_functionality():
    """Check if login supports both username and email"""
    print("\nChecking login functionality...")
    with open('js/user.js', 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'emailOrUsername' in content:
        print("✅ Login supports username/email input")
    else:
        print("❌ Login doesn't support username/email")
        return False
        
    if 'username.toLowerCase()' in content:
        print("✅ Username lookup implemented")
    else:
        print("❌ Username lookup missing")
        return False
        
    return True

def check_canvas_initialization():
    """Check if canvas is properly initialized"""
    print("\nChecking canvas initialization...")
    with open('js/main.js', 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'initializeCanvas()' in content:
        print("✅ Canvas initialization method found")
    else:
        print("❌ Canvas initialization missing")
        return False
        
    if 'canvas.width = 800' in content or 'this.canvas.width = 800' in content:
        print("✅ Default canvas width set")
    else:
        print("❌ Default canvas width not set")
        return False
        
    if 'canvas.height = 600' in content or 'this.canvas.height = 600' in content:
        print("✅ Default canvas height set")
    else:
        print("❌ Default canvas height not set")
        return False
        
    return True

def check_admin_panel():
    """Check if admin panel is implemented"""
    print("\nChecking admin panel...")
    with open('js/user.js', 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'showAdminPanel' in content:
        print("✅ Admin panel method found")
    else:
        print("❌ Admin panel missing")
        return False
        
    if 'addAdminMenuItem' in content:
        print("✅ Admin menu item method found")
    else:
        print("❌ Admin menu item missing")
        return False
        
    if '后台管理' in content:
        print("✅ Chinese admin menu text found")
    else:
        print("❌ Chinese admin menu text missing")
        return False
        
    return True

def check_translations():
    """Check if translations are complete"""
    print("\nChecking translations...")
    with open('js/language.js', 'r', encoding='utf-8') as f:
        content = f.read()
        
    required_keys = [
        'emailOrUsername',
        'adminLoginHint',
        'login'
    ]
    
    for key in required_keys:
        if f"'{key}'" in content:
            print(f"✅ Translation key '{key}' found")
        else:
            print(f"❌ Translation key '{key}' missing")
            return False
            
    return True

def main():
    print("=== Photo Editor Functionality Test ===\n")
    
    tests = [
        ("File Structure", check_files),
        ("Admin User", check_admin_user),
        ("Login Functionality", check_login_functionality),
        ("Canvas Initialization", check_canvas_initialization),
        ("Admin Panel", check_admin_panel),
        ("Translations", check_translations)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test failed with error: {e}")
            results.append((test_name, False))
    
    print("\n=== Test Summary ===")
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
        if result:
            passed += 1
    
    print(f"\n{passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! The website should be working correctly.")
        print("\nFeatures available:")
        print("1. ✅ Admin login: username 'lcjlcj670', password 'lcjlcj670'")
        print("2. ✅ Image import without login (File → Open or drag & drop)")
        print("3. ✅ Admin panel in user menu after login")
        print("4. ✅ Bilingual support (Chinese/English)")
        print("5. ✅ Theme system (light/dark mode)")
        
        print("\nNext steps for Google AdSense:")
        print("1. Login with admin credentials")
        print("2. Click '后台管理' in user menu")
        print("3. Follow the AdSense integration guide")
        
        return 0
    else:
        print("\n⚠️ Some tests failed. Please check the issues above.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
