
class Array:
    def __init__(self, *args) -> None:
        self.list = list(args)
    
    def __getitem__(self, idx:int):
        return self.list[idx]
    
    def __str__(self):
        return str(self.list)
    


array = Array(1,2,3)
