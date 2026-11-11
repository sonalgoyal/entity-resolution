# Contributing

Thanks for helping make this the most useful entity resolution resource on the web. Suggestions for any tool, including tools that compete with Zingg, are welcome.

## Adding to the awesome list

1. Put the entry in the most specific section of [README.md](README.md). Within a section, more widely used and actively maintained projects come first.
2. Use this format:

   ```
   - [Name](link) - What it does, in one sentence ending with a full stop. *(Language · Platform)*
   ```

   Add `inactive` to the tag if there have been no commits for two years, and `archived` if the repository is archived.
3. Describe what the project does, not how good it is. Avoid "best", "fastest" and "state of the art" unless you link a source.
4. Link to the canonical home: the GitHub repository for open source, the DOI or arXiv page for papers.

**What belongs:** open-source software, datasets and learning material about entity resolution, record linkage, deduplication and closely related data preparation.

**What doesn't:** unmaintained forks, personal homework repositories, and tools with no documentation. Commercial products go only in the commercial section.

## Correcting the comparison table

The table in [Open-source entity resolution tools compared](README.md#open-source-entity-resolution-tools-compared) should be accurate for every tool. If something is wrong or out of date, open an issue or pull request with a link to the tool's documentation. Maintainers of the listed projects are especially welcome to correct their own rows.

## Guides, tutorials and templates

- Guides in `docs/` should be short, plain language and tool-neutral. Link to tools as examples; don't sell them.
- Tutorials must run end to end from a clean checkout with Docker. Say which tool version you tested with.
- Code is licensed under Apache 2.0, and text under CC BY 4.0. By contributing, you agree to license your contribution under these terms.

## Links

A weekly job checks every link and opens an issue for broken ones. You can run the same check locally with [lychee](https://github.com/lycheeverse/lychee):

```bash
lychee --accept 200,206,403,429 '**/*.md'
```
