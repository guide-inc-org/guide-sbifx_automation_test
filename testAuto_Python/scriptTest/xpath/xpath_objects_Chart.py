# -*- coding: utf-8 -*-
"""
XPath Objects từ màn hình hiện tại
Generated: 2025-07-25 09:51:35
Screen: Chart (チャート) - USD/JPY Chart Screen
"""

class CurrentScreenXPaths:
    """XPath objects from current screen"""

    # Main container elements
    HIERARCHY = "//hierarchy"
    MAIN_FRAME = "//hierarchy/android.widget.FrameLayout"
    LINEAR_LAYOUT = "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
    CONTENT_FRAME = "//android.widget.FrameLayout[@resource-id='android:id/content']"
    CHART_CONTAINER = "//android.widget.FrameLayout[@pane-title=' ']"
    
    # Main content area
    MAIN_CONTENT = "//android.view.View[@bounds='[0,0][1080,2136]']"
    CHART_VIEW = "//android.view.View[@bounds='[0,0][1080,2136]']"
    
    # Header elements
    ORDER_BUTTON = "//android.view.View[@content-desc='注文'][@bounds='[35,151][230,244]']"
    
    # Currency pair header
    USD_JPY_HEADER = "//android.view.View[@content-desc='米ドル-円'][@bounds='[253,137][827,212]']"
    USD_JPY_ICON_1 = "//android.widget.ImageView[@bounds='[359,137][422,182]']"
    USD_JPY_ICON_2 = "//android.widget.ImageView[@bounds='[370,167][433,212]']"
    USD_JPY_ICON_3 = "//android.widget.ImageView[@bounds='[690,151][721,198]']"
    
    # Price information
    HIGH_LABEL = "//android.view.View[@content-desc='H'][@bounds='[252,216][276,258]']"
    HIGH_PRICE = "//android.view.View[@content-desc='147.494'][@bounds='[288,216][413,258]']"
    LOW_LABEL = "//android.view.View[@content-desc='L'][@bounds='[436,216][455,258]']"
    LOW_PRICE = "//android.view.View[@content-desc='146.964'][@bounds='[467,216][592,258]']"
    CHANGE_LABEL = "//android.view.View[@content-desc='前日比'][@bounds='[615,216][719,258]']"
    CHANGE_VALUE = "//android.view.View[@content-desc='+0.552'][@bounds='[730,218][828,256]']"
    
    # Header buttons
    HEADER_BUTTON_1 = "//android.widget.ImageView[@bounds='[850,140][965,255]']"
    HEADER_BUTTON_2 = "//android.widget.ImageView[@bounds='[965,140][1080,255]']"
    
    # Chart controls
    TIMEFRAME_1M = "//android.view.View[@content-desc='1分足'][@bounds='[35,284][230,377]']"
    BID_TYPE = "//android.view.View[@content-desc='Bid'][@bounds='[245,284][423,377]']"
    ECONOMIC_INDICATORS = "//android.view.View[@content-desc='経済指標'][@bounds='[438,284][726,377]']"
    
    # Chart control buttons
    CHART_BUTTON_1 = "//android.widget.ImageView[@bounds='[740,284][832,377]']"
    CHART_BUTTON_2 = "//android.widget.ImageView[@bounds='[847,284][939,377]']"
    CHART_BUTTON_3 = "//android.widget.ImageView[@bounds='[953,284][1045,377]']"
    
    # Chart area
    CHART_AREA = "//android.view.View[@scrollable='true'][@bounds='[0,394][1080,2136]']"
    
    # Moving averages section
    MOVING_AVERAGES_CONTAINER = "//android.view.View[@bounds='[23,509][919,546]']"
    MOVING_AVERAGES_LABEL = "//android.view.View[@content-desc='移動平均 '][@bounds='[23,509][133,546]']"
    MA_5_LABEL = "//android.view.View[@content-desc='MA(5) '][@bounds='[133,515][212,546]']"
    MA_25_LABEL = "//android.view.View[@content-desc='MA(25) '][@bounds='[212,515][307,546]']"
    MA_75_LABEL = "//android.view.View[@content-desc='MA(75) '][@bounds='[307,515][401,546]']"
    
    # Bottom navigation
    BOTTOM_NAV = "//android.view.View[@bounds='[0,2136][1080,2400]']"
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
    ALL_SCROLLABLE_VIEWS = "//*[@scrollable='true']"
    
    # Content description selectors
    ORDER_BY_DESC = "//*[@content-desc='注文']"
    USD_JPY_BY_DESC = "//*[@content-desc='米ドル-円']"
    HIGH_BY_DESC = "//*[@content-desc='H']"
    HIGH_PRICE_BY_DESC = "//*[@content-desc='147.494']"
    LOW_BY_DESC = "//*[@content-desc='L']"
    LOW_PRICE_BY_DESC = "//*[@content-desc='146.964']"
    CHANGE_BY_DESC = "//*[@content-desc='前日比']"
    CHANGE_VALUE_BY_DESC = "//*[@content-desc='+0.552']"
    TIMEFRAME_1M_BY_DESC = "//*[@content-desc='1分足']"
    BID_BY_DESC = "//*[@content-desc='Bid']"
    ECONOMIC_INDICATORS_BY_DESC = "//*[@content-desc='経済指標']"
    MOVING_AVERAGES_BY_DESC = "//*[@content-desc='移動平均 ']"
    MA_5_BY_DESC = "//*[@content-desc='MA(5) ']"
    MA_25_BY_DESC = "//*[@content-desc='MA(25) ']"
    MA_75_BY_DESC = "//*[@content-desc='MA(75) ']"
    MARKET_BY_DESC = "//*[@content-desc='マーケット']"
    CHART_BY_DESC = "//*[@content-desc='チャート']"
    SPEED_ORDER_BY_DESC = "//*[@content-desc='スピード注文']"
    LOGIN_BY_DESC = "//*[@content-desc='ログイン']"
    WEBSITE_BY_DESC = "//*[@content-desc='ウェブサイト']"
    MENU_BY_DESC = "//*[@content-desc='メニュー']"
    
    # Bounds selectors for specific positioning
    ORDER_BUTTON_BOUNDS = "//android.view.View[@bounds='[35,151][230,244]']"
    USD_JPY_HEADER_BOUNDS = "//android.view.View[@bounds='[253,137][827,212]']"
    USD_JPY_ICON_1_BOUNDS = "//android.widget.ImageView[@bounds='[359,137][422,182]']"
    USD_JPY_ICON_2_BOUNDS = "//android.widget.ImageView[@bounds='[370,167][433,212]']"
    USD_JPY_ICON_3_BOUNDS = "//android.widget.ImageView[@bounds='[690,151][721,198]']"
    HIGH_LABEL_BOUNDS = "//android.view.View[@bounds='[252,216][276,258]']"
    HIGH_PRICE_BOUNDS = "//android.view.View[@bounds='[288,216][413,258]']"
    LOW_LABEL_BOUNDS = "//android.view.View[@bounds='[436,216][455,258]']"
    LOW_PRICE_BOUNDS = "//android.view.View[@bounds='[467,216][592,258]']"
    CHANGE_LABEL_BOUNDS = "//android.view.View[@bounds='[615,216][719,258]']"
    CHANGE_VALUE_BOUNDS = "//android.view.View[@bounds='[730,218][828,256]']"
    HEADER_BUTTON_1_BOUNDS = "//android.widget.ImageView[@bounds='[850,140][965,255]']"
    HEADER_BUTTON_2_BOUNDS = "//android.widget.ImageView[@bounds='[965,140][1080,255]']"
    TIMEFRAME_1M_BOUNDS = "//android.view.View[@bounds='[35,284][230,377]']"
    BID_BOUNDS = "//android.view.View[@bounds='[245,284][423,377]']"
    ECONOMIC_INDICATORS_BOUNDS = "//android.view.View[@bounds='[438,284][726,377]']"
    CHART_BUTTON_1_BOUNDS = "//android.widget.ImageView[@bounds='[740,284][832,377]']"
    CHART_BUTTON_2_BOUNDS = "//android.widget.ImageView[@bounds='[847,284][939,377]']"
    CHART_BUTTON_3_BOUNDS = "//android.widget.ImageView[@bounds='[953,284][1045,377]']"
    CHART_AREA_BOUNDS = "//android.view.View[@bounds='[0,394][1080,2136]']"
    MOVING_AVERAGES_CONTAINER_BOUNDS = "//android.view.View[@bounds='[23,509][919,546]']"
    MOVING_AVERAGES_LABEL_BOUNDS = "//android.view.View[@bounds='[23,509][133,546]']"
    MA_5_BOUNDS = "//android.view.View[@bounds='[133,515][212,546]']"
    MA_25_BOUNDS = "//android.view.View[@bounds='[212,515][307,546]']"
    MA_75_BOUNDS = "//android.view.View[@bounds='[307,515][401,546]']"
    BOTTOM_NAV_BOUNDS = "//android.view.View[@bounds='[0,2136][1080,2400]']"
    MARKET_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[0,2136][180,2274]']"
    CHART_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[180,2136][360,2274]']"
    SPEED_ORDER_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[360,2136][540,2274]']"
    LOGIN_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[540,2136][720,2274]']"
    WEBSITE_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[720,2136][900,2274]']"
    MENU_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[900,2136][1080,2274]']"


class ScreenInfo:
    """Information about current screen"""
    
    SCREEN_NAME = "Chart (チャート)"
    SCREEN_TYPE = "USD/JPY Chart Screen"
    SCREEN_RESOLUTION = "1080x2146"
    PACKAGE_NAME = "jp.co.mobileit.SBI_FX"
    TIMESTAMP = "2025-07-25 09:51:35"
    
    # Currency pair information
    CURRENCY_PAIR = {
        "name": "米ドル-円",
        "english": "USD/JPY",
        "current_price": "147.494",
        "high": "147.494",
        "low": "146.964",
        "change": "+0.552",
        "change_label": "前日比"
    }
    
    # Chart controls
    CHART_CONTROLS = {
        "timeframe": "1分足 (1 minute)",
        "type": "Bid",
        "indicators": "経済指標 (Economic Indicators)"
    }
    
    # Moving averages
    MOVING_AVERAGES = [
        "MA(5)",
        "MA(25)", 
        "MA(75)"
    ]
    
    # Header elements
    HEADER_ELEMENTS = {
        "order_button": "注文 (Order)",
        "currency_pair": "米ドル-円 (USD/JPY)",
        "price_info": "High/Low/Change display",
        "header_buttons": "2 header control buttons"
    }
    
    # Chart area
    CHART_AREA = {
        "main_chart": "Main chart display area",
        "moving_averages": "Moving averages indicator",
        "scrollable": "Scrollable chart content"
    }
    
    # Bottom navigation
    BOTTOM_NAVIGATION = [
        "マーケット (Market)",
        "チャート (Chart)",
        "スピード注文 (Speed Order)",
        "ログイン (Login)",
        "ウェブサイト (Website)",
        "メニュー (Menu)"
    ]
    
    # Screen layout
    LAYOUT = {
        "header": "Order button, currency pair, price info, header buttons",
        "controls": "Timeframe, bid type, economic indicators, chart buttons",
        "chart_area": "Main chart with moving averages",
        "bottom_nav": "Main navigation tabs"
    }
    
    # Chart features
    CHART_FEATURES = {
        "timeframe_selection": "1分足 (1 minute timeframe)",
        "price_type": "Bid price display",
        "technical_indicators": "Economic indicators available",
        "moving_averages": "MA(5), MA(25), MA(75) displayed",
        "price_information": "High, Low, Change values shown"
    }


# Usage examples:
if __name__ == "__main__":
    print("=== XPath Objects for Current Screen ===")
    print(f"Screen: {ScreenInfo.SCREEN_NAME}")
    print(f"Screen Type: {ScreenInfo.SCREEN_TYPE}")
    print(f"Resolution: {ScreenInfo.SCREEN_RESOLUTION}")
    print(f"Package: {ScreenInfo.PACKAGE_NAME}")
    print(f"Generated: {ScreenInfo.TIMESTAMP}")
    
    print(f"\n=== Currency Pair Information ===")
    print(f"Pair: {ScreenInfo.CURRENCY_PAIR['name']} ({ScreenInfo.CURRENCY_PAIR['english']})")
    print(f"Current Price: {ScreenInfo.CURRENCY_PAIR['current_price']}")
    print(f"High: {ScreenInfo.CURRENCY_PAIR['high']}")
    print(f"Low: {ScreenInfo.CURRENCY_PAIR['low']}")
    print(f"Change: {ScreenInfo.CURRENCY_PAIR['change']}")
    
    print(f"\n=== Chart Controls ===")
    print(f"Timeframe: {ScreenInfo.CHART_CONTROLS['timeframe']}")
    print(f"Type: {ScreenInfo.CHART_CONTROLS['type']}")
    print(f"Indicators: {ScreenInfo.CHART_CONTROLS['indicators']}")
    
    print(f"\n=== Moving Averages ===")
    for ma in ScreenInfo.MOVING_AVERAGES:
        print(f"- {ma}")
    
    print(f"\n=== Bottom Navigation ===")
    for nav in ScreenInfo.BOTTOM_NAVIGATION:
        print(f"- {nav}")
    
    print("\n=== Available XPath Selectors ===")
    print(f"Order Button: {CurrentScreenXPaths.ORDER_BUTTON}")
    print(f"USD/JPY Header: {CurrentScreenXPaths.USD_JPY_HEADER}")
    print(f"Current Price: {CurrentScreenXPaths.HIGH_PRICE}")
    print(f"Timeframe 1M: {CurrentScreenXPaths.TIMEFRAME_1M}")
    print(f"Bid Type: {CurrentScreenXPaths.BID_TYPE}")
    print(f"Chart Area: {CurrentScreenXPaths.CHART_AREA}")
    print(f"Moving Averages: {CurrentScreenXPaths.MOVING_AVERAGES_LABEL}") 