import re

def printab(a,b): #Printarea a doua elemente
    print(a)
    print(b)
    print()
#Preluarea argumentelor din comanda
def Show_common_phrases(file1,file2):
        
    #Citirea frazelor din fisierele text
    f = open(file1,"r")
    x=f.read()
    f = open(file2,"r")
    y=f.read()
    #printab(x,y)
    #Inlaturam spatiile in exces din jurul frazelor citite
    x = x.strip()
    y = y.strip()
    #printab(x,y)
    #Inlaturarea spatiilor in exces din jurul punctelor
    x = re.sub(r'\s*\.\s*','.',x)
    y = re.sub(r'\s*\.\s*','.',y)
    #printab(x,y)
    #Inlaturarea spatiilor in exces dintre cuvinte
    x = re.sub(r'\s+',' ',x)
    y = re.sub(r'\s+',' ',y)
    #printab(x,y)
    #Impartirea frazelor in propozitii (in lista exista posibilitatea sa intalnim elemente goale <" ">)
    x = x.split('.')
    y = y.split('.')
    #printab(x,y)
    #Transformama din liste in set pentru a scapa de eventuale propozitii repetate
    x = set(x)
    y = set(y)
    #printab(x,y)

    prop_comune = []
    for i in x:
        i=i.lower()
        if i not in prop_comune and i != '': #Daca nu verificam element gol si daca nu l-am validat deja.
            for j in y:
                j = j.lower()
                if i == j:
                    prop_comune.append(i.capitalize() + ".")

    return(prop_comune)
