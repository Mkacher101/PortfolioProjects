import numpy
import nltk
from nltk.corpus import stopwords
from scipy import spatial
def SimilariteCosinus(a,b):
    return(1-spatial.distance.cosine(matriceBinaire[a],matriceBinaire[b]))



import mysql.connector
from nltk.stem.snowball import FrenchStemmer
matriceBinaire=numpy.zeros((0,0))
#--connexion a la base de donnnee
connexion=mysql.connector.connect(host="localhost", user="root", password="", database="sr",port=3306)
curseur=connexion.cursor()
#--recuperation des donnees de la base
curseur.execute("select * from produit")
produits=curseur.fetchall()

StopList=list(stopwords.words('french'))
StopList.extend([".", ",", ":", "/", "!","'","-"])
dictProduits={}
ListTotaliteMots=set()


for p in produits:
    idPdt=int(p[0])
    Description=p[2]
    Mots=nltk.word_tokenize(Description)
    
    stemer=FrenchStemmer()
    MotsStems=[]
    for m in Mots:
        MotsStems.append(stemer.stem(m))

    ListFinalMots=[]
    for m in MotsStems:
        if m not in StopList:
            ListFinalMots.append(m)
    #print(ListFinalMots)
    for m in ListFinalMots:
       ListTotaliteMots.add(m)
    dictProduits[idPdt]=ListFinalMots  
    
  
df={}
for m in ListTotaliteMots:
    nbr=0
    for i in range(len(dictProduits)):
        if m in dictProduits[i+1]:
            nbr+=1
    df[m]=nbr
#print(df)    
#print(dictProduits)

matriceBinaire=numpy.zeros((len(dictProduits),len(ListTotaliteMots)))
TF=0;
IDF=0; 
for i in range(len(dictProduits)):
    j=0
    for m in ListTotaliteMots:
        if m in dictProduits[i+1]:
            TF=df[m]/len(ListTotaliteMots)
            IDF=numpy.log(len(dictProduits)/df[m])
            matriceBinaire[i][j]=TF*IDF
        j+=1   
#print(matriceBinaire)



# calcul de similarite sur la base de matrice
def SimilariteJaccard(a,b):
    return(1-spatial.distance.jaccard(matriceBinaire[a],matriceBinaire[b]))
matriceSim=numpy.zeros((len(dictProduits),len(dictProduits)))
     
for i in range(len(dictProduits)):
    for j in range(len(dictProduits)):
        matriceSim[i][j]=SimilariteJaccard(i,j)        
#print(matriceSim)

print("---------------------------------------------------------------------------------------")
for p in produits:
 print("ID:"+str(p[0])+":"+p[2])
 print("---------------------------------------------------------------------------------------")
 
idp=int(input("Choisir l'id du produit:"))
print("---------------------------------------------------------------------------------------")
def maxsim(tab,n):
   tabmaxs=[] 
  
   for i in range (n):
    i=0
    maxs=min(tab)   
    idx=0
    for j in range(len(tab)):
       i+=1
       
       if((tab[j]>maxs)and(j not in tabmaxs)):
           maxs=tab[j]
           idx=j
          
           
       
    tabmaxs.append(idx)   
    
   return (tabmaxs)
lesmax=maxsim(matriceSim[idp-1],4 )
print("Reccomandation:")
print("---------------------------------------------------------------------------------------")

#print(lesmax) impo
for i in(lesmax):
    if(produits[i][2]!=produits[idp-1][2]):
     print(produits[i][2])
     print("---------------------------------------------------------------------------------------")

     
    
    




 



     
                 
                
                



        
       
        

