import numpy as np
import nashpy as nash
A = np.array([[10,0],[0,5]]) # A is the row player
B = np.array([[5,0],[0,10]]) # B is the column player
game1 = nash.Game(A,B)
print(game1)
print()
print("The nash equilibria are: ")
equilibria = game1.support_enumeration()
for eq in equilibria:
    print(eq)