class PrivateClass:
    __private_member = 5 #private member

    def __print_private(self): # private function
        print('From the private function:', self.__private_member)

    def public_func(self): # public function
        self.__print_private()


class PrivateSubClass(MyClass):
    pass


obj1 = PrivateClass()
obj2 = PrivateSubClass()
obj1.public_func()
# print(obj1.__private_member)  ERROR
# obj1.__print_private() ERROR
obj2.public_func()
