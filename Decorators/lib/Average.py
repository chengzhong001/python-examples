class Averager:
    def __init__(self) -> None:
        self.series = []
    
    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

def make_averager():
    series = []

    def averager(new_value: int | float) -> int | float:
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager