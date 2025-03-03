from collections import deque

class MovingAverage:
  def __init__(self, size: int):
    self.size = size
    self.queue = []

  def next(self, val: int) -> float:
    self.queue.append(val)

    avg = sum(self.queue[-self.size:])/min(self.size, len(self.queue))

    return avg


class MovingAverageFast:
  def __init__(self, size: int):
    self.size = size
    self.queue = deque()
    self.window_sum = 0
    self.count = 0

  def next(self, val: int) -> float:
    self.count += 1
    self.queue.append(val)
    if self.count > self.size:
      tail = self.queue.popleft()
    else:
      tail = 0
    self.window_sum = self.window_sum - tail + val
    return self.window_sum/min(self.size, self.count)

movingAverage = MovingAverage(3)

ans = movingAverage.next(1)
print(ans)
ans = movingAverage.next(10)
print(ans)
ans = movingAverage.next(3)
print(ans)
ans = movingAverage.next(5) 
print(ans)

movingAverageFast = MovingAverageFast(3)
ans = movingAverageFast.next(1)
print(ans)
ans = movingAverageFast.next(10)
print(ans)
ans = movingAverageFast.next(3)
print(ans)
ans = movingAverageFast.next(5) 
print(ans)
