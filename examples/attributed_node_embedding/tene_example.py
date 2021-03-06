"""TENE example."""

import numpy as np
import networkx as nx
from karateclub.node_embedding.attributed import TENE

g = nx.newman_watts_strogatz_graph(200, 20, 0.05)

x = np.random.uniform(0, 1, (200, 200))

model = TENE()

model.fit(g, x)
