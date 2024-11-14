from cache_system.src.cache import Cache  # Cache 클래스 임포트
from cache_system.src.lock import FIFOLock, PriorityBasedLock, RandomLock  # 필요한 락 클래스 임포트
import threading

#캐시 생성
cache_fifo  = Cache(max_size=5,lock_type="fifo")

# 캐시에 데이터를 추가하고 접근하는 작업
def cache_operations(thread_id):
    for i in range(3):
        key = f"key-{thread_id}-{i}"
        value = f"value-{thread_id}-{i}"
        # 캐시에 데이터 추가
        cache_fifo.put(key, value)
        print(f"[Thread-{thread_id}] Put {key} = {value}")

        # 캐시에서 데이터 가져오기
        retrieved_value = cache_fifo.get(key)
        print(f"[Thread-{thread_id}] Get {key} = {retrieved_value}")

# 스레드 리스트 생성
threads = [threading.Thread(target=cache_operations, args=(i,)) for i in range(3)]

# 모든 스레드 시작
for thread in threads:
    thread.start()

# 모든 스레드가 종료될 때까지 대기
for thread in threads:
    thread.join()

print("모든 스레드 작업 완료.")