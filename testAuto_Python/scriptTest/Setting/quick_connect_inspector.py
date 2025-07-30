#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quick Connect Appium Inspector
Kết nối nhanh Appium Inspector với thông tin đã cấu hình
"""

import subprocess
import json
from datetime import datetime

def check_appium_server():
    """Kiểm tra Appium server có đang chạy không"""
    try:
        import requests
        response = requests.get("http://localhost:4723/wd/hub/status", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get('value', {}).get('ready', False)
    except:
        pass
    return False

def get_android_devices():
    """Lấy danh sách Android devices đang kết nối"""
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
        devices = []
        for line in result.stdout.strip().split('\n')[1:]:  # Bỏ qua dòng header
            if line.strip() and 'device' in line:
                device_id = line.split('\t')[0]
                devices.append(device_id)
        return devices
    except Exception as e:
        print(f"❌ Lỗi khi lấy danh sách devices: {e}")
        return []

def quick_connect_inspector():
    """Kết nối nhanh Appium Inspector"""
    
    print("🚀 Quick Connect Appium Inspector")
    print("=" * 50)
    
    # Kiểm tra Appium server
    print("🔧 Kiểm tra Appium server...")
    if not check_appium_server():
        print("❌ Appium server chưa chạy hoặc không hỗ trợ /wd/hub")
        print("   Vui lòng khởi động: appium --allow-cors --base-path /wd/hub")
        return False
    
    print("✅ Appium server đang chạy với /wd/hub support")
    
    # Kiểm tra Android devices
    print("\n📱 Kiểm tra Android devices...")
    devices = get_android_devices()
    
    if not devices:
        print("❌ Không tìm thấy Android device nào được kết nối")
        print("   Vui lòng kết nối device và chạy: adb devices")
        return False
    
    print(f"✅ Tìm thấy {len(devices)} device(s):")
    for device in devices:
        print(f"   - {device}")
    
    # Thông tin kết nối
    print(f"\n🌐 Thông tin kết nối cho Appium Inspector:")
    print(f"   Remote Path: /wd/hub")
    print(f"   Host: localhost")
    print(f"   Port: 4723")
    print(f"   Device: {devices[0]}")
    
    # Capabilities
    capabilities = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": devices[0],
        "appPackage": "jp.co.mobileit.SBI_FX",
        "appActivity": ".MainActivity",
        "noReset": True
    }
    
    print(f"\n📋 Capabilities:")
    print(json.dumps(capabilities, indent=2))
    
    # Tạo file cấu hình mới
    config_file = f"inspector_config_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    inspector_config = {
        "server": {
            "remotePath": "/wd/hub",
            "host": "localhost",
            "port": 4723
        },
        "capabilities": capabilities,
        "desiredCapabilities": capabilities
    }
    
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(inspector_config, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 File cấu hình: {config_file}")
        
    except Exception as e:
        print(f"❌ Lỗi khi tạo file cấu hình: {e}")
    
    print(f"\n🎯 Hướng dẫn kết nối:")
    print(f"1. Appium Inspector đã được mở")
    print(f"2. Nhập thông tin kết nối:")
    print(f"   - Remote Path: /wd/hub")
    print(f"   - Host: localhost")
    print(f"   - Port: 4723")
    print(f"3. Nhập capabilities (như trên)")
    print(f"4. Click 'Start Session'")
    
    print(f"\n✅ Hoàn tất!")
    print(f"🎉 Appium Inspector sẵn sàng kết nối!")
    
    return True

def main():
    """Main function"""
    quick_connect_inspector()

if __name__ == "__main__":
    main() 