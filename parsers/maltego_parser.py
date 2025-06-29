import networkx as nx

def parse_maltego_graph(graphml_path):
    """
    Parse un fichier GraphML Maltego et retourne une structure de graphe exploitable.
    """
    G = nx.read_graphml(graphml_path)

    nodes = []
    edges = []

    for node_id, data in G.nodes(data=True):
        nodes.append({
            "id": node_id,
            "type": data.get("type", "Unknown"),
            "label": data.get("label", data.get("value", node_id)),
            "properties": dict(data)
        })

    for source, target, data in G.edges(data=True):
        edges.append({
            "source": source,
            "target": target,
            "type": data.get("type", "related_to"),
            "properties": dict(data)
        })

    return {
        "nodes": nodes,
        "edges": edges
    }