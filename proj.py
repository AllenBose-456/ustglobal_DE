
import csv


class Shopping:
    def __init__(self):
        pass

    def view(self):
        for key, value in Bucket.items():
            print(key, "----->", value)
        return "success"


    def add(self,item,qty):
        ask3 = 1

        ask4 = 1

        ask2 = 1

        while (ask2 == 1):
                if (len(my_bucket) == 0 and len(price_bucket) == 0):


                    item.capitalize()

                    for pro in Bucket:

                        if item == pro:

                            my_bucket.append(item)
                            price_bucket.append(qty)

                            print(my_bucket)

                            print(price_bucket)

                            ask2 = int(input("do u need to add more item press 1 else 0"))

                            flag = 0

                            break

                        else:

                            flag = 1

                            continue

                    if flag == 1:
                        return("invalid order select from list")

                else:
                    item

                    item.capitalize()
                    if item in my_bucket:
                        return("enter new item")
                    else:
                        my_bucket.append(item)

                        qty = int(input("enter the quantity"))

                        price_bucket.append(qty)

                        print(my_bucket,"and",price_bucket)

                        ask2 = int(input("do u need to add more item press 1 else 0"))
        return("success")
    def update(self):
        ask2 = 1

        ask4 = 1

        ask3 = 1

        while (ask3 == 1):

            for itm, pri in zip(my_bucket, price_bucket):
                print(itm, "---->", pri)

            try:

                ask = input("which item has to change")

                item2 = ask.capitalize()

                index = my_bucket.index(item2)

                new_qty = int(input("Enter the quantity"))

                price_bucket[index] = new_qty

                for itm, pri in zip(my_bucket, price_bucket):
                    print(itm, "---->", pri)

                ask3 = int(input("do u want to change more press 1 else press 0"))

            except:

                return("enter the item in the list")

        return("success")
    def delete(self):
        ask2 = 1

        ask3 = 1

        ask4 = 1

        while (ask4 == 1):

            for itm, pri in zip(my_bucket, price_bucket):
                print(".", itm, "---->", pri)

            try:

                ask = input("which item has to Delete")

                item2 = ask.capitalize()

                index = my_bucket.index(item2)

                my_bucket.pop(index)

                price_bucket.pop(index)

                for itm, pri in zip(my_bucket, price_bucket):
                    print(".", itm, "---->", pri)

                ask4 = int(input("do u want to change more press 1 else press 0"))

            except:

                return("enter an order in the list")
        return "success"

    def printbill(self):
        sum = 0

        for itm, pri in zip(my_bucket, price_bucket):
            sum += Bucket[itm] * pri

            print(itm, "---->", Bucket[itm] * pri)

        print("********************* ")

        print("Total ------->", sum)

        print("*******THANK YOu***********")
        return("success")

    def bill(self):
        if len(my_bucket) != 0:
            with open('bill.csv', 'w', newline='') as csvfile:
                sswrite = csv.writer(csvfile, delimiter=' ', quotechar='-', quoting=csv.QUOTE_MINIMAL)
                sswrite.writerow([f'Item---------->Quantity----->Price'])
                for i, j in zip(my_bucket, price_bucket):
                    sswrite.writerow([f'{i}---------->{j}----->{Bucket[i] * j}'])
                sswrite.writerow(['*' * 40])
                sswrite.writerow([f'total ---------->  {sum}'])
                sswrite.writerow(["*******THANK YOu***********"])
                return("bill is generated")

        else:
            return "no bill"
    def error(self):
        ask2 = 1

        ask3 = 1

        ask4 = 1

        sum = 0

        i = 0
        return("enter a valid number")
i = 0

Bucket = {"items": "price", "Orange": 250, "Apple": 320, "Grapes": 210, "Pineapple": 150, "Guava": 160}

my_bucket = []

price_bucket = []
v=Shopping()
while i == 0:

    print("Welcome to Fruits Store \n 1.View the Fruits list \n 2.Add the Fruits to cart \n 3.Update the cart \n 4. remove from the cart \n 5.Exist and calculate total")

    ask = int(input("Select the option : "))

    if (ask == 1):

        print(v.view())

    elif (ask == 2):
        item=input("enter the item")
        qty=int(input("enter the qty"))
        print(v.add(item,qty))

    elif (ask == 3):
        if (len(my_bucket) != 0 and len(price_bucket) != 0):
            print(v.update())
        else:
            continue


    elif (ask == 4):
        if(len(my_bucket) !=0  and len(price_bucket) !=0 ):
            print(v.delete())
        else:
            continue
    elif ask == 5:

        print(v.printbill())
        v.bill()

        break

    else:
        print(v.error())









