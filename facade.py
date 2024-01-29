### Facade pattern

class SubSystemA:
    def operationA(self):
        print("Subsystem A operation")

class SubSystemB:
    def operationB(self):
        print("Subsystem B operation")

class SubSystemC:
    def operationC(self):
        print("Subsystem C operation")

class FacadePattern:
    def __init__(self):
        self._subsystemA = SubSystemA()
        self._subsystemB = SubSystemB()
        self._subsystemC = SubSystemC()

    def performOperations(self):
        print("Facade executing operations...")
        self._subsystemA.operationA()
        self._subsystemB.operationB()
        self._subsystemC.operationC()

# Test FacadePattern
facade = FacadePattern()
facade.performOperations()
