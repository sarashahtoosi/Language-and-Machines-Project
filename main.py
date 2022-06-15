state = 0
str_temp = input("please enter your string(alphabet={a,b,c}  and num of 'a' and 'b' and 'c' must be greater than 1):")
main_string = list(str_temp)  # convert string to list of chars
main_string.insert(0, 'B')
main_string.append('B')
# add blank to end and beginnig of the list
n = 1  # list index

result = False
while True:
    if state == 0:
        if main_string[n] == 'a':
            main_string[n] = 'x'

            n = n + 1
            state = 1
        else:
            state = 8

    elif state == 1:
        if main_string[n] == 'b' or main_string[n] == 'a' or main_string[n] == 'c' or main_string[n] == 'z':
            while main_string[n] == 'b':
                main_string[n] = 'y'
                n = n + 1

            while main_string[n] == 'a':
                main_string[n] = 'a'
                n = n + 1
            if main_string[n] == 'c' or main_string[n] == 'z':
                state = 2
                n = n - 1
        else:
            state = 8

    elif state == 2:
        if main_string[n] == 'y':
            main_string[n] = 'b'
            n = n + 1
            state = 3
        else:
            state = 8
    elif state == 3:
        if main_string[n] == 'z' or main_string[n] == 'b' or main_string[n] == 'c':
            while main_string[n] == 'z' or main_string[n] == 'b':
                n = n + 1
            if main_string[n] == 'c':
                main_string[n] = 'z'
                n = n - 1
                state = 4
        else:
            state = 8
    elif state == 4:
        if main_string[n] == 'y' or main_string[n] == 'z' or main_string[n] == 'b' or main_string[n] == 'a' or main_string[n] == 'x':
            while main_string[n] == 'z' or main_string[n] == 'b':
                n = n - 1
            if main_string[n] == 'y':
                main_string[n] = 'b'
                n = n + 1
                state = 3
            elif main_string[n] == 'a':
                n = n - 1
                state = 5
            elif main_string[n] == 'x':
                n = n + 1
                state = 6
        else:
            state = 8
    elif state == 5:
        if main_string[n] == 'a' or main_string[n] == 'x':
            while main_string[n] == 'a':
                n = n - 1
            if main_string[n] == 'x':
                n = n + 1
                state = 0
        else:
            state = 8
    elif state == 6:
        if main_string[n] == 'b' or main_string[n] == 'z' or main_string[n] == 'B':
            while main_string[n] == 'b' or main_string[n] == 'z':
                n = n + 1
            if main_string[n] == 'B':
                state = 7
        else:
            state = 8
    elif state == 7:
        result = True
        break
    elif state == 8:
        break
if result:
    print("accepted!")
else:
    print(" failed!")
