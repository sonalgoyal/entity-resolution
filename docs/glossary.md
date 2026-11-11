# Entity resolution glossary

**Active learning** - Training approach in which the model chooses which examples a person should label, typically those it is least sure about. See [Active learning](active-learning.md).

**B-cubed** - Cluster evaluation metric computed per record and averaged. See [Evaluating entity resolution](evaluating-entity-resolution.md).

**Blocking** - Cheaply selecting candidate pairs so not every pair has to be compared. Also called indexing. See [Blocking](blocking.md).

**Blocking key** - The value used to group records for blocking, such as postcode or the first three letters of a surname.

**Candidate pair** - A pair of records that survives blocking and will be compared.

**Canopy clustering** - Blocking method that forms overlapping groups using a cheap distance.

**Clerical review** - A person reviewing uncertain pairs or clusters. Also called stewardship.

**Cluster** - A group of records judged to refer to the same entity.

**Comparison vector** - Per-field similarity scores for a candidate pair, used as features by a classifier.

**Connected components** - Graph algorithm that groups records linked by any chain of matching pairs. The simplest way to turn pairs into clusters.

**Data matching** - General term for entity resolution and record linkage.

**Deduplication** - Finding records that refer to the same entity within a single dataset.

**Deterministic matching** - Matching with exact, hand-written rules.

**EM algorithm** - Expectation-maximisation. Used to estimate Fellegi-Sunter m and u probabilities without labels.

**Entity** - The real-world thing records describe: a person, company, product, place.

**Entity linking** - Linking mentions in text to a knowledge base. A related but different task.

**Entity matching** - Deciding whether a pair of records matches. Common in database research.

**False merge** - A false positive: two different entities merged into one cluster.

**False split** - A false negative: one entity left as two or more clusters.

**Fellegi-Sunter model** - The classic probabilistic record linkage model based on m and u probabilities and match weights. See [Matching approaches](matching-approaches.md).

**Golden record** - The single best version of an entity, assembled from its records using survivorship rules.

**Ground truth** - Known correct matches, used for training and evaluation.

**Householding** - Grouping people who live at the same address or share an account.

**Identity graph** - A graph of identifiers (emails, devices, accounts) linked to people.

**Identity resolution** - Entity resolution applied to people. See [ER vs. MDM](entity-resolution-vs-mdm.md).

**Incremental matching** - Matching new or changed records against existing clusters without rerunning on all data.

**Jaro-Winkler** - String similarity measure that favours strings with matching prefixes. Popular for names.

**Levenshtein distance** - The number of single-character insertions, deletions and substitutions needed to turn one string into another. Also called edit distance.

**Linkage** - Matching records across two or more datasets.

**LSH (locality-sensitive hashing)** - Hashing so that similar items are likely to share a bucket. Used for blocking.

**m probability** - In Fellegi-Sunter, the probability that a field agrees given the records match.

**Master data management (MDM)** - Practices and software for keeping trusted master records of core business entities.

**Match weight** - In Fellegi-Sunter, log₂(m / u). The evidence a field comparison adds for or against a match.

**Merge/purge** - Older term for deduplication, especially of mailing lists.

**Pair completeness** - The share of true matching pairs that survive blocking.

**Phonetic encoding** - Turning a word into a code based on how it sounds. Examples: Soundex, Metaphone, NYSIIS.

**Precision** - Of the predicted matches, the share that are correct.

**Privacy-preserving record linkage (PPRL)** - Linking records across organisations using encoded identifiers instead of raw personal data.

**Probabilistic matching** - Matching based on statistical evidence from many fields, usually Fellegi-Sunter.

**Recall** - Of the true matches, the share that were found.

**Record linkage** - Linking records about the same entity, within or across datasets. The term used most in statistics and health research.

**Reduction ratio** - The share of all possible pairs removed by blocking.

**Sorted neighbourhood** - Blocking by sorting records on a key and comparing records within a sliding window.

**Standardisation** - Cleaning and normalising values before matching.

**Survivorship** - Rules for choosing which value from a cluster goes into the golden record.

**Threshold** - The score above which a pair or cluster is treated as a match.

**Transitivity** - If A matches B and B matches C, then A matches C. Clustering enforces it, sometimes wrongly.

**u probability** - In Fellegi-Sunter, the probability that a field agrees given the records do not match. It is roughly the chance of agreeing at random.
