Supplementary information for the publication 
# Indicators for Assessing the Robustness of Metapopulations against Habitat Loss
Henriette Heer <sup>a</sup>, Lucas Streib <sup>a</sup>, Ralf B. Schäfer <sup>a</sup>, Ulf Dieckmann <sup>b,c</sup>

<sup>a</sup> Department of Quantitative Landscape Ecology, iES Landau, University of Koblenz-Landau, Fortstr. 7, 76829 Landau i.d. Pfalz, Germany  
<sup>b</sup> Evolution and Ecology Program, International Institute of Applied Systems Analysis (IIASA), 2361 Laxenburg, Austria  
<sup>c</sup> Department of Evolutionary Studies of Biosystems, The Graduate University for Advanced Studies (Sokendai), Hayama, Kanagawa 240-0193, Japan  

### A. Framework

The software framework of this model consists of Python 2.7.17. Python packages required are the following: 
* Networkx 2.2
* Psycopg2 2.8.4
* Random
* Numpy 1.15.4
* bisect


### B. Input Data 

The following networks are required as input data: 
* Landscape-based networks (with random, clustered, and linear habitat allocation)
* Standard networks (random, regular, small-world, and scale-free networks) 
Landscape-based networks can be found at https://github.com/luclucky/HabitatConnectivity_Colonization. The function loadGraph in our Python code will load the exact networks used by our model.
The standard networks are accessible in the folder networks. 


### C. Python Code

For database access from Python, the connection parameters have to be specified in the Python script. 
The Python script RobustnessSimulation.py contains the code to load the networks, run the simulations, and save the results. In order to execute the code, the directories may have to be updated and the connection parameters to access the database for the landscape-based networks have to be specified (see lines 11 and 18 of the Python script).

For suggestions or requests for further information please contact the corresponding author Henriette Heer:  
heer@uni-koblenz.de  
+49 6341 280-32318  
Department of Quantitative Landscape Ecology  
iES - Institute for Environmental Sciences   
University of Koblenz-Landau, Campus Landau  
Fortstr. 7  
76829 Landau  
Germany  
