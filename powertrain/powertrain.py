from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def puissance(a,b):
    p=1
    for k in range(1,b+1):
        p=p*a
    return(p)
def transformer(n):
    t=1
    ch=str(n)
    if len(ch)%2==0:
        for i in range(0,len(ch)-1,2):
            t=t*puissance(int(ch[i]),int(ch[i+1]))
    else:
        for i in range(0,len(ch)-2,2):
            t=t*puissance(int(ch[i]),int(ch[i+1]))
        t=t*int(ch[len(ch)-1])
    return(t)
def chercher(n,m):
    ch=""
    for i in range(n,n+m+1):
        ch=ch+str(transformer(i))+"-"
    ch=ch[0:len(ch)-1]
    return(ch)
def play():
    n=int(windows.vn.text())
    m=int(windows.vm.text())
    if (200<=n<=999999) and (3<=m<=10):
        msg1="La transformation de"+str(n)+"et les "+str(m)+" entiers consécutifs sont:"
        msg2=chercher(n,m)
        windows.res1.setText(msg1)
        windows.res2.setText(msg2)
    else:
        msg1="veillez respecter 200<=n<=999999999 et 3<=m<=10"
        windows.res2.setText(msg1)
app=QApplication([])
windows=loadUi("interfacepowertrain.ui")
windows.show()
windows.transformer.clicked.connect(play)
app.exec_()
        

        