# Packages

If modules are the individual files within a project, 
then packages are the folders, because that is what they are.

A package is a subdirectory in python.

# How to use

- have directory with .py files in it
- import them with 'from <package> import <module>'
- use things by doing `<module>.<thing_from_module>`


## BIG NOTE:

IF your python version is < 3.3, you will need to include a file called `__init__.py` 
in your directory/folder/package for python recognize it as a package.


# Namespace Packages

As longs as the python files are contained in directories with the same name, they
can exist in two different directories and still be imported your project the same
as if they were in the same directory.


