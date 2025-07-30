# -*- coding: utf-8 -*-
"""
XPath Objects từ màn hình hiện tại
Generated: 2025-07-25 09:34:45
Screen: Login (ログイン) - Login Dialog
"""

class CurrentScreenXPaths:
    """XPath objects from current screen"""

    # Main container elements
    HIERARCHY = "//hierarchy"
    MAIN_FRAME = "//hierarchy/android.widget.FrameLayout"
    LINEAR_LAYOUT = "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
    CONTENT_FRAME = "//android.widget.FrameLayout[@resource-id='android:id/content']"
    INNER_FRAME = "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout"
    
    # Dialog container
    DIALOG_CONTAINER = "//android.widget.FrameLayout[@pane-title='ダイアログ']"
    SCROLLABLE_CONTAINER = "//android.view.View[@scrollable='true'][@bounds='[0,0][1080,2400]']"
    MAIN_CONTENT = "//android.view.View[@scrollable='true'][@bounds='[0,128][1080,2274]']"
    
    # Header elements
    CLOSE_BUTTON = "//android.widget.ImageView[@bounds='[965,134][1080,249]']"
   # NoticePrivateList_Lable="//android.widget.TextView[contains(@text,'緊急なお知らせ')]"
    NoticePrivateList_Lable="//*[contains(@content-desc,'緊急なお知らせ')]"
    # Logo and branding
    LOGO_IMAGE = "//android.widget.ImageView[@bounds='[239,312][841,404]']"
    
    # Username section
    USERNAME_LABEL = "//android.view.View[@content-desc='ユーザーネーム']"
    USERNAME_INPUT = "//android.widget.EditText[@hint='ユーザーネーム']"
    USERNAME_SAVE_BUTTON = "//android.view.View[@content-desc='保存'][@bounds='[873,527][963,642]']"
    USERNAME_SAVE_INNER = "//android.view.View[@bounds='[874,587][963,642]']"
    
    # Password section
    PASSWORD_LABEL = "//android.view.View[@content-desc='パスワード']"
    PASSWORD_INPUT = "//android.widget.EditText[@hint='パスワード']"
    PASSWORD_TOGGLE = "//android.widget.ImageView[@bounds='[701,711][816,826]']"
    PASSWORD_SAVE_BUTTON = "//android.view.View[@content-desc='保存'][@bounds='[873,711][963,826]']"
    PASSWORD_SAVE_INNER = "//android.view.View[@bounds='[874,771][963,826]']"
    
    # Auto login section
    AUTO_LOGIN_LABEL = "//android.view.View[@content-desc='自動ログイン']"
    AUTO_LOGIN_TOGGLE = "//android.view.View[@bounds='[624,890][716,947]']"
    
    # Login button
    LOGIN_BUTTON = "//android.view.View[@content-desc='ログイン']"
    
    # Help and support
    LOGIN_HELP = "//android.widget.ImageView[@content-desc='ログインでお困りの方']"
    
    # Account creation
    ACCOUNT_CREATION = "//android.view.View[@content-desc='証券総合口座開設']"
    
    # Footer links
    NOTICE_LINK = "//android.view.View[@content-desc='お知らせ']"
    POLICY_LINK = "//android.view.View[@content-desc='ポリシー/免責事項']"
    TRADING_NOTICE = "//android.view.View[@content-desc='お取引注意事項']"
    MAINTENANCE_INFO = "//android.widget.ImageView[@content-desc='メンテナンス情報']"
    SYSTEM_INFO = "//android.view.View[@content-desc='システム関連情報']"
    
    # Footer text
    COPYRIGHT_TEXT = "//android.view.View[@content-desc='(C)SBI SECURITIES Co.,Ltd.']"
    VERSION_TEXT = "//android.view.View[@content-desc='Ver 4.1.2']"
    
    # Bottom image
    BOTTOM_IMAGE = "//android.widget.ImageView[@bounds='[72,2117][1008,2175]']"
    
    # Generic selectors
    ALL_CLICKABLE_ELEMENTS = "//*[@clickable='true' or @enabled='true']"
    ALL_VIEWS = "//android.view.View"
    ALL_IMAGEVIEWS = "//android.widget.ImageView"
    ALL_EDITTEXTS = "//android.widget.EditText"
    
    # Specific element selectors by bounds
    CLOSE_BUTTON_BOUNDS = "//android.widget.ImageView[@bounds='[965,134][1080,249]']"
    LOGO_IMAGE_BOUNDS = "//android.widget.ImageView[@bounds='[239,312][841,404]']"
    USERNAME_INPUT_BOUNDS = "//android.widget.EditText[@bounds='[125,541][816,628]']"
    USERNAME_SAVE_BOUNDS = "//android.view.View[@bounds='[873,527][963,642]']"
    PASSWORD_INPUT_BOUNDS = "//android.widget.EditText[@bounds='[125,724][701,813]']"
    PASSWORD_TOGGLE_BOUNDS = "//android.widget.ImageView[@bounds='[701,711][816,826]']"
    PASSWORD_SAVE_BOUNDS = "//android.view.View[@bounds='[873,711][963,826]']"
    AUTO_LOGIN_TOGGLE_BOUNDS = "//android.view.View[@bounds='[624,890][716,947]']"
    LOGIN_BUTTON_BOUNDS = "//android.view.View[@bounds='[166,1034][914,1160]']"
    LOGIN_HELP_BOUNDS = "//android.widget.ImageView[@bounds='[292,1211][788,1315]']"
    ACCOUNT_CREATION_BOUNDS = "//android.view.View[@bounds='[166,1356][914,1472]']"
    NOTICE_LINK_BOUNDS = "//android.view.View[@bounds='[99,1786][271,1858]']"
    POLICY_LINK_BOUNDS = "//android.view.View[@bounds='[329,1786][653,1858]']"
    TRADING_NOTICE_BOUNDS = "//android.view.View[@bounds='[705,1786][981,1858]']"
    MAINTENANCE_INFO_BOUNDS = "//android.widget.ImageView[@bounds='[201,1860][552,1932]']"
    SYSTEM_INFO_BOUNDS = "//android.view.View[@bounds='[569,1860][879,1932]']"
    COPYRIGHT_BOUNDS = "//android.view.View[@bounds='[63,1961][479,2003]']"
    VERSION_BOUNDS = "//android.view.View[@bounds='[898,1961][1034,2003]']"
    BOTTOM_IMAGE_BOUNDS = "//android.widget.ImageView[@bounds='[72,2117][1008,2175]']"
    
    # Content description selectors
    USERNAME_BY_DESC = "//*[@content-desc='ユーザーネーム']"
    PASSWORD_BY_DESC = "//*[@content-desc='パスワード']"
    AUTO_LOGIN_BY_DESC = "//*[@content-desc='自動ログイン']"
    LOGIN_BY_DESC = "//*[@content-desc='ログイン']"
    LOGIN_HELP_BY_DESC = "//*[@content-desc='ログインでお困りの方']"
    ACCOUNT_CREATION_BY_DESC = "//*[@content-desc='証券総合口座開設']"
    SAVE_BY_DESC = "//*[@content-desc='保存']"
    NOTICE_BY_DESC = "//*[@content-desc='お知らせ']"
    POLICY_BY_DESC = "//*[@content-desc='ポリシー/免責事項']"
    TRADING_NOTICE_BY_DESC = "//*[@content-desc='お取引注意事項']"
    MAINTENANCE_BY_DESC = "//*[@content-desc='メンテナンス情報']"
    SYSTEM_INFO_BY_DESC = "//*[@content-desc='システム関連情報']"
    COPYRIGHT_BY_DESC = "//*[@content-desc='(C)SBI SECURITIES Co.,Ltd.']"
    VERSION_BY_DESC = "//*[@content-desc='Ver 4.1.2']"
    
    # Input field selectors
    USERNAME_INPUT_BY_HINT = "//android.widget.EditText[@hint='ユーザーネーム']"
    PASSWORD_INPUT_BY_HINT = "//android.widget.EditText[@hint='パスワード']"
    
    # Dialog selectors
    DIALOG_BY_TITLE = "//*[@pane-title='ダイアログ']"


    #Dialog setting login
    #DIALOG_SETTING_LOGIN = "//*[@pane-title='パスワードの保存機能をONにする場合は、端末にロックをかけるなどのセキュリティ対策をおすすめいたします。']"
    Dialog_Setting_Login = "//*[contains(@pane-title,'パスワードの保存機能')]"
    Button_DialogOK ="//android.view.View[@content-desc='OK']"
    Button_DialogCancel ="//android.view.View[@content-desc='キャンセル']"


class ScreenInfo:
    """Information about current screen"""
    
    SCREEN_NAME = "Login (ログイン)"
    SCREEN_TYPE = "Login Dialog"
    SCREEN_RESOLUTION = "1080x2146"
    PACKAGE_NAME = "jp.co.mobileit.SBI_FX"
    TIMESTAMP = "2025-07-25 09:34:45"
    APP_VERSION = "Ver 4.1.2"
    
    # Login form elements
    LOGIN_FORM = {
        "username": {
            "label": "ユーザーネーム",
            "input_type": "EditText",
            "hint": "ユーザーネーム",
            "save_button": "保存"
        },
        "password": {
            "label": "パスワード", 
            "input_type": "EditText",
            "hint": "パスワード",
            "toggle_visibility": True,
            "save_button": "保存"
        },
        "auto_login": {
            "label": "自動ログイン",
            "toggle": True
        },
        "login_button": {
            "text": "ログイン",
            "type": "button"
        }
    }
    
    # Footer links
    FOOTER_LINKS = [
        "お知らせ",
        "ポリシー/免責事項", 
        "お取引注意事項",
        "メンテナンス情報",
        "システム関連情報"
    ]
    
    # Help and support
    HELP_OPTIONS = [
        "ログインでお困りの方",
        "証券総合口座開設"
    ]
    
    # Company information
    COMPANY_INFO = {
        "copyright": "(C)SBI SECURITIES Co.,Ltd.",
        "version": "Ver 4.1.2"
    }
    
    # Screen layout
    LAYOUT = {
        "header": "Close button and logo",
        "form_section": "Username, password, auto-login",
        "action_section": "Login button and help links", 
        "footer": "Legal links and company info"
    }


# Usage examples:
if __name__ == "__main__":
    print("=== XPath Objects for Current Screen ===")
    print(f"Screen: {ScreenInfo.SCREEN_NAME}")
    print(f"Screen Type: {ScreenInfo.SCREEN_TYPE}")
    print(f"Resolution: {ScreenInfo.SCREEN_RESOLUTION}")
    print(f"Package: {ScreenInfo.PACKAGE_NAME}")
    print(f"Generated: {ScreenInfo.TIMESTAMP}")
    print(f"App Version: {ScreenInfo.APP_VERSION}")
    
    print("\n=== Login Form Elements ===")
    for field, details in ScreenInfo.LOGIN_FORM.items():
        print(f"{field}: {details}")
    
    print("\n=== Footer Links ===")
    for link in ScreenInfo.FOOTER_LINKS:
        print(f"- {link}")
    
    print("\n=== Help Options ===")
    for help_option in ScreenInfo.HELP_OPTIONS:
        print(f"- {help_option}")
    
    print("\n=== Available XPath Selectors ===")
    print(f"Username Input: {CurrentScreenXPaths.USERNAME_INPUT}")
    print(f"Password Input: {CurrentScreenXPaths.PASSWORD_INPUT}")
    print(f"Login Button: {CurrentScreenXPaths.LOGIN_BUTTON}")
    print(f"Close Button: {CurrentScreenXPaths.CLOSE_BUTTON}")
    print(f"Auto Login Toggle: {CurrentScreenXPaths.AUTO_LOGIN_TOGGLE}") 