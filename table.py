

class Table:

    def __init__(self, table = []):
        self.table = table

    def print_table(self):
        for li in self.table:
            print(li)

    def split_top(self):
        self.header = self.table[0]