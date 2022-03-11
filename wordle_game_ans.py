
import itertools
import enchant
alpas="abcdefghijklmnopqrstuvwxz"
dua=alpas
extra=input("if you're starting in middle, type the letters that you dont want in your ans:").split()
for i in range(5):
    print("         ")
    num=0
    dummystr1=""
    dummystr2=""
    # green
    totalgreen=int(input("total green box:"))
    green=input("letters in green box:").split()
    greenpos=list(map(int,input("position of green letters:").split()))
    #yellow
    totalyellow=int(input("total yellow box:"))
    yellow=input("letters in yellow box:").split()
    yellowpos=list(map(int,input("position of yellow letters:").split()))
    #grey
    totalgrey=int(input("total grey box:"))
    grey=input("letters in grey box:").split()
    greypos=list(map(int,input("position of grey letters:").split()))
    totalcolors=totalgreen+totalyellow+totalgrey
    if totalcolors>5:
        print("invalidinput :(")
        break
    else:
      print("try these words:")
    # first iteration
    grey=grey+extra
    for i in grey:
        dua=dua.replace(i,"")
    dummy=[]
    remaining=totalgreen-totalyellow
    for bla in range(1):
        if num>10:
            break
        combs=itertools.combinations(dua,totalgrey)
        for i in combs:
            if num>10:
              break
            dummy.append(list(i))
            dummy.append(yellow)
            for hod in dummy:
                for god in hod:
                    dummystr1+=god
            bombs=itertools.permutations(dummystr1)
            for lab in bombs:
              #print(lab)
                if num>10:
                    break
                lab=list(lab)
                if totalgreen>0:
                    for l in range(totalgreen):
                        lab.insert(greenpos[l]-1,green[l])
                        #print(lab)
                    for mod in lab:
                        for bod in mod:
                            dummystr2+=bod
                else:
                      for mod in lab:
                              for bod in mod:
                                      dummystr2+=bod
                d = enchant.Dict("en_US")
                if d.check(dummystr2):
                        print(dummystr2)
                        num+=1
                dummy=[]
                dummystr1=""
                dummystr2=""



  

  


