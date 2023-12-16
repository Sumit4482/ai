climate(warm).
climate(sunny).
climate(rainy).

mood(happy,warm).
mood(happy,sunny).
mood(sad,rainy).

weather(X,Y):- climate(X),mood(Y,X).





