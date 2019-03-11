import math


class Vector2D(object):
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def to_tuple(self):
        return self.x, self.y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def magnitude_squared(self):
        return self.x**2 + self.y**2

    def __add__(self, rhs):
        return Vector2D(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vector2D(self.x - rhs.x, self.y - rhs.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def copy(self):
        return Vector2D(self.x, self.y)


class Stack(object):
    def __init__(self):
        self.items = []

    def length(self):
        return len(self.items)

    def is_empty(self):
        if self.length() > 0:
            return False
        return True

    def clear(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.length() > 0:
            removed_item = self.items.pop(len(self.items)-1)
            return removed_item
        return None

    def peek(self):
        if self.length() > 0:
            return self.items[self.length()-1]
        return None
