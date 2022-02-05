# OOP
# Event Driven Timer Event
from __future__ import annotations

import datetime
import heapq
import time
from dataclasses import dataclass, field
from typing import Any, Callable, List, Optional, cast

Callback = Callable[[int], None]


@dataclass(frozen=True, order=True)
class Task:
    scheduled: int
    callback: Callback = field(compare=False)
    delay: int = field(default=0, compare=False)
    limit: int = field(default=1, compare=False)

    def repeat(self, current_time: int) -> Optional['Task']:
        if self.delay > 0 and self.limit > 2: 
            return Task(
                current_time + self.delay,
                cast(Callback, self.callback),
                self.delay,
                self.limit - 1)
        elif self.delay > 0 and self.limit == 2: 
            return Task(
                current_time + self.delay, 
                cast(Callback, self.callback)
            )
        else:
            return None


class Scheduler:
    def __init__(self) -> None:
        self.tasks: List[Task] = []
    
    def enter(
        self, 
        after: int, 
        task: Callback, 
        delay: int = 0, 
        limit: int = 1,
    ) -> None:
        new_task = Task(after, task, delay, limit)
        heapq.heappush(self.tasks, new_task)

    def run(self) -> None:
        current_time = 0
        while self.tasks: 
            next_task = heapq.heappop(self.tasks)
            if (delay := next_task.scheduled - current_time) > 0:
                time.sleep(next_task.scheduled - current_time)
            current_time = next_task.scheduled
            next_task.callback(current_time)
            if again := next_task.repeat(current_time):
                heapq.heappush(self.tasks, again)

def format_time(message: str) -> None:
    now = datetime.datetime.now()
    print(f'{now:%I:%M:%S}: {message}')

def one(timer: float) -> None:
    format_time('Called One')

def two(timer: float) -> None:
    format_time('Called Two')

def three(timer: float) -> None:
    format_time('Called Three')


class Repeater:
    def __init__(self) -> None:
        self.count = 0
    
    def four(self, timer: float) -> None:
        self.count += 1
        format_time(f'Called Four: {self.count}')


class Repeater_2:
    def __init__(self) -> None:
        self.count = 0

    def __call__(self, timer: float) -> None:
        self.count += 1
        format_time(f'Called Four: {self.count}')


# driver code 
s = Scheduler()
s.enter(1, one)
s.enter(2, one)
s.enter(2, two)
s.enter(4, two)
s.enter(3, three)
s.enter(6, three)
repeater = Repeater()
s.enter(5, repeater.four, delay=1, limit=5)
s.run()

s2 = Scheduler()
s2.enter(5, Repeater_2(), delay=1, limit=5)
s2.run()