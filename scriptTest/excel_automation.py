from appium import webdriver
import pandas as pd
import time
import os
from datetime import datetime
import sys
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

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

# Cấu hình Appium cho Android
def setup_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android Device"
    options.appPackage = "inc.guide.sbi.fx.dev"
    options.appActivity = ".MainActivity"
    options.no_reset = True
    
    print("[INFO] Đang kết nối Appium...")
    driver = webdriver.Remote("http://localhost:4723", options=options)
    print("[INFO] Đã kết nối thành công!")
    return driver

# Hàm thực hiện lệnh dựa trên Excel
def execute_command(driver, object_xpath, command, input_value=""):
    try:
        print(f"[INFO] Thực hiện: {command} trên {object_xpath}")
        
        if command.lower() == "click":
            element = driver.find_element(AppiumBy.XPATH, object_xpath)
            if element.is_displayed():
                element.click()
                print(f"[SUCCESS] Đã click thành công: {object_xpath}")
                return True
            else:
                print(f"[ERROR] Element không hiển thị: {object_xpath}")
                return False
                
        elif command.lower() == "input":
            element = driver.find_element(AppiumBy.XPATH, object_xpath)
            if element.is_displayed():
                element.clear()
                element.send_keys(input_value)
                print(f"[SUCCESS] Đã nhập text: {input_value}")
                return True
            else:
                print(f"[ERROR] Element không hiển thị: {object_xpath}")
                return False
                
        elif command.lower() == "wait":
            time.sleep(int(input_value) if input_value.isdigit() else 2)
            print(f"[SUCCESS] Đã đợi: {input_value} giây")
            return True
            
        elif command.lower() == "screenshot":
            take_screenshot(driver, f"excel_{input_value}")
            print(f"[SUCCESS] Đã chụp ảnh: {input_value}")
            return True
            
        else:
            print(f"[ERROR] Lệnh không được hỗ trợ: {command}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Lỗi khi thực hiện {command}: {e}")
        return False

# Hàm đọc Excel và thực hiện automation
def run_excel_automation(excel_file):
    try:
        # Đọc file Excel
        print(f"[INFO] Đang đọc file Excel: {excel_file}")
        df = pd.read_excel(excel_file)
        
        # Kiểm tra cấu trúc
        required_columns = ['Đối tượng', 'Lệnh chạy', 'Input']
        if not all(col in df.columns for col in required_columns):
            print("[ERROR] File Excel không đúng cấu trúc. Cần có: Đối tượng, Lệnh chạy, Input")
            return
        
        # Khởi tạo driver
        driver = setup_driver()
        
        # Chụp ảnh màn hình ban đầu
        take_screenshot(driver, "excel_start")
        
        # Thực hiện từng test case
        success_count = 0
        total_count = len(df)
        
        for index, row in df.iterrows():
            object_xpath = str(row['Đối tượng']).strip()
            command = str(row['Lệnh chạy']).strip()
            input_value = str(row['Input']).strip() if pd.notna(row['Input']) else ""
            
            print(f"\n[TEST CASE {index + 1}] {object_xpath} - {command}")
            
            # Chụp ảnh trước khi thực hiện
            take_screenshot(driver, f"excel_before_{index + 1}")
            
            # Thực hiện lệnh
            if execute_command(driver, object_xpath, command, input_value):
                success_count += 1
            
            # Chụp ảnh sau khi thực hiện
            take_screenshot(driver, f"excel_after_{index + 1}")
            
            # Đợi một chút giữa các test case
            time.sleep(1)
        
        # Chụp ảnh cuối
        take_screenshot(driver, "excel_end")
        
        # Báo cáo kết quả
        print(f"\n=== KẾT QUẢ AUTOMATION ===")
        print(f"Tổng số test case: {total_count}")
        print(f"Thành công: {success_count}")
        print(f"Thất bại: {total_count - success_count}")
        print(f"Tỷ lệ thành công: {(success_count/total_count)*100:.1f}%")
        
        driver.quit()
        
    except Exception as e:
        print(f"[ERROR] Lỗi khi chạy automation: {e}")
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    print("=== Bắt đầu chạy Excel Automation ===")
    
    # Kiểm tra tham số
    if len(sys.argv) < 2:
        print("Cách dùng: python excel_automation.py <file_excel>")
        print("Ví dụ: python excel_automation.py test_cases.xlsx")
        sys.exit(1)
    
    excel_file = sys.argv[1]
    
    # Kiểm tra file tồn tại
    if not os.path.exists(excel_file):
        print(f"[ERROR] File Excel không tồn tại: {excel_file}")
        sys.exit(1)
    
    # Chạy automation
    run_excel_automation(excel_file) 