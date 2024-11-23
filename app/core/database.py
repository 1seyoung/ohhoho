# SQLAlchemy를 사용하여 데이터베이스 연결 / 설정 / 관리

from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import Pool

from contextlib import contextmanager
from config import settings  # .env에서 DATABASE_URL 가져옴

# SQLAlchemy 엔진 생성
# - SQLAlchemy에서 데이터베이스와 상호작용하기 위한 엔진 객체를 생성.
# - settings.DATABASE_URL: .env 파일에서 가져온 데이터베이스 연결 문자열 (ex: mysql+pymysql://user:password@host:port/dbname).
# - pool_pre_ping=True: 데이터베이스 연결이 유효한지 확인하기 위해 “ping” 명령을 보냄, 데이터베이스 연결이 끊어졌을 때 자동으로 재연결을 시도.
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# 세션 로컬 생성
# - 데이터베이스와의 작업(쿼리 및 트랜잭션)을 수행하기 위한 세션 팩토리.
# - autocommit=False: 세션의 변경 사항을 자동으로 커밋하지 않음. 명시적으로 commit()을 호출해야 저장.
# - autoflush=False: 세션에 추가된 객체가 자동으로 데이터베이스로 플러시되지 않음. 필요한 경우 flush()를 호출하여 변경 내용을 반영.
# - bind=engine: 이 세션이 engine 객체를 통해 데이터베이스와 연결됨을 지정
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스 정의 (ORM 사용 시 필요)
# - SQLAlchemy의 Declarative 시스템에서 모든 ORM 모델이 상속받는 기본 클래스.
Base = declarative_base()

# 연결 확인 함수
def check_database_connection():
    try:
        with engine.connect() as connection:
            connection.execute("SELECT 1")
            print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")

# 세션 컨텍스트 매니저
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 연결 풀 설정 (MySQL 예시)
@event.listens_for(Pool, "connect")
def set_sql_mode(dbapi_connection, connection_record):
    with dbapi_connection.cursor() as cursor:
        cursor.execute("SET sql_mode='STRICT_TRANS_TABLES'")