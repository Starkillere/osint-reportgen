import networkx as nx
from collections import Counter

def build_nx_graph(parsed_data):
    """
    Construit un NetworkX Graph à partir des données normalisées.
    """
    G = nx.Graph()

    for node in parsed_data["nodes"]:
        G.add_node(node["id"], **node)

    for edge in parsed_data["edges"]:
        G.add_edge(edge["source"], edge["target"], **edge)

    return G

def get_entity_types_stats(parsed_data):
    """
    Compte les types d'entités dans le graphe.
    """
    types = [node["type"] for node in parsed_data["nodes"]]
    return dict(Counter(types))

def get_top_entities_by_degree(G, top_n=5):
    """
    Retourne les entités avec le plus de connexions (par degré).
    """
    degree_list = sorted(G.degree, key=lambda x: x[1], reverse=True)
    return [
        {
            "id": node,
            "label": G.nodes[node].get("label", node),
            "degree": degree
        }
        for node, degree in degree_list[:top_n]
    ]

def get_connected_components(G):
    """
    Identifie les composantes connexes du graphe.
    """
    components = list(nx.connected_components(G))
    return [list(c) for c in components]

def extract_summary_for_ai(G):
    """
    Crée un résumé simplifié du graphe pour l'analyse IA (prompt).
    """
    summary = {
        "entity_count": G.number_of_nodes(),
        "connection_count": G.number_of_edges(),
        "top_entities": get_top_entities_by_degree(G),
        "types": get_entity_types_stats({
            "nodes": [G.nodes[n] for n in G.nodes()],
            "edges": []
        }),
        "components": len(list(nx.connected_components(G)))
    }
    return summary
