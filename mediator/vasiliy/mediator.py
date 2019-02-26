import uuid


class Registry:
    def __init__(self):
        self.available_tasks = list(range(20))
        self.reserved_tasks = []

    def finalize(self, task_id):
        self.reserved_tasks.remove(task_id)

    def get_new(self):
        if self.available_tasks:
            task_id = self.available_tasks.pop()
            self.reserved_tasks.append(task_id)
            return task_id


class Worker:
    def __init__(self, registry: Registry):
        self.registry = registry
        self.worker_id = uuid.uuid4()

    def run(self):
        task_id = self.registry.get_new()
        if task_id:
            print(f'task {task_id} was processed by {self.worker_id}')
            self.registry.finalize(task_id)
        else:
            print('all tasks were exhausted')


if __name__ == '__main__':
    registry = Registry()
    workers = [Worker(registry) for i in range(5)]

    for i in range(23):
        worker = workers.pop(0)
        worker.run()
        workers.append(worker)
