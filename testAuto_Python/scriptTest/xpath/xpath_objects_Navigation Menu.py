# -*- coding: utf-8 -*-
"""
XPath Objects từ màn hình hiện tại
Generated: 2025-07-25 09:40:30
Screen: Navigation Menu (ナビゲーション メニュー) - Main Menu
"""

class CurrentScreenXPaths:
    """XPath objects from current screen"""

    # Main container elements
    HIERARCHY = "//hierarchy"
    MAIN_FRAME = "//hierarchy/android.widget.FrameLayout"
    LINEAR_LAYOUT = "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
    CONTENT_FRAME = "//android.widget.FrameLayout[@resource-id='android:id/content']"
    NAVIGATION_CONTAINER = "//android.widget.FrameLayout[@pane-title='ナビゲーション メニュー']"
    
    # Header elements
    MENU_BUTTON = "//android.widget.ImageView[@bounds='[0,143][96,239]']"
    MENU_TITLE = "//android.view.View[@content-desc='メニュー']"
    
    # Main content area
    MAIN_CONTENT = "//android.view.View[@bounds='[0,254][1080,2136]']"
    SCROLL_VIEW = "//android.widget.ScrollView[@bounds='[0,254][1080,2136]']"
    
    # Banner/Advertisement area
    BANNER_IMAGE = "//android.widget.ImageView[@bounds='[0,300][1080,458]']"
    BANNER_CONTAINER = "//android.view.View[@bounds='[0,300][1080,458]']"
    
    # Scroll indicator
    SCROLL_INDICATOR = "//android.view.View[@bounds='[517,479][563,490]']"
    
    # Content sections
    CONTENT_SECTIONS = "//android.view.View[@bounds='[0,490][1080,1962]']"
    
    # 1. お知らせ (Notifications) Section
    NOTIFICATIONS_SECTION = "//android.view.View[@content-desc='お知らせ']"
    NOTIFICATIONS_CONTAINER = "//android.view.View[@bounds='[0,490][1080,796]']"
    NOTIFICATIONS_MAIN = "//android.widget.ImageView[@content-desc='お知らせ'][@bounds='[29,606][362,796]']"
    TRADING_NOTIFICATIONS = "//android.widget.ImageView[@content-desc='取引関連お知らせ'][@bounds='[373,606][707,796]']"
    CAMPAIGN_SECTION = "//android.view.View[@content-desc='キャンペーン'][@bounds='[718,606][1051,796]']"
    CAMPAIGN_ICON = "//android.widget.ImageView[@bounds='[856,643][913,700]']"
    CAMPAIGN_BADGE = "//android.widget.ImageView[@bounds='[996,722][1022,748]']"
    
    # 2. サービス (Services) Section
    SERVICES_SECTION = "//android.view.View[@content-desc='サービス']"
    SERVICES_CONTAINER = "//android.view.View[@bounds='[0,796][1080,1103]']"
    TRANSFER_SERVICE = "//android.widget.ImageView[@content-desc='振替'][@bounds='[29,912][276,1103]']"
    NEW_ORDER = "//android.widget.ImageView[@content-desc='新規注文'][@bounds='[287,912][534,1103]']"
    SETTLEMENT_ORDER = "//android.widget.ImageView[@content-desc='決済注文'][@bounds='[546,912][793,1103]']"
    CASH_DELIVERY = "//android.widget.ImageView[@content-desc='現引'][@bounds='[804,912][1051,1103]']"
    
    # 3. 設定・その他 (Settings & Others) Section
    SETTINGS_SECTION = "//android.view.View[@content-desc='設定・その他']"
    SETTINGS_CONTAINER = "//android.view.View[@bounds='[0,1103][1080,1962]']"
    
    # Settings row 1
    SETTINGS_BUTTON = "//android.widget.ImageView[@content-desc='設定'][@bounds='[29,1219][534,1409]']"
    PUSH_NOTIFICATIONS = "//android.widget.ImageView[@content-desc='プッシュ通知'][@bounds='[546,1219][1051,1409]']"
    
    # Settings row 2
    ECONOMIC_INDICATORS = "//android.view.View[@content-desc='経済指標'][@bounds='[29,1420][534,1547]']"
    SWAP_HISTORY = "//android.view.View[@content-desc='スワップ履歴'][@bounds='[546,1420][1051,1547]']"
    
    # Settings row 3
    LEVERAGE_SETTINGS = "//android.view.View[@content-desc='レバレッジ設定'][@bounds='[29,1559][534,1685]']"
    TRADING_PERFORMANCE = "//android.view.View[@content-desc='取引成績'][@bounds='[546,1559][1051,1685]']"
    
    # Settings row 4
    REQUIRED_MARGIN = "//android.view.View[@content-desc='必要保証金'][@bounds='[29,1697][534,1823]']"
    COMPLIANCE = "//android.view.View[@content-desc='コンプライアンス'][@bounds='[546,1697][1051,1823]']"
    
    # Settings row 5
    REPORTS = "//android.view.View[@content-desc='報告書'][@bounds='[29,1835][534,1962]']"
    MAIN_SITE = "//android.widget.ImageView[@content-desc='メインサイト'][@bounds='[546,1835][1051,1962]']"
    
    # Bottom navigation tabs
    BOTTOM_TABS_CONTAINER = "//android.view.View[@bounds='[0,2032][1080,2136]']"
    STOCKS_TAB = "//android.widget.ImageView[@content-desc='株'][@bounds='[14,2032][185,2136]']"
    US_STOCKS_TAB = "//android.widget.ImageView[@content-desc='米国株'][@bounds='[234,2032][406,2136]']"
    FUTURES_OPTIONS_TAB = "//android.widget.ImageView[@content-desc='先物OP'][@bounds='[454,2032][626,2136]']"
    EXCHANGE_CFD_TAB = "//android.widget.ImageView[@content-desc='取引所CFD'][@bounds='[674,2032][846,2136]']"
    INVESTMENT_TRUST_TAB = "//android.widget.ImageView[@content-desc='投信積立'][@bounds='[895,2032][1066,2136]']"
    
    # Main bottom navigation
    MAIN_BOTTOM_NAV = "//android.view.View[@bounds='[0,2136][1080,2400]']"
    MARKET_TAB = "//android.widget.ImageView[@content-desc='マーケット'][@bounds='[0,2136][180,2274]']"
    CHART_TAB = "//android.widget.ImageView[@content-desc='チャート'][@bounds='[180,2136][360,2274]']"
    SPEED_ORDER_TAB = "//android.widget.ImageView[@content-desc='スピード注文'][@bounds='[360,2136][540,2274]']"
    LOGIN_TAB = "//android.widget.ImageView[@content-desc='ログイン'][@bounds='[540,2136][720,2274]']"
    WEBSITE_TAB = "//android.widget.ImageView[@content-desc='ウェブサイト'][@bounds='[720,2136][900,2274]']"
    MENU_TAB = "//android.widget.ImageView[@content-desc='メニュー'][@bounds='[900,2136][1080,2274]']"
    
    # Generic selectors
    ALL_CLICKABLE_ELEMENTS = "//*[@clickable='true' or @enabled='true']"
    ALL_VIEWS = "//android.view.View"
    ALL_IMAGEVIEWS = "//android.widget.ImageView"
    ALL_SCROLLVIEWS = "//android.widget.ScrollView"
    
    # Content description selectors
    MENU_BY_DESC = "//*[@content-desc='メニュー']"
    NOTIFICATIONS_BY_DESC = "//*[@content-desc='お知らせ']"
    TRADING_NOTIFICATIONS_BY_DESC = "//*[@content-desc='取引関連お知らせ']"
    CAMPAIGN_BY_DESC = "//*[@content-desc='キャンペーン']"
    SERVICES_BY_DESC = "//*[@content-desc='サービス']"
    TRANSFER_BY_DESC = "//*[@content-desc='振替']"
    NEW_ORDER_BY_DESC = "//*[@content-desc='新規注文']"
    SETTLEMENT_ORDER_BY_DESC = "//*[@content-desc='決済注文']"
    CASH_DELIVERY_BY_DESC = "//*[@content-desc='現引']"
    SETTINGS_OTHERS_BY_DESC = "//*[@content-desc='設定・その他']"
    SETTINGS_BY_DESC = "//*[@content-desc='設定']"
    PUSH_NOTIFICATIONS_BY_DESC = "//*[@content-desc='プッシュ通知']"
    ECONOMIC_INDICATORS_BY_DESC = "//*[@content-desc='経済指標']"
    SWAP_HISTORY_BY_DESC = "//*[@content-desc='スワップ履歴']"
    LEVERAGE_SETTINGS_BY_DESC = "//*[@content-desc='レバレッジ設定']"
    TRADING_PERFORMANCE_BY_DESC = "//*[@content-desc='取引成績']"
    REQUIRED_MARGIN_BY_DESC = "//*[@content-desc='必要保証金']"
    COMPLIANCE_BY_DESC = "//*[@content-desc='コンプライアンス']"
    REPORTS_BY_DESC = "//*[@content-desc='報告書']"
    MAIN_SITE_BY_DESC = "//*[@content-desc='メインサイト']"
    STOCKS_BY_DESC = "//*[@content-desc='株']"
    US_STOCKS_BY_DESC = "//*[@content-desc='米国株']"
    FUTURES_OPTIONS_BY_DESC = "//*[@content-desc='先物OP']"
    EXCHANGE_CFD_BY_DESC = "//*[@content-desc='取引所CFD']"
    INVESTMENT_TRUST_BY_DESC = "//*[@content-desc='投信積立']"
    MARKET_BY_DESC = "//*[@content-desc='マーケット']"
    CHART_BY_DESC = "//*[@content-desc='チャート']"
    SPEED_ORDER_BY_DESC = "//*[@content-desc='スピード注文']"
    LOGIN_BY_DESC = "//*[@content-desc='ログイン']"
    WEBSITE_BY_DESC = "//*[@content-desc='ウェブサイト']"
    
    # Bounds selectors for specific positioning
    MENU_BUTTON_BOUNDS = "//android.widget.ImageView[@bounds='[0,143][96,239]']"
    BANNER_BOUNDS = "//android.widget.ImageView[@bounds='[0,300][1080,458]']"
    NOTIFICATIONS_MAIN_BOUNDS = "//android.widget.ImageView[@bounds='[29,606][362,796]']"
    TRANSFER_BOUNDS = "//android.widget.ImageView[@bounds='[29,912][276,1103]']"
    NEW_ORDER_BOUNDS = "//android.widget.ImageView[@bounds='[287,912][534,1103]']"
    SETTLEMENT_ORDER_BOUNDS = "//android.widget.ImageView[@bounds='[546,912][793,1103]']"
    CASH_DELIVERY_BOUNDS = "//android.widget.ImageView[@bounds='[804,912][1051,1103]']"
    SETTINGS_BOUNDS = "//android.widget.ImageView[@bounds='[29,1219][534,1409]']"
    PUSH_NOTIFICATIONS_BOUNDS = "//android.widget.ImageView[@bounds='[546,1219][1051,1409]']"
    ECONOMIC_INDICATORS_BOUNDS = "//android.view.View[@bounds='[29,1420][534,1547]']"
    SWAP_HISTORY_BOUNDS = "//android.view.View[@bounds='[546,1420][1051,1547]']"
    LEVERAGE_SETTINGS_BOUNDS = "//android.view.View[@bounds='[29,1559][534,1685]']"
    TRADING_PERFORMANCE_BOUNDS = "//android.view.View[@bounds='[546,1559][1051,1685]']"
    REQUIRED_MARGIN_BOUNDS = "//android.view.View[@bounds='[29,1697][534,1823]']"
    COMPLIANCE_BOUNDS = "//android.view.View[@bounds='[546,1697][1051,1823]']"
    REPORTS_BOUNDS = "//android.view.View[@bounds='[29,1835][534,1962]']"
    MAIN_SITE_BOUNDS = "//android.widget.ImageView[@bounds='[546,1835][1051,1962]']"
    STOCKS_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[14,2032][185,2136]']"
    US_STOCKS_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[234,2032][406,2136]']"
    FUTURES_OPTIONS_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[454,2032][626,2136]']"
    EXCHANGE_CFD_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[674,2032][846,2136]']"
    INVESTMENT_TRUST_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[895,2032][1066,2136]']"
    MARKET_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[0,2136][180,2274]']"
    CHART_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[180,2136][360,2274]']"
    SPEED_ORDER_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[360,2136][540,2274]']"
    LOGIN_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[540,2136][720,2274]']"
    WEBSITE_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[720,2136][900,2274]']"
    MENU_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[900,2136][1080,2274]']"


class ScreenInfo:
    """Information about current screen"""
    
    SCREEN_NAME = "Navigation Menu (ナビゲーション メニュー)"
    SCREEN_TYPE = "Main Menu"
    SCREEN_RESOLUTION = "1080x2146"
    PACKAGE_NAME = "jp.co.mobileit.SBI_FX"
    TIMESTAMP = "2025-07-25 09:40:30"
    
    # Main sections
    MAIN_SECTIONS = {
        "notifications": {
            "name": "お知らせ",
            "elements": ["お知らせ", "取引関連お知らせ", "キャンペーン"]
        },
        "services": {
            "name": "サービス", 
            "elements": ["振替", "新規注文", "決済注文", "現引"]
        },
        "settings": {
            "name": "設定・その他",
            "elements": ["設定", "プッシュ通知", "経済指標", "スワップ履歴", 
                        "レバレッジ設定", "取引成績", "必要保証金", "コンプライアンス",
                        "報告書", "メインサイト"]
        }
    }
    
    # Bottom navigation tabs
    BOTTOM_TABS = [
        "株", "米国株", "先物OP", "取引所CFD", "投信積立"
    ]
    
    # Main bottom navigation
    MAIN_BOTTOM_NAV = [
        "マーケット", "チャート", "スピード注文", "ログイン", "ウェブサイト", "メニュー"
    ]
    
    # Header elements
    HEADER = {
        "menu_button": "Menu button (top left)",
        "menu_title": "メニュー (Menu title)"
    }
    
    # Screen layout
    LAYOUT = {
        "header": "Menu button and title",
        "banner": "Advertisement banner",
        "notifications": "Notifications section (top)",
        "services": "Trading services section (middle)", 
        "settings": "Settings and other options (bottom)",
        "bottom_tabs": "Product category tabs",
        "main_nav": "Main navigation tabs"
    }
    
    # Navigation structure
    NAVIGATION_STRUCTURE = {
        "level_1": "Main sections (Notifications, Services, Settings)",
        "level_2": "Individual menu items within sections",
        "level_3": "Bottom navigation tabs"
    }


# Usage examples:
if __name__ == "__main__":
    print("=== XPath Objects for Current Screen ===")
    print(f"Screen: {ScreenInfo.SCREEN_NAME}")
    print(f"Screen Type: {ScreenInfo.SCREEN_TYPE}")
    print(f"Resolution: {ScreenInfo.SCREEN_RESOLUTION}")
    print(f"Package: {ScreenInfo.PACKAGE_NAME}")
    print(f"Generated: {ScreenInfo.TIMESTAMP}")
    
    print("\n=== Main Sections ===")
    for section, details in ScreenInfo.MAIN_SECTIONS.items():
        print(f"{section}: {details['name']} - {details['elements']}")
    
    print("\n=== Bottom Navigation Tabs ===")
    for tab in ScreenInfo.BOTTOM_TABS:
        print(f"- {tab}")
    
    print("\n=== Main Bottom Navigation ===")
    for nav in ScreenInfo.MAIN_BOTTOM_NAV:
        print(f"- {nav}")
    
    print("\n=== Available XPath Selectors ===")
    print(f"Menu Button: {CurrentScreenXPaths.MENU_BUTTON}")
    print(f"Notifications Section: {CurrentScreenXPaths.NOTIFICATIONS_SECTION}")
    print(f"Services Section: {CurrentScreenXPaths.SERVICES_SECTION}")
    print(f"Settings Section: {CurrentScreenXPaths.SETTINGS_SECTION}")
    print(f"Chart Tab: {CurrentScreenXPaths.CHART_TAB}")
    print(f"Login Tab: {CurrentScreenXPaths.LOGIN_TAB}") 