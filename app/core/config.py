# Settings 클래스는 환경 변수를 읽는 데 사용


from pandantic import BaseSettings
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")  # .env 파일에서 읽음

    class Config:
        env_file = ".env"  # .env 파일 경로 명시 (기본값은 루트 디렉토리)

# 설정 객체 생성
settings = Settings()