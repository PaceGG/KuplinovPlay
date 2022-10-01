version = '2.1.1'
# Changelog 2.1
# 'id' replaced on 'class'

# Changelog 2.1.1
# tabs added

a = 33
b = 24
if a < b:
    b,a = a,b
step = a//b

episodes_a = []
for i in range(1,a+1):
    episodes_a.append(f'''<span class="a">{i}</span>''')
episodes_b = []
for i in range(1,b+1):
    episodes_b.append(f'''<span class="b">{i}</span>''')


index = []
j = 0
for i in range(1,b+1):
    index.append(i*step+j)
    j += 1
to_end = -(a%b)
j = 1
for i in range(to_end,0):
    index[i] += j
    j += 1

for i in range(b):
    episodes_a.insert(index[i],episodes_b[i])

print(*episodes_a)