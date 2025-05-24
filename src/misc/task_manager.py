from typing import List


class MaxHeap:
    def __init__(self, tasks):
        self.tasks = []
        self._heapify(tasks)

    def _heapify(self, tasks):
        for elem in tasks:
            self.insert(elem)

    def insert(self, elem):
        self.tasks.append(elem)
        length = len(self.tasks)
        self._swim(length - 1)

    def pop(self):
        elem = self.tasks[0]
        self.tasks[0], self.tasks[-1] = self.tasks[-1], self.tasks[0]
        self.tasks.pop()
        self.sink(0)
        return elem

    def _swim(self, idx):
        par_idx = self._parent(idx)
        while par_idx >= 0 and self._compare(idx, par_idx):
            self.tasks[par_idx], self.tasks[idx] = self.tasks[idx], self.tasks[par_idx]
            idx = par_idx
            par_idx = self._parent(idx)

    def _compare(self, idx1, idx2):
        task1 = self.tasks[idx1]
        task2 = self.tasks[idx2]
        if task1.priority != task2.priority:
            return task1.priority > task2.priority
        else:
            return task1.task_id > task2.task_id

    def sink(self, idx):
        left, right = self._children(idx)
        while left < len(self.tasks):
            switch_idx = left
            if right < len(self.tasks) and self._compare(right, left):
                switch_idx = right
            if self._compare(switch_idx, idx):
                self.tasks[idx], self.tasks[switch_idx] = self.tasks[switch_idx], self.tasks[idx]
                idx = switch_idx
                left, right = self._children(idx)
            else:
                break

    def empty(self):
        return len(self.tasks) == 0

    def _children(self, idx: int) -> List[int]:
        left = 2 * idx + 1
        right = 2 * idx + 2
        return left, right

    def _parent(self, idx: int) -> int:
        parent = (idx - 1) // 2
        return parent

    def print_heap(self):
        print(self.tasks)


class Task:
    def __init__(self, user_id, task_id, priority):
        self.user_id = user_id
        self.task_id = task_id
        self.priority = priority
        self.removed = False


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = []
        self.task_map = {}
        self._create_tasks(tasks)

    def _create_tasks(self, tasks):
        for t in tasks:
            task = Task(t[0], t[1], t[2])
            self.tasks.append(task)
            self.task_map[t[1]] = task
        self.max_heap = MaxHeap(self.tasks)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        task = Task(userId, taskId, priority)
        self.tasks.append(task)
        self.task_map[taskId] = task
        self.max_heap.insert(task)

    def edit(self, taskId: int, newPriority: int) -> None:
        task = self.task_map[taskId]
        new_task = Task(task.user_id, task.task_id, newPriority)
        task.removed = True
        self.max_heap.insert(new_task)
        self.task_map[task.task_id] = new_task

    def rmv(self, taskId: int) -> None:
        task = self.task_map[taskId]
        task.removed = True
        self.task_map.pop(taskId)

    def execTop(self) -> int:
        res = -1
        while not self.max_heap.empty():
            task = self.max_heap.pop()
            if task.removed:
                if task.task_id in self.task_map:
                    t = self.task_map[task.task_id]
                    if t.removed:
                        self.task_map.pop(task.task_id)
            else:
                return task.user_id
        return res


[[[[4,14,27]]],[7,4,15],[4],[0,15,33],[15,16],[],[1,7,36],[15,37],[]]

tm = TaskManager([[4,14,27]])
tm.add(7,4,15)
tm.rmv(4)
tm.add(0,15,33)
tm.edit(15,16)
a = tm.execTop()
print(a)
tm.add(1,7,36)
tm.edit(15,37)
tm.execTop()