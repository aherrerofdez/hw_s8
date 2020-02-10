str = input("Write here: ")
str.lower()
str.replace(" ", "")

alphabet = "abcdefghijklmnopqrstuvwxyz"

index = 0
temp_str = ""
sub_str = ""

if len(str) == 1:
    sub_str = str
else:
    for s in str:
        if index != 0:
            alph_index = alphabet.index(s)
            if alph_index >= alphabet.index(str[index-1]):
                if len(temp_str) == 0:
                    temp_str = temp_str + str[index-1] + s
                else:
                    temp_str += s
            else:
                if len(temp_str) > len(sub_str):
                    sub_str = temp_str
                temp_str = ""
        if len(sub_str) == 0:
            sub_str = temp_str
        index += 1
print("The longest substring in alphabetical order is '{}'".format(sub_str))