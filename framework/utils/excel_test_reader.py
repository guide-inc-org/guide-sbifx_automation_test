import pandas as pd
import os
from framework.config.config import Config

class ExcelTestReader:
    """Đọc test cases từ file Excel"""
    
    def __init__(self, excel_file):
        self.excel_file = excel_file
        self.test_data = None
        self.load_test_data()
    
    def load_test_data(self):
        """Load test data từ Excel file"""
        try:
            if not os.path.exists(self.excel_file):
                raise FileNotFoundError(f"File Excel không tồn tại: {self.excel_file}")
            
            # Đọc Excel file
            self.test_data = pd.read_excel(self.excel_file)
            
            # Kiểm tra cấu trúc
            required_columns = ['Run/NoRun', 'Action', 'Object', 'Data', 'Note']
            missing_columns = [col for col in required_columns if col not in self.test_data.columns]
            
            if missing_columns:
                raise ValueError(f"Thiếu các cột bắt buộc: {missing_columns}")
            
            # Lọc chỉ những rows có Run/NoRun = 'r'
            self.test_data = self.test_data[self.test_data['Run/NoRun'].str.lower() == 'r'].copy()
            
            print(f"[INFO] Đã load {len(self.test_data)} test steps từ {self.excel_file}")
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi load Excel file: {e}")
            raise
    
    def get_test_steps(self):
        """Lấy danh sách test steps"""
        if self.test_data is None:
            return []
        
        test_steps = []
        for index, row in self.test_data.iterrows():
            step = {
                'step_number': index + 1,
                'action': str(row['Action']).strip(),
                'object': str(row['Object']).strip() if pd.notna(row['Object']) else '',
                'data': str(row['Data']).strip() if pd.notna(row['Data']) else '',
                'note': str(row['Note']).strip() if pd.notna(row['Note']) else ''
            }
            test_steps.append(step)
        
        return test_steps
    
    def get_test_steps_by_action(self, action):
        """Lấy test steps theo action cụ thể"""
        steps = self.get_test_steps()
        return [step for step in steps if step['action'].lower() == action.lower()]
    
    def print_test_steps(self):
        """In danh sách test steps"""
        steps = self.get_test_steps()
        
        print(f"\n=== TEST STEPS TỪ EXCEL ===")
        print(f"File: {self.excel_file}")
        print(f"Tổng số steps: {len(steps)}")
        print("-" * 80)
        
        for step in steps:
            print(f"Step {step['step_number']:2d}: {step['action']:15s} | {step['object']:20s} | {step['data']:15s} | {step['note']}")
        
        print("-" * 80) 