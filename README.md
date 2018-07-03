Object Segmentation với thuật toán MeanShift.

* Đề tài : Phân đoạn ảnh với thuật toán meanshift
* Ý tưởng:
  - Với mỗi vật thể có trong ảnh ta sẽ xác định được phân vùng của chúng nhờ màu sắc. Mỗi vật thể được biểu diễn bới 1 cụm màu sắc có độ tương đồng như nhau nằm lân cận với nhau thành từng cụm. Mỗi cụm đó được phân đoạn với nhau theo màu sắc, cường độ,... 
  - Việc gom nhóm các cụm ta sẽ quét từng khoanh vùng nhất định cho trước (một vòng tròn bán kính R) để lấy ra các điểm lận cận của các điểm được gọi là cụm trung tâm
  - Mỗi cụm trung tâm đó sẽ bao quát được các điểm lân cận có mức độ màu sắc trung bình của các cụm điểm.
  - Nếu như tại điểm trung tâm đó chưa thỏa ngưỡng giá trị cho trước (còn các điểm lân cận thỏa mãn hoặc có các điểm không thỏa mãn mà lại phụ thuộc vào nó thì ta sẽ tính lại vị trí trung tâm của cụm
  - Nếu vị trí trung tâm đó không thay đổi thì ta lưu lại thông tin của cụm đó, tiếp tục quét các cụm còn lại của ảnh

*Hiện thực:
- Nhập tên bức ảnh cần phân đoạn
- Chạy file trên trình biên dịch
- Chờ chương trình xử lý và đưa ra kết quả

Goodluck!!
