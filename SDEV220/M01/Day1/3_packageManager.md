# PACKAGE MANAGERS

---

## What are package managers?

Package managers are tools which makes the tasks of installing, upgrading, removing, and configuring software easier and 'all in one place'. IT MANAGES you software PACKAGES!!!

We have already seen some for specific OS (like homebrew and chocolatey) package managers to manage software for your computer (like getting python!). Now we are transitioning to package managers specifically for installing packages for your programming language.

There is only so much code that comes by default with Python, and it would be silly to only limit ourselves to only that. That is why packages exist! They allow us as developers to use other people's code more easily. No more are the days where you copy and paste a paragraph of code from Stack Overflow; now you can install that code with a package and you are in business.

There are two different ones we will be talking about today:

pip and conda

-----

## Pip

- TYPICALLY comes with your python install
- (often used) installs packages from PyPI (Python Package Index)
- manages wheels & sources (which you would then need to build the wheel from)
- installs only python type packages
- no built in environment. You need an existing environment to pull these packages to
- no dependency checks :(
- no gui :(

-----

## Conda

- does not come with python, will need to install as third party
- (often used) installs packages from Anaconda repo and cloud
- manages binaries
- installs far more than just python packages
- has environment baked into it (no need to make a virtualenv or venv)
- has dependency checks
- has Anaconda gui for ease of use



-----

These tools can be used in conjunction if you want; probably should use conda for the sake of this class though!