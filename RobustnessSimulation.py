#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:38:07 2020

@author: henriette
"""

 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 11:31:58 2018

@author: henriette
"""

from toolsstep2 import * 
import bisect
   
        
def randomPerturbation(G, phi, extb, sigma):
    torem = []
    for v in G.nodes():
        if random.uniform(0,1) < phi: 
            torem.append(v)
#            G.remove_node(v) 
    G.remove_nodes_from(torem) 
    
    popsize = G.number_of_nodes()
    if popsize == 0:
        return(0)

    else:
        oldnumbers = 0
        
        while popsize != oldnumbers: 
            oldnumbers = popsize                            

            G = extinction(G, extb)
            G = colonisation(G, sigma)
        
            popsize = 0
            for v in G.nodes():
                if G.node[v]['pop'] == 1:
                    popsize += 1 
    
        return(popsize/float(G.number_of_nodes()))

    
    
def contagiousPerturbation(G,phi, extb, sigma):
    iSH = random.choice(G.nodes())    
    Infected = [iSH]
    
    for v in Infected:
        for w in G.neighbors(v):
            if w not in Infected:
                val = random.uniform(0,1)
                if val < phi: 
                    Infected.append(w)
                    
        G.remove_node(v)
        
    oldnumbers = 0
    n = G.number_of_nodes()
    popsize = n
    while popsize != oldnumbers:
        oldnumbers = popsize
        
        G = extinction_new(G,extb)
        G = colonisation(G,sigma)
                
        popsize = 0
        for v in G.nodes():
            if G.node[v]['pop'] == 1:
                popsize += 1
    if n > 0:
        return(popsize/float(n))
    else:
        return(0)

        

def cdf(weights):
    total = sum(weights)
    
    if total != 0:
        result = []
        cumsum = 0
        for w in weights:
            cumsum += w
            result.append(cumsum / total)
        return result
    else: 
        return weights

def choice(population, weights):
    assert len(population) == len(weights)
    if sum(weights) != 0:
        cdf_vals = cdf(weights)
        x = random.random()
        idx = bisect.bisect(cdf_vals, x)      
        return population[idx]
    else:
        idx = random.randint(0, len(population)-1)
        return population[idx]

def peripheralPerturbation(G, phi, extb, sigma):
    bc = nx.betweenness_centrality(G, weight = 'weight')  
    try:
        population, weights = zip(*bc.iteritems())
    except:
        population, weights = zip(*bc.items())

    population = list(population)
    weights = list(weights)
    
    weights_inv = []
    for w in weights: 
        weights_inv.append(1-w)

    

    chosen = []
    while len(chosen) < G.number_of_nodes()*phi:
        hab = choice(population, weights_inv)
        population.remove(hab)
        weights_inv.remove(1-bc[hab])
        chosen.append(hab)
        
    for v in chosen:
        G.remove_node(v)
    
    n = G.number_of_nodes()
    popsize = n    
    if popsize == 0:
        return(0)
        
    else:                        
        oldnumbers = 0
        while popsize != oldnumbers: 
            oldnumbers = popsize                            
            G = extinction_new(G,extb)
            G = colonisation(G,sigma)
            popsize = 0
            for v in G.nodes():
                if G.node[v]['pop'] == 1:
                    popsize += 1
    
        return(popsize/float(n)) 
        
    
        

    
    
streamnetwork = '025025050_'
maxdist = {'linear_01' : 400, 'random_01' : 900, 'clustr_01' : 650}    

Wdh = 10
Phi = np.linspace(0,1, 100) 
Robustness = {}


Perturbation = 'random'

Squares = 26
Habitats = 10


for Perturbation in ['random', 'peripheral', 'contagious']:
    for extb in range(2,10): 
        for sigma in range(2,10): 
            for graphtype in ['random_01', 'clustr_01', 'linear_01', 'ER', 'R', 'NWS', 'SF']:
                print(Perturbation, extb, sigma, graphtype)
                
                for square in range(1, Squares):
                    for habitatselection in range(Habitats):
                        print(square, habitatselection)
                        
                        if graphtype in ['random_01', 'clustr_01', 'linear_01']:
                            Gc = loadGraph(graphtype, square, habitatselection, maxdist[graphtype], streamnetwork)
                        else: 
                            Gc = loadWeightedNetwork(graphtype, square)
                            
                        Robustness[(square, habitatselection)] = []
                        for wdh in range(Wdh):
                            summe = 0
                            Popsize = []
                            for phi in Phi:
                                G = Gc.copy()
                                if Perturbation == 'random':
                                    popsizephi = randomPerturbation(G, phi, extb, sigma)
                                elif Perturbation == 'contagious':
                                    popsizephi = contagiousPerturbation(G, phi, extb, sigma)
                                elif Perturbation == 'peripheral':
                                    popsizephi = peripheralPerturbation(G, phi, extb, sigma)
                                    
                                Popsize.append(popsizephi)
                            RI = 1.0/100 * (sum(Popsize) - 0.5 * (Popsize[0] + Popsize[99]))    
                            Robustness[(square, habitatselection)].append(RI)
            
                            
                file = open(Perturbation + '/Robustness_' + graphtype + '_' + str(extb) + '_' + str(sigma) + '.csv', 'w')
                file.write('Square;Habitatselection ')
                for wdh in range(Wdh):
                    file.write(';' + str(wdh))
                file.write('\n')
                
                for square in range(1,Squares):
                    for habitatselection in range(Habitats):
    
                        file.write(str(square) + ';' + str(habitatselection))
                        for wdh in range(Wdh):
                            file.write(';' + str(Robustness[(square, habitatselection)][wdh]))
                        file.write('\n')
                file.close()
            
        
             
        
    


