import time
import threading
import random
from queue import Queue, PriorityQueue

#First in First out
#대기열에 먼저 들어온 스레드가 먼저 자원을 사용하는 방식

class SimpleLock:
    def __init__(self):
        self.is_locked = False  # 초기에는 잠겨 있지 않은 상태

    # 잠금
    def acquire(self):
        while self.is_locked:  # 이미 잠겨 있다면 기다림
            time.sleep(0.01)  # 잠시 대기 (다른 스레드에 CPU를 넘기기 위함)
        self.is_locked = True  # 잠금을 설정하여 접근 시작

    # 잠금 해제
    def release(self):
        self.is_locked = False  # 잠금을 해제하여 다른 스레드가 접근 가능하게 함

    # with 문에서 사용할 수 있도록 __enter__와 __exit__ 메서드 추가
    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.release()



class FIFOLock(SimpleLock):
    def __init__(self):
        super().__init__()
        self.queue = Queue()

    def acquire(self):
        current_thread = threading.current_thread() # 현재 스레드를 대기열에 추가
        self.queue.put(current_thread) #
        
        #차례가 올 때까지 대기 (조건 1 : 현재 대기열에 맨앞이 지금 스레드이면, 조건 2: 다른 스레드가 사용 중이라면)
        # 대기열의 맨 앞에 있으면서 자원이 잠겨 있지 않을때
        while self.queue.queue[0] != current_thread or self.is_locked:
            time.sleep(0.01)
        
        #두 조건 만족해서 빠져나가면 현재 스레드가 자원 사용할 수 있는 상태됨
        self.is_locked = True
        self.queue.get() #호출해서 제거



#스레드의 우선선위를 기준으로 높은 우선순위가 먼저 자원을 획득하는 방식
# 실시간 시스템, 우선순위 중요한 시스템
class PriorityBasedLock(SimpleLock):
    def __init__(self):
        super().__init__()
        self.queue = PriorityQueue()

    def acquire(self):
        current_thread = threading.current_thread()
        self.queue.put(current_thread)

        while self.queue[0][1] != current_thread or self.is_locked :
            time.sleep(0.01)
        
        self.is_locked = True
        self.queue.get()



# 락이 해제될때 대기열에서 무작위로 스레드를 선택해 사용
# 부하 분산 목적
class RandomLock(SimpleLock):
    def __init__(self):
        super().__init__()
        self.queue = []

    def acquire(self):
        current_thread = threading.current_thread()
        self.queue.append(current_thread)

        while self.is_locked or self.queue[0] != current_thread:
            time.sleep(0.01)
            # 락 해제 시 랜덤으로 대기열 재정렬
            if not self.is_locked:
                random.shuffle(self.queue)

        self.is_locked = True
        self.queue.pop(0)

