#!/usr/bin/env python

import os, sys, subprocess
import urllib.request
import tarfile

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.parse_args() # support --help

    repo_root = subprocess.run(["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE).stdout.decode("utf8").rstrip()
    assert os.path.samefile(repo_root, "."), "run this from the repo root"

    url = "https://sourceforge.net/projects/infozip/files/Zip%203.x%20%28latest%29/3.0/zip30.tar.gz/download"

    all_files = set()
    with urllib.request.urlopen(url) as r:
        tar = tarfile.open(fileobj=r, mode="r:gz")
        for tarinfo in tar:
            name = os.path.normpath(tarinfo.name)
            if name == "zip30": continue
            top, name = name.split(os.path.sep, 1)
            assert top == "zip30", "expected all items to be in a top-level dir called zip30"

            if tarinfo.isdir():
                os.makedirs(name, exist_ok=True)
            elif tarinfo.isfile():
                if os.path.sep in name:
                    os.makedirs(os.path.dirname(name), exist_ok=True)
                # Do not set any attrs.
                tar.makefile(tarinfo, name) # low level alternative to extract()
                all_files.add(name)
            else: assert False, "what's this? " + name

    # Remove any files that shouldn't be there.
    for dir, dirs, files in os.walk("."):
        if dir == ".":
            dirs.remove(".github")
            dirs.remove(".git")
        for file in files:
            file = os.path.normpath(os.path.join(dir, file))
            if file not in all_files:
                os.remove(file)

    # Make a commit that appears to come from the actual authors.
    subprocess.run(["git", "add", "--force"] + list(all_files))
    subprocess.run(["git", "commit", "-m", "import zip 3.0 from sourceforge"], env={**os.environ,
        # Give credit in the commit metadata.
        "GIT_AUTHOR_NAME": "The Info-ZIP Team",
        "GIT_AUTHOR_EMAIL": "no-email@fake.invalid",
        "GIT_AUTHOR_DATE": "2008-07-07T12:00:00Z", # Release date according to https://infozip.sourceforge.net/
        # Leave the GIT_COMMITTER_* fields unoverridden.
    })

if __name__ == "__main__":
    main()
