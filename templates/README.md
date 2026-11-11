# Entity resolution templates

Starter [Zingg](https://github.com/zinggAI/zingg) configurations for the three most common kinds of entity. Each folder has:

- `config.json`: field definitions with suggested match types.
- `sample.csv`: a small synthetic dataset with planted duplicates, so the template runs as-is.
- `README.md`: why each field is set up the way it is, and what to change.

| Template | Typical sources | Key fields |
|---|---|---|
| [Person and customer](person/) | CRM, e-commerce, loyalty, patient registers | Name, email, phone, date of birth, address |
| [Company and organisation](company/) | Supplier masters, CRM accounts, KYC | Legal name, website, registration ID, address |
| [Product](product/) | Catalogues, marketplaces, price feeds | Title, brand, model number, description, price |

## Try one

From the repository root:

```bash
docker run -it --rm -v "$PWD/templates:/templates" -v "$PWD/output:/tmp" zingg/zingg:0.7.0 bash

# inside the container, e.g. for people:
C=/templates/person/config.json
P="--properties-file config/zingg.conf"
zingg.sh $P --phase findTrainingData --conf $C
zingg.sh $P --phase label --conf $C       # repeat these two a few times
zingg.sh $P --phase train --conf $C
zingg.sh $P --phase match --conf $C
```

## Use one with your own data

1. Copy the folder.
2. In `config.json`, change `data[0].props.path` to your file, set `schema` to your column names and types, and rename the `fieldName` and `fields` entries to match.
3. Delete field definitions you don't have. Mark columns you want in the output but not in matching as `dont_use`.
4. Change the `modelId` so models for different datasets don't overwrite each other.

Zingg reads from CSV, Parquet, JSON, Delta, JDBC databases, Snowflake, BigQuery and more. See the [Zingg data sources docs](https://docs.zingg.ai/).

## Rules of thumb

- **Clean before you match.** Trim whitespace, normalise case, and turn placeholders like `N/A`, `unknown` and `1900-01-01` into empty values.
- **Add `null_or_blank`** to fields that are often missing, such as `"email,null_or_blank"`. By default an empty value counts as agreeing with anything. This flag lets the model learn that two empty values are not evidence of a match.
- **Combine match types** on one field instead of defining the same column twice: `"fuzzy,numeric_with_units"`.
- **Don't match on everything.** Fields that are mostly empty, or that change constantly like `last_login`, add noise.
