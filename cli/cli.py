from datetime import datetime
from pyfiglet import Figlet
from termcolor import colored

def show_banner():
    f = Figlet(font='slant')
    title = f.renderText("OsintReport")
    print(colored(title, "cyan"))
    print(colored("Créé par A.Ayouba | 27/06/2025", "white"))
    print(colored("-" * 60, "grey"))

def get_user_choices():
    print("\n📜 MENU")
    print("  [0] Generate Report")
    print("  [1] Generate Report with AI")

    while True:
        choice = input("\n👉 Choisissez une option [0/1] : ").strip()
        if choice in ["0", "1"]:
            break
        print("❌ Entrée invalide. Tapez 0 ou 1.")

    print("\n📂 Type de graphe")
    print("  [0] Maltego (.graphml)")
    print("  [1] OSINTraker (.json)")

    source_map = {"0": "maltego", "1": "osintraker"}
    while True:
        source_choice = input("\n👉 Choisissez la source [0/1] : ").strip()
        if source_choice in source_map:
            break
        print("❌ Option invalide.")

    filepath = input("\n🧾 Entrez le chemin du fichier : ").strip()
    output_path = input("💾 Nom du rapport (ex: rapport.md) : ").strip() or "rapport.md"

    return {
        "use_ai": choice == "1",
        "source": source_map[source_choice],
        "input_path": filepath,
        "output_path": output_path
    }
