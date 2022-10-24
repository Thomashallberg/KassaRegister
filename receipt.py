from datetime import datetime



class ReceiptRow:
    def __init__(self,productName,count,perPrice):
        self.__ProductName = productName
        self.__Count = count
        self.__PerPrice = perPrice
    def AddCount(self, count):
        self.__Count = self.__Count + count 

    def GetTotal(self):
        return self.__Count * self.__PerPrice
    
    def GetName(self):
        return self.__ProductName
    
    def GetCount(self):
        return self.__Count
    
    def GetPrice(self):
        return self.__PerPrice

class Receipt:
    def __init__(self):
        self.__Datum = datetime.now()
        self.__ReceiptRows = []
    
    def GetTotal(self):
        sum = 0
        for row in self.__ReceiptRows:
            sum = sum + row.GetTotal()
        return sum

    def CheckIfExist(self, productName):
        for row in self.__ReceiptRows:
            if row.GetName() == productName:
                return True
    
    def Add(self, productName:str, count:int, perPrice:float):   
        # Finns redan en receiptrow med denna productName?
        #  loopa igenom self.__ReceiptRows och försöka hitta
        # rec.AddCount(count)
        # ja -> uppdatera count 

        if self.CheckIfExist(productName):
             
            for row in self.__ReceiptRows:
                if row.GetName() == productName:
                    row.AddCount(count)
        else:
            #append new item to list
          
            
            receiptRow = ReceiptRow(productName,count,perPrice)
            self.__ReceiptRows.append(receiptRow)
            
        
    def SaveToFile(self):
        #Loopa igenom listan av items i "kvittot",
        # skriv in varje element(namn, antal, pris, total och datetime)
        datum = f"RECEIPT_{self.__Datum.strftime('%Y%m%d')}.txt"
        with open(datum, "a") as file:
            file.write(f"{self.__Datum.strftime('%d/%m/%Y %H:%M:%S')}\n")
            for row in self.__ReceiptRows:
                file.write(f"{row.GetName()} {row.GetCount()} st *{row.GetPrice()} kr {row.GetTotal()} kr\n")
            file.write(f"{self.GetTotal()} kr")
            file.write("\n-----------------\n")
        
    