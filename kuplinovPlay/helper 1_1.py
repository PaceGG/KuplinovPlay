version = '1.0'

a = 33
b = 24
if a > b:
    b,a = a,b

episodes = []
for i in range(1,a+1):
    for j in range(1,b//a+1):
        episodes.append(f'<span id="a">{j+b//a*(i-1)}</span>')
    episodes.append(f'<span id="b">{i}</span>')

for i in range(len(episodes)):
    print(episodes[i])

version = '1.1'
print(f'Требуется добавить по одной серии в {b-(b//a*a)} последних промежутка')