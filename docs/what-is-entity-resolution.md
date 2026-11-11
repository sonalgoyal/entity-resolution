# What is entity resolution?

**Entity resolution (ER)** is the task of finding records that refer to the same real-world entity when those records have no shared, reliable identifier. The entity can be a person, household, company, product, address or anything else.

The same task goes by many names:

| Term | Usually emphasises |
|---|---|
| Record linkage | Joining two or more datasets. Common in statistics and health research |
| Deduplication | Finding duplicates within one dataset |
| Data matching, fuzzy matching | The comparison step |
| Identity resolution | People and customers, often in marketing and fraud |
| Merge/purge | Mailing lists. An older term |
| Entity matching | Pairwise classification. Common in database research |

## Why it is hard

Here are three records from three systems:

| Source | Name | Address | Date of birth | Email |
|---|---|---|---|---|
| CRM | Jonathan Smith | 42 Main St, Springfield | 1984-03-07 | jsmith@acme.com |
| Billing | Jon Smith | 42 Main Street, Springfield IL | 07/03/1984 | |
| Support | J. Smyth | 42 Main St | | jon.smith@gmail.com |

A person can see these are probably one customer. A database join on any single column finds nothing. Entity resolution has to handle:

- **Variation**: typos, nicknames, abbreviations, transliteration, different formats.
- **Missing values**: one source has the email and another has the date of birth.
- **Ambiguity**: two different people really can both be called John Smith and live in the same city.
- **Scale**: 10 million records give 50 trillion possible pairs. You cannot compare them all.
- **No labels**: you rarely know the right answer in advance.

## The entity resolution pipeline

Almost every system, open source or commercial, follows the same five steps.

```
 raw records ──► 1. prepare ──► 2. block ──► 3. compare ──► 4. classify ──► 5. cluster ──► entities
```

1. **Prepare.** Standardise case, whitespace and punctuation. Parse names and addresses into parts, normalise phone numbers, strip company suffixes such as "Inc." and "GmbH". Good preparation often matters more than the choice of algorithm. See [data preparation tools](../README.md#data-preparation).
2. **Block** (also called indexing or candidate generation). Choose a small set of candidate pairs that might match, for example records that share the first three letters of a surname and a postcode. Blocking turns an impossible n² problem into a tractable one. See [Blocking](blocking.md).
3. **Compare.** For each candidate pair, compute a similarity for each field: Jaro-Winkler on names, exact match on date of birth, token overlap on descriptions, and so on. This produces a feature vector per pair.
4. **Classify.** Decide whether each pair is a match. Options range from hand-written rules, to a probabilistic Fellegi-Sunter model, to machine learning classifiers and large language models. See [Matching approaches](matching-approaches.md).
5. **Cluster.** Pairwise decisions are not always consistent: A matches B and B matches C, but A does not match C. Clustering, such as connected components or more careful graph methods, turns pairs into entities and gives each entity an ID.

After clustering, many teams add a sixth step: **survivorship** or **golden record creation**, which picks the best value for each field from the records in a cluster. This is where entity resolution meets [master data management](entity-resolution-vs-mdm.md).

## Where entity resolution is used

- **Customer 360 and CDPs**: one profile per customer across CRM, e-commerce, support and marketing tools.
- **Master data management**: clean supplier, product, customer and location masters.
- **Healthcare**: patient matching across hospitals and an enterprise master patient index (EMPI).
- **Financial crime and KYC**: link customers, counterparties and sanctions lists; uncover networks.
- **Public sector and research**: link census, tax, education and health records for statistics.
- **Marketing**: household detection, audience deduplication and attribution.
- **Knowledge graphs and AI**: resolve entities before building graphs or retrieval-augmented generation (RAG) systems, so the same company does not appear five times.
- **E-commerce**: match product listings across sellers and marketplaces.

## Deduplication vs. linking

- **Deduplication** looks for matches inside one dataset. The output gives every record a cluster ID.
- **Linking** looks for matches across datasets that are each already clean. Records are only compared across sources, never within one.

Most tools support both. See [tutorial 1](../tutorials/01-deduplicate-customer-records/) for deduplication and [tutorial 2](../tutorials/02-link-two-customer-lists/) for linking.

## Next

- [Blocking](blocking.md)
- [Open-source entity resolution tools compared](../README.md#open-source-entity-resolution-tools-compared)
