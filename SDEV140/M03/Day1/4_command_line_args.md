# Command Line Args

In most programming languages, there ia the ability to 
get command line arguments.

Here is what it looks like:

`
python program.py arg1 arg2
`


In python, we can get those arguments like this:

```python
import sys


program_name = sys.argv[0]
arg1 = sys.argv[1]
arg2 = sys.argv[2]
```













