# Company and organisation template

For suppliers, customers (B2B accounts), counterparties, legal entities and organisations.

## Fields

| Field | Match type | Why |
|---|---|---|
| `id` | `dont_use` | Your system's key |
| `name` | `fuzzy` | Legal suffixes (Inc, Ltd, GmbH), case, abbreviations, typos |
| `website` | `fuzzy,null_or_blank` | `https://www.acme.example/about` vs. `acme.example`. Often blank |
| `registration_id` | `exact,null_or_blank` | Company number, VAT, EIN, LEI or DUNS. When present it is decisive; when blank it shouldn't count |
| `address` | `fuzzy` | Street abbreviations |
| `city` | `fuzzy` | |
| `postcode` | `fuzzy` | Formats vary by country (`NW1 6XE`, `10117`). Use `pincode` if all your data is US ZIP codes |
| `country` | `exact` | ISO country code. Standardise first |

## What to change for your data

- **Parent and subsidiary.** Decide up front whether "Acme Corp" and "Acme Corp UK Ltd" are one entity or two, and label consistently. Most teams treat legal entities separately and build the hierarchy afterwards.
- **Branches and locations.** If you need one record per site, keep address fields and label different sites as non-matches. If you want one record per company, drop the street address and keep city and country.
- **Several identifiers?** Give each its own column (`vat_number`, `lei`, `duns`), each `exact,null_or_blank`.

## Standardise first

- Strip legal suffixes into their own column with [cleanco](https://github.com/psolin/cleanco), then match on the cleaned name.
- Reduce websites to the bare domain: strip `https://`, `www.` and paths.
- Uppercase identifiers and remove spaces and punctuation from them.
- Use ISO 3166 country codes.

## Sample data

`sample.csv` holds 58 synthetic companies, all fictional with `.example` domains. Duplicates have dropped or changed legal suffixes, uppercase names, typos, full URLs instead of domains, and missing registration IDs.
