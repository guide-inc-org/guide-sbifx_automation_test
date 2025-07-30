#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Kill App Functions - Simple Version
Script đơn giản để test các hàm kill app mới
"""

import sys
import os
import time

# Import các module common
sys.path.append(os.path.dirname(__file__))
from common.appium_config import AppiumConfig, kill_app, kill_all_apps, is_app_running, restart_app

def test_kill_app_functions():
    """Test các hàm kill app"""
    print("=== Test Kill App Functions ===")
    
    # Khởi tạo AppiumConfig
    appium_config = AppiumConfig("http://localhost:4723/wd/hub")
    
    print("✅ AppiumConfig đã được khởi tạo")
    
    try:
        # Setup driver
        print("🚀 Đang setup driver...")
        driver = appium_config.setup_driver("android")
        
        if driver:
            print("✅ Driver đã được setup thành công")
            
            # Demo kiểm tra app status
            print("\n📱 Demo kiểm tra app status:")
            is_running = is_app_running(driver, "android")
            print(f"   App đang chạy: {is_running}")
            
            if is_running:
                # Demo kill app
                print("\n🔴 Demo kill app:")
                success = kill_app(driver, "android")
                print(f"   Kill app thành công: {success}")
                
                time.sleep(2)
                
                # Kiểm tra lại status
                is_running_after = is_app_running(driver, "android")
                print(f"   App đang chạy sau khi kill: {is_running_after}")
                
                # Demo restart app
                print("\n🔄 Demo restart app:")
                restart_app(driver, "android")
                
                time.sleep(3)
                
                # Kiểm tra lại status
                is_running_restart = is_app_running(driver, "android")
                print(f"   App đang chạy sau khi restart: {is_running_restart}")
                
                # Demo kill app với package name tùy chỉnh
                print("\n🎯 Demo kill app với package name tùy chỉnh:")
                custom_package = "jp.co.mobileit.SBI_FX"
                success_custom = kill_app(driver, "android", app_package=custom_package)
                print(f"   Kill app {custom_package} thành công: {success_custom}")
            
            # Đóng driver
            driver.quit()
            print("\n🔒 Đã đóng driver")
            
        else:
            print("❌ Không thể setup driver")
            
    except Exception as e:
        print(f"❌ Lỗi khi demo: {e}")
        print("💡 Hãy đảm bảo Appium server đang chạy và device được kết nối")

def main():
    """Main function"""
    print("🚀 Bắt đầu Test Kill App Functions")
    print("=" * 50)
    
    try:
        test_kill_app_functions()
        
        print("\n" + "=" * 50)
        print("✅ Test hoàn thành!")
        print("\n📚 Các hàm đã được test:")
        print("1. kill_app() - Tắt app cụ thể")
        print("2. is_app_running() - Kiểm tra app có đang chạy không")
        print("3. restart_app() - Khởi động lại app")
        
    except Exception as e:
        print(f"❌ Lỗi trong quá trình test: {e}")

if __name__ == "__main__":
    main() 