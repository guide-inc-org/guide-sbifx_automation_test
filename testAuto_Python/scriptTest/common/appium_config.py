#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Appium Configuration
Cấu hình và setup Appium driver cho automation testing
"""

import time
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

class AppiumConfig:
    """Class cấu hình Appium cho Android và iOS"""
    
    def __init__(self, server_url="http://localhost:4723"):
        """
        Khởi tạo AppiumConfig
        
        Args:
            server_url (str): URL của Appium server
        """
        self.server_url = server_url
        
        # Cấu hình mặc định cho Android
        self.android_config = {
            "platform_name": "Android",
            "device_name": "Android Device",
            "app_package": "inc.guide.sbi.fx.dev",
            "app_activity": "jp.co.mobileit.SBI_FX.MainActivity",
            "no_reset": True,
            "automation_name": "UiAutomator2",
            "new_command_timeout": 3600,
            "auto_grant_permissions": True
        }
        
        # Cấu hình mặc định cho iOS
        self.ios_config = {
            "platform_name": "iOS",
            "platform_version": "16.0",
            "device_name": "iPhone 14",
            "udid": "your_device_udid",  # Cần thay đổi theo device thực tế
            "bundle_id": "jp.co.sbisec.fx.stub",
            "no_reset": True,
            "automation_name": "XCUITest"
        }
    
    def setup_android_driver(self, custom_config=None):
        """
        Setup Appium driver cho Android
        
        Args:
            custom_config (dict): Cấu hình tùy chỉnh cho Android
            
        Returns:
            webdriver.Remote: Appium driver instance
        """
        print("[INFO] Đang setup Appium driver cho Android...")
        
        # Merge cấu hình mặc định với cấu hình tùy chỉnh
        config = self.android_config.copy()
        if custom_config:
            config.update(custom_config)
        
        # Tạo UiAutomator2Options
        options = UiAutomator2Options()
        options.platform_name = config["platform_name"]
        options.set_capability("appium:deviceName", config["device_name"])
        options.set_capability("appium:appPackage", config["app_package"])
        options.set_capability("appium:appActivity", config["app_activity"])
        options.set_capability("appium:noReset", config["no_reset"])
        options.set_capability("appium:automationName", config["automation_name"])
        options.set_capability("appium:newCommandTimeout", config["new_command_timeout"])
        options.set_capability("appium:autoGrantPermissions", config["auto_grant_permissions"])
        
        # Tạo driver
        driver = webdriver.Remote(self.server_url, options=options)
        
        # Kiểm tra trạng thái app
        self._check_app_status(driver, "android", config)
        
        return driver
    
    def setup_ios_driver(self, custom_config=None):
        """
        Setup Appium driver cho iOS
        
        Args:
            custom_config (dict): Cấu hình tùy chỉnh cho iOS
            
        Returns:
            webdriver.Remote: Appium driver instance
        """
        print("[INFO] Đang setup Appium driver cho iOS...")
        
        # Merge cấu hình mặc định với cấu hình tùy chỉnh
        config = self.ios_config.copy()
        if custom_config:
            config.update(custom_config)
        
        # Tạo XCUITestOptions
        options = XCUITestOptions()
        options.platform_name = config["platform_name"]
        options.set_capability("appium:platformVersion", config["platform_version"])
        options.set_capability("appium:deviceName", config["device_name"])
        options.set_capability("appium:udid", config["udid"])
        options.set_capability("appium:bundleId", config["bundle_id"])
        options.set_capability("appium:noReset", config["no_reset"])
        options.set_capability("appium:automationName", config["automation_name"])
        
        # Tạo driver
        driver = webdriver.Remote(self.server_url, options=options)
        
        # Kiểm tra trạng thái app
        self._check_app_status(driver, "ios", config)
        
        return driver
    
    def setup_driver(self, platform, custom_config=None):
        """
        Setup Appium driver theo platform
        
        Args:
            platform (str): 'android' hoặc 'ios'
            custom_config (dict): Cấu hình tùy chỉnh
            
        Returns:
            webdriver.Remote: Appium driver instance
        """
        platform = platform.lower()
        
        if platform == "android":
            return self.setup_android_driver(custom_config)
        elif platform == "ios":
            return self.setup_ios_driver(custom_config)
        else:
            raise ValueError("Platform phải là 'android' hoặc 'ios'")
    
    def _check_app_status(self, driver, platform, config):
        """
        Kiểm tra trạng thái app trên device
        
        Args:
            driver: Appium driver instance
            platform (str): 'android' hoặc 'ios'
            config (dict): Cấu hình app
        """
        print(f"[INFO] Đang kiểm tra trạng thái app trên thiết bị {platform}...")
        
        app_started = False
        try:
            if platform == "android":
                current_package = driver.current_package
                if current_package == config["app_package"]:
                    print(f"[INFO] App Android đã chạy: {current_package}")
                    app_started = True
                else:
                    print(f"[INFO] App Android chưa chạy, sẽ khởi động app: {config['app_package']}")
                    driver.activate_app(config["app_package"])
                    
            elif platform == "ios":
                running_apps = driver.execute_script('mobile: activeApps', {})
                bundle_id = config["bundle_id"]
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
    
    def get_device_info(self, driver):
        """
        Lấy thông tin device
        
        Args:
            driver: Appium driver instance
            
        Returns:
            dict: Thông tin device
        """
        try:
            device_info = {
                "platform": driver.capabilities.get("platformName"),
                "version": driver.capabilities.get("platformVersion"),
                "device_name": driver.capabilities.get("deviceName"),
                "automation_name": driver.capabilities.get("automationName")
            }
            
            if device_info["platform"] == "Android":
                device_info["app_package"] = driver.current_package
                device_info["app_activity"] = driver.current_activity
            elif device_info["platform"] == "iOS":
                device_info["bundle_id"] = driver.capabilities.get("bundleId")
            
            return device_info
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi lấy thông tin device: {e}")
            return {}
    
    def kill_app(self, driver, platform, app_package=None, bundle_id=None):
        """
        Tắt app
        
        Args:
            driver: Appium driver instance
            platform (str): 'android' hoặc 'ios'
            app_package (str): Package name cho Android (optional)
            bundle_id (str): Bundle ID cho iOS (optional)
        """
        try:
            if platform == "android":
                package = app_package or self.android_config["app_package"]
                driver.terminate_app(package)
                print(f"[INFO] Đã tắt app Android: {package}")
            elif platform == "ios":
                bundle = bundle_id or self.ios_config["bundle_id"]
                driver.terminate_app(bundle)
                print(f"[INFO] Đã tắt app iOS: {bundle}")
            else:
                print(f"[ERROR] Platform không được hỗ trợ: {platform}")
                return False
            
            time.sleep(1)
            return True
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi tắt app: {e}")
            return False
    
    def kill_all_apps(self, driver, platform):
        """
        Tắt tất cả apps đang chạy
        
        Args:
            driver: Appium driver instance
            platform (str): 'android' hoặc 'ios'
        """
        try:
            if platform == "android":
                # Tắt tất cả apps background
                driver.execute_script('mobile: shell', {
                    'command': 'am force-stop $(pm list packages -3 | cut -d: -f2)'
                })
                print("[INFO] Đã tắt tất cả apps Android")
            elif platform == "ios":
                # Tắt tất cả apps background
                driver.execute_script('mobile: terminateApp', {
                    'bundleId': '*'
                })
                print("[INFO] Đã tắt tất cả apps iOS")
            else:
                print(f"[ERROR] Platform không được hỗ trợ: {platform}")
                return False
            
            time.sleep(2)
            return True
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi tắt tất cả apps: {e}")
            return False
    
    def is_app_running(self, driver, platform, app_package=None, bundle_id=None):
        """
        Kiểm tra app có đang chạy không
        
        Args:
            driver: Appium driver instance
            platform (str): 'android' hoặc 'ios'
            app_package (str): Package name cho Android (optional)
            bundle_id (str): Bundle ID cho iOS (optional)
            
        Returns:
            bool: True nếu app đang chạy, False nếu không
        """
        try:
            if platform == "android":
                package = app_package or self.android_config["app_package"]
                current_package = driver.current_package
                return current_package == package
            elif platform == "ios":
                bundle = bundle_id or self.ios_config["bundle_id"]
                running_apps = driver.execute_script('mobile: activeApps', {})
                return any(app.get('bundleId') == bundle for app in running_apps)
            else:
                print(f"[ERROR] Platform không được hỗ trợ: {platform}")
                return False
                
        except Exception as e:
            print(f"[ERROR] Lỗi khi kiểm tra app status: {e}")
            return False
    
    def restart_app(self, driver, platform):
        """
        Khởi động lại app
        
        Args:
            driver: Appium driver instance
            platform (str): 'android' hoặc 'ios'
        """
        try:
            if platform == "android":
                driver.terminate_app(self.android_config["app_package"])
                time.sleep(2)
                driver.activate_app(self.android_config["app_package"])
            elif platform == "ios":
                driver.terminate_app(self.ios_config["bundle_id"])
                time.sleep(2)
                driver.activate_app(self.ios_config["bundle_id"])
            
            print(f"[INFO] Đã khởi động lại app trên {platform}")
            time.sleep(3)
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi khởi động lại app: {e}")

# Hàm tiện ích global
def setup_driver(platform, server_url="http://localhost:4723", custom_config=None):
    """
    Hàm tiện ích global để setup Appium driver
    
    Args:
        platform (str): 'android' hoặc 'ios'
        server_url (str): URL của Appium server
        custom_config (dict): Cấu hình tùy chỉnh
        
    Returns:
        webdriver.Remote: Appium driver instance
    """
    appium_config = AppiumConfig(server_url)
    return appium_config.setup_driver(platform, custom_config)

def kill_app(driver, platform, app_package=None, bundle_id=None):
    """
    Hàm tiện ích global để tắt app
    
    Args:
        driver: Appium driver instance
        platform (str): 'android' hoặc 'ios'
        app_package (str): Package name cho Android (optional)
        bundle_id (str): Bundle ID cho iOS (optional)
        
    Returns:
        bool: True nếu thành công, False nếu thất bại
    """
    appium_config = AppiumConfig()
    return appium_config.kill_app(driver, platform, app_package, bundle_id)

def kill_all_apps(driver, platform):
    """
    Hàm tiện ích global để tắt tất cả apps
    
    Args:
        driver: Appium driver instance
        platform (str): 'android' hoặc 'ios'
        
    Returns:
        bool: True nếu thành công, False nếu thất bại
    """
    appium_config = AppiumConfig()
    return appium_config.kill_all_apps(driver, platform)

def is_app_running(driver, platform, app_package=None, bundle_id=None):
    """
    Hàm tiện ích global để kiểm tra app có đang chạy không
    
    Args:
        driver: Appium driver instance
        platform (str): 'android' hoặc 'ios'
        app_package (str): Package name cho Android (optional)
        bundle_id (str): Bundle ID cho iOS (optional)
        
    Returns:
        bool: True nếu app đang chạy, False nếu không
    """
    appium_config = AppiumConfig()
    return appium_config.is_app_running(driver, platform, app_package, bundle_id)

def restart_app(driver, platform):
    """
    Hàm tiện ích global để khởi động lại app
    
    Args:
        driver: Appium driver instance
        platform (str): 'android' hoặc 'ios'
    """
    appium_config = AppiumConfig()
    appium_config.restart_app(driver, platform) 