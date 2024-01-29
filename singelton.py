class SingletonPattern:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def showMessage(self):
        print("Hello from SingletonPattern!")

# Test SingletonPattern
singleton1 = SingletonPattern()
singleton1.showMessage()

singleton2 = SingletonPattern()
singleton2.showMessage()

print("Are singleton1 and singleton2 the same instance?", singleton1 is singleton2)


