class Product:
    def __init__(self, productid:str, Name:str,price:float, PriceType:str):
        self.__Name = Name
        self.__Price = price
        self.__ProductId = productid
        self.__PriceType = ""

    def GetName(self):
        return self.__Name
    
    def GetPrice(self):
        return self.__Price
    
    def GetProductId(self):
        return self.__ProductId
    
    def GetPriceType(self):
        return self.__PriceType
    
def ReadProductFromFile(): #Den hör inte till klassen men är relevant
    with open("product.txt") as file:
        allProducts = []
        for line in file:
            vara = line.split(";")
            product = Product(vara[0],(vara[1]), float(vara[2]), vara[3])
            allProducts.append(product)
            print(line)
        return allProducts
