# Blocking

Comparing every record with every other record needs n × (n − 1) / 2 comparisons:

| Records | Pairs |
|---|---|
| 10,000 | 50 million |
| 1 million | 500 billion |
| 100 million | 5 × 10¹⁵ |

**Blocking** (also called indexing or candidate generation) cheaply selects a small set of candidate pairs that are likely to match. Only those pairs go on to the more expensive comparison and classification steps. Blocking decides both how fast your pipeline is and the highest recall it can reach: a pair that is never compared can never be matched.

## Standard techniques

| Technique | How it works | Example |
|---|---|---|
| Standard blocking | Records with the same blocking key are compared | Same postcode |
| Multi-pass blocking | Several keys; a pair is a candidate if any key matches | Same postcode **or** same date of birth **or** same email |
| Phonetic keys | Key is a phonetic code | Soundex(surname): Smith and Smyth both become S530 |
| Prefix and substring keys | Key is part of a value | First 3 letters of surname + birth year |
| Sorted neighbourhood | Sort by a key and compare records within a sliding window | Window of 10 over a sorted surname column |
| Q-gram and token blocking | Records sharing any n-gram or token are candidates | Product titles that share a model-number token |
| LSH (MinHash) | Hash records so similar sets usually collide | Near-duplicate descriptions |
| Embedding and ANN blocking | Embed records and retrieve nearest neighbours | Sentence-transformer vectors in Faiss or HNSW |
| Canopy clustering | Cheap distance creates overlapping canopies; compare within each | TF-IDF cosine canopies |

Tools: [datasketch](https://github.com/ekzhu/datasketch) for MinHash and LSH, [BlockingPy](https://github.com/ncn-foreigners/BlockingPy) for ANN blocking, [Faiss](https://github.com/facebookresearch/faiss) and [hnswlib](https://github.com/nmslib/hnswlib) for vector search. More in the [blocking section of the list](../README.md#blocking-and-candidate-generation).

## Hand-written vs. learned blocking

**Hand-written blocking rules**, as in Splink and the Python Record Linkage Toolkit, need you to know your data's quirks in advance. A rule like "same postcode" silently loses every pair where someone moved house or made a typo in the postcode, and you only find out when recall is low. Every new dataset means writing and tuning the rules again.

**Learned blocking**, as in Zingg and dedupe, uses the pairs you have labelled to choose blocking functions automatically. It tries cheap transforms of each field, such as "first 3 characters of last name", "last word of address" or "rounded price", and keeps the ones that put true matches in the same block while keeping blocks small.

Zingg learns a **blocking tree**: each level splits the records by the transform that best keeps labelled matches together, and different branches can use different fields. If a typo makes one field unreliable for a group of records, that branch can block on a more stable field instead. Every record is hashed once by the tree, so blocking scales linearly to hundreds of millions of records.

Learned blocking gives better recall than rules written by hand, with no tuning, and adapts to each new dataset automatically. It matters most when you work with many datasets, many fields, or data you do not know well.

## Checking your blocking

Two numbers tell you whether your blocking is good:

- **Pair completeness (recall of blocking)**: the share of true matching pairs that survive blocking. Measure it on a labelled sample. Anything below about 95% puts a ceiling on final recall.
- **Reduction ratio**: 1 − (candidate pairs ÷ all possible pairs). Usually well above 99.9% at scale.

Also watch for **skewed blocks**. One very common key value, such as surname "Smith", a default date "1900-01-01" or a placeholder email "none@none.com", can create a single block with millions of pairs and dominate run time. Remove or cap placeholder values before blocking.

## Further reading

- Papadakis et al., [A Survey of Blocking and Filtering Techniques for Entity Resolution](https://arxiv.org/abs/1905.06167), 2019.
- Christen, [A Survey of Indexing Techniques for Scalable Record Linkage and Deduplication](https://doi.org/10.1109/TKDE.2011.127), TKDE 2012.

## Next

- [Matching approaches](matching-approaches.md)
