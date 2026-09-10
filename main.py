"""Project entry point.

Run with:
    python main.py
"""

from __future__ import annotations

import argparse
import json
from typing import Sequence


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Project command-line entry point")
    parser.add_argument(
        "--message",
        default="Project is ready.",
        help="Message to print when the application starts.",
    )
    return parser


def serialize_result(result):
    return json.dumps(result)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = {"status": "ok", "message": args.message}
    print(serialize_result(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
