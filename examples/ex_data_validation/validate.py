from __future__ import annotations

import argparse

import pandas as pd


def validate_frame(df: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    if df.empty:
        errors.append("DataFrame is empty")
    if df.columns.duplicated().any():
        errors.append("Duplicate column names detected")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, help="Path to CSV or JSON file")
    args = parser.parse_args()

    if args.path.lower().endswith(".csv"):
        df = pd.read_csv(args.path)
    else:
        df = pd.read_json(args.path)

    errs = validate_frame(df)
    if errs:
        for e in errs:
            print(f"ERROR: {e}")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
