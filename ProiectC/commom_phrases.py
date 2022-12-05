import re

def printab(a,b): #Printarea a doua elemente
    print(a)
    print(b)
    print()
#Preluarea argumentelor din comanda
def Show_common_phrases(file1,file2):
        
    #Citirea frazelor din fisierele text
    f = open(file1,"r")
    x=f.read().lower()
    f = open(file2,"r")
    y=f.read().lower()
    #printab(x,y)
    #Inlaturam spatiile in exces din jurul frazelor citite
    x = x.strip()
    y = y.strip()
    #printab(x,y)
    #Inlaturarea spatiilor in exces din jurul punctelor
    x = re.sub(r'\s*\.\s*','.',x)
    x = re.sub(r'\s*\!\s*','!',x)
    x = re.sub(r'\s*\?\s*','?',x)
    y = re.sub(r'\s*\.\s*','.',y)
    y = re.sub(r'\s*\!\s*','!',y)
    y = re.sub(r'\s*\?\s*','?',y)
    #printab(x,y)
    #Inlaturarea spatiilor in exces dintre cuvinte
    x = re.sub(r'\s+',' ',x)
    y = re.sub(r'\s+',' ',y)
    #printab(x,y)
    #Impartirea frazelor in propozitii (in lista exista posibilitatea sa intalnim elemente goale <" ">)
    #x = x.split('.')
    #y = y.split('.')
    x = re.split('[.]|!|[?]| ', x)
    y = re.split('[.]|!|[?]| ', y)
    #printab(x,y)
    #Transformama din liste in set pentru a scapa de eventuale propozitii repetate
    x_set = set(x)
    y_set = set(y)
    #printab(x,y)

    prop_comune = x_set.intersection(y_set)
    Propozitii = []
    for i in prop_comune:
        if i != '':
            Propozitii.append(i)

    for i in Propozitii:
        counter=0
        for j in x:
            if i == j:
                counter+=1
        print("Cuvant " + str(i) + " Counter " + str(counter))
    
    return(Propozitii)
