name=input("good name dear:")
game=input("Do you play Quiz Game: ")
if game=="yes":
    print("Lets begin")
    print("Q 1. How many player in cricket?")
    a=print("a.11")
    b=print("b.12")
    c=print("c.13")
    d=print("d.14")
    choose=input("Ans:")
    if (choose=="a"):
        print("Your ans is correct")
        t=(0+10)
        print("you score is ",t)
        
    else:
        t=(0-10)
        print("you score is",t)
        print("bad luck")
        
    print("Q 2.How many ball use in cricket? ")
    a=print("a.5")
    b=print("b.6")
    c=print("c.2")
    d=print("d.1")
    choose=input("Ans:")
    if (choose=="b"):
        print("Your ans is correct")
        t=(t+10)
        print("you score is ",t)
    else:
        t=(t-10)
        print("you score is",t)
        print("bad luck")
    print("Q 3. How many ball in one over ?")
    a=print("a.1")
    b=print("b.2")
    c=print("c.3")
    d=print("d.6")
    choose=input("Ans:")
    if (choose=="d"):
        print("Your ans is correct")
        t=(t+10)
        print("you score is ",t)
    else:
        t=(t-10)
        print("you score is",t)
        print("bad luck")
    print("Q 4. Which game is popular in india?")
    a=print("a.Bat ball")
    b=print("b.Foot ball")
    c=print("c.Hockey")
    d=print("d.cricket")
    choose=input("Ans:")
    if (choose=="d"):
        print("Your ans is correct")
        t=(t+10)
        print("you score is ",t)
    else:
        t=(t-10)
        print("you score is",t)
        print("bad luck")
    print("Q 5. Who is best player in cricket  ")
    a=print("a.virat")
    b=print("b.crish gell")
    c=print("c.Avd")
    d=print("d.ms")
    choose=input("Ans:")
    if (choose=="a"):
        print("Your ans is correct")
        t=(t+10)
        print("you score is ",t)
    else:
        t=(t-10)
        print("you score is",t)
        print("bad luck")
    print(t)
               
else:
    print("bye bye")
