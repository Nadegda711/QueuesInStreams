from  queue import Queue

q = Queue
q.put(5)
print(q.get(timeout=2))
print('Конец программы')
