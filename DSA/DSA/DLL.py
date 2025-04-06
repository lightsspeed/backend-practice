class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class DLL:
    def __init__(self):
        self.head = None
    
    def print_DLL(self):
        if self.head is None:
            print("LL is empty")
        else:
            print()
