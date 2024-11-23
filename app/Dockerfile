FROM python:3.9-slim AS base
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# [local ver]
# docker build --target dev -t fastapi-app-dev .
# docker run -p 8000:8000 fastapi-app-dev

FROM base AS dev
COPY . ./
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


# 상세 정보 미정 AWS 
FROM base AS prod
COPY . ./
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]