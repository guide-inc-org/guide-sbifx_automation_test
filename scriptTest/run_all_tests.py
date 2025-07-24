#!/usr/bin/env python3
"""
Script tổng hợp để chạy tất cả các loại tests
"""

import sys
import os
import argparse

# Thêm thư mục hiện tại vào Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='SBI FX Mobile Test Runner - Tất cả các loại tests')
    parser.add_argument('--mode', '-m', 
                       choices=['demo', 'mock', 'real', 'framework'],
                       default='demo',
                       help='Chế độ chạy (default: demo)')
    parser.add_argument('--excel-file', '-e',
                       default='testdata/test_cases.xlsx',
                       help='File Excel test cases')
    parser.add_argument('--list-modes', action='store_true',
                       help='Liệt kê tất cả các chế độ chạy')
    
    args = parser.parse_args()
    
    if args.list_modes:
        print("="*60)
        print("SBI FX MOBILE TEST RUNNER - CÁC CHẾ ĐỘ CHẠY")
        print("="*60)
        print("1. demo     - Chạy demo đơn giản (không cần thiết bị)")
        print("2. mock     - Chạy mock với screenshots (không cần thiết bị)")
        print("3. real     - Chạy thực tế trên thiết bị (cần Appium + thiết bị)")
        print("4. framework- Chạy với framework main")
        print("="*60)
        return
    
    print("🚀 SBI FX Mobile Test Runner")
    print("="*50)
    print(f"Mode: {args.mode}")
    print(f"Excel file: {args.excel_file}")
    print("="*50)
    
    try:
        if args.mode == 'demo':
            print("📱 Chạy DEMO mode...")
            from demo_excel_runner import main as demo_main
            demo_main()
            
        elif args.mode == 'mock':
            print("🎭 Chạy MOCK mode...")
            from run_excel_tests_mock import main as mock_main
            mock_main()
            
        elif args.mode == 'real':
            print("📱 Chạy REAL mode (cần thiết bị)...")
            print("⚠️  Đảm bảo:")
            print("   - Appium server đang chạy")
            print("   - Thiết bị Android đã kết nối")
            print("   - Android SDK đã cài đặt")
            print()
            
            from run_excel_tests import main as real_main
            real_main()
            
        elif args.mode == 'framework':
            print("🔧 Chạy FRAMEWORK mode...")
            from framework.main import main as framework_main
            # Override sys.argv để framework main nhận đúng arguments
            sys.argv = ['framework/main.py', '--excel-mode', '--excel-file', args.excel_file]
            framework_main()
            
    except KeyboardInterrupt:
        print("\n⏹️  Đã dừng bởi user")
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")
        print("\n💡 Gợi ý:")
        print("   - Chạy 'python run_all_tests.py --list-modes' để xem các chế độ")
        print("   - Bắt đầu với 'python run_all_tests.py --mode demo'")

if __name__ == "__main__":
    main() 