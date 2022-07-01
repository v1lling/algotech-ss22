from icecream import ic

def kartenfaerbung(laender, nachbarn):
    for i,land in enumerate(laender): # O(n)
        if not zugeteilte_farben[i]: # O(1) ???
            for j,nachbar in enumerate(nachbarn[i]): # O(n)
                if nachbar==0: # O(1)
                    zugeteilte_farben[j] = farben[i] # O(1)

zugeteilte_farben = ["", "", "", "", ""]
laender = ["DE", "FR", "ES", "PO", "CH"]
farben = ["blau", "rot", "gelb", "gruen", "lila"]
nachbarn = [[0,1,0,1,1],
            [1,0,1,0,1],
            [0,1,0,0,0],
            [1,0,0,0,0],
            [1,1,0,0,0]]
kartenfaerbung(laender, nachbarn)
ic(laender)
ic(zugeteilte_farben)
