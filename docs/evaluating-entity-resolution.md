# Evaluating entity resolution

You cannot improve what you don't measure. Entity resolution is easy to measure badly, though, so it helps to understand the metrics before trusting them.

## Pairwise metrics

The most common approach treats every pair of records as a yes/no decision.

- **True positive (TP)**: a pair predicted to match that really matches.
- **False positive (FP)**: a pair predicted to match that doesn't. These are wrong merges.
- **False negative (FN)**: a matching pair that was missed. These are missed duplicates.

From these:

- **Precision** = TP / (TP + FP): of the pairs you merged, how many were right?
- **Recall** = TP / (TP + FN): of the true matching pairs, how many did you find?
- **F1** = 2 × precision × recall / (precision + recall).

When the output is clusters, count pairs inside clusters. A predicted cluster of 4 records implies 6 predicted pairs. A true entity with 3 records implies 3 true pairs. This repository's [evaluate.py](../tutorials/04-evaluate-your-results/evaluate.py) computes this from any tool's output in a few lines of pandas.

**Accuracy is meaningless here.** Almost all pairs are non-matches, so a system that never merges anything is 99.99% "accurate".

## Cluster metrics

Pairwise metrics weight large clusters heavily, because a cluster of 100 records has 4,950 pairs. If that is a problem for your use case, look at cluster-level metrics as well:

- **Cluster precision and recall**: the share of predicted clusters that exactly equal a true entity, and the reverse.
- **B-cubed precision and recall**: computed per record, then averaged. Less dominated by big clusters.
- **Adjusted Rand index** and **variation of information**: standard clustering comparisons.

[ER-Evaluation](https://github.com/OlivierBinette/er-evaluation) implements these and more, and [clevr](https://github.com/cleanzr/clevr) does the same in R.

## Precision or recall?

The right balance depends on what a mistake costs:

| Use case | A wrong merge (FP) | A missed match (FN) | Usually favour |
|---|---|---|---|
| Patient matching | Wrong medical history shown to a clinician | Duplicate chart | Precision |
| Sanctions screening | Analyst reviews a false alert | Sanctioned party slips through | Recall |
| Marketing deduplication | Two people get one mailing | One person gets two mailings | Balanced |
| Fraud networks | Innocent person linked to a ring | Ring member missed | Depends on review capacity |

Most tools output a score per pair or cluster. Instead of trusting a default threshold, choose one based on these costs, and consider a **review band** between "auto-merge" and "auto-reject" that goes to a person.

## Building a ground truth

Real projects rarely have complete ground truth. Practical options:

1. **Benchmark datasets** with known matches are good for learning and comparing settings. See [Datasets](../README.md#datasets).
2. **Labelled sample.** Sample predicted clusters and have a person check them. This estimates precision directly.
3. **Recall from a stratified sample.** Sample records, search exhaustively for their true matches by hand or with a very loose matcher, and see what the system found.
4. **Known links.** Use a field that is not given to the matcher, such as a verified national ID, as partial truth.

Estimating recall is the hard part, because you need to find matches the system missed. [Binette et al.'s ER-Evaluation](https://github.com/OlivierBinette/er-evaluation) describes unbiased estimators for this.

## Common mistakes

- **Evaluating on training labels.** Labels gathered by active learning sit on the decision boundary and are not a random sample. Keep a separate evaluation sample.
- **Ignoring blocking.** If blocking drops a true pair, no classifier can recover it. Measure pair completeness separately. See [Blocking](blocking.md).
- **Ignoring transitivity.** A→B and B→C can chain unrelated records into one giant cluster. Look at the largest clusters by hand.
- **One number for the whole dataset.** Quality often differs by segment: country, source system, records with missing fields. Break metrics down.
- **Changing the definition of an entity mid-project.** Agree up front whether, for example, a person at an old address is the same entity.

## Next

- [Tutorial 4: Evaluate your results](../tutorials/04-evaluate-your-results/)
- [Entity resolution vs. MDM vs. identity resolution](entity-resolution-vs-mdm.md)
