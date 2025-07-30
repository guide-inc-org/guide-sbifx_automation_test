# -*- coding: utf-8 -*-
"""
XPath Objects từ màn hình hiện tại
Generated: 2025-07-24 15:47:26
Screen: Swap (スワップ) - Tab "スワップ"
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
    
    # Swap data header
    SWAP_HEADER = "//android.widget.ImageView[@content-desc='2025/07/23\n(水)\n通貨ペア\n売スワップ\n買スワップ\n日数']"
    
    # Currency pairs with swap data
    USD_JPY_SWAP = "//android.view.View[@content-desc='米ドル-円\n-504\n+480\n3']"
    EUR_JPY_SWAP = "//android.view.View[@content-desc='ユーロ-円\n-351\n+321\n3']"
    GBP_JPY_SWAP = "//android.view.View[@content-desc='ポンド-円\n-657\n+627\n3']"
    AUD_JPY_SWAP = "//android.view.View[@content-desc='豪ドル-円\n-300\n+270\n3']"
    MXN_JPY_SWAP = "//android.view.View[@content-desc='ﾒｷｼｺﾍﾟｿ-円\n-60\n+45\n3']"
    ZAR_JPY_SWAP = "//android.view.View[@content-desc='南アランド-円\n-51\n+42\n3']"
    TRY_JPY_SWAP = "//android.view.View[@content-desc='トルコリラ-円\n-141\n+96\n3']"
    NZD_JPY_SWAP = "//android.view.View[@content-desc='ＮＺドル-円\n-222\n+192\n3']"
    EUR_USD_SWAP = "//android.view.View[@content-desc='ユーロ-米ドル\n+318\n-333\n3']"
    
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
    USD_JPY_SWAP_BOUNDS = "//android.view.View[@bounds='[0,551][1080,712]']"
    EUR_JPY_SWAP_BOUNDS = "//android.view.View[@bounds='[0,717][1080,879]']"
    GBP_JPY_SWAP_BOUNDS = "//android.view.View[@bounds='[0,884][1080,1045]']"
    AUD_JPY_SWAP_BOUNDS = "//android.view.View[@bounds='[0,1050][1080,1211]']"
    MXN_JPY_SWAP_BOUNDS = "//android.view.View[@bounds='[0,1216][1080,1378]']"
    ZAR_JPY_SWAP_BOUNDS = "//android.view.View[@bounds='[0,1383][1080,1544]']"
    TRY_JPY_SWAP_BOUNDS = "//android.view.View[@bounds='[0,1549][1080,1710]']"
    NZD_JPY_SWAP_BOUNDS = "//android.view.View[@bounds='[0,1715][1080,1877]']"
    EUR_USD_SWAP_BOUNDS = "//android.view.View[@bounds='[0,1882][1080,2040]']"
    
    # Tab selectors by bounds
    RATE_TAB_BOUNDS = "//android.view.View[@bounds='[0,200][270,315]']"
    SWAP_TAB_BOUNDS = "//android.view.View[@bounds='[270,200][540,315]']"
    NEWS_TAB_BOUNDS = "//android.view.View[@bounds='[540,200][810,315]']"
    ECONOMIC_TAB_BOUNDS = "//android.view.View[@bounds='[810,200][1080,315]']"
    
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
    
    # Currency pair selectors by partial content-desc
    USD_JPY_BY_DESC = "//*[contains(@content-desc, '米ドル-円')]"
    EUR_JPY_BY_DESC = "//*[contains(@content-desc, 'ユーロ-円')]"
    GBP_JPY_BY_DESC = "//*[contains(@content-desc, 'ポンド-円')]"
    AUD_JPY_BY_DESC = "//*[contains(@content-desc, '豪ドル-円')]"
    MXN_JPY_BY_DESC = "//*[contains(@content-desc, 'ﾒｷｼｺﾍﾟｿ-円')]"
    ZAR_JPY_BY_DESC = "//*[contains(@content-desc, '南アランド-円')]"
    TRY_JPY_BY_DESC = "//*[contains(@content-desc, 'トルコリラ-円')]"
    NZD_JPY_BY_DESC = "//*[contains(@content-desc, 'ＮＺドル-円')]"
    EUR_USD_BY_DESC = "//*[contains(@content-desc, 'ユーロ-米ドル')]"
    
    # Tab selectors by partial content-desc
    RATE_TAB_BY_DESC = "//*[contains(@content-desc, 'レート\nタブ: 1/4')]"
    SWAP_TAB_BY_DESC = "//*[contains(@content-desc, 'スワップ\nタブ: 2/4')]"
    NEWS_TAB_BY_DESC = "//*[contains(@content-desc, 'ニュース\nタブ: 3/4')]"
    ECONOMIC_TAB_BY_DESC = "//*[contains(@content-desc, '経済指標\nタブ: 4/4')]"


class ScreenInfo:
    """Information about current screen"""
    
    SCREEN_NAME = "Swap (スワップ)"
    CURRENT_TAB = "スワップ"
    SCREEN_RESOLUTION = "1080x2106"
    PACKAGE_NAME = "jp.co.mobileit.SBI_FX"
    TIMESTAMP = "2025-07-24 15:47:26"
    
    # Current swap data
    SWAP_DATA = {
        "USD/JPY": {"sell": "-504", "buy": "+480", "days": "3"},
        "EUR/JPY": {"sell": "-351", "buy": "+321", "days": "3"},
        "GBP/JPY": {"sell": "-657", "buy": "+627", "days": "3"},
        "AUD/JPY": {"sell": "-300", "buy": "+270", "days": "3"},
        "MXN/JPY": {"sell": "-60", "buy": "+45", "days": "3"},
        "ZAR/JPY": {"sell": "-51", "buy": "+42", "days": "3"},
        "TRY/JPY": {"sell": "-141", "buy": "+96", "days": "3"},
        "NZD/JPY": {"sell": "-222", "buy": "+192", "days": "3"},
        "EUR/USD": {"sell": "+318", "buy": "-333", "days": "3"}
    }
    
    # Available tabs
    MAIN_TABS = ["レート", "スワップ", "ニュース", "経済指標"]
    
    # Bottom navigation
    BOTTOM_NAV = ["マーケット", "チャート", "スピード注文", "ログイン", "ウェブサイト", "メニュー"]
    
    # Date information
    SWAP_DATE = "2025/07/23"
    SWAP_DAY = "水"  # Wednesday


# Usage examples:
if __name__ == "__main__":
    print("=== XPath Objects for Current Screen ===")
    print(f"Screen: {ScreenInfo.SCREEN_NAME}")
    print(f"Current Tab: {ScreenInfo.CURRENT_TAB}")
    print(f"Resolution: {ScreenInfo.SCREEN_RESOLUTION}")
    print(f"Package: {ScreenInfo.PACKAGE_NAME}")
    print(f"Generated: {ScreenInfo.TIMESTAMP}")
    print(f"Swap Date: {ScreenInfo.SWAP_DATE} ({ScreenInfo.SWAP_DAY})")
    
    print("\n=== Current Swap Data ===")
    for pair, data in ScreenInfo.SWAP_DATA.items():
        print(f"{pair}: Sell {data['sell']}, Buy {data['buy']}, Days {data['days']}")
    
    print("\n=== Available XPath Selectors ===")
    print(f"Market Button: {CurrentScreenXPaths.MARKET_BUTTON}")
    print(f"Swap Tab: {CurrentScreenXPaths.SWAP_TAB}")
    print(f"USD/JPY Swap: {CurrentScreenXPaths.USD_JPY_SWAP}")
    print(f"Bottom Menu: {CurrentScreenXPaths.BOTTOM_MENU}") 