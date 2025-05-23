a = 'Maharatsra'
b = 'Gujrath'

def rev_str(st):
    reverse = ''

    for i in st:
        reverse=i+reverse
    return reverse
# print(rev_str(b))

def occurance_count_str(st):
    count_char = {}

    for i in st:
        if i in count_char:
            count_char[i]+=1
        else:
            count_char[i]=1
    return count_char
# print(occurance_count_str(a))