from appium import webdriver
import time
import os
from datetime import datetime
import sys
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
# Import các module common
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from common.screenshot_utils import ScreenshotUtils
from common.appium_config import AppiumConfig, kill_app, is_app_running

# Import xpath objects
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'xpath'))
from xpath.xpath_objects_Login import CurrentScreenXPaths as LoginXPaths
from xpath.xpath_objects_RateListSmall import CurrentScreenXPaths as RateListXPaths
from xpath.xpath_objects_NoticePrivaList import CurrentScreenXPaths as NoticePrivaListXPaths  # File này có vấn đề
from appium.webdriver.common.appiumby import AppiumBy   



class LoginAutomation:
    """Screen login"""
    
    def __init__(self, platform="android", server_url="http://localhost:4723"):
        """
        Khởi tạo LoginAutomation
        
        Args:
            platform (str): 'android' hoặc 'ios'
            server_url (str): URL của Appium server
        """
        self.platform = platform
        self.server_url = server_url
        self.driver = None
        
        # Khởi tạo các utilities
        self.screenshot_utils = ScreenshotUtils("output/screenshots/login")
        self.appium_config = AppiumConfig(server_url)
    
    def setup_driver(self, custom_config=None):
        """
        Setup Appium driver
        
        Args:
            custom_config (dict): Cấu hình tùy chỉnh
        """
        self.driver = self.appium_config.setup_driver(self.platform, custom_config)
        print(f"[INFO] Đã setup driver thành công cho {self.platform}")
    
    def test_show_startup(self):
        """Test case 1: Kiểm tra hiển thị màn hình Startup"""
        print("[#1] Kiểm tra hiển thị Startup")
        
        # Chụp màn hình trước
        self.screenshot_utils.take_screenshot(self.driver, "#01_startup", "before")
        self.appium_config.restart_app(self.driver, self.platform)
        time.sleep(2)
        # Chụp màn hình sau
        self.screenshot_utils.take_screenshot(self.driver, "#02_startup", "after")
    
    def test_show_Login(self):
        """Test case 2: Kiểm tra hiển thị màn hình Login"""
        print("[#2] Kiểm tra hiển thị Login")
        
        # Tắt app trước
        kill_app(self.driver, self.platform)
        time.sleep(2)
        
        # Chụp màn hình trước
        self.screenshot_utils.take_screenshot(self.driver, "#03_before_restart", "before")
        
        # Khởi động lại app
        self.appium_config.restart_app(self.driver, self.platform)
        time.sleep(2)
        
        # Chụp màn hình sau
        self.screenshot_utils.take_screenshot(self.driver, "#04_after_restart", "after")
        
        # Tìm tab Login trên màn hình Market
        try:
            # Thử tìm tab Login bằng content-desc
            login_tab = self.driver.find_element(AppiumBy.XPATH, "//*[@content-desc='ログイン' or @content-desc='Login']")
            if login_tab.is_displayed():
                print("[INFO] Tìm thấy tab Login, đang click...")
                login_tab.click()
                time.sleep(2)
            else:
                print("[WARNING] Tab Login không hiển thị")
        except Exception as e:
            print(f"[ERROR] Không tìm thấy tab Login: {e}")
            # Thử tìm bằng cách khác
            try:
                login_tab = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text, 'ログイン') or contains(@text, 'Login')]")
                if login_tab.is_displayed():
                    print("[INFO] Tìm thấy tab Login bằng text, đang click...")
                    login_tab.click()
                    time.sleep(2)
                else:
                    print("[WARNING] Tab Login không hiển thị")
            except Exception as e2:
                print(f"[ERROR] Không tìm thấy tab Login bằng text: {e2}")
                self.screenshot_utils.take_screenshot_on_error(self.driver, "#05_login_tab_error", str(e2))
        time.sleep(2)
        # Chụp màn hình sau
        self.screenshot_utils.take_screenshot(self.driver, "#05_after_login_tab", "after")
        #Tạm thời comment out vì không có COPYRIGHT_BY_DESC trong RateListXPaths
        copyright = self.driver.find_element(AppiumBy.XPATH, LoginXPaths.COPYRIGHT_TEXT)  
        if not copyright.is_displayed():
            print("[ERROR] Không tìm thấy màn hình Login!")
        else:
            print("[INFO] Hiển thị đúng màn hình login .")
        time.sleep(2)
        # Chụp màn hình sau
        self.screenshot_utils.take_screenshot(self.driver, "#06_login_displayed", "after")
        # Sử dụng NoticePrivateList thay vì NoticePrivateList_Lable
        #print("[INFO] Sử dụng NoticePrivateList để tìm link 緊急なお知らせ")
        NoticePrivateList_Lable = self.driver.find_element(AppiumBy.XPATH, LoginXPaths.NoticePrivateList_Lable)
        if not NoticePrivateList_Lable.is_displayed():
            print("[INFO] Không tìm thấy link 緊急なお知らせ!")
        else:
            print("[INFO] Link 緊急なお知らせ có trên màn hình login.")
            NoticePrivateList_Lable.click()
        time.sleep(2)
        # Chụp màn hình sau
        self.screenshot_utils.take_screenshot(self.driver, "#07_notice_screen", "after")
        # Sử dụng NoticePrivaListXPaths đã được sửa
        try:
            # Sử dụng XPath từ NoticePrivaListXPaths
            Back_button = self.driver.find_element(AppiumBy.XPATH, NoticePrivaListXPaths.BACK_BUTTON)
            if not Back_button.is_displayed():
                print("[ERROR] Không tìm thấy nút Back trên màn hình Notice!")
            else:
                print("[INFO] Nút back tồn tại trên màn hình 緊急なお知らせ.")
                Back_button.click()
        except Exception as e:
            print(f"[ERROR] Lỗi khi tìm nút Back: {e}")
            self.screenshot_utils.take_screenshot_on_error(self.driver, "#08_back_error", str(e))
        time.sleep(2)
        self.screenshot_utils.take_screenshot(self.driver, "#08_after_back", "after")
        login_tab.click()
        time.sleep(3)  # Tăng thời gian chờ
        
        #Precondition cho step 7 
        # Thử tìm Username input với error handling
        try:
            UserName_input = self.driver.find_element(AppiumBy.XPATH, LoginXPaths.USERNAME_INPUT)
        except Exception as e:
            print(f"[ERROR] Không tìm thấy Username input với XPath: {LoginXPaths.USERNAME_INPUT}")
            print(f"[ERROR] Chi tiết lỗi: {e}")
            # Thử với XPath khác
            try:
                UserName_input = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[1]")
                print("[INFO] Tìm thấy Username input với XPath thay thế")
            except:
                raise Exception("Không thể tìm thấy Username input field")
        if not UserName_input.is_displayed():
            print("[ERROR] Không tìm thấy màn hình Login!")
        else:
            print("[INFO] Màn hình Login hiển thị đúng.")
            # Click vào input field trước khi nhập
            UserName_input.click()
            time.sleep(1)
            # Clear text cũ nếu có
            UserName_input.clear()
            time.sleep(1)
            # Nhập text mới
            UserName_input.send_keys("Z22-0300013")
            print("[INFO] Đã nhập username: Z22-0300013")
            # Kiểm tra giá trị đã nhập
            try:
                input_value = UserName_input.get_attribute('text')
                print(f"[INFO] Giá trị trong input: '{input_value}'")
            except:
                print("[WARNING] Không thể kiểm tra giá trị input")
        time.sleep(2)
        self.screenshot_utils.take_screenshot(self.driver, "#09_username_entered", "after")
        print("[INFO] Đã nhập username: Z22-0300013")
        # Tìm Password input
        Password_input= self.driver.find_element(AppiumBy.XPATH, LoginXPaths.PASSWORD_INPUT)
        # Click vào input field trước khi nhập
        Password_input.click()
        time.sleep(1)
        # Clear text cũ nếu có
        Password_input.clear()
        time.sleep(1)
        # Nhập text mới
        Password_input.send_keys("123456")
        self.screenshot_utils.take_screenshot(self.driver, "#10_password_entered", "after")
        print("[INFO] Đã nhập password: 123456")
        # Kiểm tra giá trị đã nhập
        try:
            input_value = Password_input.get_attribute('text')
            print(f"[INFO] Giá trị trong password input: '{input_value}'")
        except:
            print("[WARNING] Không thể kiểm tra giá trị password input")
        # Tìm Save button cho Password set ON
        Password_save_button= self.driver.find_element(AppiumBy.XPATH, LoginXPaths.PASSWORD_SAVE_BUTTON)
        if not Password_save_button.is_displayed():
            print("[ERROR] Không tìm thấy element save pass!")
        else:
            print("[INFO]  Element save pass có tồn tại.")
            Password_save_button.click()
        time.sleep(10)

        self.screenshot_utils.take_screenshot(self.driver, "#11_password_save_clicked", "after")
        # Tìm click button Login
        try:
            Login_button = self.driver.find_element(AppiumBy.XPATH, LoginXPaths.LOGIN_BUTTON)
            if not Login_button.is_displayed():
                print("[ERROR] Không tìm thấy button Login!")
            else:
                print("[INFO] Hiển thị button Login.")
                Login_button.click()
                time.sleep(2)
                self.screenshot_utils.take_screenshot(self.driver, "#12_login_clicked", "after")
        except Exception as e:
            print(f"[ERROR] Lỗi khi tìm hoặc click vào Login button: {e}")
            self.screenshot_utils.take_screenshot_on_error(self.driver, "#12_login_error", str(e))       
        
        # Tắt app trước
        kill_app(self.driver, self.platform)
        time.sleep(2)
        
        # Chụp màn hình trước
        self.screenshot_utils.take_screenshot(self.driver, "#13_before_restart_2", "before")
        
        # Khởi động lại app
        self.appium_config.restart_app(self.driver, self.platform)
        time.sleep(2)
        
        # Chụp màn hình sau
        self.screenshot_utils.take_screenshot(self.driver, "#14_after_restart_2", "after")
        # Tìm tab Login trên màn hình Market
        try:
            # Thử tìm tab Login bằng content-desc
            login_tab = self.driver.find_element(AppiumBy.XPATH, "//*[@content-desc='ログイン' or @content-desc='Login']")
            if login_tab.is_displayed():
                print("[INFO] Tìm thấy tab Login, đang click...")
                login_tab.click()
                time.sleep(2)
            else:
                print("[WARNING] Tab Login không hiển thị")
        except Exception as e:
            print(f"[ERROR] Không tìm thấy tab Login: {e}")
            # Thử tìm bằng cách khác
            try:
                login_tab = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text, 'ログイン') or contains(@text, 'Login')]")
                if login_tab.is_displayed():
                    print("[INFO] Tìm thấy tab Login bằng text, đang click...")
                    login_tab.click()
                    time.sleep(2)
                else:
                    print("[WARNING] Tab Login không hiển thị")
            except Exception as e2:
                print(f"[ERROR] Không tìm thấy tab Login bằng text: {e2}")
                self.screenshot_utils.take_screenshot_on_error(self.driver, "#15_login_tab_error_2", str(e2))
        time.sleep(2)
        # Chụp màn hình sau
        self.screenshot_utils.take_screenshot(self.driver, "#15_login_screen_again", "after")
       
        # Tìm lại Username input sau khi DOM thay đổi
        try:
            UserName_input = self.driver.find_element(AppiumBy.XPATH, LoginXPaths.USERNAME_INPUT)
            if not UserName_input.is_displayed():
                print("[ERROR] Username input không hiển thị!")
                UserName_input = None
            else:
                print("[INFO] Hiển thị Username input cho Step 6.")
                self.screenshot_utils.take_screenshot(self.driver, "#16_username_field", "before")
        except:
            print("[WARNING] Không thể tìm thấy Username input cho Step 6, thử XPath khác...")
            try:
                UserName_input = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[1]")
                print("[INFO] Tìm thấy Username input với XPath thay thế")
            except:
                print("[ERROR] Không thể tìm thấy Username input với cả 2 XPath")
                UserName_input = None
                
        if UserName_input:  
            # Click vào input field trước khi nhập
            UserName_input.click()
            time.sleep(1)
            # Clear text cũ nếu có
            UserName_input.clear()
            time.sleep(1)
            # Nhập lại username
            UserName_input.send_keys("Z22-0300013")
            print("[INFO] Đã nhập lại username: Z22-0300013")
            # Kiểm tra giá trị đã nhập
            try:
                input_value = UserName_input.get_attribute('text')
                print(f"[INFO] Giá trị trong input: '{input_value}'")
            except:
                print("[WARNING] Không thể kiểm tra giá trị input")
        else:
            print("[ERROR] Không thể nhập Username vì không tìm thấy input field.")
        self.screenshot_utils.take_screenshot(self.driver, "#16_username_entered_again", "after")
        UserName_save_button = self.driver.find_element(AppiumBy.XPATH, LoginXPaths.USERNAME_SAVE_BUTTON)   
        if not UserName_save_button.is_displayed():
            print("[ERROR] Không tìm thấy element save user name!")
        else:  
            # Click vào nút Save UserName
            print("[INFO]  Element save user name có tồn tại.")
            UserName_save_button.click()
        self.screenshot_utils.take_screenshot(self.driver, "#17_username_save_clicked", "after")
        
        # Chờ dialog xuất hiện
        print("[DEBUG] Đang chờ dialog setting login xuất hiện...")
        time.sleep(3)
        
        # Chụp màn hình để kiểm tra
        self.screenshot_utils.take_screenshot(self.driver, "#18_before_dialog_check", "debug")
        
        #Check dialog setting login
        Dialog_Setting_Login = None  # Khởi tạo biến trước
        
        try:   
            Dialog_Setting_Login = self.driver.find_element(AppiumBy.XPATH, LoginXPaths.Dialog_Setting_Login)
            if not Dialog_Setting_Login.is_displayed():
                print("[ERROR] Dialog setting login không hiển thị!")
                Dialog_Setting_Login = None
            else:
                print("[INFO] Hiển thị dialog setting login.")
        except Exception as e:
            print(f"[ERROR] Lỗi khi tìm dialog setting login: {e}")
            self.screenshot_utils.take_screenshot_on_error(self.driver, "#18_dialog_not_found", str(e))
            
            # Thử tìm dialog bằng cách khác
            try:
                print("[DEBUG] Thử tìm dialog qua button OK...")
                ok_button = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='OK']")
                if ok_button.is_displayed():
                    print("[INFO] Tìm thấy button OK - dialog đang hiển thị!")
                    Dialog_Setting_Login = "found_by_ok_button"
                    self.screenshot_utils.take_screenshot(self.driver, "#18_dialog_found_by_ok", "debug")
            except:
                print("[DEBUG] Không tìm thấy button OK")
                Dialog_Setting_Login = None
        
        if Dialog_Setting_Login:
            # Click vào nút OK trong dialog
            try:
                Button_DialogOK = self.driver.find_element(AppiumBy.XPATH, LoginXPaths.Button_DialogOK)
                if not Button_DialogOK.is_displayed():
                    print("[ERROR] Không tìm thấy nút OK trong dialog!")
                else:
                    print("[INFO] Hiển thị nút OK trong dialog setting login.")
                    Button_DialogOK.click()
                    time.sleep(2)
            except Exception as e:
                print(f"[ERROR] Lỗi khi tìm hoặc cl3ick vào nút OK: {e}")
                self.screenshot_utils.take_screenshot_on_error(self.driver, "#19_ok_button_error", str(e))

                Button_DialogOK = None
        else:
            print("[WARNING] Không có dialog setting login để xử lý.")
        self.screenshot_utils.take_screenshot(self.driver, "#20_after_dialog_setting", "after")
        # Thử tìm AutoLogin switch với error handling
        # Thực hiện tap vào AutoLogin switch
        # Thử tìm AutoLogin switch với error handling
        #  Thử tìm AutoLogin switch với error handling
        try:
            AutoLogin_switch = self.driver.find_element(AppiumBy.XPATH, LoginXPaths.AUTO_LOGIN_TOGGLE)
            if not AutoLogin_switch.is_displayed():
                print("[ERROR] Không tìm thấy switch AutoLogin!")
            else:
                print("[INFO] Hiển thị switch AutoLogin.")
                # Click vào switch để bật/tắt
                AutoLogin_switch.click()
                time.sleep(2)
        except Exception as e:
            print(f"[ERROR] Lỗi khi tìm hoặc click vào AutoLogin switch: {e}")
            self.screenshot_utils.take_screenshot_on_error(self.driver, "#21_autologin_switch_error", str(e))
        self.screenshot_utils.take_screenshot(self.driver, "#21_autologin_switch_clicked", "after")     
       
        # Row 9 trong test case - Nhập lại password
        print("[DEBUG] Bắt đầu test row 9 - nhập lại password...")
        
        # Chụp màn hình để xem trạng thái hiện tại
        self.screenshot_utils.take_screenshot(self.driver, "#22_before_password_test", "debug")
        
        # Đảm bảo đang ở màn hình login
        try:
            # Kiểm tra xem có đang ở màn hình login không
            login_elements = self.driver.find_elements(AppiumBy.XPATH, LoginXPaths.LOGIN_BUTTON)
            if not login_elements:
                print("[WARNING] Không phải màn hình login, thử quay lại...")
                # Thử click back hoặc restart app nếu cần
                try:
                    back_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
                    back_button.click()
                    time.sleep(2)
                except:
                    print("[DEBUG] Không tìm thấy nút back")
        except:
            pass
            
        # Tìm lại Password input với nhiều cách
        Password_input = None
        try:
            # Cách 1: XPath từ LoginXPaths
            Password_input = self.driver.find_element(AppiumBy.XPATH, LoginXPaths.PASSWORD_INPUT)
            print("[INFO] Tìm thấy Password input với XPath chính")
        except:
            # Cách 2: Tìm theo hint
            try:
                Password_input = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@hint='パスワード']")
                print("[INFO] Tìm thấy Password input với hint")
            except:
                # Cách 3: Tìm EditText thứ 2
                try:
                    all_edittexts = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
                    if len(all_edittexts) >= 2:
                        Password_input = all_edittexts[1]  # Password thường là EditText thứ 2
                        print("[INFO] Tìm thấy Password input là EditText thứ 2")
                except:
                    pass
                    
        if Password_input and Password_input.is_displayed():
            print("[INFO] Hiển thị Password input field, đang nhập lại...")
            # Click vào input
            Password_input.click()
            time.sleep(1)
            # Clear text cũ nếu có
            Password_input.clear()
            time.sleep(1)
            # Nhập lại password
            Password_input.send_keys("123456")
            print("[INFO] Đã nhập lại password: 123456")
            
            # Kiểm tra giá trị đã nhập
            try:
                input_value = Password_input.get_attribute('text')
                print(f"[INFO] Giá trị trong password input: '{input_value}'")
            except:
                print("[WARNING] Không thể kiểm tra giá trị password input")
                
            self.screenshot_utils.take_screenshot(self.driver, "#22_password_entered_again", "after")
        else:
            print("[ERROR] Không tìm thấy Password input field!")
            # In thêm thông tin debug
            try:
                all_elements = self.driver.find_elements(AppiumBy.XPATH, "//*")
                print(f"[DEBUG] Tổng số elements trên màn hình: {len(all_elements)}")
                
                # In một số EditText để debug
                edittexts = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
                print(f"[DEBUG] Số lượng EditText: {len(edittexts)}")
                for i, et in enumerate(edittexts[:3]):
                    try:
                        hint = et.get_attribute('hint')
                        text = et.get_attribute('text')
                        print(f"[DEBUG] EditText {i}: hint='{hint}', text='{text}'")
                    except:
                        pass
            except:
                pass
            self.screenshot_utils.take_screenshot_on_error(self.driver, "#22_password_not_found", "error")
            return
            
        # Tìm và toggle Password save button
        try:
            password_save_button = self.driver.find_element(AppiumBy.XPATH, LoginXPaths.PASSWORD_SAVE_BUTTON)
            if not password_save_button.is_displayed():
                print("[ERROR] Không tìm thấy element save pass!")
            else:
                print("[INFO] Element save pass có tồn tại.")
                # Chụp trước khi click
                self.screenshot_utils.take_screenshot(self.driver, "#23_password_save_before", "before")
                # Click để toggle
                password_save_button.click()
                time.sleep(1)
                print("[INFO] Đã click toggle password save button")
                # Chụp sau khi click
                self.screenshot_utils.take_screenshot(self.driver, "#24_password_save_after", "after")
                password_save_button.click()
                time.sleep(1)
                print("[INFO] Đã click toggle password save button ON")
                # Chụp sau khi click
                self.screenshot_utils.take_screenshot(self.driver, "#24_password_save ON_after", "after")


        except Exception as e:
            print(f"[ERROR] Lỗi khi xử lý password save button: {e}")
            self.screenshot_utils.take_screenshot_on_error(self.driver, "#23_password_save_error", str(e))
                                        
         ####Row 12 
         #  #Check dialog setting login
        Dialog_Setting_Login = None  # Khởi tạo biến trước
        
        try:   
            Dialog_Setting_Login = self.driver.find_element(AppiumBy.XPATH, LoginXPaths.Dialog_Setting_Login)
            if not Dialog_Setting_Login.is_displayed():
                print("[ERROR] Dialog setting login không hiển thị!")
                Dialog_Setting_Login = None
            else:
                print("[INFO] Hiển thị dialog setting login.")
        except Exception as e:
            print(f"[ERROR] Lỗi khi tìm dialog setting login: {e}")
            self.screenshot_utils.take_screenshot_on_error(self.driver, "#18_dialog_not_found", str(e))
            
            # Thử tìm dialog bằng cách khác
            try:
                print("[DEBUG] Thử tìm dialog qua button OK...")
                ok_button = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='OK']")
                if ok_button.is_displayed():
                    print("[INFO] Tìm thấy button OK - dialog đang hiển thị!")
                    Dialog_Setting_Login = "found_by_ok_button"
                    self.screenshot_utils.take_screenshot(self.driver, "#18_dialog_found_by_ok", "debug")
            except:
                print("[DEBUG] Không tìm thấy button OK")
                Dialog_Setting_Login = None
        
        if Dialog_Setting_Login:
            # Click vào nút OK trong dialog
            try:
                Button_DialogOK = self.driver.find_element(AppiumBy.XPATH, LoginXPaths.Button_DialogOK)
                if not Button_DialogOK.is_displayed():
                    print("[ERROR] Không tìm thấy nút OK trong dialog!")
                else:
                    print("[INFO] Hiển thị nút OK trong dialog setting login.")
                    Button_DialogOK.click()
                    time.sleep(2)
            except Exception as e:
                print(f"[ERROR] Lỗi khi tìm hoặc cl3ick vào nút OK: {e}")
                self.screenshot_utils.take_screenshot_on_error(self.driver, "#19_ok_button_error", str(e))

                Button_DialogOK = None
        else:
            print("[WARNING] Không có dialog setting login để xử lý.")
        self.screenshot_utils.take_screenshot(self.driver, "#20_after_dialog_setting", "after")
        # Thử tìm AutoLogin switch với error handling
        # Thực hiện tap vào AutoLogin switch
        # Thử tìm AutoLogin switch với error handling
        #  Thử tìm AutoLogin switch với error handling
        try:
            AutoLogin_switch = self.driver.find_element(AppiumBy.XPATH, LoginXPaths.AUTO_LOGIN_TOGGLE)
            if not AutoLogin_switch.is_displayed():
                print("[ERROR] Không tìm thấy switch AutoLogin!")
            else:
                print("[INFO] Hiển thị switch AutoLogin.")
                # Click vào switch để bật/tắt
                AutoLogin_switch.click()
                time.sleep(2)
        except Exception as e:
            print(f"[ERROR] Lỗi khi tìm hoặc click vào AutoLogin switch: {e}")
            self.screenshot_utils.take_screenshot_on_error(self.driver, "#21_autologin_switch_error", str(e))
        self.screenshot_utils.take_screenshot(self.driver, "#21_autologin_switch_clicked", "after")     
                                            
        




    def run_all_tests(self):
        """Chạy tất cả test cases"""
        try:
            print(f"=== Bắt đầu chạy automation Login cho {self.platform} ===")
            
            # Setup driver
            self.setup_driver()
            
            # Chạy các test cases
            self.test_show_startup()
            self.test_show_Login()
            
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
        print("Cách dùng: python Login.py [android|ios]")
        sys.exit(1)
    
    platform = sys.argv[1].lower()
    if platform not in ["android", "ios"]:
        print("Platform phải là 'android' hoặc 'ios'")
        sys.exit(1)
    
    # Tạo instance và chạy test
    automation = LoginAutomation(platform)
    automation.run_all_tests()

if __name__ == "__main__":
    main() 



