from collections.abc import Sequence


class SortedList(Sequence):

    def __init__(self, iterable=()):
        self.iterable = sorted(iterable[:])
        self.append = self.extend = self.reverse = self.insert

    def __repr__(self):
        return f'{self.__class__.__name__}({self.iterable})'

    def __getitem__(self, item):
        return self.iterable[item]

    def __contains__(self, item):
        return item in self.iterable

    def __len__(self):
        return len(self.iterable)

    def add(self, other):
        self.iterable.append(other)
        self.iterable.sort()

    def discard(self, item):
        while item in self.iterable:
            self.iterable.remove(item)

    def update(self, other):
        self.iterable.extend(other)
        self.iterable.sort()

    def insert(self, *other):
        raise NotImplementedError

    def __reversed__(self):
        raise NotImplementedError

    def __delitem__(self, key):
        del self.iterable[key]

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.iterable + other.iterable)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.iterable += other.iterable
            return self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__class__(self.iterable * other)
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            self.iterable *= other
            self.iterable.sort()
            return self
        return NotImplemented


numbers = SortedList([5, 4, 3, 2, 1])

numbers.update([5, 4, 3, 2, 1])
print(*numbers)

numbers *= 3
print(*numbers)

numbers.discard(4)
print(*numbers)