class Pound:
    def __init__(self,rare = False):
        self.value = 10
        self.rare = rare
        if self.rare:
            self.color = "Gold"
            self.value = 12.5
        else:
            self.color = "Silver"
        self.diameter = 22.5 #mm
        self.thickness = 2.5 #mm
        self.numEdges = 1
        self.heads = True

    def __del__(self):
        print("Coin Spent!!")

    def rust(self):
        if self.color == "Gold":
            self.color = "Copperish"
        else:
            self.color = "Greenish"

