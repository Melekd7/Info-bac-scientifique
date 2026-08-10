from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def play():
    ch=str(windows.tex.text())
    m1=str(windows.mot1.text())
    m2=str(windows.mot2.text())
    if ch=="" or m1=="" or m2=="":
        msg="Veuillez saisir toutes les informations"
    elif not(test(ch)):
        msg="Veuillez saisir une chaine valide"
    elif not(valide(m1)):
        msg="Veuillez saisir un mot1 valide"
    else:
        msg=joker(ch,m1,m2)
    windows.res.setText(msg)
def test(ch):
    i=0
    while(i<len(ch) and ("a"<=ch[i]<="z" or ch[i]==" ")):
        i=i+1
    return(i==len(ch) and ch.find("  ")==-1 and ch[0]!=" " and ch[len(ch)-1]!=" " and len(ch)<=100)
def valide(ch):
    i=0
    while(i<len(ch) and ("a"<=ch[i]<="z" or ch[i]=="?")):
        i=i+1
    return(i==len(ch) and ch.find("?")!=-1 and eff(ch).find("?")==-1)
def joker(ch,m1,m2):
    ch=ch+" "
    ch2=""
    q=m1.find("?")
    mot1=m1[0:q]
    mot2=m1[q+1:]
    while(ch.find(mot1)!=-1):
        p=ch.find(mot1)
        if ch[p+len(mot1):len(mot2)]==mot2:
            ch=ch[0:p]+m2+ch[p+len(m1)-1:]
    return(ch)
def eff(ch):
    p=ch.find("?")
    return(ch[:p]+ch[p+1:])
app=QApplication([])
windows=loadUi("joker_int.ui")
windows.show()
windows.rech.clicked.connect(play)
app.exec_()

