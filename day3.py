# "named tuple-it return atuple with name entry"
# from collections import namedtuple,deque,ChainMap,Counter,OrderedDict,defaultdict
# courses=namedtuple('course','name,tech')#['name','tech']-->can also use like this
# clist=courses('datascience','python')#name='datascience',tech='python'--->can also use like this
# print(clist)
# print(getattr(clist,"tech"))
#
# rlist=['react','angular']
# print(courses._make(rlist))#converting list to named tuple
#
# "Deque-it is a optimised list to perform insertion and deletion easily"
# Team_list=["Rohith","Virat","Hardik","Rahul"]
# cqueue=deque(Team_list)
# cqueue.append("allen")
# cqueue.appendleft("siraj")
# cqueue.pop()
# cqueue.popleft()
# print(cqueue)
#
# "Chainmap-it is a dictionary like class which is able to make single view of multiple mappings "
#
# module_1={1:"Angular",2:"python"}
# module_2={3:"react",4:"angular"}
# module_list=ChainMap(module_1,module_2)
# print(module_list)
# module_3={5:"devops"}
# updatelist=module_list.new_child(module_3)
# print(updatelist)#name.maps to change the name chainmapin output
# print(list(updatelist.keys()))
# print(list(updatelist.values()))
#
# "Counter-it is a dictionary surplus which is used to count hashtable objects"
#
# Rohith_scores=[70,89,170,270,200,100,70,50,89,60,50,200]
# score_count=Counter(Rohith_scores)
# print(score_count)#scorecount.keys(),scorecount.values(),score_count.items()
#
# #orderdeic=OrderedDict()
# orderdeic=defaultdict(int)
# orderdeic[1]="17.10"
# orderdeic[2]="20.00"
# orderdeic[3]="45.21"
# print(orderdeic[4])
#
#
#iterators are used to iterate collections like list ,tuple etc
# Prime_number=[1,3,5,7,11,17]
# pn_iterator=iter(Prime_number)
# print(next(pn_iterator))
# print(next(pn_iterator))
# print(next(pn_iterator))
# print(next(pn_iterator))
# print(next(pn_iterator))
# print("*"*80)
# for num in Prime_number:
#     print(num)
#

# class pow:
#     def __init__(self,max=0):
#         self.max=max
#     def __iter__(self):
#         self.n=0
#         return self
#     def __next__(self):
#         if self.n<=self.max:
#             Result=3**self.n
#             self.n+=1
#             return Result
#         else:
#             raise StopIteration
# num=pow(10)
# i=iter(num)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# create a coustamisable iterator which gives next prime number


#
# import math
#
# class primenumber:
#     def __init__(self, max=30, min=10):
#         self.ma_x = max
#         self.mi_n = min
#         self.n = min
#
#
#     def __iter__(self):
#         return self
#
#     def is_prime(self, num):
#         if num < 2:
#             return False
#         for i in range(2, int(math.sqrt(num)) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     def __next__(self):
#         while self.n <= self.ma_x:
#             if self.is_prime(self.n):
#                 result = self.n
#                 self.n += 1
#                 return result
#             else:
#                 self.n += 1
#         raise StopIteration
#
# prime = primenumber()
# for num in prime:
#     print(num)


# class prime:
#     def __init__(self,ma=30,mi=10):
#         self.min=mi
#         self.max=ma
#         self.n=mi
#     def __iter__(self):
#         return self
#     def __next__(self):
#         flag=0
#         if self.n<=self.max and self.n>=self.min:
#             for i in (2,self.n):
#                 if(self.n%i==0):
#                     self.n+=1
#                     break
#             result=self.n
#             self.n+=1
#             return self.n
#
# pri=prime()
# print(next(pri))
# print(next(pri))
#


#Generators
#
# def generator(n):
#     value=0
#     while value<n:
#         yield value
#         value+=1
# for value in generator(10):
#     print(value)
# value=generator(10)
# print(next(value))
# print(next(value))
#
# gen=(i*i*i for i in range(6))
# for i in gen:
#     print(i)
# class power:
#     def __init__(self,max=0):
#         self.n=0;
#         self.max=max
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n>self.max:
#             raise StopIteration
#         result=3**self.n
#         self.n+=1
#         return result
#
# def gen(max):
#     value=0
#     while value<max:
#         yield 3**max
#         value+=1
#         return value

# def fibonacci_numbers(nums):
#     x,y=1,2
#     for _ in range(nums):
#         x,y=y+x
#         yield x
# def squre(nums):
#     for num in nums:
#         yield 2**num
#
# print(sum(squre(fibonacci_numbers(3))))


def fibonacci_numbers(nums):
    x,y=0,1
    for _ in range(nums):
        x,y=y,y+x
        yield x

def prime(nums):
    flag=0
    for i in range(nums):
        if(nums%i==0):
            flag=1
            break

    if flag==0 and nums!=1:
        yield nums

for value in fibonacci_numbers(10):
    print(value)
for value in prime(10):
    print(value)
print(""""kjebvuobwebvejrvljwejrv 
qehrbvuqoborvubquwrbvueruov""")
# for value in prime(fibonacci_numbers(10)):
#     print(value)
# print(sum(prime(fibonacci_numbers(10))))

#lambda

squres=lambda x:print(x*x)
squres(5)
