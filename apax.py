uinput = input().strip().split()
Yname = uinput[0]
Pname = uinput[1]
length = len(Yname)

if Yname[-1] == "e":
    print(Yname+"x"+Pname)
elif Yname[-1] in ["a", "i", "o", "u"]:
    print(Yname[:length-1]+"ex"+Pname)
elif Yname[-2]+Yname[-1] == "ex":
    print(Yname + Pname)
else :
    print(Yname + "ex" + Pname)

