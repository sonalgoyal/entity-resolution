# Product template

For catalogue items, marketplace listings, price feeds and SKUs.

## Fields

| Field | Match type | Why |
|---|---|---|
| `id` | `dont_use` | Your SKU or listing ID |
| `title` | `fuzzy,numeric_with_units` | Fuzzy similarity for the words, plus a feature comparing tokens with digits like `128gb`, `27-inch` or `xm4`. Variants that differ only in capacity or generation are the hardest non-matches |
| `brand` | `fuzzy` | Case and spelling |
| `model_number` | `fuzzy` | `WH-1000XM4` vs. `WH1000XM4` |
| `description` | `text` | Word overlap suits long text. Word order doesn't matter |
| `price` | `fuzzy` | Close but rarely identical across sellers. Type `double` |
| `gtin` | `exact,null_or_blank` | GTIN, UPC, EAN or ISBN. Decisive when present |

## What to change for your data

- **What is "the same product"?** Decide whether colours, sizes and pack sizes are variants of one product or separate products, and label consistently.
- **Model numbers buried in titles?** Extract them with a regex into their own column. This is one of the biggest accuracy wins for product matching.
- **Multiple currencies?** Convert prices first, or drop price.

## Standardise first

- Lowercase and strip marketing words ("new", "free shipping", "2024 model").
- Normalise units: `1 TB` → `1tb`, `27"` → `27-inch`.
- Remove separators from model numbers (`-`, `/`, spaces) into a normalised column.

## Sample data

`sample.csv` holds 67 synthetic listings. They include near-identical variants that are **not** matches (128GB vs. 256GB, Gen 1 vs. Gen 2, XM4 vs. XM5) and true duplicates with reformatted titles, model numbers without dashes, missing descriptions and slightly different prices. GTINs are fake values from the 200 prefix range reserved for in-store use.
