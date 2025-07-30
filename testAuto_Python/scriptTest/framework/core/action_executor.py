#!/usr/bin/env python3
"""
Action Executor - Thực hiện các actions trên mobile app
"""

import time
from datetime import datetime
from framework.utils.excel_object_repository_reader import ExcelObjectRepositoryReader
from framework.config.config import Config
import os

class ActionExecutor:
    """Class để thực hiện các actions trên mobile app"""
    
    def __init__(self, driver):
        self.driver = driver
        # Load Object Repository từ Excel
        self.object_repository = ExcelObjectRepositoryReader()
        
    def execute_step(self, step):
        """Thực hiện một test step"""
        try:
            action_type = step['action']
            object_name = step['object']
            data = step['data']
            note = step['note']
            
            print(f"[STEP {step['step_number']}] {action_type} | {object_name} | {data} | {note}")
            
            # Thực hiện action dựa trên loại
            if action_type == 'launchapp':
                return self.launch_app()
            elif action_type == 'click':
                return self.click_element_by_repository(object_name, data, note)
            elif action_type == 'input':
                return self.input_text_by_repository(object_name, data, note)
            elif action_type == 'verify':
                return self.verify_element_by_repository(object_name, data, note)
            elif action_type == 'verify_element_present':
                return self.verify_element_present_by_repository(object_name, data, note)
            elif action_type == 'take_screenshot':
                return self.take_screenshot(data, note)
            elif action_type == 'wait':
                return self.wait(data, note)
            elif action_type == 'print':
                return self.print_message(data, note)
            else:
                print(f"[ERROR] Action không được hỗ trợ: {action_type}")
                return False
                
        except Exception as e:
            print(f"[ERROR] Lỗi khi thực hiện step: {e}")
            return False
    
    def launch_app(self):
        """Khởi động ứng dụng"""
        try:
            print("[INFO] 🚀 Khởi động ứng dụng SBI FX...")
            # App đã được launch khi khởi tạo driver
            print("[SUCCESS] App đã được launch")
            return True
        except Exception as e:
            print(f"[ERROR] Lỗi khi launch app: {e}")
            return False
    
    def click_element_by_repository(self, object_name, data, note):
        """Click vào element sử dụng Object Repository"""
        try:
            if not object_name:
                print("[ERROR] Object name không được cung cấp")
                return False
            
            # Lấy thông tin object từ repository
            object_info = self.object_repository.get_object(object_name)
            if not object_info:
                print(f"[ERROR] Không tìm thấy object: {object_name}")
                return False
            
            print(f"[INFO] 🖱️ Click vào element: {object_name}")
            
            # Tìm element theo locator
            locator_type = object_info['locator_type']
            locator_value = object_info['locator_value']
            
            # Thêm wait để đợi element xuất hiện
            print(f"[INFO] ⏳ Đợi element {object_name} xuất hiện...")
            time.sleep(2)
            
            if locator_type == 'xpath':
                # Thử tìm element với wait
                try:
                    from selenium.webdriver.support.ui import WebDriverWait
                    from selenium.webdriver.support import expected_conditions as EC
                    from selenium.webdriver.common.by import By
                    
                    wait = WebDriverWait(self.driver, 10)
                    element = wait.until(EC.element_to_be_clickable((By.XPATH, locator_value)))
                except:
                    # Fallback: tìm element thông thường
                    element = self.driver.find_element('xpath', locator_value)
            elif locator_type == 'id':
                element = self.driver.find_element('id', locator_value)
            elif locator_type == 'accessibility_id':
                element = self.driver.find_element('accessibility id', locator_value)
            else:
                print(f"[ERROR] Locator type không được hỗ trợ: {locator_type}")
                return False
            
            # Kiểm tra element có clickable không
            if not element.is_enabled():
                print(f"[WARNING] Element {object_name} không enabled")
                return False
            
            # Click vào element
            element.click()
            print(f"[SUCCESS] Đã click thành công {object_name}")
            return True
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi click element {object_name}: {e}")
            return False
    
    def input_text_by_repository(self, object_name, data, note):
        """Input text vào element sử dụng Object Repository"""
        try:
            if not object_name:
                print("[ERROR] Object name không được cung cấp")
                return False
            
            if not data:
                print("[ERROR] Data không được cung cấp")
                return False
            
            # Lấy thông tin object từ repository
            object_info = self.object_repository.get_object(object_name)
            if not object_info:
                print(f"[ERROR] Không tìm thấy object: {object_name}")
                return False
            
            print(f"[INFO] 📝 Input text vào element: {object_name}")
            
            # Tìm element theo locator
            locator_type = object_info['locator_type']
            locator_value = object_info['locator_value']
            
            if locator_type == 'xpath':
                element = self.driver.find_element('xpath', locator_value)
            elif locator_type == 'id':
                element = self.driver.find_element('id', locator_value)
            elif locator_type == 'accessibility_id':
                element = self.driver.find_element('accessibility id', locator_value)
            else:
                print(f"[ERROR] Locator type không được hỗ trợ: {locator_type}")
                return False
            
            # Input text
            element.clear()
            element.send_keys(data)
            return True
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi input text vào element {object_name}: {e}")
            return False
    
    def verify_element_by_repository(self, object_name, data, note):
        """Verify element sử dụng Object Repository"""
        try:
            if not object_name:
                print("[ERROR] Object name không được cung cấp")
                return False
            
            # Lấy thông tin object từ repository
            object_info = self.object_repository.get_object(object_name)
            if not object_info:
                print(f"[ERROR] Không tìm thấy object: {object_name}")
                return False
            
            print(f"[INFO] 🔍 Verify element: {object_name}")
            
            # Tìm element theo locator
            locator_type = object_info['locator_type']
            locator_value = object_info['locator_value']
            
            if locator_type == 'xpath':
                element = self.driver.find_element('xpath', locator_value)
            elif locator_type == 'id':
                element = self.driver.find_element('id', locator_value)
            elif locator_type == 'accessibility_id':
                element = self.driver.find_element('accessibility id', locator_value)
            else:
                print(f"[ERROR] Locator type không được hỗ trợ: {locator_type}")
                return False
            
            # Verify text nếu có data
            if data:
                actual_text = element.text
                if data in actual_text:
                    print(f"[SUCCESS] Text verified: {data}")
                    return True
                else:
                    print(f"[FAILED] Text verification failed. Expected: {data}, Actual: {actual_text}")
                    return False
            else:
                print(f"[SUCCESS] Element found: {object_name}")
                return True
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi verify element {object_name}: {e}")
            return False
    
    def verify_element_present_by_repository(self, object_name, data, note):
        """Verify element present sử dụng Object Repository"""
        try:
            if not object_name:
                print("[ERROR] Object name không được cung cấp")
                return False
            
            # Lấy thông tin object từ repository
            object_info = self.object_repository.get_object(object_name)
            if not object_info:
                print(f"[ERROR] Không tìm thấy object: {object_name}")
                return False
            
            print(f"[INFO] 🔍 Verify element present: {object_name}")
            
            # Tìm element theo locator
            locator_type = object_info['locator_type']
            locator_value = object_info['locator_value']
            
            if locator_type == 'xpath':
                element = self.driver.find_element('xpath', locator_value)
            elif locator_type == 'id':
                element = self.driver.find_element('id', locator_value)
            elif locator_type == 'accessibility_id':
                element = self.driver.find_element('accessibility id', locator_value)
            else:
                print(f"[ERROR] Locator type không được hỗ trợ: {locator_type}")
                return False
            
            if element.is_displayed():
                print(f"[SUCCESS] Element present: {object_name}")
                return True
            else:
                print(f"[FAILED] Element not visible: {object_name}")
                return False
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi verify element present {object_name}: {e}")
            return False
    
    def take_screenshot(self, data, note):
        """Chụp màn hình"""
        try:
            # Tạo thư mục screenshots nếu chưa có
            screenshot_dir = Config.SCREENSHOT_DIR
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
                print(f"[INFO] Đã tạo thư mục: {screenshot_dir}")
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"excel_step_{data}_{timestamp}.png" if data else f"screenshot_{timestamp}.png"
            filepath = f"{screenshot_dir}/{filename}"
            
            self.driver.save_screenshot(filepath)
            print(f"[SCREENSHOT] Đã chụp: {filepath}")
            return True
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi chụp màn hình: {e}")
            return False
    
    def wait(self, data, note):
        """Đợi theo thời gian"""
        try:
            if not data:
                wait_time = 1
            else:
                wait_time = float(data)
            
            print(f"[INFO] ⏳ Đợi {wait_time} giây...")
            time.sleep(wait_time)
            print(f"[INFO] Đã đợi {wait_time} giây")
            return True
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi đợi: {e}")
            return False
    
    def print_message(self, data, note):
        """In thông báo"""
        try:
            message = data if data else note
            print(f"[MESSAGE] {message}")
            return True
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi in message: {e}")
            return False 