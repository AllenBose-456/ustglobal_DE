# import math
# # bill=0.11
# # towerh=442
# # num=1
# # day=1
# # # for i in range(0,442,1):
# # #     if num*bill>443:
# # #         break
# # #     else:
# # #         num*=2
# # # print("num of bills",num)
# # # print("final height of bill",num*bill)
# # # print(i)
# # while(num*bill<towerh):
# #     day+=1
# #     num*=2
# # print(day)
# # print(num)
# # print("final height of bill",num*bill)
#
# # year=int(input("enter the year"))
# # if  (year%400==0) or (year%4==0 and year%100!=0) :
# #     print(year,"is a leap year")
# # else:
# #     print(year,"not a leap year")
# #
# #
# # if (year%400==0):
# #     print(year, "is a leap year")
# # elif(year%4==0 and year%100!=0):
# #     print(year, "is a leap year")
# # else:
# #     print(year, "is not a leap year")
#
#
# #number exercise
#
# # pa=500000.00
# # h=.05
# # month=2684.1133366666
# # totalpaid=0.0
# # while pa > 0:
# #     pa=pa*(1+h/12)-month
# #     totalpaid+=month
# # print("total payment",math.trunc(totalpaid))
# # print(math.gcd(12,16,20))
#
# message="Learning python for \t Data Engineering"
# noti=('''Saturdays are
#      working''')
# print("title",message)
# print("notification of the week",noti)
#
#
#
#
#
# string=input("enter the string ")
#
# reverse=string[::-1]
# print(reverse)
#
# if string==reverse:
#     print(string,"is palindrome")
# else:
#     print(string,"is not palindrom")

#
# name="i am travelling"
# vowel=0
# con=0
# space=0
#
# for i in range(0,len(name)-1):
#     if (name[i]==' '):
#         space += 1
#     elif( name[i] =="a" or name[i] =="e" or name[i] =="i" or name[i] =="o"or name[i] =="u"):
#         vowel += 1
#     else:
#         con+=1
# print(vowel)
# print(con)
# print(space)
# print(name[1])
# print(len(name)-1)
# print(name.split(" "))
# a=[1,2,7,3,4]
# a.sort()
# print(a)
#
# fruits=["Apple","Orange","Grapes"]
# fruit=":".join(fruits)
# print(fruit)

#
# list={"Tcs":2700,"infosys":3000,"idbi":140,"NTPC":220}
# print(list["Tcs"])
# print("price of TCS",list["Tcs"])
#
# list["UST"]=1200
# print(len(list))
# print(list.values())
# for i in list:
#     print(i," has price",list[i])
# for i in list.items():
#     print(i[0])
# for key,value in list.items():
#     print(key,"--->",value)
# print(list.popitem())
# del list["Tcs"]
# print(list)
#
# swapped={}
# for key,value in list.items():
#     swapped[value]=key
# print(swapped)


"""name,shares,price
AA,100,32.20
IBM,50,91.10
CAT,150,83.44
MSFT,200,51,23
GE,95,40.37
MSQT,50,65.10
# IBM,100,70.44"""
# import csv
# with open('py.csv') as pfile:
#     csv_reader=csv.reader(pfile,delimiter=",")
#     line_count=0
#     for row in csv_reader:
#         if line_count==0:
#             print(f'colmn Names are {", ".join(row)}')
#             line_count+=1
#         else:
#             print(f'\t {row[0]} has {row[1]} no of shares at price {row[2]}')
#             line_count += 1
#     print(f'read {line_count} shares from the port folio')
# with open('py.csv',mode="w") as pfile:
#     pfile_writer=csv.writer(pfile,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
#     pfile_writer.writerow(["IBM",50,40.56])
#
#
# with open('py.csv') as pfile:
#     csv_reader=csv.reader(pfile,delimiter=",")
#     line_count=0
#     for row in csv_reader:
#         if line_count==0:
#             print(f'colmn Names are {", ".join(row)}')
#             line_count+=1
#         else:
#             print(f'\t {row[0]} has {row[1]} no of shares at price {row[2]}')
#             line_count += 1
#     print(f'read {line_count} shares from the port folio')

# allowances={"HRA":.4,"DA":.3,"TA":.15}
# deductions={"PF":.12,"Insurance":500}
#
# print("*" *20,"Calculator salary","*" *20)
# basic=int(input("enter basic salary"))
#
# def calallovance(base):
#     total=0
#     for key in allowances:
#         total+=allowances[key]*basic
#     return total
#
# def caldeductions(basic):
#     total_deductions=0
#     for key in deductions:
#         if type(deductions[key] is not int):
#             total_deductions+=deductions[key]*basic
#         else:
#             total_deductions+=deductions[key]+basic
#     return total_deductions
# def sal():
#     print('basic salary is',basic)
#     print("allowances",calallovance(basic))
#     print("deductions",caldeductions(basic))
#
#
# sal()

# try:
#
#     num=3
#     num%2==0
# except :
#     print("error:")
# else:
#     NUM=num+1
#     print(NUM)
# finally:
#     print("completed")
# from face import odd;
# print(odd(4))
class Company:
    def __init__ (self,cname):
        self.cname=cname
    def displayname(self):
        print("company name",self.cname)
    def address(self):
        print("hbsqdhcw rqhkrvrvq wv")

import datetime
today=datetime.date.today()
year=today.year
class Employee(Company):
    isMarried=True
    count=0
    def __init__(self,fname,lname,yob):
        self.fname=fname
        self.lname=lname
        self.age=year-yob
        Employee.count+=1
    def address(self):
        print("employee sgt3rcjwc")
    def getEmpDetails(self):
        print("Full Name",self.fname,"",self.lname,"working in",self.cname)
        print("age:",self.age ,"& married",self.isMarried)
        print("Company",super().address())
        print("employee",self.address())
e=Employee("Allen","Bose",2000)
e.cname="ust"
e.isMarried=False
e.getEmpDetails()
e=Employee("Albert","Bose",2002)
e.cname="infosys"
e.isMarried=False
e.getEmpDetails()
print("Employee count :",e.count)