#Class creation

class students:
    def __init__(self, name, id, address):
        self.name = name
        self.id = id
        self.address = address
        print(f"-Name:{self.name} \n Student ID: {self.id} \n Address:{self.address}")


Rick = students("Rick", "0008881111", "58 Place Rd.")
Jessica = students("Jessica", "000898223", "6850 Condo Pl.")
Michelle = students("Michelle", "000123456", "2 St - Apt. 35")
Kaneda = students("Kaneda", "000987435", "959 AHouse Circle")

