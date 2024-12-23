class Parent1:  # parent class 1
    def foo(self):
        print('called Parent1-foo()')


class Parent2:  # parent class 2
    def foo(self):
        print('called Parent2-foo()')

    def bar(self):
        print('called Parent2-bar()')


# --------------------------------------------------------

# a pair of child classes and one grandchild class.
class Child1(Parent1, Parent2):  # child 1 derived from Parent1, Parent2
    pass


class Child2(Parent1, Parent2):  # child 2 derived from Parent1, Parent2
    def foo(self):  # over riding methods
        print('called Child2-foo()')

    def bar(self):
        print('called Child2-bar()')


class GrandChild(Child1, Child2):  # define grandchild class
    pass  # derived from Child1 and Child2


# --------------------------------------------------------
gc = GrandChild()
gc.foo()  # called Child2-foo()
gc.bar()  # called Child2-bar()
Child1.foo(gc)  # called Parent1-foo()
Parent2.foo(gc)  # called Parent2-foo()
