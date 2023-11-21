import numpy as np
import nashpy as nash
A = np.array([[-6,0],[-10,-1]]) # A is the row player
B = np.array([[-6,-10],[0,-1]]) # B is the column player
game1 = nash.Game(A,B)
print(game1)
print()
print("The nash equilibria are: ")
equilibria = game1.support_enumeration()
for eq in equilibria:
    print(eq)