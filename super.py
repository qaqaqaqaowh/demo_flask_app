class Model:
    def some_func(self):
        print("First")

class Base(Model):
    def some_func(self):
        print("Second")

    def test(self):
        super().some_func()

class C(Base):
    pass

class D(C):
    def test(self):
        super().some_func()

x = D()
x.test()