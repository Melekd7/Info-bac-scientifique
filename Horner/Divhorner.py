from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def horner(z):
    m=0
    while(z!=""):
        ch=z[0]
        m=(m*2+int(ch))%7
        z=z[1:]
    return(m)
def etape1(x):
    ch=str(x)
    ch1=""
    for i in range(len(ch)):
        ch1=ch1+str(int(ch[i])%7)
    return(ch1)
def etape2(y):
    ch2=""
    if len(y)%2==0:
        for i in range(len(y)-1,0,-2):
            ch2=str(int(y[i-1:i+1])%7)+ch2
    else:
        for  i in range(len(y)-1,1,-2):
            ch2=str(int(y[i-1:i+1])%7)+ch2
        ch2=str(int(y[0])%7)+ch2
    return(ch2)
        
        
def play(x):
    x=int(windows.vx.text())
    if 5<=len(str(x))<=20:
        y=etape1(x)
        z=etape2(y)
        m=horner(z)
        if m==0:
            msg=str(x)+"est divisible par 7"
        else:
            msg=str(x)+"n'est pas divisible par 7 "
    else:
        msg="veuillez saisir un nombre de 5 à 20 chiffres"
    windows.res.setText(msg)
    




app=QApplication([])
windows=loadUi("interfaceHorner.ui")
windows.show()
windows.Verifier.clicked.connect(play)
app.exec_()
        