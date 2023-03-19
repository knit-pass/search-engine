from pywikigraph import WikiGraph

wg = WikiGraph()

paths = wg.get_shortest_paths_info("Alan Turing", "Semantic Web")
print(paths)
