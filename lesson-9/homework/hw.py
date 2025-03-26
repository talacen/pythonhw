####################### 1

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())


####################### 2

from datetime import date

class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def age(self):
        current_year = date.today().year
        return current_year - self.birth_year

p = Person("Alice", "USA", 1990)
print("Age:", p.age()) 


####################### 3

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

calc = Calculator()
print(calc.add(5, 3))       
print(calc.divide(10, 2))   


####################### 4

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


s = Square(4)
print("Square Area:", s.area())
print("Square Perimeter:", s.perimeter()) 


####################### 5

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(value, current.left)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(value, current.right)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, current):
        if current is None:
            return False
        if value == current.value:
            return True
        if value < current.value:
            return self._search(value, current.left)
        return self._search(value, current.right)

bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
print(bst.search(5))
print(bst.search(20))


####################### 6

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"

s = Stack()
s.push(10)
s.push(20)
print(s.pop())


####################### 7

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.display() 


####################### 8

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, price):
        self.cart[item] = price

    def remove_item(self, item):
        if item in self.cart:
            del self.cart[item]

    def total(self):
        return sum(self.cart.values())

cart = ShoppingCart()
cart.add_item("Apple", 1.2)
cart.add_item("Banana", 0.8)
print(cart.total())

####################### 9

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"

    def display(self):
        print(self.stack)

s = Stack()
s.push(10)
s.display() 


####################### 10

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else "Queue is empty"

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())


####################### 11

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

account = BankAccount("John Doe", 1000)
print(account.deposit(500))  
print(account.withdraw(200)) 


####################### 12

