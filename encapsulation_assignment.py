

class secretPants:

    __size = 32
    
    def __init__(self, brand, material):
        self._brand = brand
        self._material = material

    def pantsInfo(self):
        print("Size",self.__size,self._brand,self._material)

    
levis = secretPants("Levis", "denim")
levis.pantsInfo()
