# Entity resolution vs. MDM vs. identity resolution

These terms overlap and are often used interchangeably. Here is how they relate.

## Entity resolution

The core matching capability: given records, decide which refer to the same real-world entity and group them. It is a data processing step, usually batch or incremental, and it produces a cluster or entity ID per record.

## Master data management (MDM)

A discipline and a category of software for keeping one trusted version of core business entities (customers, products, suppliers, locations) across the organisation. MDM includes:

1. **Entity resolution** to find which records belong together.
2. **Survivorship or golden record rules** to pick the best name, address and so on from each cluster.
3. **Stewardship** workflows so people can review, merge and unmerge.
4. **Governance**: ownership, data quality rules, audit history.
5. **Distribution**: publishing master data back to operational systems.

Entity resolution is the hardest technical part of MDM, and the part where most MDM projects succeed or fail. Open-source entity resolution plus warehouse tables for golden records is increasingly used as a lightweight, warehouse-native alternative to traditional MDM suites.

## Identity resolution

Entity resolution applied to **people**, typically customers, users or patients. In marketing and customer data platforms it also covers:

- **Deterministic identity graphs**: linking a login, device ID, cookie and email when they are seen together.
- **Probabilistic matching**: linking profiles by name, address and behaviour.
- **Householding**: grouping people who share an address or account.

## Customer data platforms (CDPs)

CDPs collect customer events and profiles from many tools and build unified profiles. Identity resolution is a built-in component. Composable or warehouse-native CDPs often run open-source entity resolution directly on the warehouse.

## Entity linking

Often confused with entity resolution, but different. **Entity linking** connects a mention in text ("Apple announced…") to an entry in a knowledge base (Apple Inc. in Wikidata). Entity resolution matches structured records to each other. See [Related fields](../README.md#related-fields).

## Summary

| | Input | Output | Typical users |
|---|---|---|---|
| Entity resolution | Records from one or more sources | Entity ID per record | Data engineers, data scientists |
| MDM | Records plus business rules | Governed golden records, published to systems | Data governance, IT |
| Identity resolution | Person and customer records, events, identifiers | Unified person profiles, identity graph | Marketing, fraud, CX |
| Entity linking | Free text plus a knowledge base | Mentions linked to KB entries | NLP, search |

## Next

- [Glossary](glossary.md)
