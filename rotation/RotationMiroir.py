from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def mini(ch):
    i=0
    while(i<len(ch) and "a"<=ch[i]<="z"):
        i=i+1
    return(i==len(ch))
def Play():
    ch=windows.ch.text()
    if ch=="":
        msg="Veuillez introduire une chaine"
    elif len(ch)>=10 or not(mini(ch)):
        msg="Veuillez introduire une chaine valide"
    else:
        msg=("La chaine cryptée est:"+miroir(rotation(ch)))
    windows.res.setText(msg)
    
def rotation(ch):
    res=""
    for i in range(0,len(ch)):
        res=res+chr(97+(ord(ch[i])-97+13)%26)
    return(res)
def miroir(ch):
    n=len(ch)
    for i in range(n//2):
        ch=ch[0:i]+ch[n-1-i]+ch[i+1:n-1-i]+ch[i]+ch[n-i:]
    return(ch)
            
    


app=QApplication([])
windows=loadUi("InterfaceRotationMiroir.ui")
windows.show()
windows.crypt.clicked.connect(Play)
app.exec_()