![fake cookies](https://i.ibb.co/K9T27WZ/logobig.png)
---
### What is fake cookies?
Fake Cookies is a Python library that allows users to generate custom random strings. I got the idea when I found myself rewriting the same functions in many of my projects regarding http requests & API manipulation. Currently Fake Cookies has a few features such as generating random strings, generating random strings with a pattern (eg: aaa-aaaaa-aaa), and generating random mobile iOS device IDs. I'm planning on adding the ability to generate fake web headers and possibly some fake android device info.

## Documentation

### Generating random strings

To generate random strings, we can use the generate method. Here's an example:

```Python
from fakecookies import fcs

f= fcs()

f.generate(self, length=10, cbank="a0", amount=3)

>>> ['3di7vc8jfs', 'dw77v80uhh', 'zx4fb7wmdq']
```

The cbank is the variable that determines the characters will be in your string. "A0" will be capital letters and numbers, "a0" will be lowercase and numbers, "a" will be just lowercase, "A" will be just capital, and "0" will be just numbers.

### Generating random strings with a pattern

To generate random strings with a pattern we can use the genpattern method. Here's an example:

```Python
from fakecookies import fcs

f= fcs()

f.genpattern(cbank="a0", splitchar="-", pattern=[3,3,4,5], amount=1)

>>> 'ibn-po1-qf9d-9yts3'
```

The splitchar can be any string you'd like, this is what goes inbetween the different blocks of characters. The pattern is always a list, this is what sets the rule of the pattern.

### Generating iOS device identifiers

To generate an iOS device identifier/name, we can use the gendevice method. Here's an example:

```Python
from fakecookies import fcs

f= fcs()

f.gendevice(device="iPhone", amount=2)

>>> [{'id': 'iPhone5,1', 'name': 'iPhone 5 (GSM)'}, {'id': 'iPhone9,4', 'name': 'iPhone 7 Plus'}]
```

Currently, you can select from "iPhone", "Watch", "iPod", and "iPad" for the device argument. Special thanks to [adamawolf](https://gist.github.com/adamawolf/3048717) for the list of devices.

**If you're seeing this we're still in development so there may be missing information from this README file or the Python files in this repo. Use with caution!**
