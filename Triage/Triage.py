from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array
t=array([int]*15)
v=array([str]*15)
def play():
    ch=str(windows.vn.text())    
    if len(ch)<15 and ch!="":
        if ch.find("  ")!=-1:
            msg="Entre 2 mots un seul espace est autorisé"
        elif ch.find(".")==-1:
            msg="La chaine doit se terminer par un point"
        else:
            msg=trier(ch,t,v)
    else:
        msg="Veuillez introduire une phrase"
    windows.res.setText(msg)
    
def trier(ch,t,v):
    ch=ch[0:len(ch)-1]+" "
    n=0
    while(ch!=""):
        j=ch.find(" ")
        t[n]=len(ch[0:j])
        v[n]=ch[0:j]
        ch=ch[j+1:]
        n=n+1


    
    ph=""
    test=True
    i=0
    while(test):
        test=False
        for i in range(n-1):
            if t[i]>t[i+1]:
                aux=v[i]
                v[i]=v[i+1]
                v[i+1]=aux
                aux1=t[i]
                t[i]=t[i+1]
                t[i+1]=aux1
                test=True
            
    for j in range(n):
        ph=ph+v[j]+" "
    ph=ph[0:len(ph)-1]
    return(ph)
            
        
        

    

app=QApplication([])
windows=loadUi("InterfaceTriage.ui")
windows.show()
windows.trier.clicked.connect(play)
app.exec_()