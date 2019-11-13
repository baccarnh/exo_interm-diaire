liste=["'''", "*","**","***","****","*****", "'''"]
for i in liste:
    print(i)

#méthode soufien

py="*"
for taille in range(1,6):
    print(py*taille)

# methode bruno
var="\n"
s=""
for i in range(1, 6):
    s+= "*"
    var+=s+"\n"
print(var)

