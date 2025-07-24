#!/usr/bin/env python3
"""
Script đơn giản để chạy SBI FX Mobile Automation Framework
"""

import sys
import os

# Thêm thư mục hiện tại vào Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from framework.main import main

if __name__ == "__main__":
    print("🚀 Khởi động SBI FX Mobile Automation Framework...")
    main() 