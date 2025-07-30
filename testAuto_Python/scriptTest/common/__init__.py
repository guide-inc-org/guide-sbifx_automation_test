#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Common Utilities Package
Package chứa các module tiện ích chung cho automation testing
"""

from .screenshot_utils import ScreenshotUtils, take_screenshot
from .appium_config import AppiumConfig, setup_driver, kill_app, kill_all_apps, is_app_running, restart_app

__all__ = [
    'ScreenshotUtils',
    'take_screenshot',
    'AppiumConfig',
    'setup_driver',
    'kill_app',
    'kill_all_apps',
    'is_app_running',
    'restart_app'
] 