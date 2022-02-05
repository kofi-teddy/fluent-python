# oop 
# data structures 
import queue
from typing import TYPE_CHECKING, Deque, List


class ListQueue(List[Path]):
    def put(self, item: Path) -> None:
        self.append(item)

    def get(self) -> Path:
        return self.pop(0)

    def empty(self) -> bool:
        return len(self) == 0


class DeQueue(Deque[Path]):
    def put(self, item: Path) -> None:
        self.append(item)

    def get(self) -> Path:
        return self.popleft()
    
    def empty(self) -> bool:
        return len(self) == 0


if TYPE_CHECKING:
    BaseQueue = queue.Queue[Path] 
else:
    BaseQueue = queue.Queue


class ThreadQueue(BaseQueue):
    pass
