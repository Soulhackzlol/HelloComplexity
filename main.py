import threading
import time
import random
from cryptography.fernet import Fernet
from queue import Queue
import re
from math import factorial

class X(type):
    _i = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._i:
            cls._i[cls] = super().__call__(*args, **kwargs)
        return cls._i[cls]

class Y(metaclass=X):
    def __init__(self):
        self.k = [Fernet.generate_key() for _ in range(3)]

    def e(self, m, t=1):
        for _ in range(t):
            for k in self.k:
                f = Fernet(k)
                m = f.encrypt(m.encode()).decode()
        return m

    def d(self, m, t=1):
        for _ in range(t):
            for k in reversed(self.k):
                f = Fernet(k)
                m = f.decrypt(m.encode()).decode()
        return m
    
def Z(q, r, o):
    s = Y()
    while not q.empty():
        n = q.get()
        if o == 'e':
            result = s.e(n, t=3)
        else:
            result = s.d(n, t=3)
        r.put(result)
        q.task_done()

def A(n):
    g = ['Hello', 'Hi', 'Hey', 'Greetings', 'Welcome', 'Salutations']
    ro = sum(ord(c) for c in n) * factorial(len(n)) % len(g)
    return g[ro]

class B(metaclass=X):
    def __init__(self):
        self.k = Fernet.generate_key()
        self.f = Fernet(self.k)

    def e(self, u):
        time.sleep(random.uniform(0.5, 1.5))
        return self.f.encrypt(u.encode()).decode()

    def d(self, e):
        time.sleep(random.uniform(0.5, 1.5))
        return self.f.decrypt(e.encode()).decode()

    def v(self, i):
        if not re.match("^[a-zA-Z\s]*$", i):
            raise ValueError("Invalid characters in input.")
        return True

class C:
    def __init__(self):
        self.p = B()
        self.u = None

    def s(self, t):
        m = len(t) // 2
        return t[m:] + t[:m]

    def us(self, t):
        m = len(t) // 2
        return t[-m:] + t[:-m]

    def g(self):
        ir = input("Enter your name: ")
        if self.p.v(ir):
            iscr = self.s(ir)
            ienc = self.p.e(iscr)
            self.u = self.p.d(ienc)

    def proc(self):
        time.sleep(2)
        iun = self.us(self.u)
        return iun

def D(n):
    qt = Queue()
    qr = Queue()

    for _ in range(5):
        qt.put(n)

    for _ in range(5):
        threading.Thread(target=Z, args=(qt, qr, 'e')).start()

    qt.join()

    while not qr.empty():
        ne = qr.get()
        qt.put(ne)

    for _ in range(5):
        threading.Thread(target=Z, args=(qt, qr, 'd')).start()

    qt.join()

    g = A(n)
    print(f"{g}, {n}!")

def E():
    [random.randint(0, 100) for _ in range(10)]

def F():
    [E() for _ in range(5)]

F()
ic = C()
ic.g()
ip = ic.proc()
D(ip)
