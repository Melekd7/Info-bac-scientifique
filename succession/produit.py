print("==== systéme de commande en ligne ===")
n=int(input("combien de produits différents souhaitez-vous connander?"))
print("=========ticket de caisse=========")
for i in range(1,n+1):
    print ("produit",i,":")      
    nomproduit=input("nom de produit:")
    pu=float(input("prix unitaire (en TND):"))
    qt=int(input("quantité désirée:"))
    mt=pu*qt
    print("montant total:",mt)
    if mt>400:
           remise:mt*4/100
    else:
           remise=0
    totaprremise=mt-remise
    if totaprremise>1000:
        liv=0
    else:
        liv=7
    tot=totaprremise+liv
    print("remise:",remise)
    print("frais de livraison:",liv,"TND")
    print("total à payer;",tot,"TND")
