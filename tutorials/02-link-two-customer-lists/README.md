# Tutorial 2: Link two customer lists

**Goal:** you have two customer lists from different systems, say a CRM export and a billing system. Each list is clean on its own. Find which customers appear in both.

This is **record linkage**: records are compared *across* the two sources, never within one. If your lists also contain duplicates inside them, use the `match` phase from [tutorial 1](../01-deduplicate-customer-records/) instead. It will find duplicates both within and across sources.

**Time:** about 20 minutes. **You need:** Docker. **Tool:** [Zingg](https://github.com/zinggAI/zingg) 0.7.0.

## The data

Two Febrl files from the Zingg image:

- `examples/febrl/test1.csv`: 27 records, our "CRM".
- `examples/febrl/test2.csv`: 38 records, our "billing system".

## Step 0: Start the container

From the repository root:

```bash
docker run -it --rm -v "$PWD/tutorials:/tutorials" -v "$PWD/output:/tmp" zingg/zingg:0.7.0 bash
```

## Step 1: The configuration

[`config.json`](config.json) is the same as tutorial 1, except that `data` now lists **two** inputs:

```json
"data": [
  { "name": "crm",     "format": "csv", "props": { "path": "examples/febrl/test1.csv", ... } },
  { "name": "billing", "format": "csv", "props": { "path": "examples/febrl/test2.csv", ... } }
]
```

Both inputs must have the same columns. If yours don't, rename and reorder them first, for example with a SQL view, a Spark job or pandas.

## Step 2: Label and train

Same as tutorial 1: run `findTrainingData` and `label` until you have about 10 matches, usually one or two rounds, then `train`.

```bash
C=/tutorials/02-link-two-customer-lists/config.json
P="--properties-file config/zingg.conf"

zingg.sh $P --phase findTrainingData --conf $C
zingg.sh $P --phase label --conf $C
# repeat the two commands above a few times, then:
zingg.sh $P --phase train --conf $C
```

## Step 3: Link

```bash
zingg.sh $P --phase link --conf $C
```

## Step 4: Read the results

The output is in `output/customers-linked/`:

```
z_cluster,z_score,id,fname,lname,stNo,add1,add2,...,z_zsource
1794391911431:26,0.99999,rec-1032-org,brooklyn,naar-cafentas,210,duffy street,tourist park,...,crm
1794391911431:26,0.99999,rec-1032-dup-0,brooklyn,naar-cafentas,210,duffy street,tourist psrk,...,billing
```

The billing record has a typo in the address ("tourist psrk") and no date of birth, and is still linked.

| Column | Meaning |
|---|---|
| `z_cluster` | Link ID. Records with the same value refer to the same customer |
| `z_score` | Match score for the link |
| `z_zsource` | Which input the record came from (`crm` or `billing`) |

To get a simple mapping table of CRM id to billing id, pivot on `z_cluster`:

```sql
SELECT c.id AS crm_id, b.id AS billing_id, c.z_score
FROM linked c JOIN linked b
  ON c.z_cluster = b.z_cluster AND c.z_zsource = 'crm' AND b.z_zsource = 'billing';
```

## Tip: link vs. match

| You have | Use |
|---|---|
| One table with duplicates | `match` |
| Several tables, each without internal duplicates, to join | `link` |
| Several tables, each with internal duplicates | `match` on all of them together. Zingg considers all sources |

## Next

- [Tutorial 3: Match products across stores](../03-match-products-across-stores/)
- [Tutorial 4: Evaluate your results](../04-evaluate-your-results/)
