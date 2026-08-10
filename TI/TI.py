from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def cond2(ch):
    i=1
    while(i<len(ch) and not(ch[i]==" " and ch[i+1]==" ")):
        i=i+1
    return(i==len(ch))
def Impaire(ch):
    i=len(ch)-1
    while i>=0 and (ord(ch[i])-64)%2==1:
        i=i-2
    return(i<0)
def Verifier(ph):
    ch=ch
    
def cond1(ph):
    i=0
    while(i<len(ph) and ("A"<=ph[i]<="Z" or ph[i]==" " or ph[i]==".")):
        i=i+1
    return i==len(ph)
def play():
    ph=str(windows.vn.text())
    if(ph=="" or 50<=len(ph) or not("A"<=ph[0]<="Z") or ph[len(ph)-1]!="." or cond1(ph)==False or cond2(ph)==False):
        msg="verifier votre saisie"
    else:
        if(Verifier(ph)):
            msg="cette phrase est totalement impaire"
        else:
            msg="cette phrase n'est pas totalement impaire"
    windows.res.setText(msg)
app=QApplication([])
windows=loadUi("TI.ui")
windows.show()
windows.Verifier.clicked.connect(play)
app.exec_()