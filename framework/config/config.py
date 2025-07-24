import os
from datetime import datetime

class Config:
    # Appium Configuration
    APPIUM_SERVER = "http://localhost:4723"
    PLATFORM = "android"
    
    # Android Configuration
    ANDROID_PACKAGE = "inc.guide.sbi.fx.dev"
    ANDROID_ACTIVITY = ".MainActivity"
    ANDROID_DEVICE_NAME = "Android Device"
    
    # iOS Configuration (nếu cần)
    IOS_BUNDLE_ID = "jp.co.sbisec.fx.stub"
    IOS_DEVICE_NAME = "iPhone 14"
    IOS_PLATFORM_VERSION = "16.0"
    
    # Test Configuration
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    SCREENSHOT_DIR = "output/screenshots"
    REPORT_DIR = "output/reports"
    LOG_DIR = "output/logs"
    
    # Test Data
    TEST_DATA_DIR = "testdata"
    
    @classmethod
    def create_directories(cls):
        """Tạo các thư mục cần thiết"""
        directories = [
            cls.SCREENSHOT_DIR,
            cls.REPORT_DIR,
            cls.LOG_DIR,
            cls.TEST_DATA_DIR
        ]
        
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Created directory: {directory}")
    
    @classmethod
    def get_timestamp(cls):
        """Lấy timestamp hiện tại"""
        return datetime.now().strftime("%Y%m%d_%H%M%S") 