class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, elem):
        self.top = self.top + 1
        self.stack.append(elem)

    def pop(self):
        result = self.stack[self.top]
        self.stack.pop(self.top)
        self.top = self.top - 1
        return result

    def peek(self):
        return self.top

    def __str__(self):
        result = ''
        for item in self.stack:
            result += str(item) + ' '
        return result

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack)

print(stack.peek())

print(stack.pop())

print(stack.peek())

print(stack)