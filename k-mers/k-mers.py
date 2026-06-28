from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array
t=array([str]*50)
def play():
    s=str(windows.s.text())
    k=int(windows.k.text())
    if not(test(s)):
        msg="Veuillez saisir une séquence valide."
    elif not(0<k<=len(s)):
        msg="Veuillez respecter 0<k<=longueur(s)"
    else:
        msg="les k-mers de la séquence d'ADN S:"+regrouper(s,k)
    windows.res.setText(msg)
def test(ch):
    i=0
    while(i<len(ch) and (ch[i]=="A" or ch[i]=="T" or ch[i]=="C" or ch[i]=="G")):
        i=i+1
    return(i==len(ch) and 6<=len(ch)<=20)
    
def extraire(s,k,t):
    for i in range(len(s)-k+1):
        t[i]=s[i:i+k]
        print(t[i])
    
def regrouper(s,k):
    extraire(s,k,t)
    SF=""
    for i in range(len(s)-k+1):
        f=1
        j=i+1
        while(j<len(s)-k+1):
            if t[i]==t[j]:
                f=f+1
            j=j+1
        if SF.find(t[i])==-1:
            SF=SF+t[i]+str(f)
    return SF
            
     
app=QApplication([])
windows=loadUi("k-mers.ui")
windows.show()
windows.forme.clicked.connect(play)
app.exec_()