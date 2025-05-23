# a = 10
# print(type(a))
# print(dir(a))
#
# # as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes
#
# print(a.is_integer())
#
# b = 10.0
# print(type(b))
#
# c = 9+10j
# d = 1+3j
#
# (9+10j+27j-30)
# (-21+37j)
#
# print(c*d)

# print(True+True)
# print(True+False)
# print(False+False)
#
# a = 5
# a = 5-3
# a = 2-2
# print(a)
#
# a = None



di = {}

for i in str:
    if i in di:
        di[i]+=1
    else:
        di[i]=1

st = ''
for k,v in di.items():
    var = str(v)
    st = st+k+var
print(st)














