from collections import OrderedDict
from threading import Lock  
from cache.src.lock import *

#LRU / LFU 캐시
class Cache:
    lock_caseses = {
        "fifo": FIFOLock,
        "priority": PriorityBasedLock,
        "random": RandomLock,
        "simple": SimpleLock,  # 기본 락
        "thread": Lock
    }
    
    def __init__(self, max_size=10 , lock_type = "simple"):
        
        self._cache = OrderedDict() # (value, freq) 튜플 저장
        self.max_size = max_size
        self._lock = self.lock_caseses.get(lock_type, SimpleLock)()


    def get(self, key):
        with self._lock : 
            if key in self._cache:
                value , freq = self._cache.pop(key)
                self._cache[key] = (value, freq + 1)
                return value
            return None


    def put(self, key, value):
        with self._lock : 
            # 캐시의 키가 이미 있는 경우라면? 빈도를 업데이트해야함
            if key in self._cache : 
                _, freq = self._cache.pop(key)
                self._cache[key] = (value, freq + 1)
            else : 
                #캐시가 없으면 추가
                if len(self._cache) >= self.max_size :
                    # 최대 사이즈를 넘으면 삭제해야함
                    least_freq_key = min(self._cache, key=lambda x  : self._cache[x][1])
                    self._cache.pop(least_freq_key)
                self._cache[key] = (value, 1) # 값, freq
