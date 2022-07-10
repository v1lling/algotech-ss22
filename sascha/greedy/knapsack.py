from icecream import ic

def knapsack(rucksack):
    eingepackt = 0
    for i,wert in enumerate(werte):
        if rucksack >= gewicht[i]:
            rucksack = rucksack - gewicht[i]
            eingepackt = eingepackt + wert
            continue
    ic(eingepackt)
    
werte = [120, 100, 60]
gewicht = [30, 20, 10]

knapsack(50)