#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Connection Script
Script đơn giản để test kết nối Appium
"""

import requests
import json

def test_appium_connection():
    """Test kết nối Appium server"""
    print("=== Test Appium Connection ===")
    
    # Test 1: Kiểm tra status
    try:
        response = requests.get("http://localhost:4723/wd/hub/status", timeout=5)
        print(f"Status check: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Server ready: {data.get('value', {}).get('ready', False)}")
        else:
            print(f"Status response: {response.text}")
    except Exception as e:
        print(f"Status check error: {e}")
    
    # Test 2: Test session creation
    try:
        capabilities = {
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:deviceName": "Android Device",
            "appium:appPackage": "jp.co.mobileit.SBI_FX",
            "appium:appActivity": ".MainActivity",
            "appium:noReset": True
        }
        
        session_data = {
            "capabilities": {
                "firstMatch": [{}],
                "alwaysMatch": capabilities
            }
        }
        
        response = requests.post(
            "http://localhost:4723/wd/hub/session",
            json=session_data,
            timeout=30
        )
        
        print(f"Session creation: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            session_id = data.get('value', {}).get('sessionId')
            print(f"Session created: {session_id}")
            
            # Close session
            if session_id:
                requests.delete(f"http://localhost:4723/wd/hub/session/{session_id}")
                print("Session closed")
        else:
            print(f"Session creation error: {response.text}")
            
    except Exception as e:
        print(f"Session creation error: {e}")

if __name__ == "__main__":
    test_appium_connection() 