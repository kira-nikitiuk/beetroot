# Task 1
# A shared counter
# Make a class called Counter, and make it a subclass of the Thread class in the Threading module.
# Make the class have two global variables, one called counter set to 0, and another called rounds set to 100.000.
# Now implement the run() method, let it include a simple for-loop that iterates through rounds (e.i. 100.000 times)
# and for each time increments the value of the counter by 1. 
# Create 2 instances of the thread and start them, then join them and check the result of the counter, 
# it should be 200.000, right? Run it a couple of times and consider some different reasons why you get the answer that you get. 

import threading

class Counter(threading.Thread):
    counter = 0
    rounds = 100000
    lock = threading.Lock()
    
    def run(self):
        for _ in range(self.rounds):
            with self.lock:
                Counter.counter += 1 

# створення екземплярів класа каунтер
thread1 = Counter()
thread2 = Counter()

# запуск потоків 
thread1.start()
thread2.start()

# очікування завершення потоків
thread1.join()
thread2.join()

# кінцеве значення каунтера
print("очікуване значення каунтера:", Counter.rounds * 2)
print("фактичне значення каунтера:", Counter.counter)
