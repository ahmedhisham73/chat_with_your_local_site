FROM python:3.11-slim

WORKDIR /app
COPY . .

# ✅ تثبيت كل المتطلبات للبناء + GIT
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
 && pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]

