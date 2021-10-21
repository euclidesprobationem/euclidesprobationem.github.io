# Adding a Paper or Publication

Add a BibTex citation for your work to:

- For publications: `_bib/pubs.bib`
- For patents: `_bib/patents.bib`

Add new entries to the top of the indicated file.

## Citation Fields

Citation entries must contain the following:

- title
- author
- journal
- year
- url

Citations may not include the following:

- abstract
- notes

> You must manually confirm that the url is correct.

## Formatting Issues

### Encoding Issues

BibTex does not handle Unicode characters; for example, `á` will be rendered as `\{'{a}}`. Replace the escaped version (i.e. `\{'{a}}`) with the Unicode (`á`) character.

### Multi-Word Names

BibTex assumes a single word first and last name for authors; and will capture multi-word names with braces: `{de la...}`.
As the braces will be rendered on the website, they must be removed.

## Finishing Up

Commit your changes, push to Github and open a [Pull Request](https://github.com/BattModels/group-website/pulls)

- `git add _bib/pubs.bib` or `_bib/patents.bib`
- `git commit -m "Adding New Publication"`
- `git push -u origin branch_name`

> Replace `branch_name` with the name of your branch
