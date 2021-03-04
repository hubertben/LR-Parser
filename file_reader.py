
class FileReader:

    def __init__(self):
        return

    def read_grammer(path = 'grammer.txt'):
        with open(path, "r") as txt_file:
            return txt_file.read().splitlines()
    
    def read_table(path = 'table.txt'):
        read_table = None
        with open(path, "r") as txt_file:
            read_table = txt_file.read().splitlines()
        return read_table
        

