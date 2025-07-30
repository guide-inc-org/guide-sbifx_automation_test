# -*- coding: utf-8 -*-
"""
XPath Objects cho màn hình Notice Private List (緊急なお知らせ)
Generated: 2025-07-25 16:10:00
Screen: NoticePrivateList - Notice Private List
"""

class CurrentScreenXPaths:
    """XPath objects for Notice Private List screen"""
    
    # Header elements
    BACK_BUTTON = "(//*[@class='android.widget.ImageView'])[1]"

    HEADER_TITLE = "//*[@text='緊急なお知らせ' or @content-desc='緊急なお知らせ']"
    
    # Content elements
    NOTICE_CONTENT = "//*[@class='android.widget.TextView' and contains(@text, 'お知らせ')]"
    NOTICE_LIST = "//*[@class='android.widget.ListView']//*[@class='android.widget.TextView']"
    
    # Common elements
    CLOSE_BUTTON = "//*[@content-desc='閉じる' or @content-desc='Close']"
    OK_BUTTON = "//*[@text='OK' or @content-desc='OK']"
    CANCEL_BUTTON = "//*[@text='キャンセル' or @content-desc='Cancel']"
    
    # Usage examples:
    # Back button: driver.find_element(AppiumBy.XPATH, CurrentScreenXPaths.BACK_BUTTON)
    # Header: driver.find_element(AppiumBy.XPATH, CurrentScreenXPaths.HEADER_TITLE)
    # Notice content: driver.find_element(AppiumBy.XPATH, CurrentScreenXPaths.NOTICE_CONTENT)   