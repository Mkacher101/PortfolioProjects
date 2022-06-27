'''
id_pr user_id  note


'''

import numpy
import mysql.connector
connexion=mysql.connector.connect(host="localhost", user="root", password="", database="sr",port=3306)
curseur=connexion.cursor()
curseur.execute("select * from note")
notebd=curseur.fetchall()
#print(notebd)
notebd.sort()
#print(notebd)
matn=[]
matnote=[]
k=0
for i in notebd:
    matn.append(i[2])
    k+=1
    if (k==6):
        k=0
        matnote.append(matn)
        matn=[]
        
#print(matnote)    
nbpdts=len(matnote[0]);
nbusers=len(matnote);
#print(nbpdts)
matricenotes=numpy.zeros((nbusers,nbusers))
matricenotes=matnote

from scipy import spatial
def SimilariteCosinus(a,b):
    return(1-spatial.distance.cosine(matricenotes[a],matricenotes[b]))
matricesim=numpy.zeros((nbusers,nbusers))
for i in range(nbusers):
    for j in range(nbusers):
        matricesim[i][j]=SimilariteCosinus(i,j)
#print(matricesim)


  
useR=6
maxuser1=-1
maxuser2=-1
maxuser3=-1
max1=-1
max2=-1
max3=-1
print("||------------------------------------HELLO----------------------------------------||")
print("||-----------Pour obtenir la meilleure recommandation pour l'utilisateur-----------||")
print("||---------------------------------------------------------------------------------||")
curseur=connexion.cursor()

print("||---------------------------Entrez l'id d'utilisateur-----------------------------||")
print("||----------------------------(Il y'a 6 utilisateurs)------------------------------||")
while 1:
 useR=int(input("||--->"))
 if (useR>0)and(useR<7):
     break
print("||      Les prouduits les plus similaires avec l'utilisateur d'id "+str(useR)+" sont:          ||" )
print("||---------------------------------------------------------------------------------||")
for i in range(len(matricesim[useR-1])):
    sim=matricesim[useR-1][i]
    if(sim>max1)and(sim!=1):
     max1=sim
     maxuser1=i+1
#print("Le user le plus similaire est",maxuser1,"avec similarité",max1)


for i in range(len(matricesim[useR-1])):
    sim=matricesim[useR-1][i]
    if(sim>max2)and(sim!=1)and(sim<max1):
     max2=sim
     maxuser2=i+1
#print("Le user le plus similaire est",maxuser2,"avec similarité",max2)

for i in range(len(matricesim[useR-1])):
    sim=matricesim[useR-1][i]
    if(sim>max3)and(sim!=1)and(sim<max1)and(sim<max2):
     max3=sim
     maxuser3=i+1
#print("Le user le plus similaire est",maxuser3,"avec similarité",max3)
#############################

curseur.execute("select * from note")
note=curseur.fetchall()
note.sort()
#print(note)
idproduit=-1
maxnote1=-1
for i in note:
    if i[1]==maxuser1:
        if i[2]>maxnote1:
            maxnote1=i[2]
for i in note:
 if (i[1]==maxuser1)and(i[0]==maxnote1):
     idproduit=i[0]
#print(idproduit)
curseur.execute("select * from produit")
produit=curseur.fetchall()
#print(produit)
produitrec1=""
prix=0
for i in produit:
    if int(i[0])==idproduit:
        produitrec1=i[2]    
        prix=i[3]
print("||"+produitrec1) 
print("||                                Prix:"+str(prix)+"DT                                    ||")
#####################################
produitrec2=""
maxnote2=-1
for i in note:
    if i[1]==maxuser2:
        if (i[2]>maxnote2):
            maxnote2=i[2]
for i in note:
 if (i[1]==maxuser2)and(i[2]==maxnote2):
     idproduit=i[0]
#print(idproduit)
#print(produit)
produitrec2=""
for i in produit:
    if (int(i[0])==idproduit):
        produitrec2=i[2]
        prix=i[3]
print("||---------------------------------------------------------------------------------||")

print("||"+produitrec2)
print("||                                Prix:"+str(prix)+"DT                                    ||")
print("||---------------------------------------------------------------------------------||")

#################################### 
produitrec3=""
maxnote3=-1
for i in note:
    if i[1]==maxuser3:
        if i[2]>maxnote3:
            maxnote3=i[2]
for i in note:
 if (i[1]==maxuser3)and(i[2]==maxnote3):
     idproduit=i[0]
#print(idproduit)
##################

#print(produit)

for i in produit:
    if int(i[0])==idproduit:
        produitrec3=i[2]
        prix=i[3]
print("||"+produitrec3)
print("||                                Prix:"+str(prix)+"DT                                    ||")
print("||---------------------------------------------------------------------------------||")
       
    
    
   
         
            
        
    
    





  
    


    
    
    
    
    
    