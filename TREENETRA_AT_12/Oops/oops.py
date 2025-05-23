"""class Student:
    '''This class is use for student information'''
    a = 10
    def f1(self):
        pass

obj1 = Student()
print(dir(obj1))"""

# class Student:
#
#     def __init__(self,name,rollno,section):
#         self.name = name
#         self.rollno = rollno
#         self.section = section
#
#     def class_room(self,cls_name):
#         self.cls_name = cls_name
#         print(self.cls_name)
#
#
# obj = Student('Utkala',99,'Z')
# obj.class_room('music class')
# print(obj.__dict__)

"""class BankData:

    '''
        How to create a instance variable
        ---------------------------------

        inside a constructor help of self
        inside a instance method help of self
        inside a instance method help of class name
        outside of a class help of object refernce.
        '''

    def __init__(self,bank_name,accno,ifsc,branch,account_balance):
        self.bank_name = bank_name
        self.accno = accno
        self.ifsc = ifsc
        self.branch = branch
        self.account_balance = account_balance

    def debit(self,db_amount):
        self.db_amount = db_amount
        self.account_balance = self.account_balance-self.db_amount
        # BankData.account_balance = BankData.account_balance -self.db_amount


    def credit(self,cr_amount):
        self.cr_amount = cr_amount
        self.account_balance = self.account_balance+self.cr_amount


    def account_balance_check(self):
        return self.account_balance

    def fix_deposite(self):
        pass

    def recuring_deposite(self):
        pass

obj_101= BankData('BOI',10120567,'BOI123','Martha',500)
print(obj_101.account_balance_check())
# print(obj_101.bank_name)
'''obj_101.manager_name = 'Utkala'
print(obj_101.__dict__)'''

print('After debit')
obj_101.debit(300)
print(obj_101.account_balance_check())

print('After credit')
obj_101.credit(1000)
print(obj_101.account_balance_check())"""


'''after 10 debit and 10 credit, what ever amount is their fixed amount (80%)

FD:- fd_date
180:-4%
360 - 5.5%
520:- 6%
720 :- 7.1%

'''

#static variable and class method

"""class Student:

    '''
    How to static varaible

    inside a instance method help of class name
    inside a instance method help of self
    inside a classmethod help of cls variable
    '''
    father_name = input('Enter ur father name')
    mother_name = input('Enter ur mother name')

    @classmethod
    def child_access(cls,child_name):
        print(child_name ,'is son/doughter of',cls.father_name,cls.mother_name)

obj = Student()
obj.child_access('Utkal')"""

#staticmethod and Local variable

# class Math1:
#
#     @staticmethod
#     def add(a,b):
#         global sum1
#         sum1 = a+b
#         return sum1
#
#     @staticmethod
#     def sub(a):
#         s = a-sum1
#         return s
#
# obj = Math1()
# print(obj.add(100,200))
# print(obj.sub(500))

#single inh

'''class Math:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1+self.num2

    def sub(self):
        return self.num1-self.num2

class Alg(Math):

    def __init__(self,height,num1,num2):
        super().__init__(num1,num2)
        self.height = height

    def squre(self):
        data = self.height*self.height
        result = data+super().add()
        return result



obj_alg = Alg(100,10,20)
print(obj_alg.squre())'''



'''class Doctor:
    def __init__(self,doc_name,doc_spec,doc_hospital_name):
        self.doc_name = doc_name
        self.doc_spec = doc_spec
        self.doc_hospital_name = doc_hospital_name

    def clinc1(self,clinc_name,doc_time):
        self.clinc_name = clinc_name
        self.doc_time = doc_time
        return self.clinc_name,self.doc_time

    def clinc2(self,clinc_name,doc_time):
        self.clinc_name = clinc_name
        self.doc_time = doc_time
        return self.clinc_name, self.doc_time

class PtName(Doctor):
    def __init__(self,pt_name,ward_name,doc_name,doc_spec,doc_hospital_name):
        super().__init__(doc_name,doc_spec,doc_hospital_name)
        self.pt_name = pt_name
        self.ward_name = ward_name

    def correct_pt_with_doc(self):
        if self.ward_name == self.doc_spec:
            print(super().clinc1('A','7pm-8pm'))
            print(super().clinc2('B','8pm-9pm'))
        else:
            print('Doc Sepc and Ward Name Not match check with other doctor')


obj_p = PtName('Utkal','Ortho','Dr.Sanjhulata','Ortho','Home')
obj_p.correct_pt_with_doc()'''


'''
Batch-1 (batch_name,batch_strating_date(8 th July)

1 july(10,3) i want all candidates name
4 july(16,4)
7 july(10,2)
8th final candidates total num, with name

Btach-2(batch_name,batch_strating_date(26 th July)
14 july (6,0) --- 1 july 3 candidates , they are joining

16 July(34,3) 7 july 2 candidates , they are joining

batch1+batch2 total addmission candidates
how many inqury in batch1 and batch2
how many return batch1 to batch2(with name)

'''


#Multiple Inheritance


'''class Addition:
    def add(self,a,b):
        return a+b

    def a(self):
        print('a is method of Addition')'''

    # def a(self):
    #     print('a is 2nd method')#method overloading


'''class Multiplication:
    def mul(self,a,b):
        return a*b

    def a(self):
        print('a is method of Multiplication')

class MathOperation(Multiplication,Addition):
    def calculate(self,a,b):
        addition_result = super().add(a,b)
        multiplication_result = super().mul(a,b)
        return addition_result,multiplication_result,super().a()

obj_math = MathOperation()
result = obj_math.calculate(10,20)
print(result)'''


#overloading
'''class Addition:
    def add(self,a,b):
        return a+b

    def a(self):
        print('a is method of Addition')'''

'''class MathOperation(Addition):
    def add(self,a,b):
        sum = 0
        for i in range(a):
            for j in range(b):
                sum = sum+i+j
        print('Op:-',sum)

obj_math = MathOperation()
obj_math.add(2,3)'''

#Multilevel inheritance

'''class GrandFather:
    def village_land(self):
        return '200sqft jamin in village'

class Father(GrandFather):
    def city_land(self):
        return '160 sqft jamin in city'

class Son(Father):
    def banglore_land(self):
        return '140 sqft jamin in banglore'

class GrandSon(Son):
    def Chicago(self):
        return '110 sqft jamin in Chicago'

# obj_grand_father= GrandFather()
# print(obj_grand_father.village_land())

# obj_father = Father()
# print(obj_father.village_land())#gf ing
# print(obj_father.city_land())#own method

obj_son = Son()
print(obj_son.banglore_land())
print(obj_son.village_land())
print(obj_son.city_land())'''


#hyrechical inheritance

class Mahindra:
    def suv(self):
        ground_clerans = '180mm'
        vechile_length = '4000mm'
        height = '1580mm'
        return ground_clerans,vechile_length,height


class Scorpio(Mahindra):
    def scorpios11(self):
        data = super().suv()
        s11_new = 'info sys'
        return data,s11_new

class Thar(Mahindra):
    def thar_3door(self):
        data = super().suv()
        thar_new = '4*4'
        return data,thar_new


obj_sc = Scorpio()
print(obj_sc.scorpios11())

obj_thar = Thar()
print(obj_thar.thar_3door())


















