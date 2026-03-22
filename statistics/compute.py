from pathlib import Path
import argparse

from moulinetteji import Statistics

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render moulinette JSON reports to HTML and print statistics."
    )

    parser.add_argument(
        "input_dir",
        type=Path,
        help="Base directory used for statistics and render output.",
    )

    args = parser.parse_args()
    input_dir = args.input_dir.resolve()

    stats = Statistics(input_dir, recursive=True)
    stats.print_stats()


if __name__ == "__main__":
    main()
