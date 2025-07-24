from appium.webdriver.common.appiumby import AppiumBy
from framework.core.driver_manager import DriverManager

class BasePage:
    """Base class cho tất cả page objects"""
    
    def __init__(self):
        self.driver = DriverManager.get_driver()
    
    def find_element(self, locator, timeout=None):
        """Tìm element"""
        return DriverManager.find_element(locator, timeout)
    
    def find_elements(self, locator, timeout=None):
        """Tìm nhiều elements"""
        return DriverManager.find_elements(locator, timeout)
    
    def click_element(self, locator, timeout=None):
        """Click element"""
        return DriverManager.click_element(locator, timeout)
    
    def input_text(self, locator, text, timeout=None):
        """Nhập text"""
        return DriverManager.input_text(locator, text, timeout)
    
    def get_text(self, locator, timeout=None):
        """Lấy text"""
        return DriverManager.get_text(locator, timeout)
    
    def is_element_displayed(self, locator, timeout=None):
        """Kiểm tra element hiển thị"""
        return DriverManager.is_element_displayed(locator, timeout)
    
    def wait_for_element(self, locator, timeout=None):
        """Đợi element xuất hiện"""
        return DriverManager.wait_for_element(locator, timeout)
    
    def take_screenshot(self, filename):
        """Chụp màn hình"""
        return DriverManager.take_screenshot(filename)
    
    def scroll_to_element(self, locator):
        """Scroll đến element"""
        try:
            element = self.find_element(locator)
            if element:
                self.driver.execute_script("mobile: scrollGesture", {
                    "left": 100, "top": 100, "width": 600, "height": 600,
                    "direction": "down", "percent": 0.75
                })
                print(f"[SUCCESS] Đã scroll đến: {locator}")
                return True
        except Exception as e:
            print(f"[ERROR] Lỗi khi scroll: {e}")
            return False
    
    def swipe(self, start_x, start_y, end_x, end_y, duration=1000):
        """Swipe gesture"""
        try:
            self.driver.execute_script("mobile: swipeGesture", {
                "left": start_x, "top": start_y, "width": end_x - start_x, "height": end_y - start_y,
                "direction": "up", "percent": 0.75
            })
            print(f"[SUCCESS] Đã swipe từ ({start_x},{start_y}) đến ({end_x},{end_y})")
            return True
        except Exception as e:
            print(f"[ERROR] Lỗi khi swipe: {e}")
            return False
    
    def tap(self, x, y):
        """Tap gesture"""
        try:
            self.driver.execute_script("mobile: tapGesture", {
                "x": x, "y": y
            })
            print(f"[SUCCESS] Đã tap tại ({x},{y})")
            return True
        except Exception as e:
            print(f"[ERROR] Lỗi khi tap: {e}")
            return False 