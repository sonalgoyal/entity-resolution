# Active learning for entity resolution

Machine learning matchers need labelled pairs: examples of "these two records match" and "these two don't". Getting them is the main obstacle to using ML for entity resolution.

## Why random labelling fails

In a dataset of 1 million records with 10% duplicates, there are about 500 billion pairs and roughly 100,000 matching pairs. If you label random pairs, about one in five million is a match. You could label for weeks without seeing a single positive example.

Even pairs that pass blocking are mostly easy: either obvious matches or obvious non-matches. Labelling easy pairs teaches the model almost nothing.

## How active learning works

Active learning lets the model choose which pairs you label:

```
        ┌──────────────────────────────────────────┐
        ▼                                          │
  sample candidate pairs ──► model scores them ──► pick the pairs the model is
                                                    least sure about
                                                          │
                                                          ▼
                              retrain ◄── a person labels them: match / no match / unsure
```

1. Draw a sample of candidate pairs.
2. Score them with the current model. In the first round, simple similarity heuristics are used instead.
3. Show a person the pairs closest to the decision boundary: the ones the model is most uncertain about.
4. Retrain with the new labels and repeat.

Because every labelled pair is informative, a few dozen positive labels are often enough for a good first model. Labels collected this way can also train a learned blocking model, as in Zingg and dedupe.

Active learning for deduplication goes back to Sarawagi & Bhamidipaty, [Interactive Deduplication using Active Learning](https://doi.org/10.1145/775047.775087) (KDD 2002).

## How much to label

Rules of thumb from practice:

- Aim for **30-40 confirmed matches** for a first model, plus the non-matches you label along the way.
- Keep labelling until the model's predictions on the pairs it shows you mostly agree with your own judgement.

## Labelling well

- **Decide what an entity is before you start.** Is a person at a new address the same entity? Is a company's subsidiary the same entity as the parent? Write the rule down so everyone labels the same way.
- **Use "unsure" honestly.** Most labellers let you skip a pair. A wrong label hurts more than a missing one.
- **Look at all fields.** Two "John Smith" records with different dates of birth are a non-match even if everything else agrees.
- **Label edge cases on purpose.** Twins, father and son with the same name, shared family email addresses, and chain stores at different locations are where models fail.
- **Keep the labels.** They are your evaluation set too, and they let you retrain when the data changes.

## Tools with active learning

- [Zingg](https://github.com/zinggAI/zingg) - `findTrainingData` picks uncertain pairs and `label` opens an interactive labeller. Labels train both the blocking model and the classifier. See [tutorial 1](../tutorials/01-deduplicate-customer-records/).
- [dedupe](https://github.com/dedupeio/dedupe) - Console labelling with `dedupe.console_label`.
- [deduplipy](https://github.com/fritshermans/deduplipy) - Active-learning deduplication.

## Next

- [Evaluating entity resolution](evaluating-entity-resolution.md)
