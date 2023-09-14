from receipt import Receipt
from datetime import datetime

kvitto = Receipt()
kvitto.Add("banan", 3, 12.50)
kvitto.Add("Penna", 5, 5000)
kvitto.Add("Iphone", 1, 14000)
kvitto.Add("banan", 2, 12.50)
kvitto.Add("banan", 4, 12.50)
kvitto.SaveToFile()

kvitto2 = Receipt()
kvitto2.Add("Pelle", 3, 12.50)
kvitto2.Add("Mira", 5, 5000)
kvitto2.Add("Helen", 1, 14000)
kvitto2.SaveToFile()