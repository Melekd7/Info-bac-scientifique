from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def supp(x):
    ch=str(x)
    i=0
    while (i<len(ch) and ch.find("0")!=-1):
        j=ch.find("0")
        ch=ch[0:j]+ch[j+1:len(ch)]
    return(int(ch))
def miro(x):
    return(ordre(x) and multip(x))
def ordre(x):
    c=x%10
    x=x//10
    while(str(x)!="" and c<x%10):
        x=x//10
    return(str(x)!="")
def multip(x):
    ch=str(x)
    i=0
    j=0
    l=len(ch)
    while(i<l//2):
        c=int(ch[i])
        d=int(ch[l-1-i])
        if c%d==0:
            j=j+1
        i=i+1
    return(j==l//2)
        
def play(x):
    x=int(windows.vn.text())
    if x<0:
        msg="veuiller saisir un entier positif"
    else:
        y=supp(x)
        if miro(y):
            msg=str(x)+" est un nombre miro"
        else:
            msg=str(x)+" n'est pas un nombre miro"
    windows.res.setText(msg)
def effacer(x):
    msg=""
    windows.res.setText(msg)
    windows.vn.clear()
app=QApplication([])
windows=loadUi("miro.ui")
windows.show()
windows.verifier.clicked.connect(play)
windows.annuler.clicked.connect(effacer)
app.exec_()