inputs = ['2041004C', '2062002B', '00221820', '00412822', 'AD010007', '8D090007']

registers = ['00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000',
          '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000',
          '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000',
          '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000']

memory = ['00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000',
          '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000',
          '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000',
          '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000', '00000000']

binary_list = []

def hex_binary(inputs):
    hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000',
                '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    new_val = ''

    for i in range(len(inputs)):
        x = inputs[i]
        #print (x)
        for j in range(len(x)):
            new_val = new_val + hex_dict[x[j]]
        binary_list.append(new_val)
        new_val = ''
    return binary_list

def r_get_command_line(y):
    op = int ((y[:6]), 2)
    rs = int ((y[6:11]), 2)
    rt = int ((y[11:16]), 2)
    rd = int ((y[16:21]), 2)
    shift = int ((y[21:26]), 2)
    funon = int ((y[26:]), 2)

    return op, rs, rt, rd, shift, funon

def i_get_command_line(y):
    op = int (y[:6], 2)
    rs = int (y[6:11], 2)
    rt = int (y[11:16], 2)
    Im = int (y[16:] , 2)

    return op, rs, rt, Im

def bit_by_bit_and(x,y):
    new_binary = ''
    for i in range(len(x), 0, -1):
        x1 = x[i-1]
        y1 = y[i-1]

        if x1 == '1' and y1 == '1':
            new_binary = '1' + new_binary
        else:
            new_binary = '0' + new_binary
    return new_binary

#OR
def bit_by_bit_or(x,y):
    new_binary = ''
    for i in range(len(x), 0, -1):
        x1 = x[i - 1]
        y1 = y[i - 1]

        if x1 == '0' and y1 == '0':
            new_binary = '0' + new_binary
        else:
            new_binary = '1' + new_binary
    return new_binary

#ADD
def bit_by_bit_add(x,y):
    carry = 0
    new_binary = ''
#    print (x)
#    print (y)
#    print()
    for i in range(len(x), 0, -1):
        x1 = (x[i - 1])
        y1 = (y[i - 1])

        if x1 == '1' and y1 == '1':
            if carry == 1:
                new_binary = '1' + new_binary
                carry = 1
            else:
                new_binary = '0' + new_binary
                carry = 1

        elif x1 == '1' and y1 == '0':
            if carry == 1:
                new_binary = '0' + new_binary
                carry = 1
            else:
                new_binary = '1' + new_binary
                carry = 0

        elif x1 == '0' and y1 == '1':
            if carry == 1:
                new_binary = '0' + new_binary
                carry = 1
            else:
                new_binary = '1' + new_binary
                carry = 0

        else:
            if carry == 1:
                new_binary = '1' + new_binary
                carry = 0
            else:
                new_binary = '0' + new_binary
                carry = 0
    return new_binary

def bit_by_bit_sub(x,y):
    new_binary_sub = ''
    print ('Sub stuff')
    for i in range(len(y)):
        if y[i] == '1':
            new_binary_sub =  new_binary_sub + '0'
        else:
            new_binary_sub = new_binary_sub + '1'

    new_binary_sub = bit_by_bit_add(new_binary_sub, '00000000000000000000000000000001')
    new_binary_sub = bit_by_bit_add(x,new_binary_sub)

    return new_binary_sub

def bit_by_bit_xor(x,y):
    new_binary = ''
    for i in range(len(x), 0, -1):
        x1 = x[i - 1]
        y1 = y[i - 1]

        if x1 == '1' and y1 == '1' or x1 == '0' and y1 == '0':
            new_binary = '0' + new_binary
        else:
            new_binary = '1' + new_binary
    return new_binary


binary_list = hex_binary(inputs)

#for i in range(len(binary_list)):
print (binary_list[0])
print (binary_list[1])
print ()

command_list = []

for i in range(len(binary_list)):
    y = binary_list[i]
    if (int(y[:6], 2)) == 0:
        command_list.append((r_get_command_line(y)))

    else:
        command_list.append((i_get_command_line(y)))

z = command_list[2]
print (bit_by_bit_xor(binary_list[0], binary_list[1]))
