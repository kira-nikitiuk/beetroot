# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss. You're not allowed to add instances of Boss class to workers list directly via access to attribute, use getters and setters instead!
# You can refactor the existing code.
# '''
# id_ - is just a random unique integer
# class Boss:
#     def __init__(self, id_: int, name: str, company: str): 
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.workers = []

# class Worker:
#     def __init__(self, id_: int, name: str, company: str, boss: Boss):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.boss = boss
# '''


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.append(worker)
        else:
            raise ValueError

    def get_workers(self):
        return self.workers

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            if self._boss is not None:
                self._boss.workers.remove(self)
            self._boss = new_boss
            new_boss.add_worker(self)
        else:
            raise ValueError

if __name__ == "__main__":
    boss1 = Boss(1, "boss1", "company1")
    boss2 = Boss(2, "boss2", "company2")

    worker1 = Worker(101, "worker1", "company1", boss1)
    worker2 = Worker(102, "worker2", "company1", boss1)
    worker3 = Worker(103, "worker3", "company2", boss2)

    print("boss1's workers:", [worker.name for worker in boss1.get_workers()])
    print("boss2's workers:", [worker.name for worker in boss2.get_workers()])


    worker1.boss = boss2
    print("worker1's new boss:", worker1.boss.name)
