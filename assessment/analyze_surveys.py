#!/usr/bin/env python3
"""Analyze matched pre/post LiNC survey responses.

Usage:
    python analyze_surveys.py responses.csv
    python analyze_surveys.py responses.csv --year 2027
    python analyze_surveys.py responses.csv --out results.csv

Input: a CSV laid out like survey-data-template.csv, one row per student per
timepoint ("pre" or "post"), core items scored 1-5. Rows whose code starts
with "EXAMPLE" are ignored.

For each item and each domain, the script reports the mean before and after,
the mean change, how many students improved / stayed the same / declined,
and a two-sided Wilcoxon signed-rank test. With small cohorts, pool years
and read the counts and effect sizes alongside the p-values.

Requires: pandas, scipy  (pip install pandas scipy)
"""

import argparse
import sys

import pandas as pd
from scipy.stats import wilcoxon

DOMAINS = {
    "Research self-efficacy": ["SE1", "SE2", "SE3", "SE4", "SE5", "SE6"],
    "Belonging and voice": ["BE1", "BE2", "BE3", "BE4"],
    "Science identity": ["ID1", "ID2", "ID3"],
    "Educational and career intentions": ["IN1", "IN2", "IN3"],
    "Science communication": ["CO1", "CO2", "CO3"],
}
ITEMS = [item for items in DOMAINS.values() for item in items]
KEYS = ["code", "year"]


def load(path, year=None):
    df = pd.read_csv(path, dtype={"code": str})
    df["code"] = df["code"].str.strip().str.upper()
    df["timepoint"] = df["timepoint"].str.strip().str.lower()
    df = df[~df["code"].str.startswith("EXAMPLE")]
    if year is not None:
        df = df[df["year"] == year]
    missing = [c for c in KEYS + ["timepoint"] + ITEMS if c not in df.columns]
    if missing:
        sys.exit(f"Missing columns: {', '.join(missing)}")
    for domain, items in DOMAINS.items():
        df[domain] = df[items].mean(axis=1)
    return df


def match(df):
    pre = df[df["timepoint"] == "pre"].set_index(KEYS)
    post = df[df["timepoint"] == "post"].set_index(KEYS)
    both = pre.index.intersection(post.index)
    unmatched = len(pre.index.symmetric_difference(post.index))
    return pre.loc[both], post.loc[both], unmatched


def compare(pre, post, column):
    paired = pd.DataFrame({"pre": pre[column], "post": post[column]}).dropna()
    diff = paired["post"] - paired["pre"]
    n = len(paired)
    row = {
        "measure": column,
        "n": n,
        "mean_pre": paired["pre"].mean(),
        "mean_post": paired["post"].mean(),
        "mean_change": diff.mean(),
        "improved": int((diff > 0).sum()),
        "same": int((diff == 0).sum()),
        "declined": int((diff < 0).sum()),
        "p_value": float("nan"),
        "effect_size_r": float("nan"),
    }
    if n >= 2 and (diff != 0).any():
        res = wilcoxon(paired["post"], paired["pre"], zero_method="wilcox",
                       method="approx")
        row["p_value"] = res.pvalue
        nz = int((diff != 0).sum())
        # r = Z / sqrt(N); recover Z from the normal-approximation p-value
        from scipy.stats import norm
        z = norm.isf(res.pvalue / 2)
        row["effect_size_r"] = (z / nz ** 0.5) * (1 if diff.mean() >= 0 else -1)
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("csv", help="exported survey responses")
    parser.add_argument("--year", type=int, help="analyze one year only")
    parser.add_argument("--out", help="save results to this CSV")
    args = parser.parse_args()

    df = load(args.csv, args.year)
    pre, post, unmatched = match(df)
    if len(pre) == 0:
        sys.exit("No students have both a pre and a post response. Check the codes.")

    rows = [compare(pre, post, d) for d in DOMAINS]
    rows += [compare(pre, post, i) for i in ITEMS]
    results = pd.DataFrame(rows)

    pd.set_option("display.width", 140)
    pd.set_option("display.float_format", lambda v: f"{v:.2f}")
    scope = f"year {args.year}" if args.year else "all years"
    print(f"\nMatched students ({scope}): {len(pre)}")
    if unmatched:
        print(f"Responses without a match (excluded): {unmatched}")
    print("\nDOMAINS")
    print(results.iloc[: len(DOMAINS)].to_string(index=False))
    print("\nITEMS")
    print(results.iloc[len(DOMAINS):].to_string(index=False))
    print("\nWilcoxon signed-rank, two-sided. r = effect size (0.1 small, 0.3 medium, 0.5 large).")

    if args.out:
        results.to_csv(args.out, index=False)
        print(f"\nSaved to {args.out}")


if __name__ == "__main__":
    main()
