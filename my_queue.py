class Queue:
    """
    q = [1,2,5,8]
    st = [
    """
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        current = self.q
        stack = []
        while current:
            stack.append(current.pop())
        return stack.pop()

    def print(self):
        current = self.q
        stack = []
        while current:
            stack.append(current.pop())
        while stack:
            print(stack.pop())

