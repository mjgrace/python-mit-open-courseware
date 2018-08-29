from Queue import Queue

queue = Queue()
queue.insert(5)
queue.insert(6)
print queue.remove()

queue.insert(7)
print queue.remove()

print queue.remove()

print queue.remove()