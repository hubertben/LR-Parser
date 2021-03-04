

class Table:

    def __init__(self, table = []):
        self.table = table
        
        self.tokenize()
        self.rotate()
        self.split_header()
        self.seperate()
    

    def print_table(self, table):
        for li in table:
            print(li)


    def tokenize(self):
        tokenize_table = []
        for item in self.table:
            print(type(item), item)
            temp = item.split('|')
            temp = [temp[i].replace(' ', '') for i in range(len(temp))]
            tokenize_table.append(temp)

        self.table = tokenize_table
        

    def split_header(self):
        self.header = self.table.pop(0)

    def seperate(self):
        self.action = []
        self.goto = []

        isAction = True
        for item in self.table:

            if(isAction):
                self.action.append(item)
            else:
                self.goto.append(item)

            if(item[0] == '$'):
                isAction = False

        self.print_table(self.action)
        print('\n')
        self.print_table(self.goto)

        
    def rotate(self):
        for i in range(3):
            n = len(self.table)
            m = len(self.table[0])
            return_table = [[_ for _ in range(n)] for _ in range(m)]

            for i in range(n):
                for j in range(m):
                    return_table[j][i] = self.table[i][j]

            self.table = return_table