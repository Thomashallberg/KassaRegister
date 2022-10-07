class Product:
    def __init__(self, name:str, price:float, productid:str ):
        self.__Name = name
        self.__Price = price
        self.__ProductId = productid
        self.__PriceType = ""

    def GetName(self):
        return self.__Name
