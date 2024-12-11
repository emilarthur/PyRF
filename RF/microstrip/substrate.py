class Substrate:
    def __init__(self, **kwargs):
        # Set default values for all attributes and validate them
        self.setName(kwargs.get('name', None))
        self.setEr(kwargs.get('er', None))
        self.setH(kwargs.get('h', None))
        self.setT(kwargs.get('t', None))
        self.setTanD(kwargs.get('tanD', None))

    # Set methods with type checking and validation
    def setName(self, name: str) -> None:
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        self._name = name

    def setEr(self, er) -> None:
        if not isinstance(er, (float, int)):
            raise TypeError("Er must be a float or an integer.")
        if er < 1:
            raise ValueError("Relative permittivity (Er) must be greater than or equal to 1.")
        self._er = float(er)  # Convert int to float if necessary

    def setH(self, h: float) -> None:
        if not isinstance(h, (float, int)):
            raise TypeError("Height (h) must be a float or an integer.")
        if h <= 0:
            raise ValueError("Substrate height (h) must be greater than 0.")
        self._h = float(h)

    def setT(self, t: float) -> None:
        if not isinstance(t, (float, int)):
            raise TypeError("Trace thickness (t) must be a float or an integer.")
        if t < 0:
            raise ValueError("Trace thickness (t) must be equal to or greater than 0.")
        self._t = float(t)

    def setTanD(self, tanD: float) -> None:
        if not isinstance(tanD, (float, int)):
            raise TypeError("Loss tangent (tanD) must be a float or an integer.")
        if tanD < 0:
            raise ValueError("Loss tangent (tanD) must be a non-negative value.")
        self._tanD = float(tanD)

    # Get methods
    def getName(self) -> str:
        return self._name

    def getEr(self) -> float:
        return self._er

    def getH(self) -> float:
        return self._h

    def getT(self) -> float:
        return self._t
    
    def getTanD(self) -> float:
        return self._tanD

    # Method to display details
    def info(self):
        print(f"Substrate Name:...................  {self._name}")
        print(f"Dielectric constant (Er):.........  {self._er:.3f}")
        print(f"Height:...........................  {self._h * 1e3:.3f} mm")
        print(f"Copper thickness:.................  {self._t * 1e6:.3f} um")
        print(f"Loss tangent (tanD):..............  {self._tanD:.5f}")