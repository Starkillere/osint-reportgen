from cli.cli import show_banner, get_user_choices
from parsers.maltego_parser import parse_maltego_graph
from parsers.osintraker_parser import parse_osintraker_json
from utils.graph_utils import build_nx_graph, extract_summary_for_ai
from report.report_generator import generate_report
from ai.analysis import analyse_graph_with_ai

def main():
    show_banner()

    user_choices = get_user_choices()

    source = user_choices["source"]
    input_path = user_choices["input_path"]
    output_path = user_choices["output_path"]
    use_ai = user_choices["use_ai"]
    gpt_api_key = user_choices["api_gpt_key"]

    if not use_ai:
        pass
    else:

if __name__ == "__main__":
    main()

