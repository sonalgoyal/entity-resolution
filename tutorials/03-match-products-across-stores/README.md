# Tutorial 3: Match products across stores

**Goal:** match the same product listed in two catalogues, using titles, descriptions, manufacturers and prices.

Product matching is harder than person matching:

- Titles are long, free-form and word order changes: "Microsoft Office 2007 Small Business" vs. "office small business 2007 (pc)".
- **Model numbers and versions decide the match**: "Photoshop CS3" and "Photoshop CS4" differ in one character but are different products.
- Descriptions are often missing, and prices vary between sellers.

**Time:** about 30 minutes. **You need:** Docker. **Tool:** [Zingg](https://github.com/zinggAI/zingg) 0.7.0.

## The data

The **Amazon-Google Products** dataset from the [Leipzig entity resolution benchmarks](https://dbs.uni-leipzig.de/research/projects/benchmark-datasets-for-entity-resolution): 1,363 Amazon and 3,226 Google Shopping software products, with a file listing the 1,300 true matches. Zingg keeps a copy in its examples folder. Download it into `data/`:

```bash
cd tutorials/03-match-products-across-stores
mkdir -p data && cd data
for f in Amazon.csv.gz GoogleProducts.csv.gz Amzon_GoogleProducts_perfectMapping.csv.gz; do
  curl -sLO "https://github.com/zinggAI/zingg/raw/main/examples/amazon-google/$f"
done
cd ../../..
```

## Step 1: The configuration

[`config.json`](config.json) uses a different match type for each kind of field:

| Field | Match type | Why |
|---|---|---|
| `title` | `fuzzy,numeric_with_units` | Fuzzy similarity for the words, **plus** a separate feature that compares tokens like `cs3`, `2007` or `16gb` that contain digits |
| `description` | `text` | Word overlap suits long text. Order doesn't matter |
| `manufacturer` | `fuzzy` | "Microsoft" vs. "Microsoft Corp" |
| `price` | `fuzzy` | Prices are similar but rarely identical across stores |
| `id` | `dont_use` | Carried through to the output only |

**One field, several match types.** You define each column once and list as many match types as you need, separated by commas. Zingg computes a feature for each one and the model learns how much each matters. For `title`, that means general word similarity and an exact check on model numbers come from a single field definition, with no duplicate columns or extra config.

## Step 2: Start the container, label and train

```bash
docker run -it --rm -v "$PWD/tutorials:/tutorials" -v "$PWD/output:/tmp" zingg/zingg:0.7.0 bash

C=/tutorials/03-match-products-across-stores/config.json
P="--properties-file config/zingg.conf"

zingg.sh $P --phase findTrainingData --conf $C
zingg.sh $P --phase label --conf $C
# repeat a few times until you have ~40 matches, then:
zingg.sh $P --phase train --conf $C
zingg.sh $P --phase link --conf $C
```

When labelling products, **check the model number and version first**. Most non-matches that look similar differ only there.

## Step 3: Score against the true matches

From the repository root, on your machine:

```bash
python tutorials/04-evaluate-your-results/evaluate.py output/products-linked \
  --truth-pairs tutorials/03-match-products-across-stores/data/Amzon_GoogleProducts_perfectMapping.csv.gz \
  --id-col id --source-col z_zsource
```

Many Amazon-Google listings are different versions and editions of the same software, so it is a good dataset for seeing how match types like `numeric_with_units` separate "Photoshop CS3" from "Photoshop CS4" while still matching differently worded titles.

## Ideas to improve results

- **Normalise titles** before matching: lowercase, strip "(pc)", "[old version]", edition words and punctuation.
- **Extract the model or version** into its own column with a regex, and compare it with `exact`.
- **Add stop words** for words that appear in almost every title, like "software" and "edition". See the Zingg docs on stop words.

## Next

- [Tutorial 4: Evaluate your results](../04-evaluate-your-results/)
- [Product template](../../templates/product/)
