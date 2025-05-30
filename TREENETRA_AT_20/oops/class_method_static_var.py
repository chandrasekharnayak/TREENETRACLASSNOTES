#class method and static variable

# class A:
#
#     #a variable declare in inside the class and outside of methods and constructor
#
#     var = 10 # staic variable
#     def __init__(self):
#         pass
#
#     def f1(self):
#         print('Hi Treenetra')
#
#     # def soumya(self):
#     #     print(A.var)
#     @classmethod
#     def sourav(cls):
#         print(cls.var)
#         cls.f1('q')
#
#
# ob1 = A
# # ob1.soumya('a')
# ob1.sourav()

# Notes
# when we want access static variable inside the constrctor nd instance method, we will use class name
# procedure --- warpper code in a logic
#     function
#     method


#static method

class A:

    t = 10#static
    @staticmethod
    def fib_series(num):
        global li
        li = [0,1]# local variable
        for i in range(num):
            generate_fib_num = li[-1]+li[-2]
            li.append(generate_fib_num)
        return li

    @classmethod
    def fib_mean(cls):
        fib = cls.fib_series(10)
        result_mean = sum(fib)/len(fib)
        return result_mean,fib,li,cls.t


ob1 = A
print(ob1.fib_mean())

#static -- class ander , method ke bahar---- class name--- cls(@classmetod)-classname ka har behavior use kar payega
#local - inside a method-- instance, staic, class



instance method
instnace var

class method
static var

static method
local variable









