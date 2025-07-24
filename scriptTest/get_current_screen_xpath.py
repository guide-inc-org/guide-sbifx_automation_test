#!/usr/bin/env python3
"""
Script để lấy XPath của màn hình hiện tại trên Android device
"""

import os
import sys
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Cấu hình Appium
APPIUM_SERVER = "http://localhost:4723"
ANDROID_PACKAGE = "inc.guide.sbi.fx.dev"
ANDROID_ACTIVITY = ".MainActivity"
ANDROID_DEVICE_NAME = "Android Device"

def setup_driver():
    """Khởi tạo Appium driver"""
    try:
        # Cấu hình Android options
        android_options = UiAutomator2Options()
        android_options.platform_name = "Android"
        android_options.device_name = ANDROID_DEVICE_NAME
        android_options.app_package = ANDROID_PACKAGE
        android_options.app_activity = ANDROID_ACTIVITY
        android_options.no_reset = True
        android_options.automation_name = "UIAutomator2"
        
        # Kết nối Appium server
        print(f"[INFO] Đang kết nối Appium server: {APPIUM_SERVER}")
        driver = webdriver.Remote(APPIUM_SERVER, options=android_options)
        driver.implicitly_wait(10)
        
        print("[SUCCESS] Đã kết nối thành công!")
        return driver
        
    except Exception as e:
        print(f"[ERROR] Lỗi khi khởi tạo driver: {e}")
        return None

def get_page_source(driver):
    """Lấy page source của màn hình hiện tại"""
    try:
        print("[INFO] Đang lấy page source...")
        page_source = driver.page_source
        return page_source
    except Exception as e:
        print(f"[ERROR] Lỗi khi lấy page source: {e}")
        return None

def find_clickable_elements(driver):
    """Tìm tất cả elements có thể click được"""
    try:
        print("[INFO] Đang tìm clickable elements...")
        
        # Tìm elements theo các locator khác nhau
        clickable_elements = []
        
        # 1. Tìm theo accessibility id
        try:
            elements = driver.find_elements(By.ACCESSIBILITY_ID, "")
            for element in elements:
                if element.is_displayed() and element.is_enabled():
                    try:
                        text = element.text or element.get_attribute("content-desc") or "No text"
                        clickable_elements.append({
                            'type': 'accessibility_id',
                            'value': element.get_attribute("content-desc") or element.get_attribute("resource-id"),
                            'text': text,
                            'element': element
                        })
                    except:
                        pass
        except Exception as e:
            print(f"[WARNING] Lỗi khi tìm accessibility_id: {e}")
        
        # 2. Tìm theo resource-id
        try:
            elements = driver.find_elements(By.ID, "")
            for element in elements:
                if element.is_displayed() and element.is_enabled():
                    try:
                        text = element.text or element.get_attribute("content-desc") or "No text"
                        resource_id = element.get_attribute("resource-id")
                        if resource_id:
                            clickable_elements.append({
                                'type': 'id',
                                'value': resource_id,
                                'text': text,
                                'element': element
                            })
                    except:
                        pass
        except Exception as e:
            print(f"[WARNING] Lỗi khi tìm resource-id: {e}")
        
        # 3. Tìm theo class name
        try:
            elements = driver.find_elements(By.CLASS_NAME, "android.widget.Button")
            for element in elements:
                if element.is_displayed() and element.is_enabled():
                    try:
                        text = element.text or element.get_attribute("content-desc") or "No text"
                        clickable_elements.append({
                            'type': 'class_name',
                            'value': 'android.widget.Button',
                            'text': text,
                            'element': element
                        })
                    except:
                        pass
        except Exception as e:
            print(f"[WARNING] Lỗi khi tìm Button: {e}")
        
        # 4. Tìm theo XPath - tất cả elements có thể click
        try:
            xpath_query = "//*[@clickable='true' or @enabled='true']"
            elements = driver.find_elements(By.XPATH, xpath_query)
            for element in elements:
                if element.is_displayed() and element.is_enabled():
                    try:
                        text = element.text or element.get_attribute("content-desc") or "No text"
                        class_name = element.get_attribute("className") or "Unknown"
                        clickable_elements.append({
                            'type': 'xpath',
                            'value': f"//{class_name}[@clickable='true']",
                            'text': text,
                            'element': element
                        })
                    except:
                        pass
        except Exception as e:
            print(f"[WARNING] Lỗi khi tìm XPath: {e}")
        
        return clickable_elements
        
    except Exception as e:
        print(f"[ERROR] Lỗi khi tìm clickable elements: {e}")
        return []

def generate_xpath_for_element(element):
    """Tạo XPath cho một element cụ thể"""
    try:
        # Lấy thông tin element
        tag_name = element.tag_name
        class_name = element.get_attribute("className")
        text = element.text
        content_desc = element.get_attribute("content-desc")
        resource_id = element.get_attribute("resource-id")
        
        # Tạo XPath dựa trên thông tin có sẵn
        xpath = f"//{class_name}"
        
        if resource_id:
            xpath += f"[@resource-id='{resource_id}']"
        elif content_desc:
            xpath += f"[@content-desc='{content_desc}']"
        elif text:
            xpath += f"[@text='{text}']"
        
        return xpath
        
    except Exception as e:
        print(f"[ERROR] Lỗi khi tạo XPath: {e}")
        return None

def save_page_source(page_source, filename="current_page_source.xml"):
    """Lưu page source vào file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(page_source)
        print(f"[SUCCESS] Đã lưu page source vào: {filename}")
        return True
    except Exception as e:
        print(f"[ERROR] Lỗi khi lưu file: {e}")
        return False

def main():
    """Main function"""
    print("🔍 SBI FX Mobile - XPath Inspector")
    print("=" * 50)
    
    # Khởi tạo driver
    driver = setup_driver()
    if not driver:
        print("[ERROR] Không thể khởi tạo driver. Thoát...")
        return
    
    try:
        # Đợi app load
        print("[INFO] Đợi app load...")
        time.sleep(3)
        
        # Lấy page source
        page_source = get_page_source(driver)
        if page_source:
            save_page_source(page_source)
        
        # Tìm clickable elements
        clickable_elements = find_clickable_elements(driver)
        
        print(f"\n📱 TÌM THẤY {len(clickable_elements)} CLICKABLE ELEMENTS:")
        print("=" * 80)
        
        for i, element_info in enumerate(clickable_elements, 1):
            print(f"\n{i}. {element_info['type'].upper()}:")
            print(f"   Class: {element_info['class_name']}")
            print(f"   Text: {element_info['text']}")
            if element_info['resource_id']:
                print(f"   Resource ID: {element_info['resource_id']}")
            if element_info['content_desc']:
                print(f"   Content Desc: {element_info['content_desc']}")
            print(f"   XPath: {element_info['value']}")
        
        print(f"\n💾 Đã lưu page source vào: current_page_source.xml")
        print("🔍 Bạn có thể mở file này để xem cấu trúc XML của màn hình")
        
        # Tạo file XPath summary
        try:
            with open("xpath_summary.txt", "w", encoding="utf-8") as f:
                f.write("SBI FX Mobile - XPath Summary\n")
                f.write("=" * 50 + "\n\n")
                for i, element_info in enumerate(clickable_elements, 1):
                    f.write(f"{i}. {element_info['type'].upper()}:\n")
                    f.write(f"   Class: {element_info['class_name']}\n")
                    f.write(f"   Text: {element_info['text']}\n")
                    if element_info['resource_id']:
                        f.write(f"   Resource ID: {element_info['resource_id']}\n")
                    if element_info['content_desc']:
                        f.write(f"   Content Desc: {element_info['content_desc']}\n")
                    f.write(f"   XPath: {element_info['value']}\n\n")
            print("📄 Đã lưu XPath summary vào: xpath_summary.txt")
        except Exception as e:
            print(f"[WARNING] Không thể lưu XPath summary: {e}")
        
    except Exception as e:
        print(f"[ERROR] Lỗi trong quá trình inspect: {e}")
    
    finally:
        # Đóng driver
        try:
            driver.quit()
            print("[INFO] Đã đóng driver")
        except:
            pass

if __name__ == "__main__":
    main() 