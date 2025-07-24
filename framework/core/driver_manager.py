from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import logging

from framework.config.config import Config

class DriverManager:
    _driver = None
    
    @classmethod
    def get_driver(cls):
        """Lấy driver instance"""
        if cls._driver is None:
            cls._driver = cls._create_driver()
        return cls._driver
    
    @classmethod
    def _create_driver(cls):
        """Tạo Appium driver"""
        try:
            if Config.PLATFORM.lower() == "android":
                options = UiAutomator2Options()
                options.platform_name = "Android"
                options.device_name = Config.ANDROID_DEVICE_NAME
                options.app_package = Config.ANDROID_PACKAGE
                options.app_activity = Config.ANDROID_ACTIVITY
                options.no_reset = True
                
            elif Config.PLATFORM.lower() == "ios":
                options = XCUITestOptions()
                options.platform_name = "iOS"
                options.platform_version = Config.IOS_PLATFORM_VERSION
                options.device_name = Config.IOS_DEVICE_NAME
                options.bundle_id = Config.IOS_BUNDLE_ID
                options.no_reset = True
            else:
                raise ValueError(f"Platform không được hỗ trợ: {Config.PLATFORM}")
            
            print(f"[INFO] Đang kết nối Appium server: {Config.APPIUM_SERVER}")
            driver = webdriver.Remote(Config.APPIUM_SERVER, options=options)
            
            # Thiết lập implicit wait
            driver.implicitly_wait(Config.IMPLICIT_WAIT)
            
            print(f"[SUCCESS] Đã kết nối thành công với {Config.PLATFORM}")
            return driver
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi tạo driver: {e}")
            raise
    
    @classmethod
    def quit_driver(cls):
        """Đóng driver"""
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
            print("[INFO] Đã đóng driver")
    
    @classmethod
    def find_element(cls, locator, timeout=Config.EXPLICIT_WAIT):
        """Tìm element với explicit wait"""
        try:
            wait = WebDriverWait(cls._driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            print(f"[ERROR] Không tìm thấy element: {locator}")
            return None
    
    @classmethod
    def find_elements(cls, locator, timeout=Config.EXPLICIT_WAIT):
        """Tìm nhiều elements với explicit wait"""
        try:
            wait = WebDriverWait(cls._driver, timeout)
            elements = wait.until(EC.presence_of_all_elements_located(locator))
            return elements
        except TimeoutException:
            print(f"[ERROR] Không tìm thấy elements: {locator}")
            return []
    
    @classmethod
    def click_element(cls, locator, timeout=Config.EXPLICIT_WAIT):
        """Click element"""
        element = cls.find_element(locator, timeout)
        if element and element.is_displayed():
            element.click()
            print(f"[SUCCESS] Đã click: {locator}")
            return True
        else:
            print(f"[ERROR] Không thể click: {locator}")
            return False
    
    @classmethod
    def input_text(cls, locator, text, timeout=Config.EXPLICIT_WAIT):
        """Nhập text vào element"""
        element = cls.find_element(locator, timeout)
        if element and element.is_displayed():
            element.clear()
            element.send_keys(text)
            print(f"[SUCCESS] Đã nhập text: {text}")
            return True
        else:
            print(f"[ERROR] Không thể nhập text: {locator}")
            return False
    
    @classmethod
    def get_text(cls, locator, timeout=Config.EXPLICIT_WAIT):
        """Lấy text từ element"""
        element = cls.find_element(locator, timeout)
        if element:
            text = element.text
            print(f"[INFO] Text: {text}")
            return text
        return None
    
    @classmethod
    def is_element_displayed(cls, locator, timeout=Config.EXPLICIT_WAIT):
        """Kiểm tra element có hiển thị không"""
        element = cls.find_element(locator, timeout)
        return element is not None and element.is_displayed()
    
    @classmethod
    def wait_for_element(cls, locator, timeout=Config.EXPLICIT_WAIT):
        """Đợi element xuất hiện"""
        try:
            wait = WebDriverWait(cls._driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            print(f"[SUCCESS] Element đã xuất hiện: {locator}")
            return True
        except TimeoutException:
            print(f"[ERROR] Element không xuất hiện: {locator}")
            return False
    
    @classmethod
    def take_screenshot(cls, filename):
        """Chụp màn hình"""
        try:
            timestamp = Config.get_timestamp()
            full_filename = f"{filename}_{timestamp}.png"
            filepath = f"{Config.SCREENSHOT_DIR}/{full_filename}"
            cls._driver.save_screenshot(filepath)
            print(f"[SCREENSHOT] Đã chụp: {filepath}")
            return filepath
        except Exception as e:
            print(f"[ERROR] Lỗi khi chụp màn hình: {e}")
            return None 