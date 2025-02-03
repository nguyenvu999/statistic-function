# Sử dụng Python image nhẹ
FROM python:3.9-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Copy các file vào container
COPY . /app

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Expose cổng 5000 để container sử dụng
EXPOSE 5000

# Chạy ứng dụng Flask với Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
