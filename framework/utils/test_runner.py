import unittest
import sys
import os
import time
from datetime import datetime
from io import StringIO
from framework.config.config import Config

class TestRunner:
    """Test Runner để chạy test suite và tạo báo cáo"""
    
    def __init__(self):
        self.test_results = []
        self.start_time = None
        self.end_time = None
    
    def run_test_suite(self, test_module_path, test_class_name=None):
        """Chạy test suite"""
        print("=== BẮT ĐẦU CHẠY TEST SUITE ===")
        self.start_time = datetime.now()
        
        # Tạo test suite
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        
        # Import test module
        sys.path.append(os.path.dirname(test_module_path))
        module_name = os.path.basename(test_module_path).replace('.py', '')
        test_module = __import__(module_name)
        
        if test_class_name:
            # Chạy test class cụ thể
            test_class = getattr(test_module, test_class_name)
            suite.addTests(loader.loadTestsFromTestCase(test_class))
        else:
            # Chạy tất cả test cases trong module
            suite.addTests(loader.loadTestsFromModule(test_module))
        
        # Chạy tests
        runner = unittest.TextTestRunner(verbosity=2, stream=StringIO())
        result = runner.run(suite)
        
        self.end_time = datetime.now()
        
        # Lưu kết quả
        self.test_results = {
            'total_tests': result.testsRun,
            'failures': len(result.failures),
            'errors': len(result.errors),
            'skipped': len(result.skipped) if hasattr(result, 'skipped') else 0,
            'success_rate': ((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100) if result.testsRun > 0 else 0,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'duration': (self.end_time - self.start_time).total_seconds(),
            'failures': result.failures,
            'errors': result.errors
        }
        
        return self.test_results
    
    def generate_report(self, output_file=None):
        """Tạo báo cáo test"""
        if not output_file:
            timestamp = Config.get_timestamp()
            output_file = f"{Config.REPORT_DIR}/test_report_{timestamp}.html"
        
        html_content = self._generate_html_report()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"[INFO] Đã tạo báo cáo: {output_file}")
        return output_file
    
    def _generate_html_report(self):
        """Tạo HTML report"""
        results = self.test_results
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Test Report - {results['start_time'].strftime('%Y-%m-%d %H:%M:%S')}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .header {{ background-color: #f0f0f0; padding: 20px; border-radius: 5px; }}
                .summary {{ margin: 20px 0; }}
                .summary-item {{ display: inline-block; margin: 10px; padding: 10px; border-radius: 5px; }}
                .success {{ background-color: #d4edda; color: #155724; }}
                .failure {{ background-color: #f8d7da; color: #721c24; }}
                .error {{ background-color: #fff3cd; color: #856404; }}
                .details {{ margin: 20px 0; }}
                .test-case {{ margin: 10px 0; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }}
                .test-case.failure {{ border-color: #dc3545; background-color: #f8d7da; }}
                .test-case.error {{ border-color: #ffc107; background-color: #fff3cd; }}
                .test-case.success {{ border-color: #28a745; background-color: #d4edda; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Test Report</h1>
                <p>Generated: {results['end_time'].strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p>Duration: {results['duration']:.2f} seconds</p>
            </div>
            
            <div class="summary">
                <h2>Summary</h2>
                <div class="summary-item success">
                    <strong>Total Tests:</strong> {results['total_tests']}
                </div>
                <div class="summary-item success">
                    <strong>Passed:</strong> {results['total_tests'] - results['failures'] - results['errors']}
                </div>
                <div class="summary-item failure">
                    <strong>Failed:</strong> {results['failures']}
                </div>
                <div class="summary-item error">
                    <strong>Errors:</strong> {results['errors']}
                </div>
                <div class="summary-item success">
                    <strong>Success Rate:</strong> {results['success_rate']:.1f}%
                </div>
            </div>
        """
        
        # Thêm chi tiết failures
        if results['failures']:
            html += "<div class='details'><h2>Failures</h2>"
            for test, traceback in results['failures']:
                html += f"""
                <div class="test-case failure">
                    <h3>{test}</h3>
                    <pre>{traceback}</pre>
                </div>
                """
            html += "</div>"
        
        # Thêm chi tiết errors
        if results['errors']:
            html += "<div class='details'><h2>Errors</h2>"
            for test, traceback in results['errors']:
                html += f"""
                <div class="test-case error">
                    <h3>{test}</h3>
                    <pre>{traceback}</pre>
                </div>
                """
            html += "</div>"
        
        html += """
        </body>
        </html>
        """
        
        return html
    
    def print_summary(self):
        """In tóm tắt kết quả"""
        results = self.test_results
        
        print("\n" + "="*50)
        print("TEST EXECUTION SUMMARY")
        print("="*50)
        print(f"Total Tests: {results['total_tests']}")
        print(f"Passed: {results['total_tests'] - results['failures'] - results['errors']}")
        print(f"Failed: {results['failures']}")
        print(f"Errors: {results['errors']}")
        print(f"Success Rate: {results['success_rate']:.1f}%")
        print(f"Duration: {results['duration']:.2f} seconds")
        print("="*50)

def run_tests(test_module_path, test_class_name=None, generate_report=True):
    """Hàm tiện ích để chạy tests"""
    runner = TestRunner()
    
    try:
        # Chạy test suite
        results = runner.run_test_suite(test_module_path, test_class_name)
        
        # In tóm tắt
        runner.print_summary()
        
        # Tạo báo cáo
        if generate_report:
            report_file = runner.generate_report()
            print(f"[INFO] Báo cáo đã được tạo: {report_file}")
        
        return results
        
    except Exception as e:
        print(f"[ERROR] Lỗi khi chạy tests: {e}")
        return None

if __name__ == "__main__":
    # Ví dụ sử dụng
    test_module = "framework.tests.test_news_list"
    run_tests(test_module, "TestNewsList") 