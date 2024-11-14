LRU (Least Recently Used)와 LFU (Least Frequently Used)는 캐시 관리와 같은 상황에서 데이터 교체 정책으로 사용되는 두 가지 방식

1. LRU (Least Recently Used)
정의: 가장 최근에 사용되지 않은 데이터를 먼저 제거하는 정책

2. LFU (Least Frequently Used)
정의: 가장 사용 빈도가 낮은 데이터를 먼저 제거하는 정책


삭제 조건
1. 사용 빈도가 낮은 순
2. 오래된 순


@dataclass #python 3.7 부터 도입된 데코레이터 init, repr, eq,str, 함수 자동 생성
 반복적인 보일러플레이트 코드를 줄여주는데 유용



def __str__(self): #객체를 문자열로 변환할 때 사용

- 딕셔너리 키로 사용 (문자열 필요)
- 로깅할 때 readable한 형태로 출력
- 디버깅 시 객체 확인 용이

동시에 접근할때?
->  락을 건다?
from threading import Lock

self._lock = Lock()

with self._lock :
-> 락 객체를 사용하여 락을 획득하고 with 블록이 끝나면 자동으로 해제


Lock 없이 락 구현하기



문법: dictionary.get(key, default_value)
	•	key: 찾고자 하는 키
	•	default_value: key가 딕셔너리에 없을 때 반환할 기본값 (옵션)


With 문
- 컨텍스트 관리를 위해 도입
- 특정 작업 전후에 자동으로 초기화 및 정리 작업 수행 가능
    -  파일 입출력, 데이터베이스 연결, 락(ㅣock) 자원관리에 응용

with 컨텍스트_관리자 as 변수:
    코드 블록

- 컨텍스트 관리자: with 문에서 관리할 대상
- as 변수: 컨텍스트 관리자에서 반환된 값을 사용할 수 있게 함(생략 가능)
- 코드 블록 : with 안에서 실행할 것 


with open("example.txt", "w") as file:
    file.write("Hello, world!") # 알아서 파일 닫아짐


커스텀 락에서도 with를 사용하려면 __enter__이랑 __exit__ 를 추가해얗마


