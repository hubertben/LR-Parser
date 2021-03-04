
from file_reader import FileReader as fr
from table import Table
#from grammer import Grammer
#from table_builder import TableBuilder as table_builder

table = Table(fr.read_table())
table.print_table()
