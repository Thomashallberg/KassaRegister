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

class Receipt:
    def __init__(self):
        self.__Datum = datetime.now()
        self.__ReceiptRows = []
    def GetTotal(self):
        sum = 0
        for row in self.__ReceiptRows:
            sum = sum + row.GetTotal()
        return sum
    def Add(self, productName:str, count:int, perPrice:float):   
        # Finns redan en receiptrow med denna productName?
        #  loopa igenom self.__ReceiptRows ocvh försöka hitta
        # rec.AddCount(count)
        # ja -> uppdatera count 
        receiptRow = ReceiptRow(productName,count,perPrice)
        self.__ReceiptRows.append(receiptRow)

    