# -*- coding: utf-8 -*-
"""
XPath Objects từ màn hình Chart Multi
Generated: 2025-07-24 16:30:00
Screen: Chart (チャート) - Multi Chart View
"""

class ChartMultiXPaths:
    """XPath objects from Chart Multi screen"""

    # Main container elements
    HIERARCHY = "//hierarchy"
    MAIN_FRAME = "//hierarchy/android.widget.FrameLayout"
    LINEAR_LAYOUT = "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
    CONTENT_FRAME = "//android.widget.FrameLayout[@resource-id='android:id/content']"
    INNER_FRAME = "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout"
    
    # Header elements
    CHART_TITLE = "//android.view.View[@content-desc='チャート1']"
    CHART_SUBTITLE = "//android.view.View[@bounds='[451,158][629,182]']"
    
    # Header icons
    HEADER_ICON_1 = "//android.widget.ImageView[@bounds='[838,79][953,194]']"
    HEADER_ICON_2 = "//android.widget.ImageView[@bounds='[953,73][1080,199]']"
    
    # Chart areas
    CHART_AREA_1 = "//android.view.View[@content-desc='豪ドル-円\n1分足\nBid'][@bounds='[0,200][540,1082]']"
    CHART_AREA_2 = "//android.view.View[@content-desc='豪ドル-円\n1分足\nBid'][@bounds='[540,200][1080,1082]']"
    CHART_AREA_3 = "//android.view.View[@content-desc='ポンド-円\n1分足\nBid']"
    CHART_AREA_4 = "//android.view.View[@content-desc='豪ドル-円\n1分足\nBid'][@bounds='[540,1082][1080,1962]']"
    
    # Chart currency pairs
    AUD_JPY_CHART_1 = "//android.view.View[@content-desc='豪ドル-円\n1分足\nBid'][@bounds='[0,200][540,1082]']"
    AUD_JPY_CHART_2 = "//android.view.View[@content-desc='豪ドル-円\n1分足\nBid'][@bounds='[540,200][1080,1082]']"
    GBP_JPY_CHART = "//android.view.View[@content-desc='ポンド-円\n1分足\nBid']"
    AUD_JPY_CHART_3 = "//android.view.View[@content-desc='豪ドル-円\n1分足\nBid'][@bounds='[540,1082][1080,1962]']"
    
    # Chart icons within currency pairs
    AUD_JPY_ICON_1 = "//android.widget.ImageView[@bounds='[23,218][86,261]']"
    AUD_JPY_ICON_2 = "//android.widget.ImageView[@bounds='[35,249][98,292]']"
    AUD_JPY_ICON_3 = "//android.widget.ImageView[@bounds='[563,218][626,261]']"
    AUD_JPY_ICON_4 = "//android.widget.ImageView[@bounds='[575,249][638,292]']"
    GBP_JPY_ICON_1 = "//android.widget.ImageView[@bounds='[23,1099][86,1143]']"
    GBP_JPY_ICON_2 = "//android.widget.ImageView[@bounds='[35,1130][98,1174]']"
    AUD_JPY_ICON_5 = "//android.widget.ImageView[@bounds='[563,1099][626,1143]']"
    AUD_JPY_ICON_6 = "//android.widget.ImageView[@bounds='[575,1130][638,1174]']"
    
    # Timestamp
    TIMESTAMP = "//android.view.View[@content-desc='25/07/24 16:25:31']"
    
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
    CHART_SUBTITLE_BOUNDS = "//android.view.View[@bounds='[451,158][629,182]']"
    HEADER_ICON_1_BOUNDS = "//android.widget.ImageView[@bounds='[838,79][953,194]']"
    HEADER_ICON_2_BOUNDS = "//android.widget.ImageView[@bounds='[953,73][1080,199]']"
    AUD_JPY_CHART_1_BOUNDS = "//android.view.View[@bounds='[0,200][540,1082]']"
    AUD_JPY_CHART_2_BOUNDS = "//android.view.View[@bounds='[540,200][1080,1082]']"
    GBP_JPY_CHART_BOUNDS = "//android.view.View[@bounds='[0,1082][540,1962]']"
    AUD_JPY_CHART_3_BOUNDS = "//android.view.View[@bounds='[540,1082][1080,1962]']"
    TIMESTAMP_BOUNDS = "//android.view.View[@bounds='[770,1979][1057,2023]']"
    
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
    
    # Chart selectors by partial content-desc
    CHART_TITLE_BY_DESC = "//*[contains(@content-desc, 'チャート1')]"
    AUD_JPY_BY_DESC = "//*[contains(@content-desc, '豪ドル-円')]"
    GBP_JPY_BY_DESC = "//*[contains(@content-desc, 'ポンド-円')]"
    TIMESTAMP_BY_DESC = "//*[contains(@content-desc, '25/07/24')]"
    
    # Chart timeframes
    ONE_MINUTE_BY_DESC = "//*[contains(@content-desc, '1分足')]"
    BID_BY_DESC = "//*[contains(@content-desc, 'Bid')]"


class ChartMultiInfo:
    """Information about Chart Multi screen"""
    
    SCREEN_NAME = "Chart Multi (チャート)"
    CHART_TITLE = "チャート1"
    SCREEN_RESOLUTION = "1080x2106"
    PACKAGE_NAME = "jp.co.mobileit.SBI_FX"
    TIMESTAMP = "2025-07-24 16:30:00"
    
    # Current chart data
    CHARTS = {
        "chart_1": {
            "currency_pair": "豪ドル-円 (AUD/JPY)",
            "timeframe": "1分足",
            "type": "Bid",
            "bounds": "[0,200][540,1082]",
            "position": "Top Left"
        },
        "chart_2": {
            "currency_pair": "豪ドル-円 (AUD/JPY)",
            "timeframe": "1分足",
            "type": "Bid",
            "bounds": "[540,200][1080,1082]",
            "position": "Top Right"
        },
        "chart_3": {
            "currency_pair": "ポンド-円 (GBP/JPY)",
            "timeframe": "1分足",
            "type": "Bid",
            "bounds": "[0,1082][540,1962]",
            "position": "Bottom Left"
        },
        "chart_4": {
            "currency_pair": "豪ドル-円 (AUD/JPY)",
            "timeframe": "1分足",
            "type": "Bid",
            "bounds": "[540,1082][1080,1962]",
            "position": "Bottom Right"
        }
    }
    
    # Bottom navigation
    BOTTOM_NAV = ["マーケット", "チャート", "スピード注文", "ログイン", "ウェブサイト", "メニュー"]
    
    # Chart information
    CURRENT_TIMESTAMP = "25/07/24 16:25:31"
    CHART_LAYOUT = "2x2 Grid"
    
    # Currency pairs displayed
    CURRENCY_PAIRS = ["豪ドル-円 (AUD/JPY)", "ポンド-円 (GBP/JPY)"]
    
    # Chart timeframes
    TIMEFRAMES = ["1分足"]
    
    # Chart types
    CHART_TYPES = ["Bid"]


# Usage examples:
if __name__ == "__main__":
    print("=== XPath Objects for Chart Multi Screen ===")
    print(f"Screen: {ChartMultiInfo.SCREEN_NAME}")
    print(f"Chart Title: {ChartMultiInfo.CHART_TITLE}")
    print(f"Resolution: {ChartMultiInfo.SCREEN_RESOLUTION}")
    print(f"Package: {ChartMultiInfo.PACKAGE_NAME}")
    print(f"Generated: {ChartMultiInfo.TIMESTAMP}")
    print(f"Current Time: {ChartMultiInfo.CURRENT_TIMESTAMP}")
    
    print("\n=== Current Charts ===")
    for key, chart in ChartMultiInfo.CHARTS.items():
        print(f"{key}: {chart['currency_pair']} - {chart['timeframe']} - {chart['type']}")
        print(f"  Position: {chart['position']}, Bounds: {chart['bounds']}")
    
    print("\n=== Available XPath Selectors ===")
    print(f"Chart Title: {ChartMultiXPaths.CHART_TITLE}")
    print(f"First AUD/JPY Chart: {ChartMultiXPaths.AUD_JPY_CHART_1}")
    print(f"GBP/JPY Chart: {ChartMultiXPaths.GBP_JPY_CHART}")
    print(f"Timestamp: {ChartMultiXPaths.TIMESTAMP}")
    print(f"Bottom Chart: {ChartMultiXPaths.BOTTOM_CHART}") 