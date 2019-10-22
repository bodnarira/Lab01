class IFilter:
    def Connect (self):
        pass

class TimeFilter(IFilter):
    def Filter(self):
        pass

class Images:
    def __init__ (self, filter: IFilter):
        pass