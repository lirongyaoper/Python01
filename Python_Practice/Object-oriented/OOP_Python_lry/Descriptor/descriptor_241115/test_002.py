class Foo():
    @property
    def attribute1(self):
        print("accessing the attribute to get the value")
        return 42
    @attribute1.setter
    def attribute1(self,value)-> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")


mu_foo_object = Foo()
x = mu_foo_object.attribute1
print(x)