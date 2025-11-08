import argparse
import sys, os

# add project root to import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.rewrite import clean_rewrite

def main():
    parser = argparse.ArgumentParser(description="Safe text rewrite tool")
    parser.add_argument("text", type=str, nargs="+", help="Text to rewrite safely")
    args = parser.parse_args()

    joined = " ".join(args.text)
    safe = clean_rewrite(joined)
    print("\nRewritten:")
    print(safe)

if __name__ == "__main__":
    main()
