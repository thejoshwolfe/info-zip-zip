# Info-ZIP zip mirror

This is a mirror of the source code for the `zip` command line program by Info-ZIP.
Version: `3.0` aka `3.00`.

You can download the original code from the maintainers here: https://sourceforge.net/projects/infozip/files/

Note that the version of `zip` that you have installed may be patched by your package manager.
For example, see: https://github.com/NixOS/nixpkgs/blob/25.05/pkgs/by-name/zi/zip/package.nix#L37-L77

Note that this is only for `zip`. For `unzip` see: https://github.com/thejoshwolfe/info-zip-unzip

## Why host a mirror?

As far as I can tell, the Info-ZIP group does not use version control,
and SourceForge doesn't allow browsing the contents of source archives.
This GitHub mirror exists to allows browsing the code and linking to specific lines without needing to download and extract archives to your computer.

Also as far as I can tell, the official Info-ZIP homepage https://infozip.sourceforge.net/ does not actually link to the source code, despite several claims that it does.
The various ftp links are a confusing web of link rot, and I made this mirror to help anyone else struggling to navigate that.

## Boycott SourceForge

From 2013 to 2016, SourceForge modified downloads for open source projects' Windows installers to bundle adware with them against the developers' wishes.
Affected projects include GIMP, VLC, and nmap to name a few.
A code hosting platform has a responsibility to the community, and SourceForge broke the community's trust.
Although SourceForge was acquired in 2016 and the new management promised not to betray the community again, it's too late.
Free and open source software developers volunteering their labor for the betterment of humanity should not have to put up with an organization that has any track record like this.

For more information: https://en.wikipedia.org/wiki/SourceForge#Installer_with_adware

## Automation

This repo's primary content is managed by an automated script located at `.github/download.py`.
You can review the automation and run it yourself to verify that the code mirrored here is unmodified from the original.

There is no periodically-running automation to check for updates from Info-ZIP.
As of writing this, the latest stable version was published in 2008.
If you notice that a new version is available, please open an issue and I will re-run the automation and make a new commit.
https://github.com/thejoshwolfe/info-zip-zip/issues/new
