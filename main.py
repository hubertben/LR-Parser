
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
            state = int(stack[-1][1])
        else:
            state = int(stack[-1][1])
        
        red = False

        prove = ''
        for item in table.action:
            if(id == item[0]):
                prove = item[state + 1]


        if(prove == 'AC'):
            print('SYNTAX COMPATABLE')
            return 

        if(prove[0] == 'S'): # Shift
            temp = (id, prove[1:])
            stack.append(temp)
            print(stack)

        elif(prove[0] == 'R'): # Reduce
            grammer_index = int(prove[1:])-1
            grammer_row = grammer.grammer[grammer_index]
            new_tuple = [grammer_row[0], 0]

            to_pop = grammer_row[2:]
            retrive_index = -2
            
            if(len(to_pop) > 1):
                for i in range(len(to_pop)-1,-1,-1):
                    if(to_pop[i] == stack[-1][0]):
                        stack.pop()
                        retrive_index = -1

            for item in table.goto:
                if(grammer_row[0] == item[0]):
                    new_tuple[1] = (item[int(stack[retrive_index][1]) + 1]) 
                    
                    break

            if(len(to_pop) == 1):       
                stack.pop()

            stack.append((new_tuple[0], new_tuple[1]))   
            red = True
            print(stack)
            
        else:
            raise NameError('Not Interpretable by Language Grammer')
            return -1


grammer = Grammer(fr.read_grammer())
table = Table(fr.read_table())
process('id * id + id $', grammer, table)