from produkt import Product, ReadProductFromFile
from receipt import Receipt, ReceiptRow 






# for vara in ReadProductFromFile():
#     print(vara.GetName())

def HuvudMeny() -> int:
    print("1. Ny kund")
    print("2. Avsluta")
    selection = int(input(":"))
    return selection

def NyttKvitto(allProducts):
    kvitto = Receipt()
    kvitto.Add("Bananer", 3, 12.50)
    kvitto.Add("Äpple", 2, 10.50)
    print(kvitto.GetTotal())

    while True:
        print("KASSA")
        datum = "2002-10-05 13:45:12"
        print(f"KVITTO:{datum}")
        print("kommandon:")
        print("<productid> <antal>")
        print("PAY")
        action = input("Kommando:")
        if action  == "PAY":
            break

while True:
    sel = HuvudMeny()
    if sel == 2:
        break
    elif sel == 1:
        NyttKvitto(allProducts)


