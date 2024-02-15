def f(name):    
    for i in range(len(name)):
        for j in range(i, len(name)):
            ss = name[i:j+1]
            print(ss + "   " + str(sum([ord(s) for s in ss])))


<<<<<<< HEAD
f ("dilara was here")
=======
f ("tamer was here")
>>>>>>> 2e7542f3260a3ca849a4e7d17e543c90827d6e9b
