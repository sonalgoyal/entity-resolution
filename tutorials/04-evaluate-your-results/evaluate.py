"""Pairwise precision, recall and F1 for an entity resolution result.

Works with any tool's output as long as every record has:
  * a predicted cluster id (Zingg: z_cluster, Splink: cluster_id, dedupe: Cluster ID)
  * a true entity id (from ground truth)

Usage:
  python evaluate.py OUTPUT_DIR_OR_CSV --cluster-col z_cluster --truth-from-id id

  --truth-from-id derives the true entity from Febrl-style ids such as
  "rec-1021-org" and "rec-1021-dup-0" (both belong to entity "rec-1021").
  Use --truth-col instead if your file already has a true entity column.

  For linking tasks whose ground truth is a list of matching id pairs (for
  example the Leipzig Amazon-Google mapping), use:
  python evaluate.py OUTPUT --truth-pairs mapping.csv --id-col id --source-col z_zsource
"""

import argparse
import glob
import itertools
import os
import re

import pandas as pd


def read_output(path: str) -> pd.DataFrame:
    """Read a CSV file, or every part-*.csv file in a Spark output folder."""
    if os.path.isdir(path):
        files = sorted(glob.glob(os.path.join(path, "part-*")))
        files = [f for f in files if not f.endswith(".crc")]
        if not files:
            raise SystemExit(f"No part-* files found in {path}")
        return pd.concat((pd.read_csv(f, dtype=str) for f in files), ignore_index=True)
    return pd.read_csv(path, dtype=str)


def pairs(counts: pd.Series) -> int:
    """Number of record pairs inside groups of the given sizes: n * (n - 1) / 2."""
    return int((counts * (counts - 1) // 2).sum())


def evaluate(df: pd.DataFrame, cluster_col: str, truth_col: str) -> dict:
    predicted_pairs = pairs(df.groupby(cluster_col).size())
    true_pairs = pairs(df.groupby(truth_col).size())
    correct_pairs = pairs(df.groupby([cluster_col, truth_col]).size())

    precision = correct_pairs / predicted_pairs if predicted_pairs else 0.0
    recall = correct_pairs / true_pairs if true_pairs else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "records": len(df),
        "predicted_clusters": df[cluster_col].nunique(),
        "true_entities": df[truth_col].nunique(),
        "predicted_pairs": predicted_pairs,
        "true_pairs": true_pairs,
        "correct_pairs": correct_pairs,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
    }


def evaluate_against_pairs(df: pd.DataFrame, cluster_col: str, id_col: str, source_col: str, truth_file: str) -> dict:
    """Compare predicted cross-source pairs with a file of true (id_a, id_b) pairs."""
    truth = pd.read_csv(truth_file, dtype=str)
    true_pairs = {frozenset((a.strip(), b.strip())) for a, b in truth.iloc[:, :2].itertuples(index=False)}

    predicted_pairs = set()
    for _, group in df.groupby(cluster_col):
        rows = list(group[[id_col, source_col]].itertuples(index=False))
        for (id_a, src_a), (id_b, src_b) in itertools.combinations(rows, 2):
            if src_a != src_b:
                predicted_pairs.add(frozenset((id_a.strip(), id_b.strip())))

    correct = len(predicted_pairs & true_pairs)
    precision = correct / len(predicted_pairs) if predicted_pairs else 0.0
    recall = correct / len(true_pairs) if true_pairs else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "records": len(df),
        "predicted_pairs": len(predicted_pairs),
        "true_pairs": len(true_pairs),
        "correct_pairs": correct,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("output", help="CSV file or Spark output folder")
    parser.add_argument("--cluster-col", default="z_cluster")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--truth-col", help="column holding the true entity id")
    group.add_argument("--truth-from-id", metavar="ID_COL", help="derive the true entity from Febrl-style ids")
    group.add_argument("--truth-pairs", metavar="CSV", help="file of true matching id pairs (first two columns)")
    parser.add_argument("--id-col", default="id", help="record id column, used with --truth-pairs")
    parser.add_argument("--source-col", default="z_zsource", help="source column, used with --truth-pairs")
    args = parser.parse_args()

    df = read_output(args.output)
    df.columns = [c.strip() for c in df.columns]

    if args.truth_pairs:
        result = evaluate_against_pairs(df, args.cluster_col, args.id_col, args.source_col, args.truth_pairs)
        for name, value in result.items():
            print(f"{name:>20}: {value}")
        return

    if args.truth_from_id:
        df["true_entity"] = df[args.truth_from_id].str.strip().map(
            lambda rec_id: re.sub(r"-(org|dup-\d+)$", "", rec_id)
        )
        truth_col = "true_entity"
    else:
        truth_col = args.truth_col

    for name, value in evaluate(df, args.cluster_col, truth_col).items():
        print(f"{name:>20}: {value}")


if __name__ == "__main__":
    main()
