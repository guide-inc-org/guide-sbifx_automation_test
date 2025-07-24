#!/usr/bin/env python3
"""
Mock Excel Test Runner - Chạy Excel tests mà không cần thiết bị thật
"""

import sys
import os
import time
from datetime import datetime

# Thêm thư mục hiện tại vào Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from framework.utils.excel_test_reader import ExcelTestReader

class MockDriver:
    """Mock driver để mô phỏng Appium driver"""
    
    def __init__(self):
        self.current_package = "inc.guide.sbi.fx.dev"
        self.screenshots_taken = []
    
    def save_screenshot(self, filepath):
        """Mock screenshot"""
        self.screenshots_taken.append(filepath)
        print(f"[MOCK] Screenshot saved: {filepath}")
        return True
    
    def quit(self):
        """Mock quit"""
        print("[MOCK] Driver quit")

class MockActionExecutor:
    """Mock action executor - mô phỏng các actions với mock driver"""
    
    def __init__(self):
        self.driver = MockDriver()
        self.step_count = 0
        
        # Mapping các actions
        self.action_handlers = {
            'launchapp': self.launch_app,
            'take_screenshot': self.take_screenshot,
            'print': self.print_message,
            'click': self.click_element,
            'input': self.input_text,
            'wait': self.wait,
            'verify': self.verify_element,
            'swap_tab': self.click_swap_tab,
            'news_tab': self.click_news_tab,
            'economic_tab': self.click_economic_tab,
            'market_tab': self.click_market_tab,
            'chart_tab': self.click_chart_tab,
            'speed_order_tab': self.click_speed_order_tab,
            'login_tab': self.click_login_tab,
            'website_tab': self.click_website_tab,
            'menu_tab': self.click_menu_tab
        }
    
    def execute_step(self, step):
        """Thực hiện một test step (mock)"""
        try:
            action = step['action'].lower()
            object_name = step['object']
            data = step['data']
            note = step['note']
            
            self.step_count += 1
            print(f"[STEP {step['step_number']}] {action} | {object_name} | {data} | {note}")
            
            # Tìm handler cho action
            if action in self.action_handlers:
                result = self.action_handlers[action](object_name, data, note)
                if result:
                    print(f"[SUCCESS] Step {step['step_number']} completed")
                else:
                    print(f"[FAILED] Step {step['step_number']} failed")
                return result
            else:
                print(f"[ERROR] Action không được hỗ trợ: {action}")
                return False
                
        except Exception as e:
            print(f"[ERROR] Lỗi khi thực hiện step {step['step_number']}: {e}")
            return False
    
    def launch_app(self, object_name, data, note):
        """Launch app (mock)"""
        try:
            print(f"[MOCK] 🚀 Khởi động ứng dụng SBI FX...")
            print(f"[MOCK] Package: {self.driver.current_package}")
            time.sleep(2)  # Simulate app launch time
            return True
        except Exception as e:
            print(f"[ERROR] Lỗi khi launch app: {e}")
            return False
    
    def take_screenshot(self, object_name, data, note):
        """Chụp màn hình (mock)"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"mock_screenshot_{data}_{timestamp}.png" if data else f"mock_screenshot_{timestamp}.png"
            filepath = f"output/screenshots/{filename}"
            
            # Tạo thư mục nếu chưa có
            os.makedirs("output/screenshots", exist_ok=True)
            
            # Tạo file screenshot giả
            with open(filepath, 'w') as f:
                f.write(f"Mock screenshot: {filename}")
            
            self.driver.save_screenshot(filepath)
            return True
        except Exception as e:
            print(f"[ERROR] Lỗi khi chụp màn hình: {e}")
            return False
    
    def print_message(self, object_name, data, note):
        """In message"""
        try:
            message = object_name if object_name else data
            print(f"[MOCK] 💬 {message}")
            return True
        except Exception as e:
            print(f"[ERROR] Lỗi khi in message: {e}")
            return False
    
    def click_element(self, object_name, data, note):
        """Click element (mock)"""
        try:
            print(f"[MOCK] 🖱️ Click vào element: {object_name}")
            time.sleep(1)  # Simulate click time
            return True
        except Exception as e:
            print(f"[ERROR] Lỗi khi click element: {e}")
            return False
    
    def input_text(self, object_name, data, note):
        """Nhập text (mock)"""
        try:
            print(f"[MOCK] ⌨️ Nhập text '{data}' vào {object_name}")
            time.sleep(0.5)  # Simulate typing time
            return True
        except Exception as e:
            print(f"[ERROR] Lỗi khi nhập text: {e}")
            return False
    
    def wait(self, object_name, data, note):
        """Đợi (mock)"""
        try:
            wait_time = int(data) if data.isdigit() else 2
            print(f"[MOCK] ⏳ Đợi {wait_time} giây...")
            time.sleep(wait_time)
            return True
        except Exception as e:
            print(f"[ERROR] Lỗi khi đợi: {e}")
            return False
    
    def verify_element(self, object_name, data, note):
        """Verify element (mock)"""
        try:
            print(f"[MOCK] ✅ Verify element: {object_name}")
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"[ERROR] Lỗi khi verify element: {e}")
            return False
    
    # Tab actions (mock)
    def click_swap_tab(self, object_name, data, note):
        """Click Swap tab (mock)"""
        print(f"[MOCK] 🖱️ Click vào tab SWAP...")
        time.sleep(1)
        return True
    
    def click_news_tab(self, object_name, data, note):
        """Click News tab (mock)"""
        print(f"[MOCK] 🖱️ Click vào tab NEWS...")
        time.sleep(1)
        return True
    
    def click_economic_tab(self, object_name, data, note):
        """Click Economic tab (mock)"""
        print(f"[MOCK] 🖱️ Click vào tab ECONOMIC...")
        time.sleep(1)
        return True
    
    def click_market_tab(self, object_name, data, note):
        """Click Market tab (mock)"""
        print(f"[MOCK] 🖱️ Click vào tab MARKET...")
        time.sleep(1)
        return True
    
    def click_chart_tab(self, object_name, data, note):
        """Click Chart tab (mock)"""
        print(f"[MOCK] 🖱️ Click vào tab CHART...")
        time.sleep(1)
        return True
    
    def click_speed_order_tab(self, object_name, data, note):
        """Click Speed Order tab (mock)"""
        print(f"[MOCK] 🖱️ Click vào tab SPEED_ORDER...")
        time.sleep(1)
        return True
    
    def click_login_tab(self, object_name, data, note):
        """Click Login tab (mock)"""
        print(f"[MOCK] 🖱️ Click vào tab LOGIN...")
        time.sleep(1)
        return True
    
    def click_website_tab(self, object_name, data, note):
        """Click Website tab (mock)"""
        print(f"[MOCK] 🖱️ Click vào tab WEBSITE...")
        time.sleep(1)
        return True
    
    def click_menu_tab(self, object_name, data, note):
        """Click Menu tab (mock)"""
        print(f"[MOCK] 🖱️ Click vào tab MENU...")
        time.sleep(1)
        return True

def run_mock_excel_tests(excel_file):
    """Chạy mock Excel tests"""
    print("="*60)
    print("MOCK EXCEL TEST RUNNER")
    print("="*60)
    print(f"File Excel: {excel_file}")
    print("⚠️  Đang chạy với MOCK DRIVER (không cần thiết bị thật)")
    
    try:
        # Đọc Excel file
        test_reader = ExcelTestReader(excel_file)
        test_reader.print_test_steps()
        
        # Lấy test steps
        test_steps = test_reader.get_test_steps()
        
        if not test_steps:
            print("[WARNING] Không có test steps nào để chạy")
            return
        
        # Khởi tạo mock executor
        executor = MockActionExecutor()
        
        # Chạy từng step
        success_count = 0
        total_count = len(test_steps)
        
        print(f"\n=== BẮT ĐẦU CHẠY {total_count} TEST STEPS (MOCK) ===")
        
        for step in test_steps:
            print(f"\n{'='*50}")
            print(f"STEP {step['step_number']}/{total_count}")
            print(f"{'='*50}")
            
            # Thực hiện step
            start_time = datetime.now()
            result = executor.execute_step(step)
            end_time = datetime.now()
            
            duration = (end_time - start_time).total_seconds()
            
            if result:
                success_count += 1
                print(f"[SUCCESS] ✅ Step {step['step_number']} completed in {duration:.2f}s")
            else:
                print(f"[FAILED] ❌ Step {step['step_number']} failed in {duration:.2f}s")
            
            # Đợi một chút giữa các steps
            time.sleep(0.5)
        
        # In kết quả tổng quan
        print("\n" + "="*60)
        print("MOCK TEST EXECUTION SUMMARY")
        print("="*60)
        print(f"Total Steps: {total_count}")
        print(f"Successful: {success_count}")
        print(f"Failed: {total_count - success_count}")
        print(f"Success Rate: {(success_count/total_count)*100:.1f}%")
        print(f"Screenshots taken: {len(executor.driver.screenshots_taken)}")
        print("="*60)
        
        print("\n🎉 Mock test hoàn thành!")
        print("📝 Để chạy thực tế, cần:")
        print("   1. Cài đặt Android SDK")
        print("   2. Khởi động Appium server")
        print("   3. Kết nối thiết bị Android")
        print("   4. Chạy: python run_excel_tests.py")
        
        return {
            'total_steps': total_count,
            'success_count': success_count,
            'failure_count': total_count - success_count,
            'success_rate': (success_count / total_count * 100) if total_count > 0 else 0,
            'screenshots_taken': len(executor.driver.screenshots_taken)
        }
        
    except Exception as e:
        print(f"[ERROR] Lỗi khi chạy mock tests: {e}")
        return None

def main():
    """Main function"""
    print("🚀 SBI FX Mobile Excel Test Runner (MOCK)")
    print("="*50)
    
    # Tạo Excel template nếu chưa có
    excel_file = "testdata/test_cases.xlsx"
    if not os.path.exists(excel_file):
        print("📝 Tạo Excel template...")
        from framework.utils.create_excel_template import create_excel_template
        create_excel_template()
    
    # Chạy mock tests
    print(f"📊 Chạy mock test cases từ: {excel_file}")
    results = run_mock_excel_tests(excel_file)
    
    if results:
        print(f"\n✅ Mock test hoàn thành! Success rate: {results['success_rate']:.1f}%")
        print(f"📸 Screenshots: {results['screenshots_taken']}")
    else:
        print("\n❌ Có lỗi xảy ra!")

if __name__ == "__main__":
    main() 