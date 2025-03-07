# Gunakan Python sebagai base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Salin file aplikasi
COPY app.py .
COPY static/ static/

# Salin file dependency
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan aplikasi
CMD ["python", "app.py"]