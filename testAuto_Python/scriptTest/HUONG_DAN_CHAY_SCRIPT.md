# Hướng dẫn chạy Excel Test Runner

## 🚀 **Cách chạy script**
# Chuẩn bị file Object repository | test case
1.  file excel chứa object repository . 
Cấu trúc : 
ObjectName       | LocatorType       | LocatorValue        |Description        |Screen
Giải thích: 
+ ObjectName : Tên object được tham chiếu qua file test case
+ LocatorType : Loaị đối tượng . 
+ LocatorValue : Vị trí xpath của đối tượng . 
+ Description : Mô tả 
+ Screen :  màn hình . 
ví dụ : testdata/ObjectRepository.xlsx ( sheet 1)

2.  file excel chứa chứa test script . 
Cấu trúc :
Run/NoRun       | Action           |         Object        | Data|Note
Giải thích:
+ Run/NoRun : mô tả chạy lệnh hay không chạy lệnh 
+ Action :  hành vi thực hiện trên app
+ Object: Tên đối tượng được tham chiếu qua bên file Object repository để lấy localtion chính xác 
+ Data: tên biến data    
+ Note : ghi chú lại hành vi
ví dụ : testdata/TestCase.xlsx  ( sheet 1)

3.  file excel chứa test data . 
Cấu trúc :
Tên biến data     | value           | Note
Giải thích:
+ Tên biến data : tên biến data đùng dể khai vào file test case 
+ value : data sẽ điền vào script để chạy . 
+ Note : ghi chú 

Cách hoạt động auto mong muốn : 
1. Viết hàm get xpath của tất cả các đối tượng trên màn hình UI tương ứng với devices chuẩn .Xuất ra file excel có cấu trúc : 
ObjectName       | LocatorType       | LocatorValue        |Description        |Screen
Giải thích: 
+ ObjectName : Tên object được tham chiếu qua file test case
+ LocatorType : Loaị đối tượng . 
+ LocatorValue : Vị trí xpath của đối tượng . 
+ Description : Mô tả 
+ Screen :  màn hình .
2. Chuyển đổi file test case manual => auto kết hợp với đối tượng vừa xuất ra ở bước 1 thành file script có cấu trúc như sau : 
Run/NoRun       | Action           |         Object        | Data|Note
Giải thích:
+ Run/NoRun : mô tả chạy lệnh hay không chạy lệnh 
+ Action :  hành vi thực hiện trên app
+ Object: Tên đối tượng được tham chiếu qua bên file Object repository để lấy localtion chính xác 
+ Data: tên biến data    
+ Note : ghi chú lại hành vi
3. Chỉnh lại framework để có thể thực hiện chạy nhiều script trong 1 lần chạy . 

### **1. Real Mode (Cần Appium và thiết bị)**
```bash
# Chạy thực tế trên thiết bị
python run_excel_tests.py
```


### **Cho người dùng thực tế**
```bash
# 1. Cài đặt đầy đủ
pip install -r requirements.txt

# 2. Khởi động Appium
appium

# 3. Kết nối thiết bị
adb devices

# 4. Cài đặt UIAutomator2
UIAutomator2

# 5. Cài đặt selenium.webdriver
selenium.webdriver

# 4. Thiết lập environment
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

# 5. Chạy tests
python run_excel_tests.py
```

## 📈 **Best Practices**

1. **Kiểm tra thiết bị** trước khi chạy real tests
2. **Xem logs** để debug khi có lỗi
3. **Backup Excel file** trước khi chỉnh sửa
4. **Sử dụng meaningful names** cho screenshots và reports

``` 