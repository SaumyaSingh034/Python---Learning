from string import Template

class MyTemplate(Template):
    delimiter = '#'

def Main():
    cart = [ ]
    cart.append(dict(item="Coke", price= 65, qty=2))
    cart.append(dict(item="Pepsi", price= 98,qty = 5))
    cart.append(dict(item="Mountain Dew", price=658, qty = 15))

    t = MyTemplate("#qty  x  #item  =  #price")
    total = 0
    print("cart : ")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]

    print("total = "+str(total))

if __name__ =="__main__":
    Main()
