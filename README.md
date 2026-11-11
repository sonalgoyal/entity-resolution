# Entity Resolution [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A practical guide to entity resolution, plus a curated list of open-source entity resolution software, datasets, papers and learning material.

[![Links checked weekly](https://github.com/sonalgoyal/entity-resolution/actions/workflows/links.yml/badge.svg)](https://github.com/sonalgoyal/entity-resolution/actions/workflows/links.yml)
[![Last commit](https://img.shields.io/github/last-commit/sonalgoyal/entity-resolution)](https://github.com/sonalgoyal/entity-resolution/commits/main)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Entity resolution** finds the records that refer to the same real-world thing, such as a person, company, product or address, when those records don't share a reliable key. It is also called **record linkage**, **deduplication**, **data matching**, **fuzzy matching**, **identity resolution** or **merge/purge**. It is how you build a single customer view, a clean supplier master, a patient index or a knowledge graph from messy data.

This repository has four parts:

| | |
|---|---|
| 📚 [**Learn**](#learn-entity-resolution) | Short, plain-language explanations of how entity resolution works |
| 🧭 [**Tools compared**](#open-source-entity-resolution-tools-compared) | A feature comparison of the main open-source tools |
| ⭐ [**Awesome list**](#awesome-entity-resolution) | 150+ tools, datasets, papers, books and courses, checked for broken links every week |
| 🛠️ [**Tutorials**](#tutorials) and [**templates**](#templates) | Runnable examples and starter configurations |

---

## Learn entity resolution

New to the topic? Read these in order. Each takes about five minutes.

1. [What is entity resolution?](docs/what-is-entity-resolution.md) - the problem, the pipeline, and where it is used.
2. [Blocking](docs/blocking.md) - how to avoid comparing every record with every other record.
3. [Matching approaches](docs/matching-approaches.md) - rules, probabilistic (Fellegi-Sunter), machine learning, deep learning and LLMs.
4. [Active learning](docs/active-learning.md) - how to build training data by labelling a few dozen pairs.
5. [Evaluating entity resolution](docs/evaluating-entity-resolution.md) - pairwise and cluster metrics, and the mistakes to avoid.
6. [Entity resolution vs. MDM vs. identity resolution](docs/entity-resolution-vs-mdm.md) - how the terms relate.
7. [Glossary](docs/glossary.md) - every term you will meet, in one place.

---

## Open-source entity resolution tools compared

| Tool | Language | Runs on | Approach | Dedup | Link | Needs labels? | License | Activity |
|---|---|---|---|:-:|:-:|---|---|---|
| [Zingg](https://github.com/zinggAI/zingg) | Python, Java | Spark: Docker or local, Databricks, Fabric, AWS Glue and EMR, GCP Dataproc. Snowflake (Enterprise) | ML classifier with active learning; learned blocking | ✅ | ✅ | A few dozen, picked by built-in active learning, or bring your own labelled pairs | AGPL-3.0 | ![](https://img.shields.io/github/last-commit/zinggAI/zingg?label=) |
| [Splink](https://github.com/moj-analytical-services/splink) | Python, SQL | DuckDB, Spark, Athena, Postgres, SQLite | Fellegi-Sunter, trained with EM | ✅ | ✅ | No (labels optional) | MIT | ![](https://img.shields.io/github/last-commit/moj-analytical-services/splink?label=) |
| [dedupe](https://github.com/dedupeio/dedupe) | Python | Single machine | Active learning, learned blocking, logistic regression | ✅ | ✅ | Yes, via interactive labelling | MIT | ![](https://img.shields.io/github/last-commit/dedupeio/dedupe?label=) |
| [Python Record Linkage Toolkit](https://github.com/J535D165/recordlinkage) | Python | pandas | Toolkit: blocking, comparisons, supervised and unsupervised classifiers | ✅ | ✅ | Optional | BSD-3 | ![](https://img.shields.io/github/last-commit/J535D165/recordlinkage?label=) |
| [pyJedAI](https://github.com/AI-team-UoA/pyJedAI) | Python | Single machine | Configurable blocking, matching and clustering, incl. embeddings | ✅ | ✅ | Optional | Apache-2.0 | ![](https://img.shields.io/github/last-commit/AI-team-UoA/pyJedAI?label=) |
| [fastLink](https://github.com/kosukeimai/fastLink) | R | Single machine | Fellegi-Sunter with EM, handles missing data | ⚠️ | ✅ | No | GPL-3 | ![](https://img.shields.io/github/last-commit/kosukeimai/fastLink?label=) |
| [reclin2](https://github.com/djvanderlaan/reclin2) | R | Single machine | Fellegi-Sunter and ML, step-by-step pipeline | ✅ | ✅ | Optional | GPL-3.0 | ![](https://img.shields.io/github/last-commit/djvanderlaan/reclin2?label=) |
| [hlink](https://github.com/ipums/hlink) | Python | Spark | Supervised ML, built for historical census linkage | ⚠️ | ✅ | Yes | MPL-2.0 | ![](https://img.shields.io/github/last-commit/ipums/hlink?label=) |
| [Ditto](https://github.com/megagonlabs/ditto) | Python | GPU | Fine-tuned pre-trained language models (research code) | ⚠️ | ✅ | Yes, labelled pairs | Apache-2.0 | ![](https://img.shields.io/github/last-commit/megagonlabs/ditto?label=) |
| [nomenklatura](https://github.com/opensanctions/nomenklatura) | Python | Single machine | Scored candidates plus human review, FollowTheMoney entities | ✅ | ✅ | Human review | MIT | ![](https://img.shields.io/github/last-commit/opensanctions/nomenklatura?label=) |

✅ supported · ⚠️ possible with workarounds, or not the main use case. The Activity column shows each project's latest commit and updates automatically. Spotted something out of date? [Open an issue](https://github.com/sonalgoyal/entity-resolution/issues/new/choose).

---

## Awesome Entity Resolution

### Contents

- [End-to-end frameworks](#end-to-end-frameworks)
- [Libraries and toolkits](#libraries-and-toolkits)
- [Deep learning and LLM-based matching](#deep-learning-and-llm-based-matching)
- [Search engine and database-native matching](#search-engine-and-database-native-matching)
- [Blocking and candidate generation](#blocking-and-candidate-generation)
- [String and phonetic similarity](#string-and-phonetic-similarity)
- [Data preparation: names, addresses, companies, phones, text](#data-preparation)
- [Clustering and graphs](#clustering-and-graphs)
- [Labelling and evaluation](#labelling-and-evaluation)
- [Privacy-preserving record linkage](#privacy-preserving-record-linkage)
- [Domain-specific tools](#domain-specific-tools)
- [Commercial and managed services](#commercial-and-managed-services)
- [Datasets](#datasets)
- [Papers](#papers)
- [Books](#books)
- [Tutorials, courses and talks](#tutorials-courses-and-talks)
- [Related fields](#related-fields)
- [Other lists](#other-lists)

Legend: *(inactive)* means no commits for two years or more. The project may still work, but check before you depend on it.

### End-to-end frameworks

Tools that cover the whole pipeline: preparing data, blocking, comparing, classifying and clustering.

- [Zingg](https://github.com/zinggAI/zingg) - Scalable entity resolution, deduplication and identity resolution with active learning and a learned blocking model. Runs on Spark locally or in Docker, and on Databricks, Fabric, AWS Glue, EMR and GCP Dataproc. Python and Java APIs. *(Python, Java · Spark)*
- [Splink](https://github.com/moj-analytical-services/splink) - Fast probabilistic record linkage (Fellegi-Sunter) with interactive diagnostics. Runs on DuckDB, Spark, Athena and Postgres. *(Python, SQL)*
- [dedupe](https://github.com/dedupeio/dedupe) - Active-learning library for fuzzy matching, deduplication and entity resolution of structured data. *(Python)*
- [csvdedupe](https://github.com/dedupeio/csvdedupe) - Command-line wrapper around dedupe for CSV files. *(Python, inactive)*
- [pyJedAI](https://github.com/AI-team-UoA/pyJedAI) - End-to-end entity resolution with many blocking, matching and clustering algorithms, including embedding-based methods. *(Python)*
- [JedAI Toolkit](https://github.com/scify/JedAIToolkit) - The original Java toolkit behind pyJedAI, with a GUI. *(Java, archived)*
- [hlink](https://github.com/ipums/hlink) - Hierarchical record linkage at scale, built by IPUMS to link historical census data. *(Python · Spark)*
- [SparkER](https://github.com/Gaglia88/sparker) - Entity resolution on Spark with meta-blocking. *(Scala · Spark, inactive)*
- [dblink](https://github.com/cleanzr/dblink) - Distributed Bayesian entity resolution on Spark. *(Scala · Spark, inactive)*
- [Duke](https://github.com/larsga/Duke) - Fast, configurable deduplication engine built on Lucene. *(Java, inactive)*
- [LIMES](https://github.com/dice-group/LIMES) - Link discovery framework for metric spaces, aimed at RDF and linked data. *(Java)*
- [WInte.r](https://github.com/olehmberg/winter) - Java framework for end-to-end data integration, including identity resolution and data fusion. *(Java, inactive)*
- [PyDI](https://github.com/wbsg-uni-mannheim/PyDI) - Python data integration framework from the Web Data Commons group, covering schema matching, entity matching and fusion. *(Python)*
- [GoldenMatch](https://github.com/benseverndev-oss/goldenmatch) - Zero-configuration entity resolution that maintains a persistent identity layer. *(Python)*
- [deduplipy](https://github.com/fritshermans/deduplipy) - Deduplication with active learning. *(Python)*
- [RLTK](https://github.com/usc-isi-i2/rltk) - Record Linkage ToolKit from USC ISI. *(Python, inactive)*
- [AtyImo](https://github.com/pierrepita/atyimo) - Deterministic and probabilistic linkage, built for a 100-million-person Brazilian health cohort. *(Python · Spark, inactive)*
- [RELAIS](https://www.istat.it/en/methods-and-tools/methods-and-it-tools/process/processing-tools/relais) - Record linkage toolkit from Istat, the Italian national statistics office. *(R, Java)*

### Libraries and toolkits

Building blocks and smaller libraries for assembling your own pipeline.

- [Python Record Linkage Toolkit](https://github.com/J535D165/recordlinkage) - Indexing, comparisons and classifiers on pandas DataFrames. A standard choice for teaching. *(Python)*
- [py_entitymatching](https://github.com/anhaidgroup/py_entitymatching) - The Magellan entity matching system from UW-Madison: a step-by-step, human-in-the-loop workflow. *(Python)*
- [MatchFlow](https://github.com/MadMatcher/MatchFlow) - Compose entity matching workflows on Spark, from the Magellan group. *(Python · Spark)*
- [Sparkly](https://github.com/anhaidgroup/sparkly) - TF/IDF blocking at scale on Spark. *(Python · Spark)*
- [fastLink](https://github.com/kosukeimai/fastLink) - Fast Fellegi-Sunter record linkage with missing data handling. *(R)*
- [reclin2](https://github.com/djvanderlaan/reclin2) - Record linkage toolkit with a pipe-friendly API. *(R)*
- [RecordLinkage (R)](https://cran.r-project.org/package=RecordLinkage) - Long-standing CRAN package for linkage and deduplication. *(R)*
- [exchanger](https://github.com/cleanzr/exchanger) - Bayesian entity resolution with exchangeable random partition priors. *(R, C++)*
- [fuzzyjoin](https://github.com/dgrtwo/fuzzyjoin) - Join data frames on inexact matches. *(R)*
- [csvmatch](https://github.com/maxharlow/csvmatch) - Fuzzy matches between CSV files from the command line. Popular with journalists. *(Python)*
- [fuzzymatcher](https://github.com/RobinL/fuzzymatcher) - Fuzzy-join two pandas DataFrames using SQLite full-text search. *(Python, inactive)*
- [string_grouper](https://github.com/Bergvca/string_grouper) - Very fast grouping and matching of strings with TF-IDF n-grams and sparse matrix multiplication. *(Python)*
- [skrub](https://github.com/skrub-data/skrub) - Machine learning on messy dataframes, including `fuzzy_join` and deduplication helpers. *(Python)*
- [talisman](https://github.com/Yomguithereal/talisman) - Fuzzy matching, phonetics and record linkage building blocks for JavaScript. *(JavaScript)*

### Deep learning and LLM-based matching

- [Ditto](https://github.com/megagonlabs/ditto) - Entity matching by fine-tuning pre-trained language models such as BERT and RoBERTa. *(Python)*
- [DeepMatcher](https://github.com/anhaidgroup/deepmatcher) - Deep learning models for entity matching from the Magellan group. *(Python)*
- [Sudowoodo](https://github.com/megagonlabs/sudowoodo) - Contrastive self-supervised learning for matching with few labels. *(Python, inactive)*
- [LinkTransformer](https://github.com/dell-research-harvard/linktransformer) - Link, deduplicate and cluster dataframes with transformer embeddings. *(Python)*
- [Entity Embed](https://github.com/vintasoftware/entity-embed) - Turn records into vectors for approximate nearest-neighbour blocking. *(Python, inactive)*
- [DeezyMatch](https://github.com/Living-with-machines/DeezyMatch) - Deep learning fuzzy string matching and candidate ranking. *(Python)*
- [MatchGPT](https://github.com/wbsg-uni-mannheim/MatchGPT) - Prompts and code for matching entities with GPT-4, Llama and other LLMs. *(Python)*
- [libem](https://github.com/abcsys/libem) - LLM-powered toolchain for entity matching. *(Python)*
- [ComEM](https://github.com/tshu-w/ComEM) - Compares matching, comparing and selecting strategies for LLM-based entity matching. *(Python)*
- [sentence-transformers](https://github.com/huggingface/sentence-transformers) - Embedding models used for semantic blocking and matching. *(Python)*

### Search engine and database-native matching

Match inside the systems where your data already lives.

- [zentity](https://github.com/zentity-io/zentity) - Real-time entity resolution plugin for Elasticsearch. *(Java)*
- [spark-lucenerdd](https://github.com/zouzias/spark-lucenerdd) - Lucene-powered search and record linkage on Spark. *(Scala · Spark)*
- [PostgreSQL pg_trgm](https://www.postgresql.org/docs/current/pgtrgm.html) - Trigram similarity and indexes for fuzzy search in Postgres.
- [PostgreSQL fuzzystrmatch](https://www.postgresql.org/docs/current/fuzzystrmatch.html) - Levenshtein, Soundex, Metaphone and Daitch-Mokotoff in Postgres.
- [DuckDB text similarity functions](https://duckdb.org/docs/stable/sql/functions/text) - Jaro-Winkler, Levenshtein, Jaccard and more in SQL.
- [Snowflake JAROWINKLER_SIMILARITY](https://docs.snowflake.com/en/sql-reference/functions/jarowinkler_similarity) and [EDITDISTANCE](https://docs.snowflake.com/en/sql-reference/functions/editdistance) - String similarity in Snowflake SQL.
- [pgdedupe](https://github.com/dssg/pgdedupe) - Run dedupe against PostgreSQL from the command line. *(Python, inactive)*

### Blocking and candidate generation

Ways to cut the number of comparisons from n² to something manageable. Background: [Blocking](docs/blocking.md).

- [BlockingPy](https://github.com/ncn-foreigners/BlockingPy) - Blocking with approximate nearest neighbour indexes. *(Python)*
- [blocking](https://github.com/ncn-foreigners/blocking) - The same approach for R. *(R)*
- [blocklib](https://github.com/data61/blocklib) - Blocking techniques, including privacy-preserving ones. *(Python, inactive)*
- [datasketch](https://github.com/ekzhu/datasketch) - MinHash, LSH and LSH Ensemble for near-duplicate candidate search. *(Python)*
- [Faiss](https://github.com/facebookresearch/faiss) - Similarity search over dense vectors, for embedding-based blocking. *(C++, Python)*
- [hnswlib](https://github.com/nmslib/hnswlib) - Fast approximate nearest neighbour search. *(C++, Python)*
- [USearch](https://github.com/unum-cloud/USearch) - Compact vector search engine with many language bindings. *(C++, many)*
- [DeLex](https://github.com/anhaidgroup/delex) - Write and run blocking rules on Spark. *(Python · Spark)*

### String and phonetic similarity

- [RapidFuzz](https://github.com/rapidfuzz/RapidFuzz) - Very fast Levenshtein, Jaro-Winkler, token-set ratios and more. *(Python, C++)*
- [jellyfish](https://github.com/jamesturk/jellyfish) - String distances plus phonetic encoders: Soundex, Metaphone, NYSIIS and Match Rating. *(Python, Rust)*
- [textdistance](https://github.com/life4/textdistance) - Over 30 distance algorithms behind one interface. *(Python)*
- [thefuzz](https://github.com/seatgeek/thefuzz) - The library formerly known as fuzzywuzzy. *(Python)*
- [py_stringmatching](https://github.com/anhaidgroup/py_stringmatching) - Tokenizers and similarity measures designed for entity matching. *(Python)*
- [abydos](https://github.com/chrislit/abydos) - Hundreds of phonetic algorithms, distance measures and stemmers. *(Python, inactive)*
- [PolyFuzz](https://github.com/MaartenGr/PolyFuzz) - Fuzzy string matching, grouping and evaluation with pluggable models. *(Python)*
- [StringCompare](https://github.com/OlivierBinette/StringCompare) - Efficient string comparison functions. *(Python, C++)*
- [stringdist](https://github.com/markvanderloo/stringdist) - Approximate string matching and distances. *(R)*
- [comparator](https://github.com/ngmarchant/comparator) - Similarity measures for clustering and record linkage. *(R)*
- [strsim-rs](https://github.com/rapidfuzz/strsim-rs) - String similarity metrics. *(Rust)*
- [go-edlib](https://github.com/hbollon/go-edlib) - Edit distance and string comparison algorithms. *(Go)*
- [SecondString](https://secondstring.sourceforge.net/) - Classic Java library of string comparators for matching names and records. *(Java)*

### Data preparation

Clean and standardise data before matching. This often improves results more than changing the matching algorithm.

**Names**
- [python-nameparser](https://github.com/derek73/python-nameparser) - Split names into title, given, middle, family, suffix and nickname. *(Python)*
- [probablepeople](https://github.com/datamade/probablepeople) - Statistical parser for Western personal and company names. *(Python)*
- [nominally](https://github.com/vaneseltine/nominally) - Name parser designed for record linkage. *(Python)*
- [nicknames](https://github.com/carltonnorthern/nicknames) - Lookup table of US first names and their nicknames, such as William, Bill and Will. *(CSV, Python)*

**Addresses**
- [libpostal](https://github.com/openvenues/libpostal) - Parse and normalise street addresses worldwide. *(C, with many bindings)*
- [pypostal](https://github.com/openvenues/pypostal) - Python bindings for libpostal. *(Python)*
- [deepparse](https://github.com/GRAAL-Research/deepparse) - Deep learning parser for addresses in many countries. *(Python)*
- [usaddress](https://github.com/datamade/usaddress) - Parse US addresses into components. *(Python)*
- [usaddress-scourgify](https://github.com/GreenBuildingRegistry/usaddress-scourgify) - Normalise US addresses to USPS Publication 28. *(Python)*
- [whereabouts](https://github.com/ajl2718/whereabouts) - Fast geocoding and address matching. *(Python)*

**Companies**
- [cleanco](https://github.com/psolin/cleanco) - Strip legal suffixes such as Ltd, GmbH and Inc. from company names. *(Python)*
- [name_matching](https://github.com/DeNederlandscheBank/name_matching) - Company name matching from De Nederlandsche Bank. *(Python)*
- [EntityMatchingModel](https://github.com/ing-bank/EntityMatchingModel) - ING's model for matching company names between two datasets. *(Python · Spark)*

**Phones, text and encoding**
- [libphonenumber](https://github.com/google/libphonenumber) - Parse, validate and format phone numbers. *(Java, C++, JS)*
- [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) - Python port of libphonenumber. *(Python)*
- [ftfy](https://github.com/rspeer/python-ftfy) - Fix mojibake and broken Unicode. *(Python)*
- [Unidecode](https://github.com/avian2/unidecode) - Transliterate Unicode text to ASCII. *(Python)*
- [rigour](https://github.com/opensanctions/rigour) - Normalise names, identifiers and languages, from OpenSanctions. *(Python)*

### Clustering and graphs

Turn matched pairs into entities, or treat entity resolution as a graph problem.

- [GraphFrames](https://github.com/graphframes/graphframes) - Connected components and other graph algorithms on Spark DataFrames. *(Scala, Python · Spark)*
- [NetworkX](https://github.com/networkx/networkx) - Connected components and community detection on a single machine. *(Python)*
- [Neo4j Graph Data Science WCC](https://neo4j.com/docs/graph-data-science/current/algorithms/wcc/) - Weakly connected components inside Neo4j.
- [neo4j entity resolution example](https://github.com/neo4j-graph-examples/entity-resolution) - Worked example of entity resolution in a graph database.
- [Strwythura](https://github.com/DerwenAI/strwythura) - Build an entity-resolved knowledge graph from structured and unstructured sources. *(Python)*
- [clevr](https://github.com/cleanzr/clevr) - Clustering and link prediction metrics. *(R)*

### Labelling and evaluation

- [ER-Evaluation](https://github.com/OlivierBinette/er-evaluation) - End-to-end evaluation: summary statistics, performance estimators and error analysis. *(Python)*
- [recordlinkage-annotator](https://github.com/J535D165/recordlinkage-annotator) - Browser interface for labelling record pairs. *(JavaScript, inactive)*
- [Zingg labeller](https://docs.zingg.ai/) - Built-in active-learning labeller that asks you about the pairs it is least sure of.
- [evaluate.py](tutorials/04-evaluate-your-results/evaluate.py) - Small, tool-agnostic script for pairwise precision, recall and F1 from this repository.

### Privacy-preserving record linkage

Link records across organisations without sharing raw personal data.

- [anonlink](https://github.com/data61/anonlink) - Linkage over cryptographic linkage keys (Bloom filter encodings). *(Python)*
- [clkhash](https://github.com/data61/clkhash) - Hash personal data into cryptographic long-term keys (CLKs) for anonlink. *(Python)*
- [anonlink-entity-service](https://github.com/data61/anonlink-entity-service) - REST service for privacy-preserving linkage between parties. *(Python, inactive)*

### Domain-specific tools

- [nomenklatura](https://github.com/opensanctions/nomenklatura) - Deduplication and integration of FollowTheMoney entities, used by OpenSanctions. *(Python)*
- [FollowTheMoney](https://github.com/alephdata/followthemoney) - Data model for people, companies and assets in investigations. *(Python)*
- [uk_address_matcher](https://github.com/moj-analytical-services/uk_address_matcher) - High-accuracy matching of UK addresses. *(Python)*
- [lieu](https://github.com/openvenues/lieu) - Deduplicate addresses and venues worldwide with libpostal. *(Python, inactive)*
- [soweego](https://github.com/Wikidata/soweego) - Link Wikidata items to large external catalogues. *(Python)*
- [OpenRefine](https://github.com/OpenRefine/OpenRefine) - Desktop data cleaning with clustering and reconciliation against Wikidata and other services. *(Java)*
- [conciliator](https://github.com/codeforkjeff/conciliator) - OpenRefine reconciliation services for VIAF, ORCID and Open Library. *(Java)*

### Commercial and managed services

Listed for completeness. Not open source.

- [Zingg Enterprise](https://www.zingg.ai/) - Commercial edition of Zingg that adds persistent entity IDs, incremental matching and native Snowflake execution.
- [AWS Entity Resolution](https://aws.amazon.com/entity-resolution/) - Managed rule-based, ML and provider-based matching on AWS.
- [Senzing](https://senzing.com/) - Embeddable entity resolution engine for people and organisations.
- [Tamr](https://www.tamr.com/) - AI-driven data mastering.
- [Quantexa](https://www.quantexa.com/) - Entity resolution and network analytics for financial crime and customer intelligence.
- [Reltio](https://www.reltio.com/) - Cloud MDM with entity resolution.
- [Informatica MDM](https://www.informatica.com/products/master-data-management.html) - Enterprise master data management.
- [Tilores](https://tilores.io/) - Real-time entity resolution API.
- [Amperity](https://amperity.com/) - Customer data platform with identity resolution.
- [Google Cloud Entity Reconciliation](https://cloud.google.com/enterprise-knowledge-graph/docs/entity-reconciliation-console) - Part of Enterprise Knowledge Graph.

### Datasets

Datasets with known matches (ground truth) for learning, testing and research.

- [Leipzig benchmark datasets](https://dbs.uni-leipzig.de/research/projects/benchmark-datasets-for-entity-resolution) - DBLP-ACM, DBLP-Scholar, Abt-Buy and Amazon-Google, plus multi-source sets such as North Carolina voters and MusicBrainz.
- [Magellan data repository](https://sites.google.com/site/anhaidgroup/useful-stuff/the-magellan-data-repository) - Dozens of entity matching tasks collected by UW-Madison students.
- [DeepMatcher datasets](https://github.com/anhaidgroup/deepmatcher/blob/master/Datasets.md) - Structured, textual and dirty matching tasks with train/validation/test splits.
- [WDC Products](https://webdatacommons.org/largescaleproductcorpus/wdc-products/) - Product matching benchmark built from schema.org offers, with seen and unseen entities. ([paper](https://arxiv.org/abs/2301.09521))
- [Mannheim benchmark matching tasks](https://data.dws.informatik.uni-mannheim.de/benchmarkmatchingtasks/) - 21 entity matching tasks with fixed train, validation and test sets.
- [Febrl synthetic data](https://recordlinkage.readthedocs.io/en/latest/ref-datasets.html) - Synthetic Australian person records with duplicates, loadable from the Python Record Linkage Toolkit.
- [Splink datasets](https://moj-analytical-services.github.io/splink/api_docs/datasets.html) - Small person-record datasets bundled with Splink.
- [Zingg examples](https://github.com/zinggAI/zingg/tree/main/examples) - Febrl (65 to 5M records), NC Voters 5M, Amazon-Google and iTunes-Amazon with ready-made configs.
- [OpenSanctions](https://www.opensanctions.org/datasets/) - Real sanctions and PEP data from many sources, useful for cross-source person and company matching.
- [North Carolina voter registration](https://www.ncsbe.gov/results-data/voter-registration-data) - Public voter files. Snapshots over time contain real-world duplicates.

### Papers

**Foundations**
- Fellegi & Sunter, [A Theory for Record Linkage](https://doi.org/10.1080/01621459.1969.10501049), JASA 1969 - The probabilistic model behind most statistical linkage.
- Hernández & Stolfo, [The Merge/Purge Problem for Large Databases](https://doi.org/10.1145/223784.223807), SIGMOD 1995 - Sorted neighbourhood blocking.
- Sarawagi & Bhamidipaty, [Interactive Deduplication using Active Learning](https://doi.org/10.1145/775047.775087), KDD 2002 - Active learning for matching.
- Bilenko & Mooney, [Adaptive Duplicate Detection using Learnable String Similarity Measures](https://doi.org/10.1145/956750.956759), KDD 2003.

**Surveys**
- Elmagarmid, Ipeirotis & Verykios, [Duplicate Record Detection: A Survey](https://doi.org/10.1109/TKDE.2007.250581), TKDE 2007.
- Christen, [A Survey of Indexing Techniques for Scalable Record Linkage and Deduplication](https://doi.org/10.1109/TKDE.2011.127), TKDE 2012.
- Getoor & Machanavajjhala, [Entity Resolution: Theory, Practice & Open Challenges](https://doi.org/10.14778/2367502.2367564), VLDB 2012 tutorial.
- Christophides et al., [End-to-End Entity Resolution for Big Data: A Survey](https://arxiv.org/abs/1905.06397), 2019.
- Papadakis et al., [A Survey of Blocking and Filtering Techniques for Entity Resolution](https://arxiv.org/abs/1905.06167), 2019.
- Binette & Steorts, [(Almost) All of Entity Resolution](https://arxiv.org/abs/2008.04443), Science Advances 2022.
- Barlaug & Gulla, [Neural Networks for Entity Matching: A Survey](https://arxiv.org/abs/2010.11075), TKDD 2021.

**Systems and machine learning**
- Köpcke, Thor & Rahm, [Evaluation of Entity Resolution Approaches on Real-World Match Problems](https://doi.org/10.14778/1920841.1920904), VLDB 2010.
- Konda et al., [Magellan: Toward Building Entity Matching Management Systems](https://doi.org/10.14778/2994509.2994535), VLDB 2016.
- Mudgal et al., [Deep Learning for Entity Matching: A Design Space Exploration](https://doi.org/10.1145/3183713.3196926), SIGMOD 2018.
- Wu et al., [ZeroER: Entity Resolution using Zero Labeled Examples](https://arxiv.org/abs/1908.06049), SIGMOD 2020.
- Li et al., [Deep Entity Matching with Pre-Trained Language Models](https://arxiv.org/abs/2004.00584) (Ditto), VLDB 2021.

**Bayesian and statistical**
- Steorts, Hall & Fienberg, [A Bayesian Approach to Graphical Record Linkage and De-duplication](https://arxiv.org/abs/1312.4645), JASA 2016.
- Enamorado, Fifield & Imai, [Using a Probabilistic Model to Assist Merging of Large-Scale Administrative Records](https://doi.org/10.1017/S0003055418000783) (fastLink), APSR 2019.

**Large language models**
- Narayan et al., [Can Foundation Models Wrangle Your Data?](https://arxiv.org/abs/2205.09911), VLDB 2023.
- Peeters, Steiner & Bizer, [Entity Matching using Large Language Models](https://arxiv.org/abs/2310.11244), EDBT 2025.
- Peeters, Der & Bizer, [WDC Products: A Multi-Dimensional Entity Matching Benchmark](https://arxiv.org/abs/2301.09521), EDBT 2024.

**Privacy-preserving linkage**
- Schnell, Bachteler & Reiher, [Privacy-Preserving Record Linkage using Bloom Filters](https://doi.org/10.1186/1472-6947-9-41), BMC Medical Informatics and Decision Making 2009.

### Books

- Christen, [Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection](https://doi.org/10.1007/978-3-642-31164-2), Springer 2012 - The standard textbook.
- Christen, Ranbaduge & Schnell, [Linking Sensitive Data](https://doi.org/10.1007/978-3-030-59706-1), Springer 2020 - Privacy-preserving record linkage in depth.
- Papadakis, Ioannou, Thanos & Palpanas, [The Four Generations of Entity Resolution](https://doi.org/10.1007/978-3-031-01878-7), Springer 2021 - From batch, to big data, to incremental and progressive methods.
- Shearer, [Hands-On Entity Resolution](https://www.oreilly.com/library/view/hands-on-entity-resolution/9781098148478/), O'Reilly 2024 - Practical, Python-first introduction.

### Tutorials, courses and talks

- [Tutorials in this repository](#tutorials) - Runnable examples covering deduplication, linkage, products and evaluation.
- [An interactive introduction to probabilistic record linkage](https://www.robinlinacre.com/intro_to_probabilistic_linkage/) - Robin Linacre's visual explainer of the Fellegi-Sunter model.
- [Splink tutorials](https://moj-analytical-services.github.io/splink/demos/tutorials/00_Tutorial_Introduction.html) - Step-by-step notebooks from data exploration to clustering.
- [dedupe: how it works](https://docs.dedupe.io/en/latest/how-it-works/How-it-works.html) - Clear write-up of active learning, blocking and clustering.
- [dedupe-examples](https://github.com/dedupeio/dedupe-examples) - Runnable dedupe examples for CSV, PostgreSQL and MySQL.
- [Zingg documentation](https://docs.zingg.ai/) - Step-by-step guides for Zingg on Spark, Databricks, Snowflake and Fabric.
- [Zingg Databricks notebooks](https://github.com/zinggAI/zingg/tree/main/examples/databricks) - Set up, label, train and match on Databricks.

### Related fields

These are often confused with entity resolution. They solve different problems.

- **Entity linking**: link mentions in text to a knowledge base. See [Entity-Linking-Recent-Trends](https://github.com/izuna385/Entity-Linking-Recent-Trends) and [ReFinED](https://github.com/amazon-science/ReFinED).
- **Near-duplicate document detection**: find similar documents or web pages. See [datasketch](https://github.com/ekzhu/datasketch).
- **Schema matching**: match columns, not records. See [PyDI](https://github.com/wbsg-uni-mannheim/PyDI).

### Other lists

- [Awesome-Entity-Resolution](https://github.com/OlivierBinette/Awesome-Entity-Resolution) - Olivier Binette's list.
- [data-matching-software](https://github.com/J535D165/data-matching-software) - Feature table of free data matching software.
- [record-linkage-resources](https://github.com/ropeladder/record-linkage-resources) - Resources for record linkage and deduplication.

---

## Tutorials

Each tutorial is self-contained and runs with Docker. No local Spark install is needed.

| # | Tutorial | What you learn |
|---|---|---|
| 1 | [Deduplicate customer records](tutorials/01-deduplicate-customer-records/) | Find duplicate people in one table, label with active learning, train and match |
| 2 | [Link two customer lists](tutorials/02-link-two-customer-lists/) | Match records across a CRM extract and a billing system |
| 3 | [Match products across stores](tutorials/03-match-products-across-stores/) | Match product listings using text, model numbers and prices |
| 4 | [Evaluate your results](tutorials/04-evaluate-your-results/) | Measure precision, recall and F1 against known matches |

## Templates

Starter Zingg configurations for common entity types. Copy one, change the paths and column names, then follow [tutorial 1](tutorials/01-deduplicate-customer-records/).

- [Person and customer](templates/person/) - names, email, phone, date of birth, address
- [Company and organisation](templates/company/) - legal name, domain, registration ID, address
- [Product](templates/product/) - title, brand, model number, description, price

---

## Contributing

Know a tool, dataset or paper that belongs here? Found a mistake? Read the [contribution guide](CONTRIBUTING.md) and open a pull request. Links are checked automatically every week.

## License

Text and lists: [CC BY 4.0](LICENSE). Code in `tutorials/` and `templates/`: [Apache 2.0](LICENSE-CODE).

Maintained by [Sonal Goyal](https://github.com/sonalgoyal), creator of [Zingg](https://github.com/zinggAI/zingg).
