# Common Utilities Package

Package chứa các module tiện ích chung cho automation testing với Appium.

## Cấu trúc thư mục

```
common/
├── __init__.py
├── screenshot_utils.py
├── appium_config.py
└── README.md
```

## Modules

### 1. ScreenshotUtils (`screenshot_utils.py`)

Class tiện ích cho việc chụp màn hình trong automation testing.

#### Cách sử dụng:

```python
from common.screenshot_utils import ScreenshotUtils, take_screenshot

# Sử dụng class
screenshot_utils = ScreenshotUtils("output/screenshots")
screenshot_utils.take_screenshot(driver, "TC1", "before")

# Hoặc sử dụng hàm global
take_screenshot(driver, "TC1", "before")
```

#### Các phương thức chính:

- `take_screenshot(driver, test_case, step="", description="")`: Chụp màn hình cơ bản
- `take_screenshot_with_wait(driver, test_case, step="", wait_time=2)`: Chụp màn hình với thời gian chờ
- `take_screenshot_on_error(driver, test_case, error_msg="")`: Chụp màn hình khi có lỗi
- `take_screenshot_before_after(driver, test_case, action_func, step_name="")`: Chụp trước và sau khi thực hiện action
- `get_screenshot_count()`: Đếm số lượng screenshots
- `clear_old_screenshots(days_old=7)`: Xóa screenshots cũ

### 2. AppiumConfig (`appium_config.py`)

Class cấu hình và setup Appium driver cho Android và iOS.

#### Cách sử dụng:

```python
from common.appium_config import AppiumConfig, setup_driver

# Sử dụng class
appium_config = AppiumConfig("http://localhost:4723")
driver = appium_config.setup_driver("android")

# Hoặc sử dụng hàm global
driver = setup_driver("android")
```

#### Các phương thức chính:

- `setup_android_driver(custom_config=None)`: Setup driver cho Android
- `setup_ios_driver(custom_config=None)`: Setup driver cho iOS
- `setup_driver(platform, custom_config=None)`: Setup driver theo platform
- `get_device_info(driver)`: Lấy thông tin device
- `kill_app(driver, platform, app_package=None, bundle_id=None)`: Tắt app cụ thể
- `kill_all_apps(driver, platform)`: Tắt tất cả apps
- `is_app_running(driver, platform, app_package=None, bundle_id=None)`: Kiểm tra app có đang chạy không
- `restart_app(driver, platform)`: Khởi động lại app

## Ví dụ sử dụng

### Ví dụ 1: Sử dụng cả hai modules

```python
from common.screenshot_utils import ScreenshotUtils
from common.appium_config import AppiumConfig

class MyAutomation:
    def __init__(self):
        self.screenshot_utils = ScreenshotUtils("output/screenshots/my_test")
        self.appium_config = AppiumConfig()
    
    def run_test(self):
        # Setup driver
        driver = self.appium_config.setup_driver("android")
        
        try:
            # Chụp màn hình trước
            self.screenshot_utils.take_screenshot(driver, "MyTest", "before")
            
            # Thực hiện test
            # ... test logic ...
            
            # Chụp màn hình sau
            self.screenshot_utils.take_screenshot(driver, "MyTest", "after")
            
        except Exception as e:
            # Chụp màn hình lỗi
            self.screenshot_utils.take_screenshot_on_error(driver, "MyTest", str(e))
            raise
        finally:
            driver.quit()
```

### Ví dụ 2: Sử dụng hàm global

```python
from common import take_screenshot, setup_driver, kill_app, is_app_running

def simple_test():
    driver = setup_driver("android")
    
    try:
        take_screenshot(driver, "SimpleTest", "start")
        
        # Kiểm tra app status
        if is_app_running(driver, "android"):
            print("App đang chạy")
        
        # Tắt app
        kill_app(driver, "android")
        
        # ... test logic ...
        take_screenshot(driver, "SimpleTest", "end")
    finally:
        driver.quit()
```

### Ví dụ 3: Quản lý app lifecycle

```python
from common import setup_driver, kill_app, restart_app, is_app_running

def app_lifecycle_test():
    driver = setup_driver("android")
    
    try:
        # 1. Kiểm tra app có đang chạy không
        if is_app_running(driver, "android"):
            print("App đang chạy")
        
        # 2. Tắt app
        kill_app(driver, "android")
        
        # 3. Kiểm tra lại
        if not is_app_running(driver, "android"):
            print("App đã được tắt")
        
        # 4. Khởi động lại app
        restart_app(driver, "android")
        
        # 5. Kiểm tra lại
        if is_app_running(driver, "android"):
            print("App đã được khởi động lại")
            
    finally:
        driver.quit()
```

## Cấu hình tùy chỉnh

### Cấu hình Android tùy chỉnh:

```python
custom_android_config = {
    "device_name": "1B141FDF600124",
    "app_package": "jp.co.mobileit.SBI_FX",
    "app_activity": ".MainActivity",
    "no_reset": True
}

driver = appium_config.setup_android_driver(custom_android_config)
```

### Cấu hình iOS tùy chỉnh:

```python
custom_ios_config = {
    "platform_version": "17.0",
    "device_name": "iPhone 15",
    "udid": "your_device_udid",
    "bundle_id": "jp.co.sbisec.fx.stub"
}

driver = appium_config.setup_ios_driver(custom_ios_config)
```

## Lợi ích của việc sử dụng Common Modules

1. **Tái sử dụng code**: Các hàm chung có thể được sử dụng trong nhiều test scripts
2. **Dễ bảo trì**: Chỉ cần sửa một chỗ khi có thay đổi logic
3. **Tính nhất quán**: Đảm bảo tất cả test scripts sử dụng cùng cách chụp màn hình và cấu hình
4. **Dễ mở rộng**: Có thể thêm tính năng mới vào các module common
5. **Giảm lỗi**: Giảm thiểu lỗi do copy-paste code

## Lưu ý

- Đảm bảo Appium server đang chạy trước khi sử dụng
- Kiểm tra đường dẫn thư mục output có quyền ghi
- Cấu hình device UDID cho iOS phải chính xác
- Xử lý exception phù hợp trong test scripts 