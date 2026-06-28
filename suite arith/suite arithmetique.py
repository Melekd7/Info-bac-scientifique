from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def trier(ch):
    permut=True
    while(permut):
        permut=False
        for k in range(0,len(ch)-2,2):
            BLOC1=ch[k:k+2]
            BLOC2=ch[k+2:k+4]
            if BLOC1>BLOC2 :
                ch=ch[0:k]+BLOC2+BLOC1+ch[k+4:len(ch)]
                permut=True
    return(ch)
def calculer(x):
    ch=trier(str(x))
    c=int(ch[2:4])-int(ch[0:2])
    i=2
    while(i<len(ch)-2 and c==int(ch[i+2:i+4])-int(ch[i:i+2])):
        i=i+2
    if i==len(ch)-2:
        return(c)
    else:
        return(0)
def play():
    x=int(windows.vx.text())
    if (6<=len(str(x))<=20 and x%2==0):
        msg1="les tranches de chiffres triées "+str(x)
        msg2=" des termes d'une suite arithmétique"
        c=calculer(x)
        if c!=0:
            msg=msg1+" forment"+msg2+" (r="+str(c)+")"
        else:
            msg=msg1+" ne forment pas"+msg2
        windows.res.setText(msg)
    else:
        msg="veuillez saisir un nombre de 6 à 20 chiffres et de longueur paire"
        windows.res.setText(msg)
        
        
        
    
    

app=QApplication([])
windows=loadUi("InterfaceArithmétique.ui")
windows.show()
windows.transformer.clicked.connect(play)
app.exec_()

