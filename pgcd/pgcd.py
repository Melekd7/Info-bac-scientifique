from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array
tn=array([int()]*12)
tm=array([int()]*12)
tc=array([int()]*12)
def play1():
    n=int(windows.n.text())
    m=int(windows.m.text())
    windows.res.setText(str(pgcd(n,m,tn,tm,tc)))
def remp(x,t):
    k=0
    for i in range(1,x):
        if x%i==0:
            t[k]=i
            k=k+1
                
def nbrdiv(x):
    k=2
    for i in range(2,x):
        if x%i==0:
            k=k+1
    return(k)
def pgcd(n,m,tn,tm,tc):
    remp(n,tn)
    remp(m,tm)
    l1=nbrdiv(n)
    l2=nbrdiv(m)
    k=0
    for i in range(l1):
        for j in range(l2):
            if tn[i]==tm[j]:
                tc[k]=tn[i]
                k=k+1
    return(tc[k-2])
        
    
    

    
    
    
app=QApplication([])
windows=loadUi("pgcd.ui")
windows.show()
windows.calc.clicked.connect(play1)
app.exec_()
