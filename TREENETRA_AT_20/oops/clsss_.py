'''class ClassName:
    var = 10

    def m1(self):
        print('hi m1')


ob1 = ClassName
print(ob1.var)
ob1.m1('jk')'''


# class College:
#
#     def __init__(self,college,activation,st_stregth):
#         self.college = college
#         self.activation = activation
#         self.st_stregth = st_stregth
#
#     def declare(self):
#         print(self.college,self.activation,self.st_stregth)
#
#
#
#
#
# ob1 = College('KBRC','101018',660)
# print(ob1.a)



# class is a blueprint, where we will collection and assign the var,method


#instamnce method and instance variable


# how many ways create a instance variable?
# 1. useing the self inside the constructor
# 2. using the self inside the instance method
# 3 using class or object refenece name outside of class.

class Car:#class name

    def __init__(self,car_name,car_type): #constrctor
        self.car_name = car_name
        self.car_type = car_type


    def mhaw(self,model):  # instance method
        self.model = model # instance variable
        return self.car_name,self.car_type,self.model

    def mhaw_refine(self,new_model):
        self.new_model = new_model
        scrpio_retuning = self.new_model+self.model+'100hp'
        del self.model
        # return scrpio_retuning,self.new_model,self.xuv900

ob1 = Car('Mahindra','SUV')
ob1.xuv900 = 'mhaw_new_2025' #instance variable , outside class , using object refrenece
print(ob1.mhaw('Scorpio'))
print(ob1.mhaw_refine('Scoripo N'))
del ob1.car_type
# print(len(ob1.__dict__))
print(ob1.__dict__)

# ob2 = Car('Mahindra','MUV')
# print(ob2.mhaw('Marazzo'))

# What is a instance method?

# where we will declare the instance variable, help of self, that method knowns as instance method.\


# createing a object ------ allocated ---- location--- memory

# a = 10-1m
# b = 10-1m
#
#
#
#
# a = 'jaydev'
# a = 'banivihar'


