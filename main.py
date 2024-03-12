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
    
    def arg_n_info(self):
        return len(self.args)

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
    
class gene:
    def __init__(self,gene):
        self.gene:str = gene
        if self.gene == "":
            raise ValueError("Gene cannot be empty")
    
    def calculate(self):
        gene = self.gene
        gene = gene.split("Z")
        for i in range(len(gene)):
            if "N" in gene[i] :
                gene[i] = "n"
            else :
                gene[i] = int("0x64",gene[i])
        n_args = 0
        for k in range(len(gene)) :
            if n_args == 0 :
                formula = gene[k]
                