from abc import ABC,abstractmethod
class User:
    def __init__(self,name,email,password): 
        self.name=name
        self.email=email
        self.password=password
class Admin(User):
    def __init__(self, name,items):
        self.name=name
        self.items=items
        
class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
        
class Cart:
    items=[]
    
    def add_items(self,new_item,price):
        Cart.items.append({new_item:price})
    
    def delete_items(self,item_name):
        for i in Cart.items:
            if i.get(item_name):
                Cart.items.remove(i)
                print("item deleted successfully")
                break
        else:
            print("item not found")

class Order:
    def __init__(self,name,items):
        self.name=name
        self.items=items
    
    def total_sum():
        Sum=sum([val for i in Cart.items for key,val in i.items()])
        return Sum
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class UPI(Payment):
    def pay(self,amount):
        print(f"{amount} payment successful via UPI✅")
class Card(Payment):
    def pay(self,amount):
        print(f"{amount} payment succesful via Card✅")
class Gpay(Payment):
    def pay(self,amount):
        print(f"{amount} payment successful via Gpay✅")
class Phonepay(Payment):
    def pay(self,amount):
        print(f"{amount} payment successful via Phonepay✅")
class COD(Payment):
    def pay(self,amount):
        print(f"{amount} to be paid on delivery✅")

 
name = input("Enter Name: ")
email = input("Enter Email: ")
password = input("Enter Password: ")
p1=User(name,email,password)
print(p1.name,p1.email,p1.password)
items={"mens":{"1.shirts":500,"2.pants":450,"3.jeans":400},
    "womens":{"1.sarees":600,"2.pants":300,"3.dresses":350},
    "child":{"1.shirts":200,"2.pants":250,"3.shorts":150}}
print(items)
while True:
    def add():
        print("1.Flipkart 2.Amazon 3.Myntra")
        option=input("choose option:")
        match option:
            case "1":
                selected=Admin("Flipkart",items)
            case "2":
                selected=Admin("Amazon",items)
            case "3":
                selected=Admin("Myntra",items)
            case __:
                print("invalid option")

        print(selected.name,selected.items)
        product_category=input("choose 1.mens 2.womens 3.child:")

        if product_category=="1":
            print(selected.items['mens'])
            while True:
                item=input("choose your item:")
                c1=Cart()
                if item=="1":
                    c1.add_items("shirts",500)
                elif item=="2":
                    c1.add_items("pants",450)
                elif item=="3":
                    c1.add_items("jeans",400)
                else:
                    break

        elif product_category=="2":
            print(selected.items['womens'])
            while True:
                item=input("choose your item:")
                c1=Cart()
                if item=="1":
                    c1.add_items("sarees",600)
                elif item=="2":
                    c1.add_items("pants",300)
                elif item=="3":
                    c1.add_items("dresses",350)
                else:
                    break

        elif product_category=="3":
            print(selected.items['child'])
            while True:
                item=input("choose your item:")
                c1=Cart()
                if item=="1":
                    c1.add_items("shirts",200)
                elif item=="2":
                    c1.add_items("pants",250)
                elif item=="3":
                    c1.add_items("shorts",150)
                else:
                    break
    
    def view_cart():
        c1=Cart()
        print(c1.items)


    print("operations")
    print("1.add_item 2.delete_item 3.view_cart 4.view_bill 5.Exit")
    operation=input("enter operation:")
    match operation:
        case "1":
            add()
        case "2":
            c1=Cart()
            delete_item=input("choose item:").lower()
            c1.delete_items(delete_item)
        case "3":
            view_cart()
        case "4":
            Total_bill=Order.total_sum()
            print(Total_bill)
        case __:
            print("Exited")
            break


    print("enter payment mode")
    print("1.upi 2.card 3.gpay 4.ppay 5.cod")
    bill=input("select 1 or 2 or 3 or 4 or 5:")
    if bill=="1":
        payment=UPI()
    elif bill=="2":
        payment=Card()
    elif bill=="3":
        payment=Gpay()
    elif bill=="4":
        payment=Phonepay()
    elif bill=="5":
        payment=COD()
    else:
        print("payment mode is not available") 

    payment.pay(Order.total_sum())
