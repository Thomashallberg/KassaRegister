from produkt import Product, ReadProductFromFile
from receipt import Receipt, ReceiptRow 
from datetime import date, datetime


# for vara in ReadProductFromFile():
#     print(vara.GetName())

def HuvudMeny() -> int:
    print("1. Ny kund")
    print("2. Avsluta")
    selection = int(input(":"))
    return selection

def NyttKvitto(allProducts):
    kvitto = Receipt()
    
    Kund = [] 
    while True:
        print("KASSA")
        now = datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"KVITTO:{now}")
        print("kommandon:")

        print("<productid> <antal>")
        print("PAY")
        action = input("Kommando:")
        if action  == "PAY":
            break
        
           
        Nuvarande = action.split(" ")
        produktid = Nuvarande[0]
        antal = int(Nuvarande[1])
       
        Produkt = GetProdukt(allProducts, produktid)
        #print(Produkt.GetName())
        Kund.append(Produkt)
        kvitto.Add(Produkt.GetName(),antal,Produkt.GetPrice())
        for x in Kund:
            print(f"{x.GetName()} * {antal} = {antal*x.GetPrice()}")
        print(f"Total: {kvitto.GetTotal()}")            
        
   
        
def GetProdukt(Produkter, productid):         
    for x in Produkter:
        if x.GetProductId() == productid:
            return x         
        

allProducts = ReadProductFromFile()
while True:
    sel = HuvudMeny()
    if sel == 1:
        NyttKvitto(allProducts)
    elif sel == 2:
        break

