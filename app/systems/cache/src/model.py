from dataclasses import dataclass, field
from datetime import datetime



@dataclass #python 3.7 부터 도입된 데코레이터 init, repr, eq,str, 함수 자동 생성
class CacheKey:
    type: str
    resource_id: str
    created_at: datetime = field(default_factory=datetime.now)  # 기본값
    
    def __str__(self): #객체를 문자열로 변환할 때 사용
        return f"{self.type}:{self.resource_id}:{self.created_at.isoformat()}"
    
