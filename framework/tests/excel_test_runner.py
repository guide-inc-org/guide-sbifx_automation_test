#!/usr/bin/env python3
"""
Excel Test Runner - Chạy test cases từ file Excel
"""

import sys
import os
import time
from datetime import datetime

# Thêm thư mục hiện tại vào Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from framework.utils.excel_test_case_reader import ExcelTestCaseReader
from framework.utils.excel_object_repository_reader import ExcelObjectRepositoryReader
from framework.core.action_executor import ActionExecutor
from framework.utils.report_generator import ReportGenerator

class ExcelTestRunner:
    def __init__(self, test_case_file="testdata/TestCase.xlsx", object_repo_file="testdata/ObjectRepository.xlsx"):
        self.test_case_file = test_case_file
        self.object_repo_file = object_repo_file
        self.test_case_reader = ExcelTestCaseReader(test_case_file)
        self.object_repo_reader = ExcelObjectRepositoryReader(object_repo_file)
        self.action_executor = None
        self.report_generator = ReportGenerator()
        
        # Test results tracking
        self.test_results = {
            'total_steps': 0,
            'successful': 0,
            'failed': 0,
            'success_rate': 0.0,
            'step_results': {}
        }
    
    def run_tests(self, driver):
        """Chạy tất cả test cases từ file Excel"""
        print("=" * 60)
        print("EXCEL TEST RUNNER")
        print("=" * 60)
        print(f"File Excel: {self.test_case_file}")
        print()
        
        # Load test cases và object repository
        test_steps = self.test_case_reader.load_test_cases()
        self.object_repo_reader.load_objects()
        
        if not test_steps:
            print("[WARNING] Không có test steps nào để chạy")
            return
        
        # Khởi tạo action executor
        self.action_executor = ActionExecutor(driver)
        
        # In thông tin test cases
        self._print_test_cases_info(test_steps)
        
        # Bắt đầu chạy tests
        print(f"\n=== BẮT ĐẦU CHẠY {len(test_steps)} TEST STEPS ===")
        print()
        
        start_time = time.time()
        
        # Chạy từng test step
        for i, step in enumerate(test_steps, 1):
            self._execute_test_step(i, step)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Tính toán kết quả
        self._calculate_results(len(test_steps))
        
        # In kết quả tổng quan
        self._print_summary()
        
        # Tạo báo cáo
        self._generate_reports(test_steps, execution_time)
        
        print(f"\n✅ Hoàn thành! Success rate: {self.test_results['success_rate']:.1f}%")
    
    def _execute_test_step(self, step_number, step):
        """Thực hiện một test step"""
        print("=" * 50)
        print(f"STEP {step_number}/{len(self.test_case_reader.test_steps)}")
        print("=" * 50)
        
        action = step.get('action', '')
        object_name = step.get('object', '')
        data = step.get('data', '')
        note = step.get('note', '')
        
        print(f"[STEP {step_number}] {action} | {object_name} | {data} | {note}")
        
        start_time = time.time()
        success = False
        error_message = ""
        
        try:
            # Thực hiện action
            if action == 'launchapp':
                success = self.action_executor.launch_app()
            elif action == 'click':
                success = self.action_executor.click_element_by_repository(object_name, data, note)
            elif action == 'input':
                success = self.action_executor.input_text_by_repository(object_name, data, note)
            elif action == 'verify':
                success = self.action_executor.verify_element_by_repository(object_name, data, note)
            elif action == 'take_screenshot':
                success = self.action_executor.take_screenshot(data, note)
            elif action == 'wait':
                success = self.action_executor.wait(data, note)
            elif action == 'print':
                success = self.action_executor.print_message(data, note)
            else:
                error_message = f"Action không được hỗ trợ: {action}"
                success = False
            
        except Exception as e:
            error_message = str(e)
            success = False
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Lưu kết quả
        status = "PASS" if success else "FAIL"
        self.test_results['step_results'][step_number] = {
            'status': status,
            'duration': duration,
            'error': error_message,
            'action': action
        }
        
        # In kết quả
        if success:
            print(f"[SUCCESS] Step {step_number} completed in {duration:.2f}s")
        else:
            print(f"[FAILED] Step {step_number} failed in {duration:.2f}s")
            if error_message:
                print(f"[ERROR] {error_message}")
        
        print()
    
    def _calculate_results(self, total_steps):
        """Tính toán kết quả tổng quan"""
        successful = 0
        failed = 0
        
        for step_result in self.test_results['step_results'].values():
            if step_result['status'] == 'PASS':
                successful += 1
            else:
                failed += 1
        
        self.test_results['total_steps'] = total_steps
        self.test_results['successful'] = successful
        self.test_results['failed'] = failed
        self.test_results['success_rate'] = (successful / total_steps) * 100 if total_steps > 0 else 0
    
    def _print_test_cases_info(self, test_steps):
        """In thông tin test cases"""
        print("=== TEST CASES ===")
        print(f"File: {self.test_case_file}")
        print(f"Tổng số steps: {len(test_steps)}")
        print("-" * 100)
        print(f"{'Step':<6} | {'Action':<15} | {'Object':<20} | {'Data':<30} | {'Note'}")
        print("-" * 100)
        
        for i, step in enumerate(test_steps, 1):
            action = step.get('action', '')
            object_name = step.get('object', '')
            data = step.get('data', '')
            note = step.get('note', '')
            
            # Cắt ngắn các field nếu quá dài
            action = action[:14] + "..." if len(action) > 15 else action
            object_name = object_name[:19] + "..." if len(object_name) > 20 else object_name
            data_str = str(data) if data is not None else ""
            data_str = data_str[:29] + "..." if len(data_str) > 30 else data_str
            
            print(f"{i:<6} | {action:<15} | {object_name:<20} | {data_str:<30} | {note}")
        
        print("-" * 100)
        print()
    
    def _print_summary(self):
        """In kết quả tổng quan"""
        print("=" * 60)
        print("TEST EXECUTION SUMMARY")
        print("=" * 60)
        print(f"Total Steps: {self.test_results['total_steps']}")
        print(f"Successful: {self.test_results['successful']}")
        print(f"Failed: {self.test_results['failed']}")
        print(f"Success Rate: {self.test_results['success_rate']:.1f}%")
        print("=" * 60)
        
        print("\nDETAILED RESULTS:")
        print("-" * 80)
        print(f"{'Step':<6} | {'Action':<15} | {'Object':<20} | {'Status':<8} | {'Duration':<8}")
        print("-" * 80)
        
        for step_num in sorted(self.test_results['step_results'].keys()):
            step_result = self.test_results['step_results'][step_num]
            action = step_result.get('action', '')
            object_name = ""  # Có thể lấy từ test steps nếu cần
            status = step_result.get('status', 'UNKNOWN')
            duration = step_result.get('duration', 0)
            
            # Cắt ngắn các field
            action = action[:14] + "..." if len(action) > 15 else action
            object_name = object_name[:19] + "..." if len(object_name) > 20 else object_name
            
            status_icon = "✅" if status == "PASS" else "❌"
            print(f"{step_num:<6} | {action:<15} | {object_name:<20} | {status_icon} {status:<6} | {duration:<7.2f}s")
        
        print("-" * 80)
    
    def _generate_reports(self, test_steps, execution_time):
        """Tạo báo cáo Excel và HTML"""
        try:
            # Tạo báo cáo Excel
            excel_report = self.report_generator.generate_excel_report(
                self.test_results, test_steps, execution_time
            )
            
            # Tạo báo cáo HTML
            html_report = self.report_generator.generate_html_report(
                self.test_results, test_steps, execution_time
            )
            
            if excel_report:
                print(f"📊 Excel Report: {excel_report}")
            if html_report:
                print(f"🌐 HTML Report: {html_report}")
                
        except Exception as e:
            print(f"[ERROR] Lỗi khi tạo báo cáo: {e}")

def main():
    """Main function để chạy Excel Test Runner"""
    runner = ExcelTestRunner()
    
    # Import và khởi tạo driver
    from framework.core.driver_manager import DriverManager
    
    driver = DriverManager.get_driver()
    if driver:
        runner.run_tests(driver)
    else:
        print("[ERROR] Không thể khởi tạo driver")

if __name__ == "__main__":
    main() 