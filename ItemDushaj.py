class ItemDushaj:
    def __init__(self, quantityC, nameC, unitpriceC):
        self.myQuantity = quantityC
        self.myName = nameC
        self.myUnitPrice = unitpriceC

    def getQuantity(self):

        return self.myQuantity
    def getName(self):

        return self.myName
    def getUnitPrice(self):

        return self.myUnitPrice

    def setQuantity(self, quantityC):
        self.myQuantity = quantityC
        

    def setName(self, nameC):
        self.myName = nameC

        
    def setUnitPrice(self, unitpriceC):
        self.myUnitPrice = unitpriceC

        


    def __str__(self):
     
        answer_print = str(self.myQuantity)+  "            " + self.myName +  "           " + str("${0:0.2f} ".format(self.myUnitPrice))
        
        

        

        return answer_print
