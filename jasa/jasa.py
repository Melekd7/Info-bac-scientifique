from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def play():
    x=str(windows.vc.text())
    if not(verif(x)):
        msg="vérifier votre saisie"
    else:
        ch=supp(x)
        if jasa(ch):
            msg=x+" est une phrase jasa"
        else:
            msg=x+" n'est pas une phrase jasa"
    windows.res.setText(msg)
def effacer():
    msg=""
    windows.res.clear()
    windows.vc.clear()
def verif(ch):
    i=0
    j=0
    while(i<len(ch) and ("A"<=ch[i].upper()<="Z" or ch[i]==" ")):
        if ch[i]!=" ":
            j=j+1
        i=i+1
    return(j<=100 and i==len(ch))
def supp(ch):
    i=0
    while(i<len(ch)):
        if ch[i]==" ":
            if ch[i+1]==" ":
                ch=ch[0:i+1]+ch[i+2:len(ch)]
        i=i+1
            
    return(ch)
def jasa(ch):
    n=0
    j=0
    p=ch.find(" ")
    ch1=ch[0:p]
    c=len(ch1)
    ch=ch[p+1:len(ch)]
    while(ch!=""):
        i=ch.find(" ")
        if i!=-1:
            r=ch[0:i]
            ch=ch[i+1:len(ch)]
            if c<len(r):
                c=len(r)
                j=j+1
        else:
            if c<len(ch):
                j=j+1
            ch=""
        n=n+1
        if c<len(ch1):
            c=len(ch1)
            j=j+1
            
            
    return j==n
    
    
    




app=QApplication([])
windows=loadUi("InterfacephraseJasa.ui")
windows.show()
windows.verifier.clicked.connect(play)
windows.annuler.clicked.connect(effacer)
app.exec_()