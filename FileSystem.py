class FileSystemComponent:
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        pass


class File(FileSystemComponent):
    def display(self, indent=0):
        print(" " * indent + self.name)


class Directory(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self, indent=0):
        print(" " * indent + self.name)
        for child in self.children:
            child.display(indent + 2)
