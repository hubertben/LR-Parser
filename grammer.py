
# Seperate input by spaces. Example: id + id * id, not id+id*id
# Using 'append' and 'pop' for stack operations

class Grammer:

    def __init__(self, grammer):
       self.grammer = grammer
       self.tokenize()
       #self.print_table(self.grammer)

    def tokenize(self):
        grammer_table = []
        for item in self.grammer:
            #print(type(item), item)
            item = item.split(' ')#[item[i].replace(' ', '') for i in range(len(item))]
            while("" in item) : 
                item.remove("") 
            grammer_table.append(item)
        self.grammer = grammer_table

    def print_table(self, table):
        for li in table:
            print(li)



