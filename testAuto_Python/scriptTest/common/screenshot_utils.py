#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Screenshot Utilities
Các hàm tiện ích cho việc chụp màn hình trong automation testing
"""

import os
import time
from datetime import datetime
from appium import webdriver

class ScreenshotUtils:
    """Utility class cho việc chụp màn hình"""
    
    def __init__(self, output_dir="output/screenshots"):
        """
        Khởi tạo ScreenshotUtils
        
        Args:
            output_dir (str): Thư mục lưu screenshots
        """
        self.output_dir = output_dir
        self._create_output_dir()
    
    def _create_output_dir(self):
        """Tạo thư mục output nếu chưa có"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            print(f"[INFO] Đã tạo thư mục: {self.output_dir}")
    
    def take_screenshot(self, driver, test_case, step="", description=""):
        """
        Chụp màn hình và lưu file
        
        Args:
            driver: Appium WebDriver instance
            test_case (str): Tên test case
            step (str): Bước thực hiện (before, after, step1, etc.)
            description (str): Mô tả thêm cho screenshot
            
        Returns:
            str: Đường dẫn file screenshot đã lưu
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Tạo tên file
            if step:
                filename = f"{test_case}_{step}_{timestamp}.png"
            else:
                filename = f"{test_case}_{timestamp}.png"
            
            # Thêm description nếu có
            if description:
                filename = f"{test_case}_{step}_{description}_{timestamp}.png"
            
            filepath = os.path.join(self.output_dir, filename)
            
            # Chụp màn hình
            driver.save_screenshot(filepath)
            
            print(f"[SCREENSHOT] Đã chụp màn hình: {filepath}")
            return filepath
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi chụp màn hình: {e}")
            return None
    
    def take_screenshot_with_wait(self, driver, test_case, step="", wait_time=2):
        """
        Chụp màn hình với thời gian chờ
        
        Args:
            driver: Appium WebDriver instance
            test_case (str): Tên test case
            step (str): Bước thực hiện
            wait_time (int): Thời gian chờ trước khi chụp (giây)
            
        Returns:
            str: Đường dẫn file screenshot đã lưu
        """
        time.sleep(wait_time)
        return self.take_screenshot(driver, test_case, step)
    
    def take_screenshot_on_error(self, driver, test_case, error_msg=""):
        """
        Chụp màn hình khi có lỗi
        
        Args:
            driver: Appium WebDriver instance
            test_case (str): Tên test case
            error_msg (str): Thông báo lỗi
            
        Returns:
            str: Đường dẫn file screenshot đã lưu
        """
        return self.take_screenshot(driver, test_case, "error", error_msg)
    
    def take_screenshot_before_after(self, driver, test_case, action_func, step_name=""):
        """
        Chụp màn hình trước và sau khi thực hiện action
        
        Args:
            driver: Appium WebDriver instance
            test_case (str): Tên test case
            action_func (function): Hàm action cần thực hiện
            step_name (str): Tên bước thực hiện
            
        Returns:
            tuple: (filepath_before, filepath_after)
        """
        # Chụp trước
        before_screenshot = self.take_screenshot(driver, test_case, f"{step_name}_before")
        
        # Thực hiện action
        try:
            action_func()
            # Chụp sau
            after_screenshot = self.take_screenshot(driver, test_case, f"{step_name}_after")
            return before_screenshot, after_screenshot
        except Exception as e:
            # Chụp lỗi nếu có
            error_screenshot = self.take_screenshot_on_error(driver, test_case, str(e))
            raise e
    
    def get_screenshot_count(self):
        """Đếm số lượng screenshots trong thư mục"""
        try:
            files = [f for f in os.listdir(self.output_dir) if f.endswith('.png')]
            return len(files)
        except Exception as e:
            print(f"[ERROR] Lỗi khi đếm screenshots: {e}")
            return 0
    
    def clear_old_screenshots(self, days_old=7):
        """
        Xóa screenshots cũ
        
        Args:
            days_old (int): Số ngày cũ để xóa
        """
        try:
            current_time = datetime.now()
            files = os.listdir(self.output_dir)
            
            for file in files:
                if file.endswith('.png'):
                    filepath = os.path.join(self.output_dir, file)
                    file_time = datetime.fromtimestamp(os.path.getctime(filepath))
                    
                    if (current_time - file_time).days > days_old:
                        os.remove(filepath)
                        print(f"[INFO] Đã xóa file cũ: {file}")
                        
        except Exception as e:
            print(f"[ERROR] Lỗi khi xóa screenshots cũ: {e}")

# Hàm tiện ích global
def take_screenshot(driver, test_case, step="", output_dir="output/screenshots"):
    """
    Hàm tiện ích global để chụp màn hình
    
    Args:
        driver: Appium WebDriver instance
        test_case (str): Tên test case
        step (str): Bước thực hiện
        output_dir (str): Thư mục output
        
    Returns:
        str: Đường dẫn file screenshot
    """
    screenshot_utils = ScreenshotUtils(output_dir)
    return screenshot_utils.take_screenshot(driver, test_case, step) 