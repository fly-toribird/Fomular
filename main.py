class formula :
    """ sample_formula = formula("3 * 2 ** n",["n"]) 
     96
        sample_formula.info()
     3 * 2 ** n
    """
    def __init__(self, formula,args):
        self.formula:str = formula
        self.args:list = args

    def calculate(self,args:list):
        if len(args)!= len(self.args):
            raise ValueError("Wrong number of arguments")
        for i in range(len(self.args)):
            globals()[self.args[i]] = args[i]
        return eval(self.formula)
    
    def info(self):
        print(self.formula)

class CMS :
    def __init__(self,formula,num):
        self.formula:formula = formula
        self.num:int = num
        if self.num <= 0:
            raise ValueError("Number must be positive")

    def calculate(self):
        return_n = self.formula.calculate([self.num])
        self.num += 1
        return return_n
    
class formular:
    def __init__(self,gene):
        self.gene:str = gene