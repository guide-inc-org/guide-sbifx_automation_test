#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NewsList Automation Test - Refactored Version
Sử dụng các module common cho screenshot và Appium configuration
"""

import sys
import time
import os

# Import các module common
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from common.screenshot_utils import ScreenshotUtils, take_screenshot
from common.appium_config import AppiumConfig, setup_driver


# XPath constants from extracted objects
class XPathConstants:
    MARKET_TAB = "//android.view.View[@content-desc='マーケット']"
    RATE_TAB = "//android.view.View[@content-desc='レート\nタブ: 1/4']"
    SWAP_TAB = "//android.view.View[@content-desc='スワップ\nタブ: 2/4']"
    NEWS_TAB = "//android.view.View[@content-desc='ニュース\nタブ: 3/4']"
    ECONOMIC_TAB = "//android.view.View[@content-desc='経済指標\nタブ: 4/4']"
    チャート_TAB = "//android.widget.ImageView[@content-desc='チャート']"
    スピード注文_TAB = "//android.widget.ImageView[@content-desc='スピード注文']"
    ログイン_TAB = "//android.widget.ImageView[@content-desc='ログイン']"
    ウェブサイト_TAB = "//android.widget.ImageView[@content-desc='ウェブサイト']"
    メニュー_TAB = "//android.widget.ImageView[@content-desc='メニュー']"

class NewsListAutomation:
    """Class chính cho automation testing NewsList"""
    
    def __init__(self, platform="android", server_url="http://localhost:4723"):
        """
        Khởi tạo NewsListAutomation
        
        Args:
            platform (str): 'android' hoặc 'ios'
            server_url (str): URL của Appium server
        """
        self.platform = platform
        self.server_url = server_url
        self.driver = None
        
        # Khởi tạo các utilities
        self.screenshot_utils = ScreenshotUtils("output/screenshots/newslist")
        self.appium_config = AppiumConfig(server_url)
    
    def setup_driver(self, custom_config=None):
        """
        Setup Appium driver
        
        Args:
            custom_config (dict): Cấu hình tùy chỉnh
        """
        self.driver = self.appium_config.setup_driver(self.platform, custom_config)
        print(f"[INFO] Đã setup driver thành công cho {self.platform}")
    
    def test_show_news_list(self):
        """Test case 1: Kiểm tra hiển thị danh sách tin tức"""
        print("[TC1] Kiểm tra hiển thị danh sách tin tức khi vào màn hình")
        
        # Chụp màn hình trước
        self.screenshot_utils.take_screenshot(self.driver, "TC1", "before")
        
        # TODO: Thêm code kiểm tra element danh sách, so sánh dữ liệu API nếu cần
        # Ví dụ: kiểm tra xem có ít nhất 1 tin tức hiển thị
        # news_list = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View")
        # if not news_list:
        #     print("[ERROR] Không tìm thấy danh sách tin tức!")
        # else:
        #     print(f"[INFO] Đã tìm thấy {len(news_list)} tin tức hiển thị.")
        
        print("[INFO] TC1 completed")
        time.sleep(2)
        
        # Chụp màn hình sau
        self.screenshot_utils.take_screenshot(self.driver, "TC1", "after")
    
    def test_tab_Swap(self):
        """Test case 2: Kiểm tra hiển thị dữ liệu khi tab Swap"""
        print("[TC2] Kiểm tra hiển thị dữ liệu khi tab Swap")
        
        # Chụp màn hình trước
        self.screenshot_utils.take_screenshot(self.driver, "TC2", "before")
        
        try:
            from appium.webdriver.common.appiumby import AppiumBy
            news_tab = self.driver.find_element(AppiumBy.XPATH, XPathConstants.SWAP_TAB)
            
            if not news_tab.is_displayed():
                print("[ERROR] Không tìm thấy tab スワップ!")
            else:
                print("[INFO] Tab スワップ hiển thị đúng.")
                news_tab.click()
                
        except Exception as e:
            print(f"[ERROR] Lỗi khi tìm tab: {e}")
            # Chụp màn hình lỗi
            self.screenshot_utils.take_screenshot_on_error(self.driver, "TC2", str(e))
        
        time.sleep(2)
        # Chụp màn hình sau
        self.screenshot_utils.take_screenshot(self.driver, "TC2", "after")
    
    def test_tab_News(self):
        """Test case 3: Kiểm tra chuyển tab マーケット/ニュース"""
        print("[TC3] Kiểm tra chuyển tab マーケット/ニュース")
        
        # Chụp màn hình trước
        self.screenshot_utils.take_screenshot(self.driver, "TC3", "before")
        
        try:
            from appium.webdriver.common.appiumby import AppiumBy
            news_tab = self.driver.find_element(AppiumBy.XPATH, XPathConstants.NEWS_TAB)
            
            if not news_tab.is_displayed():
                print("[ERROR] Không tìm thấy tab ニュース!")
            else:
                print("[INFO] Tab ニュース hiển thị đúng.")
                news_tab.click()
                
        except Exception as e:
            print(f"[ERROR] Lỗi khi tìm tab: {e}")
            self.screenshot_utils.take_screenshot_on_error(self.driver, "TC3", str(e))
        
        time.sleep(2)
        # Chụp màn hình sau
        self.screenshot_utils.take_screenshot(self.driver, "TC3", "after")
    
    def test_tab_Economic(self):
        """Test case 4: Kiểm tra chuyển tab マーケット/経済指標"""
        print("[TC4] Kiểm tra chuyển tab マーケット/経済指標")
        
        # Chụp màn hình trước
        self.screenshot_utils.take_screenshot(self.driver, "TC4", "before")
        
        try:
            from appium.webdriver.common.appiumby import AppiumBy
            news_tab = self.driver.find_element(AppiumBy.XPATH, XPathConstants.ECONOMIC_TAB)
            
            if not news_tab.is_displayed():
                print("[ERROR] Không tìm thấy tab 経済指標!")
            else:
                print("[INFO] Tab 経済指標 hiển thị đúng.")
                news_tab.click()
                
        except Exception as e:
            print(f"[ERROR] Lỗi khi tìm tab: {e}")
            self.screenshot_utils.take_screenshot_on_error(self.driver, "TC4", str(e))
        
        time.sleep(2)
        # Chụp màn hình sau
        self.screenshot_utils.take_screenshot(self.driver, "TC4", "after")
    
    def test_tab_Market(self):
        """Test case 5: Kiểm tra reload page"""
        print("[TC5] Kiểm tra reload page")
        
        # Chụp màn hình trước
        self.screenshot_utils.take_screenshot(self.driver, "TC5", "before")
        
        try:
            from appium.webdriver.common.appiumby import AppiumBy
            news_tab = self.driver.find_element(AppiumBy.XPATH, XPathConstants.MARKET_TAB)
            
            if not news_tab.is_displayed():
                print("[ERROR] Không tìm thấy tab reload!")
            else:
                print("[INFO] Tab hiển thị đúng.")
                news_tab.click()
                
        except Exception as e:
            print(f"[ERROR] Lỗi khi tìm tab: {e}")
            self.screenshot_utils.take_screenshot_on_error(self.driver, "TC5", str(e))
        
        time.sleep(2)
        # Chụp màn hình sau
        self.screenshot_utils.take_screenshot(self.driver, "TC5", "after")
    
    def test_tab_Chart(self):
        """Test case 6: Kiểm tra hiển thị Chart"""
        print("[TC6] Kiểm tra hiển thị Chart")
        
        # Chụp màn hình trước
        self.screenshot_utils.take_screenshot(self.driver, "TC6", "before")
        
        try:
            from appium.webdriver.common.appiumby import AppiumBy
            news_tab = self.driver.find_element(AppiumBy.XPATH, XPathConstants.チャート_TAB)
            
            if not news_tab.is_displayed():
                print("[ERROR] Không tìm thấy tab Chart!")
            else:
                print("[INFO] Tab Chart hiển thị đúng.")
                news_tab.click()
                
        except Exception as e:
            print(f"[ERROR] Lỗi khi tìm tab: {e}")
            self.screenshot_utils.take_screenshot_on_error(self.driver, "TC6", str(e))
        
        time.sleep(2)
        # Chụp màn hình sau
        self.screenshot_utils.take_screenshot(self.driver, "TC6", "after")
    
    def test_speed_order(self):
        """Test case 7: Kiểm tra hiển thị スピード注文"""
        print("[TC7] Kiểm tra hiển thị スピード注文")
        
        # Chụp màn hình trước
        self.screenshot_utils.take_screenshot(self.driver, "TC7", "before")
        
        try:
            from appium.webdriver.common.appiumby import AppiumBy
            news_tab = self.driver.find_element(AppiumBy.XPATH, XPathConstants.スピード注文_TAB)
            
            if not news_tab.is_displayed():
                print("[ERROR] Không tìm thấy tab スピード注文!")
            else:
                print("[INFO] Tab スピード注文 hiển thị đúng.")
                news_tab.click()
                
        except Exception as e:
            print(f"[ERROR] Lỗi khi tìm tab: {e}")
            self.screenshot_utils.take_screenshot_on_error(self.driver, "TC7", str(e))
        
        time.sleep(2)
        # Chụp màn hình sau
        self.screenshot_utils.take_screenshot(self.driver, "TC7", "after")
    
    def run_all_tests(self):
        """Chạy tất cả test cases"""
        try:
            print(f"=== Bắt đầu chạy automation NewsList cho {self.platform} ===")
            
            # Setup driver
            self.setup_driver()
            
            # Chạy các test cases
            self.test_show_news_list()
            self.test_tab_Swap()
            self.test_tab_News()
            self.test_tab_Economic()
            self.test_tab_Market()
            self.test_tab_Chart()
            self.test_speed_order()
            
            print("=== Hoàn thành tất cả test cases ===")
            
        except Exception as e:
            print(f"[ERROR] Lỗi trong quá trình chạy test: {e}")
            if self.driver:
                self.screenshot_utils.take_screenshot_on_error(self.driver, "FATAL_ERROR", str(e))
        finally:
            if self.driver:
                self.driver.quit()
                print("[INFO] Đã đóng driver")

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Cách dùng: python NewsList_auto_refactored.py [android|ios]")
        sys.exit(1)
    
    platform = sys.argv[1].lower()
    if platform not in ["android", "ios"]:
        print("Platform phải là 'android' hoặc 'ios'")
        sys.exit(1)
    
    # Tạo instance và chạy test
    automation = NewsListAutomation(platform)
    automation.run_all_tests()

if __name__ == "__main__":
    main() 