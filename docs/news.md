# Adding a News Item

Create a new file in `_post` named `YYYY-MM-DD-title-for-url.md` and copy the following template:

```markdown
---
layout: post
shortnews: true
icon: newspaper-o

---

Put Markdown formatted news content here
```

Replace `icon` with an appropriate selection from the table below

| News Item                         | Icon              |
|-----------------------------------|-------------------|
| Mention in newspaper, blog, etc.  | `newspaper-o`     |
| Mention on / Link to Twitter      | `twitter`         |
| Announcement of an Event          | `calendar`        |
| Link to Video Platform            | `film`            |
| Graduation, Defense or related    | `graduation-cap`  |


I.e. A post linking to YouTube should have: `icon: film`

## Post Contents

Short news should have the following traits

- Short, concise and positive
    - Ideally less than 200 characters, and no more than 500
    - Primary goal is linking out to other sites. Explanatory detail should be avoided.

- Don't: link [here](www.example.com), Do: Read our [article](www.example.com)
- Follow [CMU Brand Guidelines](https://www.cmu.edu/brand/brand-guidelines/web.html)

---

## Talks

To announce an up-coming talk use the following template:


### Zoom Talks

```markdown
---
layout: talk
icon: put_icon_here
title: talk_title
when: August 2nd at 4:00 PM EST
zoom:
    id: put_zoom_meeting_id_here
    link: zoom link
    passcode: put_zoom_passcode_here
---

Please join us for John's talk on {{ page.when }} via [Zoom] on the "*{{ page. title }}*"

[Zoom]: {{ page.zoom.link }}

```

> If no passcode is required, omit the `passcode` entry

### In-Person Talks

If the talk is in person, use the following [front matter](https://jekyllrb.com/docs/front-matter/) instead

```markdown
---
layout: talk
icon: put_icon_here
title: talk_title
when: July 19th, 2021, from 2 to 4:30 pm EST
where: location of talk

---
```

### Recordings

If a available of the talk is available, please append a link to the recording.

---
