# Matching approaches

Once blocking has produced candidate pairs, you need to decide which pairs are matches. There are five broad families of methods. Production systems often combine several.

## 1. Deterministic (rule-based) matching

Write rules by hand:

```
match if  email is equal
      or (date_of_birth is equal and jaro_winkler(last_name) > 0.9 and postcode is equal)
```

- **Good for:** strong identifiers such as national ID, email and tax number; regulated settings where every decision must be explained; a first pass before a probabilistic or ML model.
- **Weak at:** the long tail of variation. Every new data problem needs a new rule, rules interact in surprising ways, and recall is usually low.

## 2. Probabilistic matching (Fellegi-Sunter)

The [Fellegi-Sunter model](https://doi.org/10.1080/01621459.1969.10501049) (1969) estimates, for each field and each level of agreement, two probabilities:

- **m**: the probability that the field agrees at this level when the records **are** a match.
- **u**: the probability that the field agrees at this level when the records are **not** a match.

Each comparison contributes a weight of log₂(m / u). The weights are added up, and pairs above a threshold are matches. Agreement on a rare surname counts for more than agreement on a common one. The m and u values can be estimated without labels using the EM algorithm.

- **Good for:** explainable scores, no labelled data needed, well understood by statisticians.
- **Weak at:** it assumes fields are independent given match status, which is often false, for example city and postcode. Complex interactions between fields are hard to capture.
- **Tools:** [Splink](https://github.com/moj-analytical-services/splink), [fastLink](https://github.com/kosukeimai/fastLink), [reclin2](https://github.com/djvanderlaan/reclin2).

## 3. Machine learning matching

Treat matching as binary classification. Compute similarity features for each pair, such as edit distance, Jaro-Winkler, token overlap and numeric difference, then train a classifier such as logistic regression, a random forest or gradient boosting.

The hard part is training data. Matches are rare: in a random sample of pairs, almost all are obvious non-matches, so labelling random pairs wastes time. [Active learning](active-learning.md) solves this by asking a person to label only the most informative pairs.

- **Good for:** learning interactions between fields, adapting to each dataset, high accuracy with modest labelling effort.
- **Needs:** a few dozen labels, which active learning makes quick to collect.
- **Tools:** [Zingg](https://github.com/zinggAI/zingg), [dedupe](https://github.com/dedupeio/dedupe), [Python Record Linkage Toolkit](https://github.com/J535D165/recordlinkage), [py_entitymatching](https://github.com/anhaidgroup/py_entitymatching), [hlink](https://github.com/ipums/hlink).

## 4. Deep learning matching

Use neural networks, now mostly pre-trained language models, to compare records serialised as text, for example `title: iPhone 15 128GB [SEP] brand: Apple`. [Ditto](https://arxiv.org/abs/2004.00584) fine-tunes BERT-style models. [DeepMatcher](https://doi.org/10.1145/3183713.3196926) explored the design space before that.

- **Good for:** text-heavy, heterogeneous records such as product listings and descriptions, where string similarity breaks down.
- **Weak at:** needs hundreds to thousands of labelled pairs and GPUs. Harder to explain. Often no better than ML with good features on structured person and company data.
- **Tools:** [Ditto](https://github.com/megagonlabs/ditto), [DeepMatcher](https://github.com/anhaidgroup/deepmatcher), [LinkTransformer](https://github.com/dell-research-harvard/linktransformer).

## 5. Large language model (LLM) matching

Ask an LLM, zero-shot or with a few examples, whether two records refer to the same entity. Research such as [Peeters et al.](https://arxiv.org/abs/2310.11244) shows strong LLMs can match well on product data without task-specific training.

- **Good for:** hard pairs that need world knowledge ("IBM" and "International Business Machines"), bootstrapping labels, reviewing borderline cases.
- **Weak at:** cost and latency. Classifying millions of pairs with an LLM is expensive and slow. Outputs can vary between runs, and sending personal data to an external API raises privacy questions.
- **Practical pattern:** use a fast ML or probabilistic matcher on all pairs, then send only the uncertain middle band to an LLM or a person.
- **Tools:** [MatchGPT](https://github.com/wbsg-uni-mannheim/MatchGPT), [libem](https://github.com/abcsys/libem), [ComEM](https://github.com/tshu-w/ComEM).

## Choosing

| Situation | Start with |
|---|---|
| Strong shared IDs on most records | Deterministic rules, then a model for the rest |
| Person, company or product data, any scale | ML with active learning (minutes of labelling) |
| Research setting that calls for a Fellegi-Sunter model | Probabilistic |
| Product or text-heavy data with labelled pairs | Deep learning |
| Small volume of hard, knowledge-heavy pairs | LLM, often as a second stage |

## Next

- [Active learning](active-learning.md)
