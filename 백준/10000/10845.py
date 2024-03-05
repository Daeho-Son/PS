from collections import deque
import sys


class Queue:
    __q = deque()

    def push(self, x):
        self.__q.append(x)

    def pop(self):
        print(self.__q.popleft() if self.__q else -1)

    def size(self):
        print(len(self.__q))

    def empty(self):
        print(0 if self.__q else 1)

    def front(self):
        print(self.__q[0] if self.__q else -1)

    def back(self):
        print(self.__q[-1] if self.__q else -1)

    def print(self):
        print(self.__q)

input = sys.stdin.readline
n = int(input())
queue = Queue()
for _ in range(n):
    command = input().split()
    c = command[0]
    if c == "push":
        queue.push(command[1])
    elif c == "pop":
        queue.pop()
    elif c == "size":
        queue.size()
    elif c == "empty":
        queue.empty()
    elif c == "front":
        queue.front()
    elif c == "back":
        queue.back()
    elif c == "print":
        queue.print()