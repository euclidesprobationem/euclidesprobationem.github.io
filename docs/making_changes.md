# Making Changes

This file will guide you through editing files, committing your changes, and opening a pull request. For information about specific types of edits (i.e. making a news post) see [README.md](../README.md)

## Editing Files

### Clone the Repo with Git

- Clone the repo with [git]: `git clone https://github.com/BattModels/group-website.git`
- Check out a branch to make edits: `git checkout -b branch_name`
- Make some changes
- Stage (`git add`) and commit (`git commit`) your changes
- Push to Github: `git push -u origin branch_name`
- Open a [Pull Request](https://github.com/BattModels/group-website/pulls)

> Replace `branch_name` with a short, descriptive name

```shell
git fetch origin
git checkout master
git reset --hard origin/master
```

> This will delete any local changes you have, please stash or save them if important

### Editing On GitHub

Edits can also be made directly on Github:

- [Editing files in your repository](https://docs.github.com/en/github/managing-files-in-a-repository/managing-files-on-github/editing-files-in-your-repository)
- [Creating new files](https://docs.github.com/en/github/managing-files-in-a-repository/managing-files-on-github/creating-new-files)

When committing changes be sure to "create a new branch...", committing directly to master is blocked.



## Peer Review

Peer review helps to catch issues before the changes go live (~10 minutes after
merging into master) and gives stakeholders a chance to provide feedback. What
follows is a rough guide, but when in doubt, ask for a review.

| Change                                        | Reviewer Needed?                         |
|-----------------------------------------------|------------------------------------------|
| Update your profile image, website, or email  | Nope, you are good to go                 |
| News post about someone else?                 | Add them as a reviewer                   |
| New project page?                             | Add someone (not just you) as a reviewer |
| Edits to an existing page?                    | Add the prior author                     |
| Docs, testing, or code changes?               | Add Alex as a reviewer                   |

## Status Checks

In order to prevent broken links, missing images, or other mayhem, we run a
battery of checks on all submissions. You can run these test locally with:

```shell
make test
```

This will attempt to install any needed python / ruby dependencies but may fail
if you use an older version of python. For reference, the following versions are
used to build the released website:

- Python Latest 3.x version
- Ruby Latest 3.x version

Most `pre-commit` checks will also make the necessary corrections when failed.
To apply these fixes, add and commit the corrections.

## Building Locally

To build and serve the website locally, run:

```shell
make serve
```

You can then make browse the website, make changes and immediately see (most)
changes reflected on the local website. Some changes do require rebuilding the
site to take affect. In a separate shell run:

```shell
make build
```

To fully re-build the site, the `make serve` command will pick these up and
immediately display them.
