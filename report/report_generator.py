import networkx as nx
import os
import openai

def generate_report(parsed_data, graph: nx.Graph, output_path: str, format="md", ai_text=None):
    if format != "md":
        raise ValueError("Seul le format 'md' est supporté.")

    if ai_text == "use_gpt":
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            openai_api_key = input("🔐 Entrez votre clé API OpenAI : ").strip()

        openai.api_key = openai_api_key

  
        from utils.graph_utils import extract_summary_for_ai
        summary = extract_summary_for_ai(graph)

        prompt = (
            "Tu es un expert en cybersécurité. À partir du résumé suivant d’un graphe OSINT, "
            "génère un rapport complet en Markdown clair, structuré, avec titres, analyse, statistiques, et recommandations.\n\n"
            f"Résumé du graphe :\n{summary}\n\n"
            "Le rapport doit contenir au moins :\n"
            "- Un titre principal\n"
            "- Un résumé d’analyse\n"
            "- Des sections pour les entités clés, relations critiques, et hypothèses\n"
            "- Une conclusion\n"
            "- Des bullets ou des tableaux si nécessaire"
        )

        print("🤖 Génération du rapport par GPT...")
        response = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=[
                {"role": "system", "content": "Tu es un analyste OSINT qui rédige des rapports professionnels."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        md_report = response.choices[0].message.content.strip()

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_report)

        print(f"\n✅ Rapport généré par GPT et sauvegardé dans : {output_path}")
        return
