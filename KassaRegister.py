from produkt import Product, ReadProductFromFile
from receipt import Receipt, ReceiptRow 
from datetime import date, datetime


# for vara in ReadProductFromFile():
#     print(vara.GetName())

def HuvudMeny() -> int:
    print("1. Ny kund")
    print("2. Avsluta")
    #selection = int(input(":"))
    selection = input(":")

    try:
        selection = int(selection)  
    except ValueError:
        print('The provided value is not an integer')
        return
        
    if selection == 1 or selection == 2:
        return selection
    else:
        raise ValueError("You have to choose between the numbers 1-2")    

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
            kvitto.SaveToFile()
            break
        
           
        Nuvarande = action.split(" ")
        produktid = Nuvarande[0]
        #antal = int(Nuvarande[1])
        
        try:
            antal = int(Nuvarande[1])  
        except ValueError:
            print('The provided value is not an integer')
            return
        try:
            Produkt = GetProdukt(allProducts, produktid)
        #print(Produkt.GetName())
            Kund.append(Produkt)
            kvitto.Add(Produkt.GetName(),antal,Produkt.GetPrice())
            for x in Kund:
                print(f"{x.GetName()} * {antal} = {antal*x.GetPrice()}")
            print(f"Total: {kvitto.GetTotal()}")            
        except ValueError:
            print("Produkten finns inte, skriv in rätt PLU")
            return
        
   
        
def GetProdukt(Produkter, productid):         
    for x in Produkter:
        if x.GetProductId() == productid:
            return x      

    # Hit kommer vi inte om vi har hittat en produkt
    raise ValueError("Produkten finns inte, skriv in rätt PLU")

       
        

allProducts = ReadProductFromFile()
while True:
    try:
        sel = HuvudMeny()
        if sel == 1:
            NyttKvitto(allProducts)
        elif sel == 2:
            break
    except ValueError as ex:    
        print(ex)

