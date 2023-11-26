ent = list(map(int,input().split()))
rota = sum(ent[2:])
rota2 = abs(rota)%360
if rota < 0:
    rota = -rota2
else: 
    rota = rota2
if ent[0] == 1:
    fig = [['A','-','-'],
           ['B','-','-'],
           ['C','D','-']]
elif ent[0] == 2:
    fig = [['-','-','A'],
           ['-','-','B'],
           ['-','D','C']]
elif ent[0] == 3:
    fig = [['-','-','-'],
           ['A','B','-'],
           ['-','C','D']]
elif ent[0] == 4:
    fig = [['-','-','-'],
           ['-','C','D'],
           ['A','B','-']]
elif ent[0] == 5:
    fig = [['-','-','-'],
           ['-','D','-'],
           ['A','B','C']]
else:
    fig = [['-','-','-'],
           ['A','B','-'],
           ['C','D','-']]

if rota == 180 or rota == -180:
    print(f"{fig[2][2]}{fig[2][1]}{fig[2][0]}\n{fig[1][2]}{fig[1][1]}{fig[1][0]}\n{fig[0][2]}{fig[0][1]}{fig[0][0]}")
elif rota == 90 or rota == -270:
    print(f"{fig[2][0]}{fig[1][0]}{fig[0][0]}\n{fig[2][1]}{fig[1][1]}{fig[0][1]}\n{fig[2][2]}{fig[1][2]}{fig[0][2]}")
elif rota == 270 or rota == -90:
    print(f"{fig[0][2]}{fig[1][2]}{fig[2][2]}\n{fig[0][1]}{fig[1][1]}{fig[2][1]}\n{fig[0][0]}{fig[1][0]}{fig[2][0]}")
else:
    print(f"{fig[0][0]}{fig[0][1]}{fig[0][2]}\n{fig[1][0]}{fig[1][1]}{fig[1][2]}\n{fig[2][0]}{fig[2][1]}{fig[2][2]}")