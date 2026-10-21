# import modules
from ddgs import DDGS
import argparse

# Parser Part
parser = argparse.ArgumentParser(description="A lightweight command-line utility for web searching")

parser.add_argument("-q", "--query", type=str, required=True, help="Search QUery")
parser.add_argument("-m", "--max-results", type=int, default=3, help="Maximum Results")

args = parser.parse_args()

# Main Code (Web Search)
with DDGS() as ddgs:
    results = ddgs.text(query=args.query, max_results=args.max_results)

    for item in results:
        print(f"Title: {item.get('title')}\n")
        print(f"Description:  {item.get('body')}\n")
        print(f"Link: {item.get('href')}\n")
        print("-" * 50)