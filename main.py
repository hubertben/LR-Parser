
from file_reader import FileReader as fr
from grammer import Grammer
from table import Table

#from table_builder import TableBuilder as table_builder


def process(inp, grammer, table):
    accept = False
    inp = inp.split(' ') # input as id for now, change to token later to acom numbers and letters
    stack = [('!', 0)] # (action id, state)
    write_list = []
    red = False

    id = 0
    state = 0

    while(not accept):
        print(stack)
       
        if(not red):
            id = inp.pop(0)
            state = int(stack[-1][1])
        else:
            state = int(stack[-1][1])
        
        print_list = [id] + inp
        print('Input :', print_list)
        red = False
        

        #print('ID :', id, '| State :', state)

        prove = ''
        for item in table.action:
            if(id == item[0]):
                prove = item[state + 1]

        print('Prove :', prove)

        write_list.append(format_writable(stack, print_list, prove))

        print('~~~~~~~~~~~~~~~~~~~~~~~~')

        if(prove == ' ' or prove == ''):
            write_to_file(write_list)
            print('SYNTAX INCOMPATABLE')
            return 

        if(prove == 'AC'):
            write_to_file(write_list)
            print('SYNTAX COMPATABLE')
            return 

        if(prove[0] == 'S'): # Shift
            #print('SHIFT')
            temp = (id, prove[1:])
            stack.append(temp)
            

        elif(prove[0] == 'R'): # Reduce
            #print('REDUCE')
            grammer_index = int(prove[1:])-1
            #print('Grammer Index :', grammer_index)
            grammer_row = grammer.grammer[grammer_index]
            #print('Grammer Row :', grammer_row)
            new_tuple = [grammer_row[0], 0]

            to_pop = grammer_row[2:]
            #print('TO_POP :', to_pop)

            #print('New Tuple 1 :', new_tuple)

            retrive_index = -2
            
            if(len(to_pop) > 1):
                for i in range(len(to_pop)-1,-1,-1):
                    if(to_pop[i] == stack[-1][0]):
                        #print('POPPED :', stack.pop())
                        stack.pop()
                        retrive_index = -1

            #print(stack)

            for item in table.goto:
                if(grammer_row[0] == item[0]):
                    #print(item[0])
                    #print('TO PUSH TO :', str(item[int(stack[-2][1]) + 1]))
                    #print('FROM STACK INDEX :', [int(stack[-2][1]) + 1])
                    new_tuple[1] = (item[int(stack[retrive_index][1]) + 1]) 
                    
                    break

            if(len(to_pop) == 1):
                
                stack.pop()
                #print('POPPED :', )


            #print('New Tuple 2 :', new_tuple)

            stack.append((new_tuple[0], new_tuple[1]))   
            red = True
            
        

        else:
            raise NameError('Not Interpretable by Language Grammer')
            return -1
    

def format_writable(stack, input, prove):
    string = '' 
    for c in stack:
        if c[0] != '!':
            string += str(c[0])
        string += str(c[1])
    string += ' ' * (15 - len(string))
    for i in input:
        string += i
    string += ' ' * (35 - len(string))
    p1 = 'Shift' if prove[0] == 'S' else 'Reduce'
    p2 = prove[1]
    string += p1 + ' '
    string += p2
    return string

def write_to_file(l):
    file1 = open("output.txt","w+") 
    for f in l:
        file1.readline()
        write_string = str(f) + '\n'
        file1.write(write_string)
    file1.close()


grammer = Grammer(fr.read_grammer())
table = Table(fr.read_table())
process('( id + id ) * id $', grammer, table)

