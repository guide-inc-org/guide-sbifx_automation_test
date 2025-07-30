from appium import webdriver
import time
import os
from datetime import datetime
import sys
from object_repository  import (
    NewsListScreen, NewsDetailScreen,
    FilterScreen, CommonElements,
    LocatorHelper
)
# from xpath_objects_20250723_124846 import xpathObjects
# from testAuto.scriptTest import object_repository
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

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

# Cấu hình Appium cho iOS (bạn cần chỉnh lại cho đúng app thực tế)

# Tạo thư mục output nếu chưa có
screenshots_dir = "output"
if not os.path.exists(screenshots_dir):
    os.makedirs(screenshots_dir)

# Hàm chụp màn hình
def take_screenshot(driver, test_case, step=""):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_case}_{step}_{timestamp}.png" if step else f"{test_case}_{timestamp}.png"
    filepath = os.path.join(screenshots_dir, filename)
    driver.save_screenshot(filepath)
    print(f"[SCREENSHOT] Đã chụp màn hình: {filepath}")
    return filepath

# Cấu hình Appium cho Android/iOS
def setup_driver(platform):
    if platform == "android":
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "Android Device"
        options.appPackage = "jp.co.mobileit.SBI_FX"
        options.appActivity = ".MainActivity"
        options.no_reset = True
        
    elif platform == "ios":
        options = XCUITestOptions()
        options.platform_name = "iOS"
        options.platform_version = "16.0"
        options.device_name = "iPhone 14"
        options.udid = "your_device_udid"
        options.bundle_id = "jp.co.sbisec.fx.stub"
        options.no_reset = True
    else:
        raise ValueError("Platform phải là 'android' hoặc 'ios'")
    print(f"[INFO] Đang kiểm tra trạng thái app trên thiết bị {platform}...")
    driver = webdriver.Remote("http://localhost:4723", options=options)
    app_started = False
    try:
        if platform == "android":
            current_package = driver.current_package
            if current_package == options.app_package:
                print(f"[INFO] App Android đã chạy: {current_package}")
                app_started = True
            else:
                print(f"[INFO] App Android chưa chạy, sẽ khởi động app: {options.app_package}")
                driver.activate_app(options.app_package)
        elif platform == "ios":
            running_apps = driver.execute_script('mobile: activeApps', {})
            bundle_id = options.bundle_id
            if any(app.get('bundleId') == bundle_id for app in running_apps):
                print(f"[INFO] App iOS đã chạy: {bundle_id}")
                app_started = True
            else:
                print(f"[INFO] App iOS chưa chạy, sẽ khởi động app: {bundle_id}")
                driver.activate_app(bundle_id)
    except Exception as e:
        print(f"[WARN] Không kiểm tra được trạng thái app: {e}")
    if not app_started:
        print("[INFO] Đã gửi lệnh khởi động app, đợi app mở...")
        time.sleep(5)
    return driver

def test_show_news_list(driver):
    print("[TC1] Kiểm tra hiển thị danh sách tin tức khi vào màn hình")
    take_screenshot(driver, "TC1", "before")
    # TODO: Thêm code kiểm tra element danh sách, so sánh dữ liệu API nếu cần
    # Ví dụ: kiểm tra xem có ít nhất 1 tin tức hiển thị
    # news_list = driver.find_elements(AppiumBy.XPATH, "//android.view.View")  # Generic check   
    # if not news_list:
    #      print("[ERROR] Không tìm thấy danh sách tin tức!")
    # else:
    #      print(f"[INFO] Đã tìm thấy {len(news_list)} tin tức hiển thị.")
    print("[INFO] TC1 completed")
    time.sleep(2)
    take_screenshot(driver, "TC1", "after")

def test_tab_Swap(driver):
    print("[TC2] Kiểm tra hiển thị dữ liệu khi tab Swap")
    take_screenshot(driver, "TC2", "before")
    # TODO: Thêm code kiểm tra giao diện không có tin tức
    try:
        from appium.webdriver.common.appiumby import AppiumBy
        news_tab = driver.find_element(AppiumBy.XPATH, XPathConstants.SWAP_TAB)  
        if not news_tab.is_displayed():
            print("[ERROR] Không tìm thấy tab スワップ!")
        else:
            print("[INFO] Tab スワップ hiển thị đúng.")
            news_tab.click()
    except Exception as e:
        print(f"[ERROR] Lỗi khi tìm tab: {e}")
    time.sleep(2)
    take_screenshot(driver, "TC2", "after")


def test_tab_News(driver):
    print("[TC3] Kiểm tra chuyển tab マーケット/ニュース")
    take_screenshot(driver, "TC3", "before")
    # TODO: Tìm và click tab, kiểm tra dữ liệu hiển thị đúng   
    try:
        from appium.webdriver.common.appiumby import AppiumBy
        news_tab = driver.find_element(AppiumBy.XPATH, XPathConstants.NEWS_TAB)  
        if not news_tab.is_displayed():
            print("[ERROR] Không tìm thấy tab ニュース!")
        else:
            print("[INFO] Tab ニュース hiển thị đúng.")
            news_tab.click()
    except Exception as e:
        print(f"[ERROR] Lỗi khi tìm tab: {e}")
    
    # Giả sử sau khi click tab, sẽ chuyển sang tab tin tức
    time.sleep(2)
    take_screenshot(driver, "TC3", "after")

def test_tab_Economic(driver):
    print("[TC4] Kiểm tra chuyển tab マーケット/経済指標")
    take_screenshot(driver, "TC4", "before")
    # TODO: Tìm và click tab, kiểm tra dữ liệu hiển thị đúng   
    try:
        from appium.webdriver.common.appiumby import AppiumBy
        news_tab = driver.find_element(AppiumBy.XPATH, XPathConstants.ECONOMIC_TAB)  
        if not news_tab.is_displayed():
            print("[ERROR] Không tìm thấy tab 経済指標!")
        else:
            print("[INFO] Tab 経済指標 hiển thị đúng.")
            news_tab.click()
    except Exception as e:
        print(f"[ERROR] Lỗi khi tìm tab: {e}")
    
    # Giả sử sau khi click tab, sẽ chuyển sang tab tin tức
    time.sleep(2)
    take_screenshot(driver, "TC4", "after")

def test_tab_Market(driver):
    print("[TC5] Kiểm tra reload page ")
    take_screenshot(driver, "TC5", "before")
    # TODO: Tìm và click tab, kiểm tra dữ liệu hiển thị đúng   
    try:
        from appium.webdriver.common.appiumby import AppiumBy
        news_tab = driver.find_element(AppiumBy.XPATH, XPathConstants.MARKET_TAB)  
        if not news_tab.is_displayed():
            print("[ERROR] Không tìm thấy tab reload!")
        else:
            print("[INFO] Tab  hiển thị đúng.")
            news_tab.click()
    except Exception as e:
        print(f"[ERROR] Lỗi khi tìm tab: {e}")
    
    # Giả sử sau khi click tab, sẽ chuyển sang tab tin tức
    time.sleep(2)
    take_screenshot(driver, "TC5", "after")

def test_tab_Chart(driver):
    print("[TC6] Kiểm tra hiển thị Chart")
    take_screenshot(driver, "TC6", "before")
    # TODO: Implement chart functionality check
    try:
        from appium.webdriver.common.appiumby import AppiumBy
        news_tab = driver.find_element(AppiumBy.XPATH, XPathConstants.チャート_TAB)  
        if not news_tab.is_displayed():
            print("[ERROR] Không tìm thấy tab reload!")
        else:
            print("[INFO] Tab  hiển thị đúng.")
            news_tab.click()
    except Exception as e:
        print(f"[ERROR] Lỗi khi tìm tab: {e}")
    time.sleep(2)
    take_screenshot(driver, "TC6", "after")

def test_speed_order(driver):
    print("[TC7] Kiểm tra hiển thị スピード注文")
    take_screenshot(driver, "TC7", "before")
    # TODO: Implement speed order functionality check
    try:
        from appium.webdriver.common.appiumby import AppiumBy
        news_tab = driver.find_element(AppiumBy.XPATH, XPathConstants.スピード注文_TAB)  
        if not news_tab.is_displayed():
            print("[ERROR] Không tìm thấy tab reload!")
        else:
            print("[INFO] Tab  hiển thị đúng.")
            news_tab.click()
    except Exception as e:
        print(f"[ERROR] Lỗi khi tìm tab: {e}")
    time.sleep(2)
    take_screenshot(driver, "TC7", "after")


def run_all_tests(platform):
    driver = setup_driver(platform)
    try:
        test_show_news_list(driver)
        test_tab_Swap(driver)
        test_tab_News(driver)
        test_tab_Economic(driver)
        test_tab_Market(driver)
        test_tab_Chart(driver)
        test_speed_order(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    print("=== Bắt đầu chạy automation NewsList ===")
    if len(sys.argv) < 2:
        print("Cách dùng: python NewsList_auto.py [android|ios]")
        sys.exit(1)
    platform = sys.argv[1].lower()
    run_all_tests(platform)
