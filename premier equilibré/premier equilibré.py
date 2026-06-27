from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def premier(x):
    i=2
    d=x//2
    while(i<=d and x%i!=0):
        i=i+1
    return(i>d)
def prem_equib(x):
    if premier(x):
        a=x+2
        b=x-2
        while(not(premier(a))):
            a=a+2
        while(not(premier(b))):
            b=b-2
        return(((a+b)//2)==x)
    else:
        return(False)
    
def play(x):
    x=int(windows.vn.text())
    if x<=2:
        msg="veuiller saisir un entier >2"
    else:
        if prem_equib(x):
            msg=str(x)+" est un nombre premier équilibré"
        else:
            msg=str(x)+" n'est un nombre premier équilibré"
    windows.res.setText(msg)
def effacer(x):
    msg=""
    windows.res.setText(msg)
    windows.vn.clear()
app=QApplication([])
windows=loadUi("interface.ui")
windows.show()
windows.verifier.clicked.connect(play)
windows.annuler.clicked.connect(effacer)
app.exec_()