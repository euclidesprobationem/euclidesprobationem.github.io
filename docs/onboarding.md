# On-Boarding

Welcome to the team! As a quick order of business, let's get you added to the website!

1) Install [git], create a [GitHub] account and request to join [BattModels]
2) Clone the website: `git clone https://github.com/BattModels/group-website.git`
3) Open `_data/people.yml` in the newly created `group-website` folder
4) Add a small (<100 Kb) headshot here: `img/people/andrewid.png`
    - If your headshot is too large, try compressing it with an online tool
    - Aspect ratio should be 1:1 with the head centered in the image

5) Add an entry to the end of the appropriate section:
    - i.e. if you're a master's student, add your entry under `# masters`
    - Refer to [Entry Format](#entry-format) for the desired format

5) Commit and push your changes:
    - Create a new branch: `git checkout -b add_john_doe`
    - Add files to the staging area with `git add`
        - `git add _data/people.yml`
        - `git add img/people/andrewid.png`
    - Commit the staged changes: `git commit -m "Adding John Doe's Info"`
    - Push the commit to Githib with `git push -u origin add_john_doe`

6) Open a [pull request on Github][pr]
    - If this is your first commit, slack @awadell1 to approve running CI
    - If all checks pass, merge your pull request
    - Otherwise, try to [fix the issues](1) or [ask for help](2)

7) Congrats on making your first pull request in the group!

[1]: https://github.com/BattModels/group-website/blob/master/docs/making_changes.md#status-checks
[2]: https://github.com/BattModels/group-website/issues

> Remember: All references to John Doe are for illustration. Please use
> a more descriptive branch name. Like `add_your_name`

## Entry Format

```yaml
your_andrew_id:
    display_name: "John Doe"
    role: staff
    image: img/people/your_andrew_id.png
    webpage: "www.john_doe_awesome_site.com"
    email: "jdoe [at] andrew [dot] cmu [dot] com"
    bio: Current Position
```


### Roles

We define several roles (Full List is in `_config.yml`), but you probably want
one of the following:

- `phd`
- `masters`
- `ugrad`
- `postdoc`
- `staff`

[git]: https://git-scm.com/
[GitHub]: https://github.com
[BattModels]: https://github.com/BattModels
[pr]: https://github.com/BattModels/group-website/pulls

### Personal Website

Common websites to link to:

- [Linkedin](https://www.linkedin.com)
- [Google Scholar](https://scholar.google.com/)
- Personal Blog

If you do not have a website, please omit this entry. You are always welcome to add one later.

### Bio

For your bio enter your current title, omitting your educational level. For
example, a P.h.D student in Mechanical Engineering, would put "Mechanical
Engineer".

If you have already graduated, you may include your educational level if desired.
