from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array
t=array([int()]*500)
def play(x):
    x=int(windows.vn.text())
    if x<10000:
        msg="veuillez introduire n>10000"
    else:
        if div13(x):
            msg=str(x)+"est divisible par 13"
        else:
            msg=str(x)+"n'est pas divisible par13"
        windows.res.setText(msg)
def div13(x):
    ch=str(x)
    i=0
    while i<=len(ch)//3 and ch!="":
        t[i]=x%1000
        x=x//1000
        i=i+1
        s=0
        for j in range(0,i,2):
            s=s-t[j]
        for k in range(1,i+1,2):
            s=s+t[k]
    return(abs(s)%13==0)
def effacer(x):
    msg=""
    windows.res.setText(msg)
        
        
        
            


app=QApplication([])
windows=loadUi("div13.ui")
windows.show()
windows.tester.clicked.connect(play)
windows.annuler.clicked.connect(effacer)
app.exec_()