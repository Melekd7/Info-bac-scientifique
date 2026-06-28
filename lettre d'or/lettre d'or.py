from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array
t=array([str]*50)
def play1():
    ch=str(windows.ch.text())
    if ch=="":
        msg1="Veuillez saisir la chaine"
    elif not(test(ch)):
        msg1="Veuilez saisir une chaine valide"
    else :
        msg1=lettre1(ch,t)
        msg2=lettre2(ch,t)
    windows.res1.clear()
    windows.res1.setText(msg1)
    windows.res2.clear()
    windows.res2.setText(msg2)
def play2():
    ch=str(windows.ch.text())
    if ch=="":
        msg="Veuillez saisir la chaine"
    elif (test(ch)):
        msg=inverse(ch,t)
    else :
       msg="Veuilez saisir une chaine valide"
    windows.res1.clear()
    windows.res2.clear()
    windows.res1.setText(msg)
        
    
def test(ch):
    i=1
    while (i<len(ch)-1 and ("A"<=ch[i]<="Z" or ch[i]==" ")):
        i=i+1
    return (i==len(ch)-1 and ch.find("  ")==-1 and len(ch)<=50 and ch[0]!=" " and ch[len(ch)-1]!=" ")
def mot(ch,t):
    n=taille(ch)
    ch=ch+" "
    for i in range(n):
        p=ch.find(" ")
        t[i]=ch[0:p]
        ch=ch[p+1:len(ch)]
    
def taille(ch):
    n=1
    while(ch.find(" ")!=-1):
        p=ch.find(" ")
        ch=ch[p+1:]
        n=n+1
    return n

def efface(ch):
    ch1=""
    for i in range(len(ch)):
        if ch1.find(ch[i])==-1:
            ch1=ch1+ch[i]
    return(ch1)

def recherche(ch,t):
    mot(ch,t)
    m=efface(t[0])
    n=taille(ch)
    ch2=""
    for i in range(len(m)):
        j=1
        while(j<n and t[j].find(m[i])!=-1):
            j=j+1
        if j==n:
            ch2=ch2+m[i] 
    return(ch2)
        
            
def lettre1(ch,t):
    ch2=recherche(ch,t)
    msg=""
    if len(ch2)==1:
        msg=msg+ch2+" est une lettre d'or"
    elif len(ch2)>1:
        for i in range(len(ch2)):
            msg=msg+ch[i]+" ; "
        msg=msg[0:len(msg)-1]+"sont les lettres d'or"
    return(msg)
def lettre2(ch,t):
    ch2=recherche(ch,t)
    msg="le nombre des lettres d'or = "+str(len(ch2))
    return(msg)

def inverse(ch,t):
    n=taille(ch)
    ch1=""
    ch=ch+" "
    mot(ch,t)
    for i in range(n):
        ch1=t[i]+" "+ch1
    return(ch1[0:len(ch)-1])
    
app=QApplication([])
windows=loadUi("Lettre d'or.ui")
windows.show()
windows.L.clicked.connect(play1)
windows.Inv.clicked.connect(play2)
app.exec_()