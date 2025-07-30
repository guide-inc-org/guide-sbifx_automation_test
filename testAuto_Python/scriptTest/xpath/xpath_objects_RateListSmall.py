# -*- coding: utf-8 -*-
"""
XPath Objects từ màn hình hiện tại
Generated: 2025-07-24 15:43:32
Screen: Rate List (レート一覧) - Tab "レート小"
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
    
    # Sub-tabs
    RATE_SMALL_TAB = "//android.view.View[@content-desc='レート小']"
    RATE_LARGE_TAB = "//android.view.View[@content-desc='レート大']"
    
    # Currency pairs container
    CURRENCY_PAIRS_CONTAINER = "//android.view.View[@content-desc='通貨ペア\n売(Bid)\n買(Ask)']"
    
    # Currency pairs (clickable elements)
    USD_JPY = "//android.view.View[@content-desc='米ドル-円\n146.372\n高値\n146.524\nSW 売/買\n-504/480\n0.2\n146.374\n安値\n145.856\n前日比\n-0.092']"
    EUR_JPY = "//android.view.View[@content-desc='ユーロ-円\n172.199\n高値\n172.506\nSW 売/買\n-351/321\n0.5\n172.204\n安値\n171.751\n前日比\n-0.227']"
    GBP_JPY = "//android.view.View[@content-desc='ポンド-円\n198.347\n高値\n199.015\nSW 売/買\n-657/627\n0.9\n198.356\n安値\n198.137\n前日比\n-0.567']"
    AUD_JPY = "//android.view.View[@content-desc='豪ドル-円\n96.847\n高値\n96.880\nSW 売/買\n-300/270\n0.6\n96.853\n安値\n96.397\n前日比\n+0.162']"
    MXN_JPY = "//android.view.View[@content-desc='ﾒｷｼｺﾍﾟｿ-円\n7.894\n高値\n7.903\nSW 売/買\n-60/45\n0.3\n7.897\n安値\n7.867\n前日比\n-0.005']"
    ZAR_JPY = "//android.view.View[@content-desc='南アランド-円\n8.315\n高値\n8.364\nSW 売/買\n-51/42\n0.9\n8.324\n安値\n8.308\n前日比\n-0.038']"
    TRY_JPY = "//android.view.View[@content-desc='トルコリラ-円\n3.592\n高値\n3.620\nSW 売/買\n-141/96\n2.8\n3.620\n安値\n3.597\n前日比\n-0.014']"
    
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
    USD_JPY_BOUNDS = "//android.view.View[@bounds='[0,562][1080,793]']"
    EUR_JPY_BOUNDS = "//android.view.View[@bounds='[0,798][1080,1028]']"
    GBP_JPY_BOUNDS = "//android.view.View[@bounds='[0,1033][1080,1264]']"
    AUD_JPY_BOUNDS = "//android.view.View[@bounds='[0,1269][1080,1499]']"
    MXN_JPY_BOUNDS = "//android.view.View[@bounds='[0,1504][1080,1735]']"
    ZAR_JPY_BOUNDS = "//android.view.View[@bounds='[0,1740][1080,1970]']"
    TRY_JPY_BOUNDS = "//android.view.View[@bounds='[0,1975][1080,2040]']"
    
    # Tab selectors by bounds
    RATE_TAB_BOUNDS = "//android.view.View[@bounds='[0,200][270,315]']"
    SWAP_TAB_BOUNDS = "//android.view.View[@bounds='[270,200][540,315]']"
    NEWS_TAB_BOUNDS = "//android.view.View[@bounds='[540,200][810,315]']"
    ECONOMIC_TAB_BOUNDS = "//android.view.View[@bounds='[810,200][1080,315]']"
    
    # Sub-tab selectors by bounds
    RATE_SMALL_TAB_BOUNDS = "//android.view.View[@bounds='[37,347][540,445]']"
    RATE_LARGE_TAB_BOUNDS = "//android.view.View[@bounds='[540,347][1043,445]']"
    
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
    
    # Tab selectors by partial content-desc
    RATE_TAB_BY_DESC = "//*[contains(@content-desc, 'レート\nタブ: 1/4')]"
    SWAP_TAB_BY_DESC = "//*[contains(@content-desc, 'スワップ\nタブ: 2/4')]"
    NEWS_TAB_BY_DESC = "//*[contains(@content-desc, 'ニュース\nタブ: 3/4')]"
    ECONOMIC_TAB_BY_DESC = "//*[contains(@content-desc, '経済指標\nタブ: 4/4')]"
    
    # Sub-tab selectors by partial content-desc
    RATE_SMALL_BY_DESC = "//*[contains(@content-desc, 'レート小')]"
    RATE_LARGE_BY_DESC = "//*[contains(@content-desc, 'レート大')]"


class ScreenInfo:
    """Information about current screen"""
    
    SCREEN_NAME = "Rate List (レート一覧)"
    CURRENT_TAB = "レート小"
    SCREEN_RESOLUTION = "1080x2106"
    PACKAGE_NAME = "jp.co.mobileit.SBI_FX"
    TIMESTAMP = "2025-07-24 15:43:32"
    
    # Current rates
    CURRENT_RATES = {
        "USD/JPY": "146.372",
        "EUR/JPY": "172.199", 
        "GBP/JPY": "198.347",
        "AUD/JPY": "96.847",
        "MXN/JPY": "7.894",
        "ZAR/JPY": "8.315",
        "TRY/JPY": "3.592"
    }
    
    # Available tabs
    MAIN_TABS = ["レート", "スワップ", "ニュース", "経済指標"]
    SUB_TABS = ["レート小", "レート大"]
    
    # Bottom navigation
    BOTTOM_NAV = ["マーケット", "チャート", "スピード注文", "ログイン", "ウェブサイト", "メニュー"]


# Usage examples:
if __name__ == "__main__":
    print("=== XPath Objects for Current Screen ===")
    print(f"Screen: {ScreenInfo.SCREEN_NAME}")
    print(f"Current Tab: {ScreenInfo.CURRENT_TAB}")
    print(f"Resolution: {ScreenInfo.SCREEN_RESOLUTION}")
    print(f"Package: {ScreenInfo.PACKAGE_NAME}")
    print(f"Generated: {ScreenInfo.TIMESTAMP}")
    
    print("\n=== Current Rates ===")
    for pair, rate in ScreenInfo.CURRENT_RATES.items():
        print(f"{pair}: {rate}")
    
    print("\n=== Available XPath Selectors ===")
    print(f"Market Button: {CurrentScreenXPaths.MARKET_BUTTON}")
    print(f"USD/JPY: {CurrentScreenXPaths.USD_JPY}")
    print(f"Rate Tab: {CurrentScreenXPaths.RATE_TAB}")
    print(f"Bottom Chart: {CurrentScreenXPaths.BOTTOM_CHART}") 