import networkx as nx
from GraphRicciCurvature.OllivierRicci import OllivierRicci


#ok here is the peterson graph from shomee's package
G = nx.petersen_graph()

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())


# do the the actual Ollivier-Ricci curvature calc.
orc = OllivierRicci(G, alpha=0.5, verbose="INFO")
orc.compute_ricci_curvature()


#print it out curvature for every edge
print("Edge curvatures:")

for u, v, data in orc.G.edges(data=True):
    print(f"{u} -- {v}: {data['ricciCurvature']}")
