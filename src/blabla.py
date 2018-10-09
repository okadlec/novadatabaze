novepole=[]
pole=[5,1,6,8,42,25,25,366,99,366,99,336,336]
print pole
idx=0
while pole.__len__() > 0:
    minhodnota=999
    for objpole in pole:
        if minhodnota >= objpole:
            minhodnota=objpole
    print  minhodnota
    if minhodnota <> 999:
        pole.remove(minhodnota)
        novepole.append(minhodnota)
print novepole
