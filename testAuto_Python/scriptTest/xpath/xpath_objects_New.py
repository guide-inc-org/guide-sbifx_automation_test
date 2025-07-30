# -*- coding: utf-8 -*-
"""
XPath Objects từ màn hình hiện tại
Generated: 2025-07-24 15:53:02
Screen: News (ニュース) - Tab "ニュース"
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
    SETTINGS_ICON_1 = "//android.widget.ImageView[@bounds='[850,90][942,182]']"
    SETTINGS_ICON_2 = "//android.widget.ImageView[@bounds='[965,84][1068,188]']"
    
    # Main tab navigation
    RATE_TAB = "//android.view.View[@content-desc='レート\nタブ: 1/4']"
    SWAP_TAB = "//android.view.View[@content-desc='スワップ\nタブ: 2/4']"
    NEWS_TAB = "//android.view.View[@content-desc='ニュース\nタブ: 3/4']"
    ECONOMIC_INDICATORS_TAB = "//android.view.View[@content-desc='経済指標\nタブ: 4/4']"
    
    # Sub-tabs
    NEWS_SUB_TAB = "//android.view.View[@content-desc='ニュース']"
    PREMIUM_NEWS_SUB_TAB = "//android.view.View[@content-desc='プレミアムニュース']"
    
    # News articles
    NEWS_ARTICLE_1 = "//android.view.View[@content-desc='【相場の細道】6月の「基調的なインフレ率を捕捉するための指標」\n07/24 17:45\n為替分析']"
    NEWS_ARTICLE_2 = "//android.view.View[@content-desc='テクニカルポイント＝ユーロ／豪ドル　レジスタンス1　1.7889（90日移動平均線）\n07/24 17:38\n為替分析']"
    NEWS_ARTICLE_3 = "//android.view.View[@content-desc='ポンドドル、1.3550ドル割れまで弱含み　英サービス業PMIが予想を下回る\n07/24 17:37\n為替分析']"
    NEWS_ARTICLE_4 = "//android.view.View[@content-desc='【指標】7月英製造業PMI速報値 48.2、予想 48.0ほか\n07/24 17:31\n相場ニュース']"
    NEWS_ARTICLE_5 = "//android.view.View[@content-desc='日経平均先物、売り戻し先行　大証終値比70円安\n07/24 17:25\n為替分析']"
    NEWS_ARTICLE_6 = "//android.view.View[@content-desc='香港株大引け（24日）：ハンセン指数は0.51％高\n07/24 17:21\n為替分析']"
    NEWS_ARTICLE_7 = "//android.view.View[@content-desc='【指標発表予定】17:30　7月英製造業PMI速報値など\n07/24 17:15\n指標予定']"
    NEWS_ARTICLE_8 = "//android.view.View[@content-desc='東京外国為替市場概況・17時　ドル円、強含み\n07/24 17:08\n為替分析']"
    NEWS_ARTICLE_9 = "//android.view.View[@content-desc='【指標】7月ユーロ圏製造業PMI速報値 49.8、予想 49.7ほか\n07/24 17:01\n相場ニュース']"
    
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
    NEWS_ARTICLE_1_BOUNDS = "//android.view.View[@bounds='[0,477][1080,689]']"
    NEWS_ARTICLE_2_BOUNDS = "//android.view.View[@bounds='[0,694][1080,907]']"
    NEWS_ARTICLE_3_BOUNDS = "//android.view.View[@bounds='[0,912][1080,1125]']"
    NEWS_ARTICLE_4_BOUNDS = "//android.view.View[@bounds='[0,1130][1080,1303]']"
    NEWS_ARTICLE_5_BOUNDS = "//android.view.View[@bounds='[0,1308][1080,1481]']"
    NEWS_ARTICLE_6_BOUNDS = "//android.view.View[@bounds='[0,1486][1080,1658]']"
    NEWS_ARTICLE_7_BOUNDS = "//android.view.View[@bounds='[0,1664][1080,1836]']"
    NEWS_ARTICLE_8_BOUNDS = "//android.view.View[@bounds='[0,1841][1080,2014]']"
    NEWS_ARTICLE_9_BOUNDS = "//android.view.View[@bounds='[0,2019][1080,2040]']"
    
    # Tab selectors by bounds
    RATE_TAB_BOUNDS = "//android.view.View[@bounds='[0,200][270,315]']"
    SWAP_TAB_BOUNDS = "//android.view.View[@bounds='[270,200][540,315]']"
    NEWS_TAB_BOUNDS = "//android.view.View[@bounds='[540,200][810,315]']"
    ECONOMIC_TAB_BOUNDS = "//android.view.View[@bounds='[810,200][1080,315]']"
    
    # Sub-tab selectors by bounds
    NEWS_SUB_TAB_BOUNDS = "//android.view.View[@bounds='[37,347][540,445]']"
    PREMIUM_NEWS_SUB_TAB_BOUNDS = "//android.view.View[@bounds='[540,347][1043,445]']"
    
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
    
    # News selectors by partial content-desc
    NEWS_BY_DESC = "//*[contains(@content-desc, 'ニュース')]"
    PREMIUM_NEWS_BY_DESC = "//*[contains(@content-desc, 'プレミアムニュース')]"
    
    # Tab selectors by partial content-desc
    RATE_TAB_BY_DESC = "//*[contains(@content-desc, 'レート\nタブ: 1/4')]"
    SWAP_TAB_BY_DESC = "//*[contains(@content-desc, 'スワップ\nタブ: 2/4')]"
    NEWS_TAB_BY_DESC = "//*[contains(@content-desc, 'ニュース\nタブ: 3/4')]"
    ECONOMIC_TAB_BY_DESC = "//*[contains(@content-desc, '経済指標\nタブ: 4/4')]"
    
    # News article selectors by partial content-desc
    NEWS_ARTICLE_1_BY_DESC = "//*[contains(@content-desc, '【相場の細道】')]"
    NEWS_ARTICLE_2_BY_DESC = "//*[contains(@content-desc, 'テクニカルポイント')]"
    NEWS_ARTICLE_3_BY_DESC = "//*[contains(@content-desc, 'ポンドドル')]"
    NEWS_ARTICLE_4_BY_DESC = "//*[contains(@content-desc, '7月英製造業PMI')]"
    NEWS_ARTICLE_5_BY_DESC = "//*[contains(@content-desc, '日経平均先物')]"
    NEWS_ARTICLE_6_BY_DESC = "//*[contains(@content-desc, '香港株大引け')]"
    NEWS_ARTICLE_7_BY_DESC = "//*[contains(@content-desc, '【指標発表予定】')]"
    NEWS_ARTICLE_8_BY_DESC = "//*[contains(@content-desc, '東京外国為替市場概況')]"
    NEWS_ARTICLE_9_BY_DESC = "//*[contains(@content-desc, '7月ユーロ圏製造業PMI')]"


class ScreenInfo:
    """Information about current screen"""
    
    SCREEN_NAME = "News (ニュース)"
    CURRENT_TAB = "ニュース"
    SCREEN_RESOLUTION = "1080x2106"
    PACKAGE_NAME = "jp.co.mobileit.SBI_FX"
    TIMESTAMP = "2025-07-24 15:53:02"
    
    # Current news data
    NEWS_ARTICLES = {
        "article_1": {
            "title": "【相場の細道】6月の「基調的なインフレ率を捕捉するための指標」",
            "time": "07/24 17:45",
            "category": "為替分析"
        },
        "article_2": {
            "title": "テクニカルポイント＝ユーロ／豪ドル　レジスタンス1　1.7889（90日移動平均線）",
            "time": "07/24 17:38",
            "category": "為替分析"
        },
        "article_3": {
            "title": "ポンドドル、1.3550ドル割れまで弱含み　英サービス業PMIが予想を下回る",
            "time": "07/24 17:37",
            "category": "為替分析"
        },
        "article_4": {
            "title": "【指標】7月英製造業PMI速報値 48.2、予想 48.0ほか",
            "time": "07/24 17:31",
            "category": "相場ニュース"
        },
        "article_5": {
            "title": "日経平均先物、売り戻し先行　大証終値比70円安",
            "time": "07/24 17:25",
            "category": "為替分析"
        },
        "article_6": {
            "title": "香港株大引け（24日）：ハンセン指数は0.51％高",
            "time": "07/24 17:21",
            "category": "為替分析"
        },
        "article_7": {
            "title": "【指標発表予定】17:30　7月英製造業PMI速報値など",
            "time": "07/24 17:15",
            "category": "指標予定"
        },
        "article_8": {
            "title": "東京外国為替市場概況・17時　ドル円、強含み",
            "time": "07/24 17:08",
            "category": "為替分析"
        },
        "article_9": {
            "title": "【指標】7月ユーロ圏製造業PMI速報値 49.8、予想 49.7ほか",
            "time": "07/24 17:01",
            "category": "相場ニュース"
        }
    }
    
    # Available tabs
    MAIN_TABS = ["レート", "スワップ", "ニュース", "経済指標"]
    SUB_TABS = ["ニュース", "プレミアムニュース"]
    
    # Bottom navigation
    BOTTOM_NAV = ["マーケット", "チャート", "スピード注文", "ログイン", "ウェブサイト", "メニュー"]
    
    # News categories
    NEWS_CATEGORIES = ["為替分析", "相場ニュース", "指標予定"]


# Usage examples:
if __name__ == "__main__":
    print("=== XPath Objects for Current Screen ===")
    print(f"Screen: {ScreenInfo.SCREEN_NAME}")
    print(f"Current Tab: {ScreenInfo.CURRENT_TAB}")
    print(f"Resolution: {ScreenInfo.SCREEN_RESOLUTION}")
    print(f"Package: {ScreenInfo.PACKAGE_NAME}")
    print(f"Generated: {ScreenInfo.TIMESTAMP}")
    
    print("\n=== Current News Articles ===")
    for key, article in ScreenInfo.NEWS_ARTICLES.items():
        print(f"{key}: {article['title']}")
        print(f"  Time: {article['time']}, Category: {article['category']}")
    
    print("\n=== Available XPath Selectors ===")
    print(f"Market Button: {CurrentScreenXPaths.MARKET_BUTTON}")
    print(f"News Tab: {CurrentScreenXPaths.NEWS_TAB}")
    print(f"News Sub Tab: {CurrentScreenXPaths.NEWS_SUB_TAB}")
    print(f"First News Article: {CurrentScreenXPaths.NEWS_ARTICLE_1}")
    print(f"Bottom Menu: {CurrentScreenXPaths.BOTTOM_MENU}") 