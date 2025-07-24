#!/usr/bin/env python3
"""
Script tự động chạy XPath inspector và tạo Object Repository
"""

import os
import sys
import subprocess
import time

def run_xpath_inspector():
    """Chạy XPath inspector để lấy thông tin elements"""
    try:
        print("🔍 Đang chạy XPath Inspector...")
        
        # Chạy script get_current_screen_xpath.py
        result = subprocess.run([
            sys.executable, "get_current_screen_xpath.py"
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print("✅ XPath Inspector chạy thành công")
            return True
        else:
            print(f"❌ XPath Inspector lỗi: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ XPath Inspector timeout")
        return False
    except Exception as e:
        print(f"❌ Lỗi khi chạy XPath Inspector: {e}")
        return False

def create_object_repository_from_xpath():
    """Tạo Object Repository từ file XPath summary"""
    try:
        print("📝 Đang tạo Object Repository từ XPath...")
        
        # Import function từ module
        sys.path.append('framework/utils')
        from create_object_repository_excel import create_object_repository_from_xpath_file
        
        # Tạo Object Repository từ file xpath_summary.txt
        if os.path.exists("xpath_summary.txt"):
            result = create_object_repository_from_xpath_file("xpath_summary.txt")
            if result:
                print("✅ Đã tạo Object Repository thành công")
                return True
            else:
                print("❌ Lỗi khi tạo Object Repository")
                return False
        else:
            print("❌ Không tìm thấy file xpath_summary.txt")
            return False
            
    except Exception as e:
        print(f"❌ Lỗi khi tạo Object Repository: {e}")
        return False

def main():
    """Main function"""
    print("🤖 SBI FX Mobile - Auto Object Repository Creator")
    print("=" * 60)
    
    # Bước 1: Chạy XPath Inspector
    print("\n📋 BƯỚC 1: Chạy XPath Inspector")
    print("-" * 40)
    
    if not run_xpath_inspector():
        print("❌ Không thể chạy XPath Inspector. Thoát...")
        return
    
    # Đợi một chút để file được tạo
    time.sleep(2)
    
    # Bước 2: Tạo Object Repository
    print("\n📋 BƯỚC 2: Tạo Object Repository")
    print("-" * 40)
    
    if not create_object_repository_from_xpath():
        print("❌ Không thể tạo Object Repository. Thoát...")
        return
    
    # Bước 3: Hiển thị kết quả
    print("\n📋 BƯỚC 3: Kết quả")
    print("-" * 40)
    
    if os.path.exists("testdata/ObjectRepository.xlsx"):
        print("✅ Đã tạo thành công:")
        print(f"   📄 ObjectRepository.xlsx: testdata/ObjectRepository.xlsx")
        print(f"   📄 XPath Summary: xpath_summary.txt")
        print(f"   📄 Page Source: current_page_source.xml")
        
        # Hiển thị thông tin về Object Repository
        try:
            import pandas as pd
            df = pd.read_excel("testdata/ObjectRepository.xlsx")
            print(f"   📊 Tổng số objects: {len(df)}")
            print(f"   📱 Screens: {', '.join(df['Screen'].unique()) if 'Screen' in df.columns else 'N/A'}")
        except Exception as e:
            print(f"   ⚠️ Không thể đọc thông tin chi tiết: {e}")
    else:
        print("❌ Không tìm thấy file ObjectRepository.xlsx")
    
    print("\n🎉 Hoàn thành!")

if __name__ == "__main__":
    main() 