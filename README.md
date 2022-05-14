         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 

## Đề tài: Tìm hiểu Amazon Cloud9 và viết ứng dụng minh họa

    Trần Thành Quang - 19133047
    Bùi Quốc Kiệt    - 19133030
    Phạm Thanh Bách  - 19133007
## Các dịch vụ sử dụng trong AWS

-   AWS RDS
-   AWS cloud9
-   AWS EC2

## Cài đặt và xây dựng ứng dụng trên AWS cloud9 
### Cài đặt AWS cloud9
-   **Tìm kiếm AWS cloud9 trên**
  
![image](https://user-images.githubusercontent.com/93425051/168407648-c3730a42-83ca-4f84-a637-3fe3d9c5eac3.png)

-   **Trên giao diện ta click vào Create Environment để tạo IDE**

![image](https://user-images.githubusercontent.com/93425051/168407665-a2d7f93d-a484-48aa-bba1-14c0f22e1a75.png)

-   **Đặt tên cho IDE**

![image](https://user-images.githubusercontent.com/93425051/168407675-efda999b-39ad-4e18-be29-779c8f0628f1.png)

-   **Cài đặt cấu hình**

![image](https://user-images.githubusercontent.com/93425051/168407682-e1f613a7-9a72-4bfa-84c4-e997e7b24ee3.png)

         ở bước này thì bạn chọn cách tạo IDE , cấu hình máy instance thích hợp
         
![image](https://user-images.githubusercontent.com/93425051/168407692-9d81afd9-959b-4653-b817-522d0754b262.png)

         Chọn nền tản platform để chạy và một số thứ khác
         
-  **Xem lại cấu hình**

![image](https://user-images.githubusercontent.com/93425051/168407738-8173d32c-f6ac-4fe2-b58b-60994a28b263.png)

         Sau khi xem sau bạn nhấn vào:***Create enviroment***
 
-   **Giao diện của cloud9 IDE**

![image](https://user-images.githubusercontent.com/93425051/168407783-f82c3fd7-f342-444e-b4b8-9b84a8643813.png)

### Để chạy code trên Cloud9
-   B1: Cài đặt python 3.8 
-   B2: tải code lên
-   B3: Thiết lập port và địa chỉ Ip ở EC2
-   B4: Thay đổi đường dẫn database ( __init__.py dòng 18)
-   B5: Cài đặt thư viện ở file reqiurement.txt 
-   Lưu ý: Cài đặt Database bằng folder backupsql

####  *Bạn có thể tham khảo thêm thông tin của AWS Cloud9 ở nguồn này.
 https://docs.aws.amazon.com/console/cloud9/
