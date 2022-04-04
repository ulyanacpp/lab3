
class Stack:

    def __init__(self):
        self._stack = []

    def __iter__(self):
        return self

    def __next__(self):
        value = self.pop()

        if value is None:
            raise StopIteration

        return value

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        if len(self._stack) == 0:
            return None

        return self._stack.pop()
