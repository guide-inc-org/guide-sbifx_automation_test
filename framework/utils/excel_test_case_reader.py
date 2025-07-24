#!/usr/bin/env python3
"""
Excel Test Case Reader - Đọc test cases từ file Excel
"""

import pandas as pd
import os
from typing import List, Dict, Any

class ExcelTestCaseReader:
    """Class để đọc Test Cases từ file Excel"""
    
    def __init__(self, excel_file: str = "testdata/TestCase.xlsx"):
        self.excel_file = excel_file
        self.test_steps = []
        # Không load test cases trong __init__, chỉ khi gọi load_test_cases()
    
    def load_test_cases(self):
        """Load tất cả test cases từ file Excel"""
        try:
            if not os.path.exists(self.excel_file):
                print(f"[WARNING] File {self.excel_file} không tồn tại")
                return []
            
            # Đọc sheet đầu tiên
            df = pd.read_excel(self.excel_file, sheet_name=0)
            
            # Chuyển đổi thành list of dictionaries
            for index, row in df.iterrows():
                test_step = {
                    'step_number': index + 1,  # Sử dụng index + 1 làm step number
                    'action': row['Action'],
                    'object': row['Object'] if pd.notna(row['Object']) else '',
                    'data': row['Data'] if pd.notna(row['Data']) else '',
                    'note': row['Note'] if pd.notna(row['Note']) else ''
                }
                self.test_steps.append(test_step)
            
            print(f"[INFO] Đã load {len(self.test_steps)} test steps từ {self.excel_file}")
            return self.test_steps
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi load Test Cases: {e}")
            return []
    
    def get_test_steps(self) -> List[Dict[str, Any]]:
        """Lấy tất cả test steps"""
        return self.test_steps
    
    def get_test_steps_by_action(self, action: str) -> List[Dict[str, Any]]:
        """Lấy test steps theo action"""
        return [step for step in self.test_steps if step['action'] == action]
    
    def get_test_steps_by_object(self, object_name: str) -> List[Dict[str, Any]]:
        """Lấy test steps theo object"""
        return [step for step in self.test_steps if step['object'] == object_name]
    
    def get_test_case_steps(self, test_case_name: str) -> List[Dict[str, Any]]:
        """Lấy test steps theo test case name (dựa vào Data field)"""
        return [step for step in self.test_steps 
                if test_case_name in str(step['data'])]
    
    def print_test_steps(self):
        """In danh sách tất cả test steps"""
        print("\n=== TEST CASES ===")
        print(f"File: {self.excel_file}")
        print(f"Tổng số steps: {len(self.test_steps)}")
        print("-" * 100)
        print(f"{'Step':<6} | {'Action':<15} | {'Object':<20} | {'Data':<30} | {'Note'}")
        print("-" * 100)
        
        for step in self.test_steps:
            print(f"{step['step_number']:<6} | {step['action']:<15} | {step['object']:<20} | {str(step['data']):<30} | {step['note']}")
        
        print("-" * 100)
    
    def print_test_case_summary(self):
        """In tóm tắt test cases"""
        print("\n=== TEST CASE SUMMARY ===")
        
        # Nhóm theo test case
        test_cases = {}
        for step in self.test_steps:
            if 'TC' in str(step['data']):
                tc_name = str(step['data'])
                if tc_name not in test_cases:
                    test_cases[tc_name] = []
                test_cases[tc_name].append(step)
        
        print(f"Tổng số test cases: {len(test_cases)}")
        print("-" * 60)
        
        for tc_name, steps in test_cases.items():
            print(f"{tc_name}: {len(steps)} steps")
        
        print("-" * 60)
    
    def validate_test_steps(self) -> List[str]:
        """Validate test steps và trả về danh sách lỗi"""
        errors = []
        
        for step in self.test_steps:
            # Kiểm tra action không được rỗng
            if not step['action']:
                errors.append(f"Step {step['step_number']}: Action không được rỗng")
            
            # Kiểm tra step number phải là số
            if not isinstance(step['step_number'], int):
                errors.append(f"Step {step['step_number']}: Step number phải là số")
        
        return errors
    
    def get_unique_actions(self) -> List[str]:
        """Lấy danh sách các actions duy nhất"""
        return list(set(step['action'] for step in self.test_steps))
    
    def get_unique_objects(self) -> List[str]:
        """Lấy danh sách các objects duy nhất"""
        objects = [step['object'] for step in self.test_steps if step['object']]
        return list(set(objects))
    
    def export_to_excel(self, output_file: str = None):
        """Export test steps ra file Excel mới"""
        if not output_file:
            output_file = f"testdata/TestCase_Export_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        
        df = pd.DataFrame(self.test_steps)
        df.to_excel(output_file, index=False)
        print(f"[INFO] Đã export test cases ra: {output_file}")

if __name__ == "__main__":
    # Test
    reader = ExcelTestCaseReader()
    reader.print_test_steps()
    reader.print_test_case_summary()
    
    # Test lấy test steps theo action
    click_steps = reader.get_test_steps_by_action('click')
    print(f"\nClick steps: {len(click_steps)}")
    
    # Test lấy unique actions
    unique_actions = reader.get_unique_actions()
    print(f"\nUnique actions: {unique_actions}")
    
    # Test validate
    errors = reader.validate_test_steps()
    if errors:
        print(f"\nValidation errors: {errors}")
    else:
        print("\n✅ All test steps are valid") 