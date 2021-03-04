
from file_reader import FileReader as fr
from grammer import Grammer
from table import Table

#from table_builder import TableBuilder as table_builder


def process(inp, grammer, table):
    accept = False
    inp = inp.split(' ') # input as id for now, change to token later to acom numbers and letters
    stack = [('!', 0)] # (action id, state)
    
    red = False

    id = 0
    state = 0

    while(not accept):


        if(not red):
            id = inp.pop(0)
            if(stack[-1][1] == 'AC'):
                return 1

            state = int(stack[-1][1])
        else:

            if(stack[-1][1] == 'AC'):
                return 1
            state = int(stack[-1][1])
        
        red = False

        print('~~~~~~~~~~~~~~~~~~~~~~~~')
        
        print('ID :', id, '| State :', state)

        prove = ''
        for item in table.action:
            if(id == item[0]):
                prove = item[state + 1]

        print('Prove :', prove)

        if(prove[0] == 'S'): # Shift
            print('SHIFT')
            temp = (id, prove[1:])
            stack.append(temp)
            print(stack)

        elif(prove[0] == 'R'): # Reduce
            print('REDUCE')
            grammer_index = int(prove[1:])-1
            print('Grammer Index :', grammer_index)
            grammer_row = grammer.grammer[grammer_index]
            print('Grammer Row :', grammer_row)
            new_tuple = [grammer_row[0], 0]
            print('New Tuple 1 :', new_tuple)
            
            for item in table.goto:
                if(grammer_row[0] == item[0]):
                    print(item[0])
                    new_tuple[1] = (item[int(stack[-2][1]) + 1]) 
                    break
            print('New Tuple 2 :', new_tuple)
            stack.pop()
            stack.append((new_tuple[0], new_tuple[1]))   
            red = True
            print(stack)
            

        else:
            raise NameError('Not Interpretable by Language Grammer')
            return -1


grammer = Grammer(fr.read_grammer())
table = Table(fr.read_table())
process('id + id * id $', grammer, table)