import numpy as np
import nashpy as nash
A = np.array([[4.5,4,2,2],[4,4,2,2],[2,2,2,2],[2,2,2,2]]) # A is the row player
B = np.array([[4.5,5,3,3],[3,3,3,3],[1,1,1,1],[1,1,1,1]]) # B is the column player
game1 = nash.Game(A,B)
print(game1)
print()
print("The nash equilibria are: ")
equilibria = game1.support_enumeration()
for eq in equilibria:
    print(eq)