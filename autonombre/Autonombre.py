from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def Sommechiffres(x):
    s=0
    while(x!=0):
        s=s+x%10
        x=x//10 
    return(s)
def verifier(x):
    i=0
    while(i<x and x!=i+Sommechiffres(i)):
        i=i+1
    return(i==x)
def chercher(n,m):
    ch=""
    for i in range(n,m+1):
        if verifier(i)==True:
            ch=ch+str(i)+"-"
    ch=ch[0:len(ch)-1]
    return(ch)
def play(x):
    n=int(windows.vn.text())
    m=int(windows.vm.text())
    if 20<=n<=50 and n<m<=100:
        ch=chercher(n,m)
        if ch=="":
            msg="Aucun autonombre entre "+str(n)+" et "+str(m)
        else:
            msg="Le(s) nombre(s) autonombre(s): "+ch
    else:
        msg="veuillez respecter 20≤n≤50 et n<m≤100"
    windows.res.setText(msg)
        



app=QApplication([])
windows=loadUi("interfaceAutonombre.ui")
windows.show()
windows.Afficher.clicked.connect(play)
app.exec_()