inputs = ['2041004C', '2062002B', '00221820', '00412822', 'AD010007', '8D090007']
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

binary_list = hex_binary(inputs)

for i in range(len(binary_list)):
    print (binary_list[i])
print ()

command_list = []

for i in range(len(binary_list)):
    y = binary_list[i]
    if (int(y[:6], 2)) == 0:
        command_list.append((r_get_command_line(y)))

    else:
        command_list.append((i_get_command_line(y)))

for i in range(len(command_list)):
    print (command_list[i])