from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array
t=array([str()]*50)
v=array([int()]*50)
def play():
    ch=str(windows.ch.text())
    if 1<=len(ch)<=50:
        msg=crypter(ch)
    else:
        msg="Vérifier la chaine"
    windows.res.setText(msg)
def efface():
    windows.res.clear()
    
    
def seul(ch):
    m=ch[0]
    i=1
    while(i<len(ch) and ch[i]==m):
        i=i+1
    return(i==len(ch))
def occ(c,ch):
    nb=0
    test=True
    while (c==ch[nb]):
        if seul(ch):
            test=False
        else:
            nb=nb+1
    return(nb)
def crypter(ch):
    ch=ch+" "
    i=0
    ch1=""
    while(ch!="" and not(seul(ch))):
        nb=occ(ch[0],ch)
        t[i]=ch[0:nb]
        v[i]=nb
        ch=ch[nb:]
        ch1=ch1+str(v[i])+t[i]
        i=i+1
    return(ch1)


app=QApplication([])
windows=loadUi("InterCRYPTE.ui")
windows.show()
windows.cryp.clicked.connect(play)
windows.eff.clicked.connect(efface)
app.exec()