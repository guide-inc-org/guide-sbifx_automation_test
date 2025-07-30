# -*- coding: utf-8 -*-
"""
XPath Objects từ màn hình hiện tại
Generated: 2025-07-24 15:57:06
Screen: Economic Indicators (経済指標) - Tab "経済指標"
"""

class CurrentScreenXPaths:
    """XPath objects from current screen"""

    # Main container elements
    HIERARCHY = "//hierarchy"
    MAIN_FRAME = "//hierarchy/android.widget.FrameLayout"
    LINEAR_LAYOUT = "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
    CONTENT_FRAME = "//android.widget.FrameLayout[@resource-id='android:id/content']"
    INNER_FRAME = "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout"
    
    # Header elements
    MARKET_BUTTON = "//android.view.View[@content-desc='マーケット']"
    SETTINGS_ICON = "//android.widget.ImageView[@bounds='[976,90][1068,182]']"
    
    # Main tab navigation
    RATE_TAB = "//android.view.View[@content-desc='レート\nタブ: 1/4']"
    SWAP_TAB = "//android.view.View[@content-desc='スワップ\nタブ: 2/4']"
    NEWS_TAB = "//android.view.View[@content-desc='ニュース\nタブ: 3/4']"
    ECONOMIC_INDICATORS_TAB = "//android.view.View[@content-desc='経済指標\nタブ: 4/4']"
    
    # Date range header
    DATE_RANGE_HEADER = "//android.view.View[@content-desc='2025/07/18\n(金)\n〜\n2025/07/24\n(木)']"
    
    # Date picker elements
    DATE_PICKER_ICON = "//android.widget.ImageView[@bounds='[942,338][1045,442]']"
    CALENDAR_ICON = "//android.widget.ImageView[@bounds='[0,465][130,569]']"
    
    # Date elements
    YEAR_LABEL = "//android.view.View[@content-desc='年']"
    MONTH_LABEL = "//android.view.View[@content-desc='月']"
    YEAR_VALUE = "//android.view.View[@content-desc='2025']"
    MONTH_VALUE = "//android.view.View[@content-desc='7']"
    DAY_VALUE = "//android.view.View[@content-desc='24']"
    DAY_LABEL = "//android.view.View[@content-desc='日(木)']"
    
    # Economic indicators
    INDICATOR_1 = "//android.widget.ImageView[@content-desc='15:00\nドイツ\nGFK消費者信頼感調査\n前回\n-20.3\n予想\n-19.3\n結果\n-21.5']"
    INDICATOR_2 = "//android.widget.ImageView[@content-desc='15:45\nフランス\n企業景況感指数[季調済]\n前回\n96⇒97\n予想\n97\n結果\n96']"
    INDICATOR_3 = "//android.widget.ImageView[@content-desc='15:45\nフランス\n生産アウトルック指数\n前回\n-13⇒-12\n予想\n-12\n結果\n-12']"
    INDICATOR_4 = "//android.view.View[@content-desc='16:15\nフランス\n製造業PMI\n前回\n48.1\n予想\n48.5\n結果\n48.4']"
    INDICATOR_5 = "//android.view.View[@content-desc='16:15\nフランス\n非製造業PMI\n前回\n49.6\n予想\n49.6\n結果\n49.7']"
    INDICATOR_6 = "//android.view.View[@content-desc='16:30\nドイツ\n製造業PMI\n前回\n49.0\n予想\n49.5\n結果\n49.2']"
    
    # Bottom navigation
    BOTTOM_MARKET = "//android.widget.ImageView[@content-desc='マーケット']"
    BOTTOM_CHART = "//android.widget.ImageView[@content-desc='チャート']"
    BOTTOM_SPEED_ORDER = "//android.widget.ImageView[@content-desc='スピード注文']"
    BOTTOM_LOGIN = "//android.widget.ImageView[@content-desc='ログイン']"
    BOTTOM_WEBSITE = "//android.widget.ImageView[@content-desc='ウェブサイト']"
    BOTTOM_MENU = "//android.widget.ImageView[@content-desc='メニュー']"
    
    # Generic selectors
    ALL_CLICKABLE_ELEMENTS = "//*[@clickable='true' or @enabled='true']"
    ALL_VIEWS = "//android.view.View"
    ALL_IMAGEVIEWS = "//android.widget.ImageView"
    
    # Specific element selectors by bounds
    INDICATOR_1_BOUNDS = "//android.widget.ImageView[@bounds='[0,465][1080,574]']"
    INDICATOR_2_BOUNDS = "//android.widget.ImageView[@bounds='[0,574][1080,885]']"
    INDICATOR_3_BOUNDS = "//android.widget.ImageView[@bounds='[0,885][1080,1196]']"
    INDICATOR_4_BOUNDS = "//android.view.View[@bounds='[0,1196][1080,1507]']"
    INDICATOR_5_BOUNDS = "//android.view.View[@bounds='[0,1507][1080,1818]']"
    INDICATOR_6_BOUNDS = "//android.view.View[@bounds='[0,1818][1080,2040]']"
    
    # Tab selectors by bounds
    RATE_TAB_BOUNDS = "//android.view.View[@bounds='[0,200][270,315]']"
    SWAP_TAB_BOUNDS = "//android.view.View[@bounds='[270,200][540,315]']"
    NEWS_TAB_BOUNDS = "//android.view.View[@bounds='[540,200][810,315]']"
    ECONOMIC_TAB_BOUNDS = "//android.view.View[@bounds='[810,200][1080,315]']"
    
    # Date elements by bounds
    YEAR_LABEL_BOUNDS = "//android.view.View[@bounds='[445,488][491,546]']"
    MONTH_LABEL_BOUNDS = "//android.view.View[@bounds='[517,488][563,546]']"
    YEAR_VALUE_BOUNDS = "//android.view.View[@bounds='[342,490][445,544]']"
    MONTH_VALUE_BOUNDS = "//android.view.View[@bounds='[491,490][517,544]']"
    DAY_VALUE_BOUNDS = "//android.view.View[@bounds='[563,490][615,544]']"
    DAY_LABEL_BOUNDS = "//android.view.View[@bounds='[615,488][738,546]']"
    
    # Bottom navigation by bounds
    BOTTOM_MARKET_BOUNDS = "//android.widget.ImageView[@bounds='[0,2040][180,2178]']"
    BOTTOM_CHART_BOUNDS = "//android.widget.ImageView[@bounds='[180,2040][360,2178]']"
    BOTTOM_SPEED_ORDER_BOUNDS = "//android.widget.ImageView[@bounds='[360,2040][540,2178]']"
    BOTTOM_LOGIN_BOUNDS = "//android.widget.ImageView[@bounds='[540,2040][720,2178]']"
    BOTTOM_WEBSITE_BOUNDS = "//android.widget.ImageView[@bounds='[720,2040][900,2178]']"
    BOTTOM_MENU_BOUNDS = "//android.widget.ImageView[@bounds='[900,2040][1080,2178]']"
    
    # Content description selectors
    MARKET_BY_DESC = "//*[@content-desc='マーケット']"
    CHART_BY_DESC = "//*[@content-desc='チャート']"
    SPEED_ORDER_BY_DESC = "//*[@content-desc='スピード注文']"
    LOGIN_BY_DESC = "//*[@content-desc='ログイン']"
    WEBSITE_BY_DESC = "//*[@content-desc='ウェブサイト']"
    MENU_BY_DESC = "//*[@content-desc='メニュー']"
    
    # Tab selectors by partial content-desc
    RATE_TAB_BY_DESC = "//*[contains(@content-desc, 'レート\nタブ: 1/4')]"
    SWAP_TAB_BY_DESC = "//*[contains(@content-desc, 'スワップ\nタブ: 2/4')]"
    NEWS_TAB_BY_DESC = "//*[contains(@content-desc, 'ニュース\nタブ: 3/4')]"
    ECONOMIC_TAB_BY_DESC = "//*[contains(@content-desc, '経済指標\nタブ: 4/4')]"
    
    # Economic indicator selectors by partial content-desc
    INDICATOR_1_BY_DESC = "//*[contains(@content-desc, 'GFK消費者信頼感調査')]"
    INDICATOR_2_BY_DESC = "//*[contains(@content-desc, '企業景況感指数')]"
    INDICATOR_3_BY_DESC = "//*[contains(@content-desc, '生産アウトルック指数')]"
    INDICATOR_4_BY_DESC = "//*[contains(@content-desc, 'フランス\n製造業PMI')]"
    INDICATOR_5_BY_DESC = "//*[contains(@content-desc, 'フランス\n非製造業PMI')]"
    INDICATOR_6_BY_DESC = "//*[contains(@content-desc, 'ドイツ\n製造業PMI')]"
    
    # Date selectors by partial content-desc
    YEAR_BY_DESC = "//*[contains(@content-desc, '年')]"
    MONTH_BY_DESC = "//*[contains(@content-desc, '月')]"
    DAY_BY_DESC = "//*[contains(@content-desc, '日')]"


class ScreenInfo:
    """Information about current screen"""
    
    SCREEN_NAME = "Economic Indicators (経済指標)"
    CURRENT_TAB = "経済指標"
    SCREEN_RESOLUTION = "1080x2106"
    PACKAGE_NAME = "jp.co.mobileit.SBI_FX"
    TIMESTAMP = "2025-07-24 15:57:06"
    
    # Current economic indicators data
    ECONOMIC_INDICATORS = {
        "indicator_1": {
            "time": "15:00",
            "country": "ドイツ",
            "name": "GFK消費者信頼感調査",
            "previous": "-20.3",
            "forecast": "-19.3",
            "result": "-21.5"
        },
        "indicator_2": {
            "time": "15:45",
            "country": "フランス",
            "name": "企業景況感指数[季調済]",
            "previous": "96⇒97",
            "forecast": "97",
            "result": "96"
        },
        "indicator_3": {
            "time": "15:45",
            "country": "フランス",
            "name": "生産アウトルック指数",
            "previous": "-13⇒-12",
            "forecast": "-12",
            "result": "-12"
        },
        "indicator_4": {
            "time": "16:15",
            "country": "フランス",
            "name": "製造業PMI",
            "previous": "48.1",
            "forecast": "48.5",
            "result": "48.4"
        },
        "indicator_5": {
            "time": "16:15",
            "country": "フランス",
            "name": "非製造業PMI",
            "previous": "49.6",
            "forecast": "49.6",
            "result": "49.7"
        },
        "indicator_6": {
            "time": "16:30",
            "country": "ドイツ",
            "name": "製造業PMI",
            "previous": "49.0",
            "forecast": "49.5",
            "result": "49.2"
        }
    }
    
    # Available tabs
    MAIN_TABS = ["レート", "スワップ", "ニュース", "経済指標"]
    
    # Bottom navigation
    BOTTOM_NAV = ["マーケット", "チャート", "スピード注文", "ログイン", "ウェブサイト", "メニュー"]
    
    # Date information
    DATE_RANGE = "2025/07/18 (金) 〜 2025/07/24 (木)"
    CURRENT_DATE = "2025/07/24 (木)"
    
    # Countries
    COUNTRIES = ["ドイツ", "フランス"]
    
    # Indicator types
    INDICATOR_TYPES = ["消費者信頼感調査", "企業景況感指数", "生産アウトルック指数", "製造業PMI", "非製造業PMI"]


# Usage examples:
if __name__ == "__main__":
    print("=== XPath Objects for Current Screen ===")
    print(f"Screen: {ScreenInfo.SCREEN_NAME}")
    print(f"Current Tab: {ScreenInfo.CURRENT_TAB}")
    print(f"Resolution: {ScreenInfo.SCREEN_RESOLUTION}")
    print(f"Package: {ScreenInfo.PACKAGE_NAME}")
    print(f"Generated: {ScreenInfo.TIMESTAMP}")
    print(f"Date Range: {ScreenInfo.DATE_RANGE}")
    
    print("\n=== Current Economic Indicators ===")
    for key, indicator in ScreenInfo.ECONOMIC_INDICATORS.items():
        print(f"{key}: {indicator['time']} - {indicator['country']} - {indicator['name']}")
        print(f"  Previous: {indicator['previous']}, Forecast: {indicator['forecast']}, Result: {indicator['result']}")
    
    print("\n=== Available XPath Selectors ===")
    print(f"Market Button: {CurrentScreenXPaths.MARKET_BUTTON}")
    print(f"Economic Indicators Tab: {CurrentScreenXPaths.ECONOMIC_INDICATORS_TAB}")
    print(f"Date Range Header: {CurrentScreenXPaths.DATE_RANGE_HEADER}")
    print(f"First Indicator: {CurrentScreenXPaths.INDICATOR_1}")
    print(f"Bottom Menu: {CurrentScreenXPaths.BOTTOM_MENU}") 