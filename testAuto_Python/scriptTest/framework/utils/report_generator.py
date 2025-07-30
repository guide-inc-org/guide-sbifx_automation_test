#!/usr/bin/env python3
"""
Report Generator cho Excel Test Runner
"""

import os
import pandas as pd
from datetime import datetime
import time

class ReportGenerator:
    def __init__(self, output_dir="output/reports"):
        self.output_dir = output_dir
        self.ensure_output_dir()
    
    def ensure_output_dir(self):
        """Tạo thư mục output nếu chưa tồn tại"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def generate_excel_report(self, test_results, test_steps, execution_time):
        """Generate Excel report từ test results"""
        try:
            # Tạo timestamp cho filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"test_report_{timestamp}.xlsx"
            filepath = os.path.join(self.output_dir, filename)
            
            # Tạo Excel writer
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                
                # Sheet 1: Test Summary
                self._create_summary_sheet(writer, test_results, execution_time)
                
                # Sheet 2: Detailed Results
                self._create_detailed_sheet(writer, test_steps, test_results)
                
                # Sheet 3: Test Steps
                self._create_steps_sheet(writer, test_steps)
                
                # Sheet 4: Statistics
                self._create_statistics_sheet(writer, test_results)
            
            print(f"✅ Đã tạo báo cáo Excel: {filepath}")
            return filepath
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi tạo báo cáo Excel: {e}")
            return None
    
    def _create_summary_sheet(self, writer, test_results, execution_time):
        """Tạo sheet Summary"""
        summary_data = {
            'Metric': [
                'Tổng số Test Steps',
                'Thành công',
                'Thất bại',
                'Success Rate (%)',
                'Thời gian thực thi',
                'Ngày thực hiện',
                'Framework Version'
            ],
            'Value': [
                test_results['total_steps'],
                test_results['successful'],
                test_results['failed'],
                f"{test_results['success_rate']:.1f}%",
                f"{execution_time:.2f}s",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'Excel Test Runner v1.0'
            ]
        }
        
        df_summary = pd.DataFrame(summary_data)
        df_summary.to_excel(writer, sheet_name='Summary', index=False)
        
        # Format summary sheet
        worksheet = writer.sheets['Summary']
        for column in worksheet.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = min(max_length + 2, 50)
            worksheet.column_dimensions[column_letter].width = adjusted_width
    
    def _create_detailed_sheet(self, writer, test_steps, test_results):
        """Tạo sheet Detailed Results"""
        detailed_data = []
        
        for i, step in enumerate(test_steps, 1):
            step_result = test_results['step_results'].get(i, {})
            
            detailed_data.append({
                'Step': i,
                'Action': step.get('action', ''),
                'Object': step.get('object', ''),
                'Data': step.get('data', ''),
                'Note': step.get('note', ''),
                'Status': step_result.get('status', 'UNKNOWN'),
                'Duration (s)': step_result.get('duration', 0),
                'Error Message': step_result.get('error', '')
            })
        
        df_detailed = pd.DataFrame(detailed_data)
        df_detailed.to_excel(writer, sheet_name='Detailed Results', index=False)
        
        # Format detailed sheet
        worksheet = writer.sheets['Detailed Results']
        for column in worksheet.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = min(max_length + 2, 30)
            worksheet.column_dimensions[column_letter].width = adjusted_width
    
    def _create_steps_sheet(self, writer, test_steps):
        """Tạo sheet Test Steps"""
        steps_data = []
        
        for i, step in enumerate(test_steps, 1):
            steps_data.append({
                'Step': i,
                'Action': step.get('action', ''),
                'Object': step.get('object', ''),
                'Data': step.get('data', ''),
                'Note': step.get('note', '')
            })
        
        df_steps = pd.DataFrame(steps_data)
        df_steps.to_excel(writer, sheet_name='Test Steps', index=False)
        
        # Format steps sheet
        worksheet = writer.sheets['Test Steps']
        for column in worksheet.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = min(max_length + 2, 30)
            worksheet.column_dimensions[column_letter].width = adjusted_width
    
    def _create_statistics_sheet(self, writer, test_results):
        """Tạo sheet Statistics"""
        # Tính toán statistics
        total_steps = test_results['total_steps']
        successful = test_results['successful']
        failed = test_results['failed']
        success_rate = test_results['success_rate']
        
        # Thống kê theo action type
        action_stats = {}
        for step_result in test_results['step_results'].values():
            action = step_result.get('action', 'unknown')
            status = step_result.get('status', 'UNKNOWN')
            
            if action not in action_stats:
                action_stats[action] = {'success': 0, 'failed': 0, 'total': 0}
            
            action_stats[action]['total'] += 1
            if status == 'PASS':
                action_stats[action]['success'] += 1
            else:
                action_stats[action]['failed'] += 1
        
        # Tạo data cho statistics
        stats_data = []
        
        # Overall statistics
        stats_data.append({
            'Category': 'Overall',
            'Metric': 'Total Steps',
            'Value': total_steps,
            'Percentage': '100%'
        })
        stats_data.append({
            'Category': 'Overall',
            'Metric': 'Successful',
            'Value': successful,
            'Percentage': f"{success_rate:.1f}%"
        })
        stats_data.append({
            'Category': 'Overall',
            'Metric': 'Failed',
            'Value': failed,
            'Percentage': f"{100-success_rate:.1f}%"
        })
        
        # Action type statistics
        for action, stats in action_stats.items():
            action_success_rate = (stats['success'] / stats['total']) * 100 if stats['total'] > 0 else 0
            
            stats_data.append({
                'Category': 'Action Type',
                'Metric': action,
                'Value': f"{stats['success']}/{stats['total']}",
                'Percentage': f"{action_success_rate:.1f}%"
            })
        
        df_stats = pd.DataFrame(stats_data)
        df_stats.to_excel(writer, sheet_name='Statistics', index=False)
        
        # Format statistics sheet
        worksheet = writer.sheets['Statistics']
        for column in worksheet.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = min(max_length + 2, 25)
            worksheet.column_dimensions[column_letter].width = adjusted_width
    
    def generate_html_report(self, test_results, test_steps, execution_time):
        """Generate HTML report"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"test_report_{timestamp}.html"
            filepath = os.path.join(self.output_dir, filename)
            
            html_content = self._generate_html_content(test_results, test_steps, execution_time)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"✅ Đã tạo báo cáo HTML: {filepath}")
            return filepath
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi tạo báo cáo HTML: {e}")
            return None
    
    def _generate_html_content(self, test_results, test_steps, execution_time):
        """Generate HTML content"""
        html = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SBI FX Mobile Test Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .header {{
            text-align: center;
            border-bottom: 2px solid #007bff;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        .summary {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .summary-card {{
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            border-left: 4px solid #007bff;
        }}
        .summary-card.success {{
            border-left-color: #28a745;
        }}
        .summary-card.failed {{
            border-left-color: #dc3545;
        }}
        .summary-card h3 {{
            margin: 0;
            color: #333;
        }}
        .summary-card .value {{
            font-size: 2em;
            font-weight: bold;
            margin: 10px 0;
        }}
        .success .value {{
            color: #28a745;
        }}
        .failed .value {{
            color: #dc3545;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #007bff;
            color: white;
        }}
        .status-pass {{
            color: #28a745;
            font-weight: bold;
        }}
        .status-fail {{
            color: #dc3545;
            font-weight: bold;
        }}
        .error-message {{
            color: #dc3545;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 SBI FX Mobile Test Report</h1>
            <p>Excel Test Runner Framework</p>
            <p>Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        </div>
        
        <div class="summary">
            <div class="summary-card">
                <h3>Total Steps</h3>
                <div class="value">{test_results['total_steps']}</div>
            </div>
            <div class="summary-card success">
                <h3>Successful</h3>
                <div class="value">{test_results['successful']}</div>
            </div>
            <div class="summary-card failed">
                <h3>Failed</h3>
                <div class="value">{test_results['failed']}</div>
            </div>
            <div class="summary-card">
                <h3>Success Rate</h3>
                <div class="value">{test_results['success_rate']:.1f}%</div>
            </div>
            <div class="summary-card">
                <h3>Execution Time</h3>
                <div class="value">{execution_time:.2f}s</div>
            </div>
        </div>
        
        <h2>📋 Detailed Results</h2>
        <table>
            <thead>
                <tr>
                    <th>Step</th>
                    <th>Action</th>
                    <th>Object</th>
                    <th>Data</th>
                    <th>Status</th>
                    <th>Duration</th>
                    <th>Error</th>
                </tr>
            </thead>
            <tbody>
"""
        
        for i, step in enumerate(test_steps, 1):
            step_result = test_results['step_results'].get(i, {})
            status = step_result.get('status', 'UNKNOWN')
            status_class = 'status-pass' if status == 'PASS' else 'status-fail'
            
            html += f"""
                <tr>
                    <td>{i}</td>
                    <td>{step.get('action', '')}</td>
                    <td>{step.get('object', '')}</td>
                    <td>{step.get('data', '')}</td>
                    <td class="{status_class}">{status}</td>
                    <td>{step_result.get('duration', 0):.2f}s</td>
                    <td class="error-message">{step_result.get('error', '')}</td>
                </tr>
"""
        
        html += """
            </tbody>
        </table>
    </div>
</body>
</html>
"""
        
        return html 