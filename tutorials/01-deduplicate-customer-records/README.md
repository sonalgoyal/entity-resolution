# Tutorial 1: Deduplicate customer records

**Goal:** find the duplicate people in a customer table, and give every real person one ID.

**Time:** about 20 minutes, including about 10 minutes of labelling.
**You need:** [Docker](https://docs.docker.com/get-docker/). No Spark or Java install.
**Tool:** [Zingg](https://github.com/zinggAI/zingg) 0.7.0, open source.

## The data

We use the classic **Febrl** synthetic customer data, which ships inside the Zingg image at `examples/febrl/test.csv`. It has 65 records, some of which are noisy duplicates of the same person:

```
id               fname    lname     stNo  add1               city              dob       ssn
rec-1021-org     thomas   george    1     mcmanus place      north turramurra  19630225  5460534
rec-1021-dup-0   thomas   georgze   1     mcmanus place      north turarmurra  19630225  5460534
rec-1022-dup-1   Érik     Guay      840   mountview          burlei gh heads   19830807  2932837
```

`rec-1021-org` and `rec-1021-dup-0` are the same person: note the typos in the surname and city. The ids tell us the right answer, which we use in [tutorial 4](../04-evaluate-your-results/) to score the result. The matcher never sees them, because `id` is marked `dont_use`.

## Step 0: Start the Zingg container

From the root of this repository:

```bash
docker run -it --rm \
  -v "$PWD/tutorials:/tutorials" \
  -v "$PWD/output:/tmp" \
  zingg/zingg:0.7.0 bash
```

The rest of the commands run **inside** the container. Models and results are written to `/tmp`, which is mapped to `./output` on your machine.

## Step 1: Tell Zingg about your fields

[`config.json`](config.json) describes the input, the output and how each field should be compared:

```json
{ "fieldName": "id",    "fields": "id",    "dataType": "string", "matchType": "dont_use" },
{ "fieldName": "fname", "fields": "fname", "dataType": "string", "matchType": "fuzzy" },
...
```

The `matchType` values used here are:

| Match type | Use for |
|---|---|
| `fuzzy` | Names, addresses, short strings with typos |
| `exact` | Codes and IDs that must be identical |
| `email` | Email addresses. Compares the part before `@` |
| `pincode` | Postcodes and ZIP codes. `94102-1234` matches `94102` |
| `numeric` | Numbers inside strings, such as street numbers |
| `text` | Long descriptions where word overlap matters |
| `dont_use` | Carry the column through to the output without using it for matching |

See the [templates](../../templates/) for suggested settings for people, companies and products.

## Step 2: Find pairs worth labelling

```bash
zingg.sh --properties-file config/zingg.conf --phase findTrainingData \
  --conf /tutorials/01-deduplicate-customer-records/config.json
```

Zingg samples the data and picks pairs it is unsure about. This is [active learning](../../docs/active-learning.md): you label only pairs that teach the model something.

> `--properties-file config/zingg.conf` sets the Spark memory and other settings for your machine. Use it on every command.

## Step 3: Label them

```bash
zingg.sh --properties-file config/zingg.conf --phase label \
  --conf /tutorials/01-deduplicate-customer-records/config.json
```

Zingg shows you pairs of records, one at a time:

```
	What do you think? Your choices are:

	No, they do not match : 0
	Yes, they match       : 1
	Not sure              : 2

	To exit               : 9

	Please enter your choice [0,1,2 or 9]:
```

Answer each pair. For this dataset, **about 10 matching pairs** is enough, usually one or two rounds of **steps 2 and 3**. On larger, messier data, run a few more rounds. Each round, Zingg picks harder pairs as its model improves. See [labelling well](../../docs/active-learning.md#labelling-well) for tips.

## Step 4: Train and match

```bash
zingg.sh --properties-file config/zingg.conf --phase train \
  --conf /tutorials/01-deduplicate-customer-records/config.json

zingg.sh --properties-file config/zingg.conf --phase match \
  --conf /tutorials/01-deduplicate-customer-records/config.json
```

`train` builds two models from your labels: a **blocking model** that decides which records to compare, and a **classifier** that decides whether a pair matches. `match` applies them to all records.

## Step 5: Read the results

The output is in `output/customers-deduped/` on your machine. It is a folder of CSV part files, one per Spark partition:

```
z_minScore,z_maxScore,z_cluster,id,fname,lname,...
0.9999,0.9999,1,rec-1021-org,thomas,george,...
0.9999,0.9999,1,rec-1021-dup-0,thomas,georgze,...
```

| Column | Meaning |
|---|---|
| `z_cluster` | Entity ID. Records with the same value are the same person |
| `z_minScore` | Lowest match score between this record and others in its cluster |
| `z_maxScore` | Highest match score between this record and others in its cluster |

A low `z_minScore` in a large cluster is worth a look: it can mean that two different people were chained together.

## Shortcut: skip labelling

To see the whole pipeline before you label anything, [`config-prelabeled.json`](config-prelabeled.json) points Zingg at a set of pairs that are already labelled, shipped in the image as `examples/febrl/training.csv`. It has just **8 matching and 13 non-matching pairs**:

```bash
zingg.sh --properties-file config/zingg.conf --phase trainMatch \
  --conf /tutorials/01-deduplicate-customer-records/config-prelabeled.json
```

From those 8 matches, our run found 30 clusters for the 27 real people, with pairwise **precision 1.00, recall 0.92 and F1 0.96**. See [tutorial 4](../04-evaluate-your-results/) for how to compute this.

## The same thing in Python

[`dedupe_customers.py`](dedupe_customers.py) does the same with the Zingg Python API. Pass the phase on the command line:

```bash
zingg.sh --properties-file config/zingg.conf \
  --run /tutorials/01-deduplicate-customer-records/dedupe_customers.py --phase findTrainingData
# then --phase label, --phase train, --phase match
```

## Next

- Run on your own data: copy a [template](../../templates/), change the path and columns, and repeat steps 2-4.
- [Tutorial 2: Link two customer lists](../02-link-two-customer-lists/)
- Scale up: the image also has 120,000 Febrl records in `examples/febrl120k/`. Zingg runs the same configuration on a Spark cluster or Databricks for millions of records.
