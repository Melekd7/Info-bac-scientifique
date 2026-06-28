from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from random import randint
from numpy import array
t=array([str]*50)
def remp(n,t):
    for i in range(n):
        t[i]=chr(randint(ord("A"),ord("Z")))
def tri(n,t):
    permut=True
    while permut:
        permut=False
        for i in range(n-1):
            if t[i]>t[i+1]:
                aux=t[i]
                t[i]=t[i+1]
                t[i+1]=aux
                permut=True
def nombre(n,t):
    ch=""
    for i in range(n):
        ch=ch+str((ord(t[i])-64))
    return int(ch)
def play():
    a=int(windows.vn.text())
    if a<10:
        msg="age non approprié"
    else:
        remp(a//5,t)
        tri(a//5,t)
        x=nombre(a//5,t)
        if premier(x):
            msg="Félicitations vous avez gagné"
        else:
            msg="Désolé vous n'avez pas gagné"
    windows.res.setText(msg)
def premier(x):
    i=2
    d=x//2
    while(i<(d) and x%i!=0):
        i=i+1
    return(i==d)
    
    





app=QApplication([])
windows=loadUi("tri.ui")
windows.show()
windows.verifier.clicked.connect(play)
app.exec_()