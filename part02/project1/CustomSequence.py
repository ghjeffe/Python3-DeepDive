from functools import lru_cache


class Silly():
    def __init__(self, n):
        self.n = n

    def __len__(self):
        print('Called __len__')
        return self.n

    def __getitem__(self, value):
        # print(f'You requested item at {value}')
        if value < 0 or value >= self.n:
            raise IndexError
        else:
            return 'Big, giant buns!'


class Fib():
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = self.n + s
            if s < 0 or s >= self.n:
                raise IndexError
            else:
                return Fib._fib(s)
        else:
            start, stop, step = s.indices(self.n)
            return [Fib._fib(i) for i in range(start, stop, step)]

    @staticmethod
    @lru_cache(2 ** 10)
    def _fib(n):
        if n < 2:
            return 1
        else:
            return Fib._fib(n-1) + Fib._fib(n-2)
