parent(harsh,nipun).
parent(divyam,aditya).

mother_Children(Aditya,Harsh).
father_Children(Divyam,Harsh).

father_Children(Harsh,Kawale).
mother_Children(Nipun,Sakare).

sibling(X,Y):-father_Children(Z,X),mother_Children(Z,Y).
grandfather(A,B):-father_Children(A,Z),father_Children(Z,B).

