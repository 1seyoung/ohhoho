FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# PYTHONPATH 환경 변수 설정
ENV PYTHONPATH="${PYTHONPATH}:/app"

# app.py 실행
CMD ["python", "app.py"]