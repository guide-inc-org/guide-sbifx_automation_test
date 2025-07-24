#!/usr/bin/env python3
"""
Script để tạo file ObjectRepository.xlsx chứa các object definitions
"""

import pandas as pd
import os
from datetime import datetime

def create_object_repository_excel():
    """Tạo file ObjectRepository.xlsx với các object definitions"""
    
    # Tạo thư mục testdata nếu chưa có
    os.makedirs("testdata", exist_ok=True)
    
    # Định nghĩa các objects
    objects_data = [
        # Tab Navigation Objects - Sử dụng content-desc thực tế từ app
        {
            'ObjectName': 'SWAP_TAB',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.view.View[@content-desc="スワップ\nタブ: 2/4"]',
            'Description': 'Tab Swap trong bottom navigation',
            'Screen': 'MainScreen'
        },
        {
            'ObjectName': 'NEWS_TAB',
            'LocatorType': 'xpath', 
            'LocatorValue': '//android.view.View[@content-desc="ニュース\nタブ: 3/4"]',
            'Description': 'Tab News trong bottom navigation',
            'Screen': 'MainScreen'
        },
        {
            'ObjectName': 'ECONOMIC_TAB',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.view.View[@content-desc="経済指標\nタブ: 4/4"]',
            'Description': 'Tab Economic trong bottom navigation',
            'Screen': 'MainScreen'
        },
        {
            'ObjectName': 'MARKET_TAB',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.view.View[@content-desc="マーケット\nタブ: 1/4"]',
            'Description': 'Tab Market trong bottom navigation',
            'Screen': 'MainScreen'
        },
        {
            'ObjectName': 'CHART_TAB',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.view.View[@content-desc="チャート\nタブ: 5/4"]',
            'Description': 'Tab Chart trong bottom navigation',
            'Screen': 'MainScreen'
        },
        {
            'ObjectName': 'SPEED_ORDER_TAB',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.view.View[@content-desc="スピード注文\nタブ: 6/4"]',
            'Description': 'Tab Speed Order trong bottom navigation',
            'Screen': 'MainScreen'
        },
        
        # News List Screen Objects - Sử dụng resource-id thực tế
        {
            'ObjectName': 'NEWS_LIST_CONTAINER',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.widget.RecyclerView[@resource-id="inc.guide.sbi.fx.dev:id/news_list_recycler"]',
            'Description': 'Container chứa danh sách news',
            'Screen': 'NewsListScreen'
        },
        {
            'ObjectName': 'NEWS_ITEM_FIRST',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.widget.RecyclerView[@resource-id="inc.guide.sbi.fx.dev:id/news_list_recycler"]/android.view.ViewGroup[1]',
            'Description': 'News item đầu tiên trong danh sách',
            'Screen': 'NewsListScreen'
        },
        {
            'ObjectName': 'NEWS_TITLE_FIRST',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.widget.RecyclerView[@resource-id="inc.guide.sbi.fx.dev:id/news_list_recycler"]/android.view.ViewGroup[1]//android.widget.TextView[@resource-id="inc.guide.sbi.fx.dev:id/news_title_text"]',
            'Description': 'Tiêu đề của news đầu tiên',
            'Screen': 'NewsListScreen'
        },
        {
            'ObjectName': 'NEWS_DATE_FIRST',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.widget.RecyclerView[@resource-id="inc.guide.sbi.fx.dev:id/news_list_recycler"]/android.view.ViewGroup[1]//android.widget.TextView[@resource-id="inc.guide.sbi.fx.dev:id/news_date_text"]',
            'Description': 'Ngày của news đầu tiên',
            'Screen': 'NewsListScreen'
        },
        
        # News Detail Screen Objects
        {
            'ObjectName': 'NEWS_DETAIL_TITLE',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.widget.TextView[@resource-id="inc.guide.sbi.fx.dev:id/news_detail_title_text"]',
            'Description': 'Tiêu đề chi tiết của news',
            'Screen': 'NewsDetailScreen'
        },
        {
            'ObjectName': 'NEWS_DETAIL_CONTENT',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.widget.TextView[@resource-id="inc.guide.sbi.fx.dev:id/news_detail_content_text"]',
            'Description': 'Nội dung chi tiết của news',
            'Screen': 'NewsDetailScreen'
        },
        {
            'ObjectName': 'BACK_BUTTON',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.widget.ImageButton[@content-desc="Navigate up"]',
            'Description': 'Nút back để quay lại màn hình trước',
            'Screen': 'CommonElements'
        },
        
        # Filter Screen Objects
        {
            'ObjectName': 'FILTER_BUTTON',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.widget.ImageButton[@resource-id="inc.guide.sbi.fx.dev:id/filter_button"]',
            'Description': 'Nút filter để mở màn hình filter',
            'Screen': 'NewsListScreen'
        },
        {
            'ObjectName': 'FILTER_DATE_FROM',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.widget.EditText[@resource-id="inc.guide.sbi.fx.dev:id/filter_date_from_input"]',
            'Description': 'Input chọn ngày bắt đầu filter',
            'Screen': 'FilterScreen'
        },
        {
            'ObjectName': 'FILTER_DATE_TO',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.widget.EditText[@resource-id="inc.guide.sbi.fx.dev:id/filter_date_to_input"]',
            'Description': 'Input chọn ngày kết thúc filter',
            'Screen': 'FilterScreen'
        },
        {
            'ObjectName': 'FILTER_APPLY_BUTTON',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.widget.Button[@text="適用"]',
            'Description': 'Nút apply filter',
            'Screen': 'FilterScreen'
        },
        {
            'ObjectName': 'FILTER_RESET_BUTTON',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.widget.Button[@text="リセット"]',
            'Description': 'Nút reset filter',
            'Screen': 'FilterScreen'
        },
        
        # Common Elements
        {
            'ObjectName': 'LOADING_INDICATOR',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.widget.ProgressBar[@resource-id="inc.guide.sbi.fx.dev:id/loading_indicator"]',
            'Description': 'Loading indicator khi đang tải dữ liệu',
            'Screen': 'CommonElements'
        },
        {
            'ObjectName': 'ERROR_MESSAGE',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.widget.TextView[@resource-id="inc.guide.sbi.fx.dev:id/error_message_text"]',
            'Description': 'Thông báo lỗi',
            'Screen': 'CommonElements'
        },
        {
            'ObjectName': 'NO_DATA_MESSAGE',
            'LocatorType': 'xpath',
            'LocatorValue': '//android.widget.TextView[@text="データがありません"]',
            'Description': 'Thông báo không có dữ liệu',
            'Screen': 'CommonElements'
        }
    ]
    
    # Tạo DataFrame
    df = pd.DataFrame(objects_data)
    
    # Tạo file Excel
    output_file = "testdata/ObjectRepository.xlsx"
    
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # Sheet chính chứa tất cả objects
        df.to_excel(writer, sheet_name='AllObjects', index=False)
        
        # Sheet theo từng screen
        for screen in df['Screen'].unique():
            screen_df = df[df['Screen'] == screen]
            sheet_name = screen.replace('Screen', '').replace('Elements', '')
            if len(sheet_name) > 31:  # Excel sheet name limit
                sheet_name = sheet_name[:31]
            screen_df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    print(f"✅ Đã tạo file ObjectRepository.xlsx: {output_file}")
    print(f"📊 Tổng số objects: {len(objects_data)}")
    print(f"📱 Screens: {', '.join(df['Screen'].unique())}")
    
    return output_file

def read_from_existing_file(file_path):
    """Đọc dữ liệu từ file Excel hiện có và cập nhật Object Repository"""
    try:
        print(f"[INFO] Đang đọc dữ liệu từ file: {file_path}")
        
        # Đọc file Excel
        df = pd.read_excel(file_path, sheet_name=0)  # Đọc sheet đầu tiên
        
        print(f"[SUCCESS] Đã đọc {len(df)} objects từ file")
        print(f"[INFO] Columns: {list(df.columns)}")
        
        # Chuyển đổi DataFrame thành list of dictionaries
        objects_data = df.to_dict('records')
        
        return objects_data
        
    except Exception as e:
        print(f"[ERROR] Lỗi khi đọc file: {e}")
        return None

def update_object_repository_from_file(source_file, output_file="testdata/ObjectRepository.xlsx"):
    """Cập nhật Object Repository từ file nguồn"""
    try:
        # Tạo thư mục testdata nếu chưa có
        os.makedirs("testdata", exist_ok=True)
        
        # Đọc dữ liệu từ file nguồn
        objects_data = read_from_existing_file(source_file)
        if not objects_data:
            print("[ERROR] Không thể đọc dữ liệu từ file nguồn")
            return None
        
        # Tạo DataFrame
        df = pd.DataFrame(objects_data)
        
        # Tạo file Excel
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            # Sheet chính chứa tất cả objects
            df.to_excel(writer, sheet_name='AllObjects', index=False)
            
            # Sheet theo từng screen (nếu có column Screen)
            if 'Screen' in df.columns:
                for screen in df['Screen'].unique():
                    screen_df = df[df['Screen'] == screen]
                    sheet_name = screen.replace('Screen', '').replace('Elements', '')
                    if len(sheet_name) > 31:  # Excel sheet name limit
                        sheet_name = sheet_name[:31]
                    screen_df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        print(f"✅ Đã cập nhật file ObjectRepository.xlsx: {output_file}")
        print(f"📊 Tổng số objects: {len(objects_data)}")
        if 'Screen' in df.columns:
            print(f"📱 Screens: {', '.join(df['Screen'].unique())}")
        
        return output_file
        
    except Exception as e:
        print(f"[ERROR] Lỗi khi cập nhật Object Repository: {e}")
        return None

def create_object_repository_from_xpath_file(xpath_file):
    """Tạo Object Repository từ file XPath summary"""
    try:
        print(f"[INFO] Đang đọc XPath từ file: {xpath_file}")
        
        objects_data = []
        
        with open(xpath_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        current_object = {}
        object_count = 0
        
        for line in lines:
            line = line.strip()
            
            if line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')) or line.startswith(('10.', '11.', '12.', '13.', '14.', '15.')):
                # Bắt đầu object mới
                if current_object:
                    objects_data.append(current_object)
                    object_count += 1
                
                current_object = {
                    'ObjectName': f'OBJECT_{object_count + 1}',
                    'LocatorType': 'xpath',
                    'LocatorValue': '',
                    'Description': '',
                    'Screen': 'MainScreen'
                }
                
            elif line.startswith('   Class:'):
                class_name = line.replace('   Class:', '').strip()
                current_object['Description'] = f'Element class: {class_name}'
                
            elif line.startswith('   Text:'):
                text = line.replace('   Text:', '').strip()
                if text and text != 'No text':
                    current_object['Description'] += f', Text: {text}'
                
            elif line.startswith('   Resource ID:'):
                resource_id = line.replace('   Resource ID:', '').strip()
                if resource_id:
                    current_object['Description'] += f', Resource ID: {resource_id}'
                
            elif line.startswith('   Content Desc:'):
                content_desc = line.replace('   Content Desc:', '').strip()
                if content_desc:
                    current_object['Description'] += f', Content Desc: {content_desc}'
                
            elif line.startswith('   XPath:'):
                xpath = line.replace('   XPath:', '').strip()
                current_object['LocatorValue'] = xpath
        
        # Thêm object cuối cùng
        if current_object and current_object['LocatorValue']:
            objects_data.append(current_object)
        
        # Tạo file Excel
        output_file = "testdata/ObjectRepository.xlsx"
        os.makedirs("testdata", exist_ok=True)
        
        df = pd.DataFrame(objects_data)
        
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='AllObjects', index=False)
        
        print(f"✅ Đã tạo Object Repository từ XPath file: {output_file}")
        print(f"📊 Tổng số objects: {len(objects_data)}")
        
        return output_file
        
    except Exception as e:
        print(f"[ERROR] Lỗi khi tạo Object Repository từ XPath file: {e}")
        return None

if __name__ == "__main__":
    import sys
    
    print("🔧 SBI FX Mobile - Object Repository Creator")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        
        if mode == "from_file" and len(sys.argv) > 2:
            source_file = sys.argv[2]
            print(f"📁 Chế độ: Đọc từ file {source_file}")
            update_object_repository_from_file(source_file)
            
        elif mode == "from_xpath" and len(sys.argv) > 2:
            xpath_file = sys.argv[2]
            print(f"🔍 Chế độ: Đọc từ XPath file {xpath_file}")
            create_object_repository_from_xpath_file(xpath_file)
            
        else:
            print("❌ Tham số không hợp lệ")
            print("Cách sử dụng:")
            print("  python create_object_repository_excel.py                    # Tạo mặc định")
            print("  python create_object_repository_excel.py from_file <file>   # Đọc từ file Excel")
            print("  python create_object_repository_excel.py from_xpath <file>  # Đọc từ file XPath")
    else:
        print("📝 Chế độ: Tạo Object Repository mặc định")
        create_object_repository_excel() 