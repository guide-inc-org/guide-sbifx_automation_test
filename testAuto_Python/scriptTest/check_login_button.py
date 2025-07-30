#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script kiểm tra Login button trên màn hình hiện tại
"""

from appium import webdriver
import time
import os
import sys
from appium.webdriver.common.appiumby import AppiumBy

# Import các module common
sys.path.append(os.path.join(os.path.dirname(__file__)))
from common.screenshot_utils import ScreenshotUtils
from common.appium_config import AppiumConfig

class CheckLoginButton:
    """Kiểm tra Login button trên màn hình hiện tại"""
    
    def __init__(self, platform="android", server_url="http://localhost:4723/wd/hub"):
        self.platform = platform
        self.server_url = server_url
        self.driver = None
        self.screenshot_utils = ScreenshotUtils("output/screenshots/check")
        self.appium_config = AppiumConfig(server_url)
    
    def setup_driver(self):
        """Setup Appium driver"""
        self.driver = self.appium_config.setup_driver(self.platform)
        print(f"[INFO] Đã setup driver thành công cho {self.platform}")
    
    def check_login_button(self):
        """Kiểm tra Login button"""
        print("\n=== KIỂM TRA LOGIN BUTTON ===")
        
        # XPath cần kiểm tra
        login_xpath = "//*[@content-desc='ログイン']"
        
        try:
            # Tìm element
            print(f"[INFO] Đang tìm element với XPath: {login_xpath}")
            login_button = self.driver.find_element(AppiumBy.XPATH, login_xpath)
            
            # Kiểm tra các thuộc tính
            print(f"[SUCCESS] ✅ Tìm thấy Login button!")
            print(f"[INFO] Element class: {login_button.tag_name}")
            print(f"[INFO] Element text: '{login_button.text}'")
            print(f"[INFO] Element content-desc: '{login_button.get_attribute('content-desc')}'")
            print(f"[INFO] Element enabled: {login_button.is_enabled()}")
            print(f"[INFO] Element displayed: {login_button.is_displayed()}")
            print(f"[INFO] Element clickable: {login_button.get_attribute('clickable')}")
            
            # Chụp screenshot
            self.screenshot_utils.take_screenshot(self.driver, "login_button_found", "check")
            
            # Thử click (không thực sự click, chỉ kiểm tra)
            print(f"[INFO] Element có thể click: {login_button.is_enabled() and login_button.is_displayed()}")
            
            return True
            
        except Exception as e:
            print(f"[ERROR] ❌ Không tìm thấy Login button: {e}")
            
            # Thử tìm các element khác có thể là login button
            print("\n=== TÌM KIẾM CÁC ELEMENT KHÁC ===")
            alternative_xpaths = [
                "//*[contains(@content-desc, 'ログイン')]",
                "//*[contains(@text, 'ログイン')]",
                "//*[@content-desc='Login']",
                "//*[@text='Login']",
                "//android.view.View[@content-desc='ログイン']",
                "//android.widget.Button[@content-desc='ログイン']",
                "//*[contains(@class, 'Button') and contains(@content-desc, 'ログイン')]"
            ]
            
            for i, xpath in enumerate(alternative_xpaths, 1):
                try:
                    element = self.driver.find_element(AppiumBy.XPATH, xpath)
                    print(f"[INFO] ✅ Tìm thấy element {i}: {xpath}")
                    print(f"   - Class: {element.tag_name}")
                    print(f"   - Text: '{element.text}'")
                    print(f"   - Content-desc: '{element.get_attribute('content-desc')}'")
                    print(f"   - Displayed: {element.is_displayed()}")
                except:
                    print(f"[INFO] ❌ Không tìm thấy: {xpath}")
            
            # Chụp screenshot lỗi
            self.screenshot_utils.take_screenshot(self.driver, "login_button_not_found", "error")
            
            return False
    
    def check_current_screen(self):
        """Kiểm tra thông tin màn hình hiện tại"""
        print("\n=== THÔNG TIN MÀN HÌNH HIỆN TẠI ===")
        try:
            # Lấy page source để xem cấu trúc
            page_source = self.driver.page_source
            print(f"[INFO] Page source length: {len(page_source)} characters")
            
            # Tìm tất cả elements có content-desc
            elements_with_desc = self.driver.find_elements(AppiumBy.XPATH, "//*[@content-desc]")
            print(f"[INFO] Tìm thấy {len(elements_with_desc)} elements có content-desc")
            
            # In ra các content-desc
            print("\n=== CÁC CONTENT-DESC CÓ SẴN ===")
            for i, element in enumerate(elements_with_desc[:10], 1):  # Chỉ in 10 đầu tiên
                desc = element.get_attribute('content-desc')
                if desc and desc.strip():
                    print(f"{i}. '{desc}' (class: {element.tag_name})")
            
            if len(elements_with_desc) > 10:
                print(f"... và {len(elements_with_desc) - 10} elements khác")
                
        except Exception as e:
            print(f"[ERROR] Lỗi khi kiểm tra màn hình: {e}")
    
    def run_check(self):
        """Chạy kiểm tra"""
        try:
            print("=== BẮT ĐẦU KIỂM TRA LOGIN BUTTON ===")
            
            # Setup driver
            self.setup_driver()
            
            # Kiểm tra màn hình hiện tại
            self.check_current_screen()
            
            # Kiểm tra login button
            found = self.check_login_button()
            
            if found:
                print("\n🎉 KẾT QUẢ: Login button TỒN TẠI và có thể sử dụng!")
            else:
                print("\n⚠️ KẾT QUẢ: Login button KHÔNG TỒN TẠI hoặc không tìm thấy!")
            
            print("\n=== KẾT THÚC KIỂM TRA ===")
            
        except Exception as e:
            print(f"[ERROR] Lỗi trong quá trình kiểm tra: {e}")
            if self.driver:
                self.screenshot_utils.take_screenshot_on_error(self.driver, "check_fatal_error", str(e))
        finally:
            if self.driver:
                self.driver.quit()
                print("[INFO] Đã đóng driver")

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Cách dùng: python check_login_button.py [android|ios]")
        sys.exit(1)
    
    platform = sys.argv[1].lower()
    if platform not in ["android", "ios"]:
        print("Platform phải là 'android' hoặc 'ios'")
        sys.exit(1)
    
    # Tạo instance và chạy kiểm tra
    checker = CheckLoginButton(platform)
    checker.run_check()

if __name__ == "__main__":
    main() 