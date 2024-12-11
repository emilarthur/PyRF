from .mlcalc import analyze as _analyze

class MLIN:
    
    def __init__(self, **kwargs) -> None:

        self.w = kwargs.get("w")
        self.L = kwargs.get("L")
        self.substrate = kwargs.get("substrate")

    def info(self):
        print("Width  =",self.w*1e3,"mm")
        print("Length =",self.L*1e3,"mm")

    def getL(self) -> float:
        return self.L

    def getW(self) -> float:
        return self.w