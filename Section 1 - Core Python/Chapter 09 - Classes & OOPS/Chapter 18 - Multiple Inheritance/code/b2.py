class Base1:
    def test(self):
        print("in Base1 -> test")

class Base2:
    def test(self):
        print("in Base2 -> test")

    def test1(self):
        print("in test1 of Base2")


class MultiDerived(Base1, Base2):
    def test2(self):
        super().test()
        Base2.test(Base2)
        Base2().test()
        super().test1()


#     def __init__(self):
#         print("Hello MultiDerived")

class MultiDerived2(Base2, Base1):
    def test2(self):
        super().test()
        Base2.test(Base2)

print("Please check the result of test()")

# d = Base2()
# print(type(d))
md = MultiDerived()
md.test2()
md.test()
# print(type(md))

# md2 = MultiDerived2
# md2.test(md2)
