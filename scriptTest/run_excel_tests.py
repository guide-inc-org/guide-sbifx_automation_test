#!/usr/bin/env python3
"""
SBI FX Mobile Excel Test Runner
Chạy test cases từ file Excel với Object Repository
"""

import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from framework.core.driver_manager import DriverManager
from framework.tests.excel_test_runner import ExcelTestRunner
from framework.utils.create_object_repository_excel import create_object_repository_excel
from framework.utils.create_test_case_excel import create_test_case_excel

def main():
    """Main function để chạy Excel tests"""
    print("🚀 SBI FX Mobile Excel Test Runner")
    print("=" * 50)
    
    # Tạo Object Repository và Test Case Excel files nếu chưa có
    print("🔧 Đang khởi tạo driver...")
    
    # Tạo Excel files nếu chưa tồn tại
    if not os.path.exists("testdata/ObjectRepository.xlsx"):
        print("📝 Tạo ObjectRepository.xlsx...")
        create_object_repository_excel()
    
    if not os.path.exists("testdata/TestCase.xlsx"):
        print("📝 Tạo TestCase.xlsx...")
        create_test_case_excel()
    
    # Khởi tạo driver
    driver = DriverManager.get_driver()
    
    if not driver:
        print("❌ Có lỗi xảy ra!")
        return
    
    print("📊 Chạy test cases từ: testdata/TestCase.xlsx")
    
    # Khởi tạo và chạy Excel Test Runner
    runner = ExcelTestRunner()
    runner.run_tests(driver)
    
    print("✅ Hoàn thành!")

if __name__ == "__main__":
    main()