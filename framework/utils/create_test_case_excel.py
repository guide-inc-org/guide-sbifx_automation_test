#!/usr/bin/env python3
"""
Script để tạo file TestCase.xlsx với test cases mẫu
"""

import pandas as pd
import os

def create_test_case_excel():
    """Tạo file TestCase.xlsx với test cases mẫu"""
    
    # Tạo thư mục testdata nếu chưa có
    os.makedirs("testdata", exist_ok=True)
    
    # Dữ liệu test cases mẫu
    test_cases = [
        {
            'Run/NoRun': 'r',
            'Action': 'launchapp',
            'Object': '',
            'Data': '',
            'Note': 'Khởi động ứng dụng'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'take_screenshot',
            'Object': '',
            'Data': 'initial_screen',
            'Note': 'Chụp màn hình ban đầu'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'print',
            'Object': '',
            'Data': '[TC2] Kiểm tra hiển thị dữ liệu khi tab Swap',
            'Note': 'In thông báo test case'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'click',
            'Object': 'SWAP_TAB',
            'Data': '',
            'Note': 'Click vào tab Swap'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'take_screenshot',
            'Object': '',
            'Data': 'after_swap_click',
            'Note': 'Chụp màn hình sau khi click Swap'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'wait',
            'Object': '',
            'Data': '2',
            'Note': 'Đợi 2 giây'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'print',
            'Object': '',
            'Data': '[TC3] Kiểm tra chuyển tab News',
            'Note': 'In thông báo test case'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'click',
            'Object': 'NEWS_TAB',
            'Data': '',
            'Note': 'Click vào tab News'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'take_screenshot',
            'Object': '',
            'Data': 'after_news_click',
            'Note': 'Chụp màn hình sau khi click News'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'print',
            'Object': '',
            'Data': '[TC4] Kiểm tra chuyển tab Economic',
            'Note': 'In thông báo test case'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'click',
            'Object': 'ECONOMIC_TAB',
            'Data': '',
            'Note': 'Click vào tab Economic'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'take_screenshot',
            'Object': '',
            'Data': 'after_economic_click',
            'Note': 'Chụp màn hình sau khi click Economic'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'print',
            'Object': '',
            'Data': '[TC5] Kiểm tra reload page',
            'Note': 'In thông báo test case'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'click',
            'Object': 'MARKET_TAB',
            'Data': '',
            'Note': 'Click vào tab Market để reload'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'take_screenshot',
            'Object': '',
            'Data': 'after_market_click',
            'Note': 'Chụp màn hình sau khi click Market'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'print',
            'Object': '',
            'Data': '[TC6] Kiểm tra hiển thị Chart',
            'Note': 'In thông báo test case'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'click',
            'Object': 'CHART_TAB',
            'Data': '',
            'Note': 'Click vào tab Chart'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'take_screenshot',
            'Object': '',
            'Data': 'after_chart_click',
            'Note': 'Chụp màn hình sau khi click Chart'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'print',
            'Object': '',
            'Data': '[TC7] Kiểm tra hiển thị Speed Order',
            'Note': 'In thông báo test case'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'click',
            'Object': 'SPEED_ORDER_TAB',
            'Data': '',
            'Note': 'Click vào tab Speed Order'
        },
        {
            'Run/NoRun': 'r',
            'Action': 'take_screenshot',
            'Object': '',
            'Data': 'after_speed_order_click',
            'Note': 'Chụp màn hình sau khi click Speed Order'
        }
    ]
    
    # Tạo DataFrame
    df = pd.DataFrame(test_cases)
    
    # Lưu thành file Excel
    output_file = "testdata/TestCase.xlsx"
    df.to_excel(output_file, index=False, sheet_name='NewOrder')
    
    print(f"✅ Đã tạo file TestCase.xlsx: {output_file}")
    print(f"📊 Tổng số test steps: {len(test_cases)}")
    
    return output_file

if __name__ == "__main__":
    create_test_case_excel() 