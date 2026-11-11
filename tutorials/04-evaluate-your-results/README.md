# Tutorial 4: Evaluate your results

**Goal:** measure how good an entity resolution result is, with numbers you can track as you change settings, labels or data preparation.

**You need:** Python 3 with pandas (`pip install pandas`). The script works with output from **any** tool, not only Zingg.

## The script

[`evaluate.py`](evaluate.py) computes **pairwise precision, recall and F1**. For background, see [Evaluating entity resolution](../../docs/evaluating-entity-resolution.md).

It supports three kinds of ground truth:

| Ground truth | Flag | Example |
|---|---|---|
| A column with the true entity id | `--truth-col true_id` | Your own labelled sample |
| Febrl-style record ids | `--truth-from-id id` | `rec-1021-org` and `rec-1021-dup-0` are entity `rec-1021` |
| A file of true matching pairs | `--truth-pairs mapping.csv` | Leipzig benchmark mappings |

It reads a single CSV file or a whole Spark output folder of `part-*` files.

## Example: tutorial 1 output

```bash
python tutorials/04-evaluate-your-results/evaluate.py output/customers-deduped --truth-from-id id
```

```
             records: 65
  predicted_clusters: 30
       true_entities: 27
     predicted_pairs: 70
          true_pairs: 76
       correct_pairs: 70
           precision: 1.0
              recall: 0.9211
                  f1: 0.9589
```

This is the run from tutorial 1's pre-labelled shortcut: **8 labelled matches** and about a minute of compute. How to read it:

- **Precision 1.0**: every pair Zingg merged is a true duplicate. Not a single wrong merge.
- **F1 0.96** out of the box, with no tuning.
- **Recall 0.92**: 70 of the 76 true duplicate pairs found. Recall goes up further with a few more labels: join the output with the true entity, find entities that span more than one `z_cluster`, and label pairs like them in the next round.

## Using it with other tools

The script only needs a cluster column and some form of ground truth:

```bash
# Splink: predictions clustered with cluster_pairwise_predictions_at_threshold
python evaluate.py splink_clusters.csv --cluster-col cluster_id --truth-col true_id

# dedupe: output of the csv_example
python evaluate.py dedupe_output.csv --cluster-col "Cluster ID" --truth-col true_id
```

## No ground truth?

Most real projects don't have one. Build a small one:

1. Randomly sample 100-200 output clusters, with more weight on large clusters and low `z_minScore`.
2. Have a person mark each cluster as correct, over-merged or under-merged. This estimates precision.
3. For recall, sample records and search by hand, or with a very loose fuzzy search, for matches the system missed.
4. Save the result as a CSV with a `true_id` column and rerun this script every time you change something.

For statistically sound estimates from samples, see [ER-Evaluation](https://github.com/OlivierBinette/er-evaluation).
