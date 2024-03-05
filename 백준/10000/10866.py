from collections import deque
import sys


class Deque:
    __deque = deque()

    def push_front(self, x):
        self.__deque.appendleft(x)

    def push_back(self, x):
        self.__deque.append(x)

    def pop_front(self):
        print(self.__deque.popleft() if self.__deque else -1)

    def pop_back(self):
        print(self.__deque.pop() if self.__deque else -1)

    def size(self):
        print(len(self.__deque))

    def empty(self):
        print(0 if self.__deque else 1)

    def front(self):
        print(self.__deque[0] if self.__deque else -1)

    def back(self):
        print(self.__deque[-1] if self.__deque else -1)


input = sys.stdin.readline
n = int(input())
dq = Deque()
for _ in range(n):
    command = input().split()
    c = command[0]
    if c == "push_front":
        dq.push_front(command[1])
    elif c == "push_back":
        dq.push_back(command[1])
    elif c == "pop_front":
        dq.pop_front()
    elif c == "pop_back":
        dq.pop_back()
    elif c == "size":
        dq.size()
    elif c == "empty":
        dq.empty()
    elif c == "front":
        dq.front()
    elif c == "back":
        dq.back()
