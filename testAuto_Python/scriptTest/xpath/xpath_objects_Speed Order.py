# -*- coding: utf-8 -*-
"""
XPath Objects từ màn hình hiện tại
Generated: 2025-07-25 09:56:14
Screen: Speed Order (スピード注文) - USD/JPY Trading Screen
"""

class CurrentScreenXPaths:
    """XPath objects from current screen"""

    # Main container elements
    HIERARCHY = "//hierarchy"
    MAIN_FRAME = "//hierarchy/android.widget.FrameLayout"
    LINEAR_LAYOUT = "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
    CONTENT_FRAME = "//android.widget.FrameLayout[@resource-id='android:id/content']"
    SPEED_ORDER_CONTAINER = "//android.widget.FrameLayout[@pane-title=' ']"
    
    # Main content area
    MAIN_CONTENT = "//android.view.View[@bounds='[0,0][1080,2136]']"
    SPEED_ORDER_VIEW = "//android.view.View[@bounds='[0,0][1080,2136]']"
    
    # Header elements
    BACK_BUTTON = "//android.widget.ImageView[@bounds='[0,134][127,261]']"
    
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
    CHANGE_VALUE = "//android.view.View[@content-desc='+0.482'][@bounds='[730,218][828,256]']"
    
    # Header buttons
    HEADER_BUTTON_1 = "//android.widget.ImageView[@bounds='[844,140][959,255]']"
    TRADING_SETTINGS = "//android.view.View[@content-desc='取引\n設定'][@bounds='[959,151][1051,244]']"
    
    # Timeframe controls
    TICK_BUTTON = "//android.view.View[@content-desc='Tick'][@bounds='[0,267][117,382]']"
    TIMEFRAME_1M = "//android.view.View[@content-desc='1分'][@bounds='[117,267][233,382]']"
    TIMEFRAME_5M = "//android.view.View[@content-desc='5分'][@bounds='[233,267][350,382]']"
    TIMEFRAME_15M = "//android.view.View[@content-desc='15分'][@bounds='[350,267][467,382]']"
    MORE_TIMEFRAMES = "//android.view.View[@content-desc='···'][@bounds='[467,267][583,382]']"
    
    # Trading controls
    BID_TYPE = "//android.view.View[@content-desc='Bid'][@bounds='[606,279][698,372]']"
    DEPOSIT_TRANSFER = "//android.view.View[@content-desc='入金\n振替'][@bounds='[721,279][814,372]']"
    TRADING_BUTTON_1 = "//android.widget.ImageView[@bounds='[837,279][929,372]']"
    TRADING_BUTTON_2 = "//android.widget.ImageView[@bounds='[952,279][1044,372]']"
    
    # Main trading area
    TRADING_AREA = "//android.view.View[@bounds='[0,384][1080,2136]']"
    
    # Chart area
    CHART_AREA = "//android.view.View[@bounds='[0,384][1080,2136]']"
    CHART_BUTTON = "//android.widget.ImageView[@bounds='[12,954][104,1046]']"
    
    # Moving averages section
    MOVING_AVERAGES_CONTAINER = "//android.view.View[@bounds='[23,508][919,545]']"
    MOVING_AVERAGES_LABEL = "//android.view.View[@content-desc='移動平均 '][@bounds='[23,508][133,545]']"
    MA_5_LABEL = "//android.view.View[@content-desc='MA(5) '][@bounds='[133,514][212,545]']"
    MA_25_LABEL = "//android.view.View[@content-desc='MA(25) '][@bounds='[212,514][307,545]']"
    MA_75_LABEL = "//android.view.View[@content-desc='MA(75) '][@bounds='[307,514][401,545]']"
    
    # Trading buttons
    BID_SELL_BUTTON = "//android.view.View[@content-desc='Bid / 売\n147.400'][@bounds='[29,1150][534,1311]']"
    BID_SPREAD = "//android.view.View[@content-desc='0.2'][@bounds='[512,1204][568,1257]']"
    ASK_BUY_BUTTON = "//android.view.View[@content-desc='Ask / 買\n147.402'][@bounds='[546,1150][1051,1311]']"
    
    # Position information
    POSITION_QUANTITY_LABEL = "//android.view.View[@content-desc='建玉数量'][@bounds='[471,1345][609,1387]']"
    AVERAGE_PRICE_LABEL = "//android.view.View[@content-desc='平均建単価'][@bounds='[454,1408][626,1450]']"
    TOTAL_PL_LABEL = "//android.view.View[@content-desc='総合計評価損益'][@bounds='[419,1471][661,1513]']"
    
    # Quantity section
    QUANTITY_LABEL = "//android.view.View[@content-desc='数量'][@bounds='[23,1603][104,1653]']"
    QUANTITY_MINUS_BUTTON = "//android.widget.ImageView[@bounds='[305,1579][403,1677]']"
    QUANTITY_INPUT = "//android.view.View[@bounds='[412,1579][942,1677]']"
    QUANTITY_PLUS_BUTTON = "//android.widget.ImageView[@bounds='[950,1579][1048,1677]']"
    
    # Available quantity
    AVAILABLE_QUANTITY_LABEL = "//android.view.View[@content-desc='注文可能数量(参考)：'][@bounds='[297,1703][675,1753]']"
    
    # Slippage section
    SLIPPAGE_LABEL = "//android.view.View[@content-desc='スリッページ'][@bounds='[23,1839][258,1889]']"
    SLIPPAGE_MINUS_BUTTON = "//android.widget.ImageView[@bounds='[305,1815][403,1913]']"
    SLIPPAGE_INPUT = "//android.view.View[@bounds='[412,1815][798,1913]']"
    SLIPPAGE_PLUS_BUTTON = "//android.widget.ImageView[@bounds='[806,1815][904,1913]']"
    
    # Close all positions
    CLOSE_ALL_POSITIONS = "//android.view.View[@content-desc='全決済'][@bounds='[953,1783][1057,1945]']"
    CLOSE_ALL_BUTTON = "//android.view.View[@bounds='[961,1864][1051,1918]']"
    
    # Trading password
    TRADING_PASSWORD_LABEL = "//android.view.View[@content-desc='取引\nパスワード'][@bounds='[23,1996][297,2075]']"
    TRADING_PASSWORD_INPUT = "//android.view.View[@bounds='[297,1986][815,2076]']"
    TRADING_PASSWORD_BUTTON = "//android.widget.ImageView[@bounds='[815,1973][913,2089]']"
    
    # Save button
    SAVE_BUTTON = "//android.view.View[@content-desc='保存'][@bounds='[913,1950][1057,2112]']"
    SAVE_BUTTON_INNER = "//android.view.View[@bounds='[962,2029][1051,2084]']"
    
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
    BACK_BY_DESC = "//*[@content-desc='Back']"
    USD_JPY_BY_DESC = "//*[@content-desc='米ドル-円']"
    HIGH_BY_DESC = "//*[@content-desc='H']"
    HIGH_PRICE_BY_DESC = "//*[@content-desc='147.494']"
    LOW_BY_DESC = "//*[@content-desc='L']"
    LOW_PRICE_BY_DESC = "//*[@content-desc='146.964']"
    CHANGE_BY_DESC = "//*[@content-desc='前日比']"
    CHANGE_VALUE_BY_DESC = "//*[@content-desc='+0.482']"
    TRADING_SETTINGS_BY_DESC = "//*[@content-desc='取引\n設定']"
    TICK_BY_DESC = "//*[@content-desc='Tick']"
    TIMEFRAME_1M_BY_DESC = "//*[@content-desc='1分']"
    TIMEFRAME_5M_BY_DESC = "//*[@content-desc='5分']"
    TIMEFRAME_15M_BY_DESC = "//*[@content-desc='15分']"
    MORE_TIMEFRAMES_BY_DESC = "//*[@content-desc='···']"
    BID_BY_DESC = "//*[@content-desc='Bid']"
    DEPOSIT_TRANSFER_BY_DESC = "//*[@content-desc='入金\n振替']"
    MOVING_AVERAGES_BY_DESC = "//*[@content-desc='移動平均 ']"
    MA_5_BY_DESC = "//*[@content-desc='MA(5) ']"
    MA_25_BY_DESC = "//*[@content-desc='MA(25) ']"
    MA_75_BY_DESC = "//*[@content-desc='MA(75) ']"
    BID_SELL_BY_DESC = "//*[@content-desc='Bid / 売\n147.400']"
    BID_SPREAD_BY_DESC = "//*[@content-desc='0.2']"
    ASK_BUY_BY_DESC = "//*[@content-desc='Ask / 買\n147.402']"
    POSITION_QUANTITY_BY_DESC = "//*[@content-desc='建玉数量']"
    AVERAGE_PRICE_BY_DESC = "//*[@content-desc='平均建単価']"
    TOTAL_PL_BY_DESC = "//*[@content-desc='総合計評価損益']"
    QUANTITY_BY_DESC = "//*[@content-desc='数量']"
    AVAILABLE_QUANTITY_BY_DESC = "//*[@content-desc='注文可能数量(参考)：']"
    SLIPPAGE_BY_DESC = "//*[@content-desc='スリッページ']"
    CLOSE_ALL_BY_DESC = "//*[@content-desc='全決済']"
    TRADING_PASSWORD_BY_DESC = "//*[@content-desc='取引\nパスワード']"
    SAVE_BY_DESC = "//*[@content-desc='保存']"
    MARKET_BY_DESC = "//*[@content-desc='マーケット']"
    CHART_BY_DESC = "//*[@content-desc='チャート']"
    SPEED_ORDER_BY_DESC = "//*[@content-desc='スピード注文']"
    LOGIN_BY_DESC = "//*[@content-desc='ログイン']"
    WEBSITE_BY_DESC = "//*[@content-desc='ウェブサイト']"
    MENU_BY_DESC = "//*[@content-desc='メニュー']"
    
    # Bounds selectors for specific positioning
    BACK_BUTTON_BOUNDS = "//android.widget.ImageView[@bounds='[0,134][127,261]']"
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
    HEADER_BUTTON_1_BOUNDS = "//android.widget.ImageView[@bounds='[844,140][959,255]']"
    TRADING_SETTINGS_BOUNDS = "//android.view.View[@bounds='[959,151][1051,244]']"
    TICK_BUTTON_BOUNDS = "//android.view.View[@bounds='[0,267][117,382]']"
    TIMEFRAME_1M_BOUNDS = "//android.view.View[@bounds='[117,267][233,382]']"
    TIMEFRAME_5M_BOUNDS = "//android.view.View[@bounds='[233,267][350,382]']"
    TIMEFRAME_15M_BOUNDS = "//android.view.View[@bounds='[350,267][467,382]']"
    MORE_TIMEFRAMES_BOUNDS = "//android.view.View[@bounds='[467,267][583,382]']"
    BID_BOUNDS = "//android.view.View[@bounds='[606,279][698,372]']"
    DEPOSIT_TRANSFER_BOUNDS = "//android.view.View[@bounds='[721,279][814,372]']"
    TRADING_BUTTON_1_BOUNDS = "//android.widget.ImageView[@bounds='[837,279][929,372]']"
    TRADING_BUTTON_2_BOUNDS = "//android.widget.ImageView[@bounds='[952,279][1044,372]']"
    TRADING_AREA_BOUNDS = "//android.view.View[@bounds='[0,384][1080,2136]']"
    CHART_BUTTON_BOUNDS = "//android.widget.ImageView[@bounds='[12,954][104,1046]']"
    MOVING_AVERAGES_CONTAINER_BOUNDS = "//android.view.View[@bounds='[23,508][919,545]']"
    MOVING_AVERAGES_LABEL_BOUNDS = "//android.view.View[@bounds='[23,508][133,545]']"
    MA_5_BOUNDS = "//android.view.View[@bounds='[133,514][212,545]']"
    MA_25_BOUNDS = "//android.view.View[@bounds='[212,514][307,545]']"
    MA_75_BOUNDS = "//android.view.View[@bounds='[307,514][401,545]']"
    BID_SELL_BUTTON_BOUNDS = "//android.view.View[@bounds='[29,1150][534,1311]']"
    BID_SPREAD_BOUNDS = "//android.view.View[@bounds='[512,1204][568,1257]']"
    ASK_BUY_BUTTON_BOUNDS = "//android.view.View[@bounds='[546,1150][1051,1311]']"
    POSITION_QUANTITY_LABEL_BOUNDS = "//android.view.View[@bounds='[471,1345][609,1387]']"
    AVERAGE_PRICE_LABEL_BOUNDS = "//android.view.View[@bounds='[454,1408][626,1450]']"
    TOTAL_PL_LABEL_BOUNDS = "//android.view.View[@bounds='[419,1471][661,1513]']"
    QUANTITY_LABEL_BOUNDS = "//android.view.View[@bounds='[23,1603][104,1653]']"
    QUANTITY_MINUS_BUTTON_BOUNDS = "//android.widget.ImageView[@bounds='[305,1579][403,1677]']"
    QUANTITY_INPUT_BOUNDS = "//android.view.View[@bounds='[412,1579][942,1677]']"
    QUANTITY_PLUS_BUTTON_BOUNDS = "//android.widget.ImageView[@bounds='[950,1579][1048,1677]']"
    AVAILABLE_QUANTITY_LABEL_BOUNDS = "//android.view.View[@bounds='[297,1703][675,1753]']"
    SLIPPAGE_LABEL_BOUNDS = "//android.view.View[@bounds='[23,1839][258,1889]']"
    SLIPPAGE_MINUS_BUTTON_BOUNDS = "//android.widget.ImageView[@bounds='[305,1815][403,1913]']"
    SLIPPAGE_INPUT_BOUNDS = "//android.view.View[@bounds='[412,1815][798,1913]']"
    SLIPPAGE_PLUS_BUTTON_BOUNDS = "//android.widget.ImageView[@bounds='[806,1815][904,1913]']"
    CLOSE_ALL_POSITIONS_BOUNDS = "//android.view.View[@bounds='[953,1783][1057,1945]']"
    CLOSE_ALL_BUTTON_BOUNDS = "//android.view.View[@bounds='[961,1864][1051,1918]']"
    TRADING_PASSWORD_LABEL_BOUNDS = "//android.view.View[@bounds='[23,1996][297,2075]']"
    TRADING_PASSWORD_INPUT_BOUNDS = "//android.view.View[@bounds='[297,1986][815,2076]']"
    TRADING_PASSWORD_BUTTON_BOUNDS = "//android.widget.ImageView[@bounds='[815,1973][913,2089]']"
    SAVE_BUTTON_BOUNDS = "//android.view.View[@bounds='[913,1950][1057,2112]']"
    SAVE_BUTTON_INNER_BOUNDS = "//android.view.View[@bounds='[962,2029][1051,2084]']"
    BOTTOM_NAV_BOUNDS = "//android.view.View[@bounds='[0,2136][1080,2400]']"
    MARKET_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[0,2136][180,2274]']"
    CHART_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[180,2136][360,2274]']"
    SPEED_ORDER_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[360,2136][540,2274]']"
    LOGIN_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[540,2136][720,2274]']"
    WEBSITE_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[720,2136][900,2274]']"
    MENU_TAB_BOUNDS = "//android.widget.ImageView[@bounds='[900,2136][1080,2274]']"


class ScreenInfo:
    """Information about current screen"""
    
    SCREEN_NAME = "Speed Order (スピード注文)"
    SCREEN_TYPE = "USD/JPY Trading Screen"
    SCREEN_RESOLUTION = "1080x2146"
    PACKAGE_NAME = "jp.co.mobileit.SBI_FX"
    TIMESTAMP = "2025-07-25 09:56:14"
    
    # Currency pair information
    CURRENCY_PAIR = {
        "name": "米ドル-円",
        "english": "USD/JPY",
        "current_price": "147.494",
        "high": "147.494",
        "low": "146.964",
        "change": "+0.482",
        "change_label": "前日比"
    }
    
    # Trading controls
    TRADING_CONTROLS = {
        "timeframes": ["Tick", "1分", "5分", "15分", "···"],
        "trading_types": ["Bid", "入金\n振替"],
        "header_buttons": ["Back", "Trading Settings"]
    }
    
    # Moving averages
    MOVING_AVERAGES = [
        "MA(5)",
        "MA(25)", 
        "MA(75)"
    ]
    
    # Trading buttons
    TRADING_BUTTONS = {
        "bid_sell": "Bid / 売\n147.400",
        "ask_buy": "Ask / 買\n147.402",
        "spread": "0.2"
    }
    
    # Position information
    POSITION_INFO = {
        "quantity": "建玉数量 (Position Quantity)",
        "average_price": "平均建単価 (Average Price)",
        "total_pl": "総合計評価損益 (Total P&L)"
    }
    
    # Trading form
    TRADING_FORM = {
        "quantity": "数量 (Quantity)",
        "available_quantity": "注文可能数量(参考) (Available Quantity)",
        "slippage": "スリッページ (Slippage)",
        "trading_password": "取引\nパスワード (Trading Password)",
        "save": "保存 (Save)"
    }
    
    # Action buttons
    ACTION_BUTTONS = {
        "close_all": "全決済 (Close All Positions)",
        "chart": "Chart button"
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
        "header": "Back button, currency pair, price info, trading settings",
        "controls": "Timeframes, trading types, control buttons",
        "chart_area": "Chart with moving averages",
        "trading_form": "Bid/Ask buttons, quantity, slippage, password",
        "bottom_nav": "Main navigation tabs"
    }
    
    # Trading features
    TRADING_FEATURES = {
        "timeframe_selection": "Tick, 1分, 5分, 15分, more options",
        "bid_ask_buttons": "Bid/Sell and Ask/Buy buttons with current prices",
        "quantity_control": "Quantity input with +/- buttons",
        "slippage_control": "Slippage setting with +/- buttons",
        "position_management": "Close all positions button",
        "security": "Trading password required",
        "save_function": "Save trading settings"
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
    
    print(f"\n=== Trading Controls ===")
    print(f"Timeframes: {', '.join(ScreenInfo.TRADING_CONTROLS['timeframes'])}")
    print(f"Trading Types: {', '.join(ScreenInfo.TRADING_CONTROLS['trading_types'])}")
    
    print(f"\n=== Trading Buttons ===")
    print(f"Bid/Sell: {ScreenInfo.TRADING_BUTTONS['bid_sell']}")
    print(f"Ask/Buy: {ScreenInfo.TRADING_BUTTONS['ask_buy']}")
    print(f"Spread: {ScreenInfo.TRADING_BUTTONS['spread']}")
    
    print(f"\n=== Position Information ===")
    for key, value in ScreenInfo.POSITION_INFO.items():
        print(f"- {value}")
    
    print(f"\n=== Trading Form ===")
    for key, value in ScreenInfo.TRADING_FORM.items():
        print(f"- {value}")
    
    print(f"\n=== Action Buttons ===")
    for key, value in ScreenInfo.ACTION_BUTTONS.items():
        print(f"- {value}")
    
    print(f"\n=== Bottom Navigation ===")
    for nav in ScreenInfo.BOTTOM_NAVIGATION:
        print(f"- {nav}")
    
    print("\n=== Available XPath Selectors ===")
    print(f"Back Button: {CurrentScreenXPaths.BACK_BUTTON}")
    print(f"USD/JPY Header: {CurrentScreenXPaths.USD_JPY_HEADER}")
    print(f"Bid/Sell Button: {CurrentScreenXPaths.BID_SELL_BUTTON}")
    print(f"Ask/Buy Button: {CurrentScreenXPaths.ASK_BUY_BUTTON}")
    print(f"Quantity Input: {CurrentScreenXPaths.QUANTITY_INPUT}")
    print(f"Save Button: {CurrentScreenXPaths.SAVE_BUTTON}")
    print(f"Close All Positions: {CurrentScreenXPaths.CLOSE_ALL_POSITIONS}") 