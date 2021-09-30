from collections import defaultdict


class Unique(object):
    
    def __init__(self, items, **kwargs):
        if ("ignore_case") in kwargs.keys() and kwargs.get("ignore_case")==True:
            pass
        else:
            kwargs=defaultdict(ignore_case=False)
        self.ignore_case=kwargs.get("ignore_case")
        self.items=iter(items)
        self.i=-1
        self.ban=[]

    def __next__(self):
        try:
            g=self.items.__next__()
            self.ban.append(g)
        except:
            raise StopIteration
        if type(self.ban[0])==int or self.ignore_case==False:
            k=0
            for item in self.ban:
                if item==g:
                    k=k+1
                    if k>1:
                        return(self.__next__())          
            return(g)
        else:
            k=0
            for item in self.ban:
                if item.lower()==g.lower():
                    k=k+1
            if k >1:
                return(self.__next__())
            else:
                
                return(self.ban[-1])

    def __iter__(self):
        return self