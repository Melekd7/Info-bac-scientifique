from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array
t=array([str]*1000)
def play():
    m=int(windows.m.text())
    n=int(windows.n.text())
    if m<0 or n<0:
        msg="Veuillez introduire 2 entiers positifs"
    else:
        if Verifier(m,n):
            msg=str(m)+" et "+str(n)+" forment une succession parfaite"
        else:   
            msg=str(m)+" et "+str(n)+" ne forment pas une succession parfaite"
    windows.res.setText(msg)
def tri(ch,t):
    n=len(ch)
    for i in range(n):
        t[i]=ch[i]
    permut=True
    while permut:
        permut=False
        for i in range(n-1):
            if t[i]>t[i+1]:
                aux=t[i]
                t[i]=t[i+1]
                t[i+1]=aux
                permut=True
def form(ch,t,n):
    ch=""
    for j in range(n):
        ch=ch+t[j]
    return(ch)
        
def Verifier(m,n):
    ch=str(m)+str(n)
    tri(ch,t)
    n=len(ch)
    ch1=form(ch,t,n)
    i=0
    while(i<len(ch1)-1 and int(ch1[i+1])-int(ch1[i])==1):
        i=i+1
    return(i==len(ch1)-1)
    
    
app=QApplication([])
windows=loadUi("InterfaceSuccession.ui")
windows.show()
windows.verif.clicked.connect(play)
app.exec_()