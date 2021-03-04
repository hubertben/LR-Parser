

class Token:

    def __init__(self, val, ID):
        self.val = val
        self.ID = ID
        self.unit_type = define_type()

    def define_type(self, table):

        if(self.val.isnumeric() or self.val.isalpha() or self.val == 'id'):
            return 'id'
        else:
            if()
        

