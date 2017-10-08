class Base:
    def test(self):
        print("In Base test")

    def test_alone(self):
        print("In Base test: test_alone")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")
        super().test()

    def test_alone(self, val):
        print("In Derived1 test: test_alone ", val)

#     def test_alone(self):
#         print("In Base test: test_alone")

class Derived2(Derived1):
    def test2(self):
        print("in Derived2 test2")

obj = Derived2()
obj.test()
obj.test2()
obj.test_alone("ty")
Base.test(Base)
