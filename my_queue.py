from typing import List, Optional


class MyQueue:
    def __init__(self) -> None:
        self.data: List[Optional[int]] = []

    def enqueue(self, element: int) -> None:
        self.data.append(element)

    def dequeue(self) -> Optional[int]:
        if self.data:
            return self.data.pop(0)
        return None

    def read(self) -> Optional[int]:
        if self.data:
            return self.data[0]
        return None


class PrintManager:
    def __init__(self):
        self.queue = MyQueue()

    def queue_print_job(self, document: str) -> None:
        self.queue.enqueue(document)

    def run(self) -> None:
        # Each time this loop runs, we read the document at the front of the queue:
        while self.queue.read():
            # We dequeue the document and print it:
            print(self.queue.dequeue())

    def print(self, document: str) -> None:
        # Code to run the actual printer goes here.
        # For demo purposes, we'll print to the terminal:
        print(document)


print_manager = PrintManager()
print_manager.queue_print_job("First Document")
print_manager.queue_print_job("Second Document")
print_manager.queue_print_job("Third Document")
print_manager.run()



