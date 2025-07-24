#!/usr/bin/env python3
"""
Excel Object Repository Reader - Đọc object definitions từ file Excel
"""

import pandas as pd
import os
from typing import Dict, Any, Optional

class ExcelObjectRepositoryReader:
    """Class để đọc Object Repository từ file Excel"""
    
    def __init__(self, excel_file: str = "testdata/ObjectRepository.xlsx"):
        self.excel_file = excel_file
        self.objects = {}
        self.load_objects()
    
    def load_objects(self):
        """Load tất cả objects từ file Excel"""
        try:
            if not os.path.exists(self.excel_file):
                print(f"[WARNING] File {self.excel_file} không tồn tại")
                return
            
            # Đọc sheet đầu tiên
            df = pd.read_excel(self.excel_file, sheet_name=0)
            
            # Chuyển đổi thành dictionary
            for _, row in df.iterrows():
                object_name = row['ObjectName']
                self.objects[object_name] = {
                    'locator_type': row['LocatorType'],
                    'locator_value': row['LocatorValue'],
                    'description': row['Description'],
                    'screen': row['Screen']
                }
            
            print(f"[INFO] Đã load {len(self.objects)} objects từ {self.excel_file}")
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi load Object Repository: {e}")
    
    def get_object(self, object_name: str) -> Optional[Dict[str, Any]]:
        """Lấy thông tin object theo tên"""
        return self.objects.get(object_name)
    
    def get_all_objects(self) -> Dict[str, Dict[str, Any]]:
        """Lấy tất cả objects"""
        return self.objects
    
    def get_objects_by_screen(self, screen_name: str) -> Dict[str, Dict[str, Any]]:
        """Lấy tất cả objects theo screen"""
        return {name: obj for name, obj in self.objects.items() 
                if obj['screen'] == screen_name}
    
    def print_objects(self):
        """In danh sách tất cả objects"""
        print("\n=== OBJECT REPOSITORY ===")
        print(f"File: {self.excel_file}")
        print(f"Tổng số objects: {len(self.objects)}")
        print("-" * 80)
        
        for object_name, obj_info in self.objects.items():
            print(f"{object_name:20s} | {obj_info['locator_type']:10s} | {obj_info['screen']:15s} | {obj_info['description']}")
        
        print("-" * 80)
    
    def print_objects_by_screen(self, screen_name: str):
        """In danh sách objects theo screen"""
        screen_objects = self.get_objects_by_screen(screen_name)
        print(f"\n=== OBJECTS FOR SCREEN: {screen_name} ===")
        print(f"Số lượng objects: {len(screen_objects)}")
        print("-" * 80)
        
        for object_name, obj_info in screen_objects.items():
            print(f"{object_name:20s} | {obj_info['locator_type']:10s} | {obj_info['description']}")
        
        print("-" * 80)
    
    def validate_object(self, object_name: str) -> bool:
        """Kiểm tra object có tồn tại không"""
        return object_name in self.objects
    
    def get_locator(self, object_name: str) -> Optional[Dict[str, str]]:
        """Lấy locator của object"""
        obj = self.get_object(object_name)
        if obj:
            return {
                'type': obj['locator_type'],
                'value': obj['locator_value']
            }
        return None

if __name__ == "__main__":
    # Test
    reader = ExcelObjectRepositoryReader()
    reader.print_objects()
    
    # Test lấy object cụ thể
    swap_tab = reader.get_object('SWAP_TAB')
    print(f"\nSWAP_TAB: {swap_tab}")
    
    # Test lấy objects theo screen
    reader.print_objects_by_screen('MainScreen') 