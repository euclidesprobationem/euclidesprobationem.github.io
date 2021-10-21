#!/usr/env/python
# Content check on _data/people.yaml
from os import error
import yaml
import logging
from pathlib import Path

DIR = Path(__file__).parent.parent


def check_people():
    with open("_data/people.yml", "r") as io:
        people = yaml.load(io, Loader=yaml.SafeLoader)

    errors = 0
    for name, info in people.items():
        # Check for required info
        valid = True
        for k in ["role", "display_name"]:
            if k not in info:
                errors += 1
                valid = False
                logging.error("Missing %s for %s", k, name)

        if not valid:
            continue

        # Check for obfuscated email
        if "email" in info and "@" in info["email"]:
            errors += 1
            logging.error("Non-obfuscated email (%s) for %s", info["email"], name)

        # Skip checks for alumni
        if info["role"].startswith("alumni"):
            continue

        # Check Phot
        if "image" not in info:
            errors += 1
            logging.error("Missing 'image' for %s", name)
        else:
            img = Path(DIR, info["image"])
            if info["image"].startswith("/"):
                errors += 1
                logging.error("Remove leading '/' from 'image' for %s", name)
            if not img.is_file():
                errors += 1
                logging.error("Missing 'image' (%s) for %s does not exist", img, name)
            elif not str(img.name).startswith(name):
                errors += 1
                logging.error(
                    "Images should be named after yaml key (%s), currently %s",
                    name,
                    img.name,
                )
                img.rename(Path(img.parent, name + img.suffix))

        # Check that name matches andrew id for current students
        # Ideally should match for prior students too, but that's harder
        # to validate
        if "email" in info:
            andrewid = info["email"].split(" ")[0]
            if name != andrewid:
                errors += 1
                logging.error("Expected andrew id (%s) for %s", andrewid, name)
                continue

    if errors > 0:
        logging.critical("Found %d errors -> Please Fix and resubmit", errors)
        exit(1)


if __name__ == "__main__":
    check_people()
