import json

def parse_osintraker_json(json_path):
    """
    Parse un export JSON d'OSINTraker et retourne une structure normalisée.
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    nodes = []
    edges = []

    for ent in data.get("entities", []):
        nodes.append({
            "id": ent.get("id"),
            "type": ent.get("type", "Unknown"),
            "label": ent.get("name") or ent.get("label"),
            "properties": ent
        })

    for link in data.get("links", []):
        edges.append({
            "source": link.get("source"),
            "target": link.get("target"),
            "type": link.get("type", "connected_to"),
            "properties": link
        })

    return {
        "nodes": nodes,
        "edges": edges
    }
