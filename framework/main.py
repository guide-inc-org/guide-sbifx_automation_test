#!/usr/bin/env python3
"""
Framework Automation cho SBI FX Mobile App
Tương tự OpenTest với cấu trúc Page Object Model
"""

import sys
import os
import argparse
from framework.config.config import Config
from framework.utils.test_runner import run_tests
from framework.tests.excel_test_runner import run_excel_tests
from framework.core.driver_manager import DriverManager

def main():
    """Main function để chạy framework"""
    parser = argparse.ArgumentParser(description='SBI FX Mobile Automation Framework')
    parser.add_argument('--test-module', '-t', 
                       default='framework.tests.test_news_list',
                       help='Test module để chạy (default: framework.tests.test_news_list)')
    parser.add_argument('--test-class', '-c',
                       default='TestNewsList',
                       help='Test class cụ thể để chạy (default: TestNewsList)')
    parser.add_argument('--no-report', action='store_true',
                       help='Không tạo báo cáo HTML')
    parser.add_argument('--platform', '-p',
                       choices=['android', 'ios'],
                       default='android',
                       help='Platform để test (default: android)')
    parser.add_argument('--list-tests', action='store_true',
                       help='Liệt kê tất cả test cases')
    parser.add_argument('--excel-file', '-e',
                       default='testdata/test_cases.xlsx',
                       help='File Excel chứa test cases (default: testdata/test_cases.xlsx)')
    parser.add_argument('--excel-mode', action='store_true',
                       help='Chạy test cases từ file Excel')
    
    args = parser.parse_args()
    
    # Thiết lập platform
    Config.PLATFORM = args.platform
    
    # Tạo thư mục cần thiết
    Config.create_directories()
    
    print("="*60)
    print("SBI FX MOBILE AUTOMATION FRAMEWORK")
    print("="*60)
    print(f"Platform: {Config.PLATFORM}")
    if args.excel_mode:
        print(f"Excel File: {args.excel_file}")
        print(f"Mode: Excel Test Runner")
    else:
        print(f"Test Module: {args.test_module}")
        print(f"Test Class: {args.test_class}")
    print(f"Generate Report: {not args.no_report}")
    print("="*60)
    
    try:
        # Liệt kê test cases nếu được yêu cầu
        if args.list_tests:
            list_test_cases(args.test_module, args.test_class)
            return
        
        # Chạy Excel tests nếu được yêu cầu
        if args.excel_mode:
            results = run_excel_tests(
                excel_file=args.excel_file,
                generate_report=not args.no_report
            )
        else:
            # Chạy tests thông thường
            results = run_tests(
                test_module_path=args.test_module,
                test_class_name=args.test_class,
                generate_report=not args.no_report
            )
        
        if results:
            # Kiểm tra kết quả
            if results['failures'] > 0 or results['errors'] > 0:
                print(f"\n[WARNING] Có {results['failures']} failures và {results['errors']} errors!")
                sys.exit(1)
            else:
                print(f"\n[SUCCESS] Tất cả {results['total_tests']} tests đã pass!")
                sys.exit(0)
        else:
            print("\n[ERROR] Không thể chạy tests!")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n[INFO] Đã dừng bởi user")
        DriverManager.quit_driver()
        sys.exit(0)
    except Exception as e:
        print(f"\n[ERROR] Lỗi không mong muốn: {e}")
        DriverManager.quit_driver()
        sys.exit(1)

def list_test_cases(test_module_path, test_class_name):
    """Liệt kê tất cả test cases"""
    try:
        import unittest
        
        # Import test module
        sys.path.append(os.path.dirname(test_module_path))
        module_name = os.path.basename(test_module_path).replace('.py', '')
        test_module = __import__(module_name)
        
        if test_class_name:
            # Liệt kê test cases trong class cụ thể
            test_class = getattr(test_module, test_class_name)
            loader = unittest.TestLoader()
            test_methods = loader.getTestCaseNames(test_class)
            
            print(f"\nTest Cases trong {test_class_name}:")
            print("-" * 40)
            for i, method in enumerate(test_methods, 1):
                print(f"{i:2d}. {method}")
        else:
            # Liệt kê tất cả test classes trong module
            test_classes = [name for name in dir(test_module) 
                          if name.startswith('Test') and 
                          isinstance(getattr(test_module, name), type)]
            
            print(f"\nTest Classes trong {module_name}:")
            print("-" * 40)
            for i, class_name in enumerate(test_classes, 1):
                print(f"{i:2d}. {class_name}")
                
                # Liệt kê test methods trong class
                test_class = getattr(test_module, class_name)
                loader = unittest.TestLoader()
                test_methods = loader.getTestCaseNames(test_class)
                
                for j, method in enumerate(test_methods, 1):
                    print(f"    {i}.{j}. {method}")
    
    except Exception as e:
        print(f"[ERROR] Không thể liệt kê test cases: {e}")

if __name__ == "__main__":
    main() 