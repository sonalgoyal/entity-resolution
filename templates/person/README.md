# Person and customer template

For customer, patient, member, employee and contact records.

## Fields

| Field | Match type | Why |
|---|---|---|
| `id` | `dont_use` | Your system's key. Kept in the output so you can join back |
| `first_name` | `fuzzy` | Typos, initials, transliteration. Nicknames like Bob and Robert are better handled by standardising first (see below) |
| `last_name` | `fuzzy` | Typos, hyphenation, O'Neill vs. ONeill |
| `email` | `email,null_or_blank` | `email` compares the part before `@` and ignores the domain, so `jsmith@work.com` and `jsmith@gmail.com` agree. Often blank |
| `phone` | `numeric,null_or_blank` | Compares the digits, so `(212) 555-0144` and `2125550144` agree. Often blank |
| `dob` | `fuzzy` | Catches transposed digits and day/month swaps. Standardise the format first |
| `address` | `fuzzy` | St vs. Street, apartment numbers |
| `city` | `fuzzy` | Case, abbreviations |
| `postcode` | `pincode` | `94110` matches `94110-1234` |

## What to change for your data

- **No date of birth?** Delete it. Matching will lean more on address and email, so label more pairs.
- **Multiple emails or phones per person?** Put each in its own column, such as `email_work` and `email_personal`.
- **Non-Western names?** Keep `fuzzy`. Zingg works with Chinese, Japanese, Thai, Hindi and other scripts. Don't strip accents if the source data is consistent about them.
- **Strict use case, like patient matching?** Add any strong identifier you have (medical record number, national ID) as `exact,null_or_blank`, and choose a higher match threshold when you review results.

## Standardise first

These steps often improve accuracy more than more labelling does:

- Map nicknames to formal names with [nicknames](https://github.com/carltonnorthern/nicknames).
- Parse full names with [python-nameparser](https://github.com/derek73/python-nameparser).
- Normalise phones to E.164 with [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers).
- Parse addresses with [libpostal](https://github.com/openvenues/libpostal).
- Convert dates to `YYYY-MM-DD`.

## Sample data

`sample.csv` holds 24 synthetic people with planted duplicates: nicknames, typos, reformatted phones, ZIP+4 postcodes, missing emails. It includes two different people both called Robert Smith, to test that the model doesn't merge them.
