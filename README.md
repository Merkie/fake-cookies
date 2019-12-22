![fake cookies](https://i.ibb.co/K9T27WZ/logobig.png)
---
### What is fake cookies?
Fake Cookies is a Python library that allows users to generate custom random strings. I got the idea when I found myself rewriting the same functions in many of my projects regarding http requests & API manipulation. Currently Fake Cookies has a few features such as generating random strings, generating random strings with a pattern (eg: aaa-aaaaa-aaa), and generating random mobile iOS device IDs. I'm planning on adding the ability to generate fake web headers and possibly some fake android device info.

## Documentation

**Generating random strings**

To generate random strings, we can use the generate method. Here's an example:

```Python
generate(self, length=10, cbank="a0", amount=3)

>>> ['3di7vc8jfs', 'dw77v80uhh', 'zx4fb7wmdq']
```

The cbank is the variable that determines the characters will be in your string. "A0" will be capital letters and numbers, "a0" will be lowercase and numbers, "a" will be just lowercase, "A" will be just capital, and "0" will be just numbers.

**If you're seeing this we're still in development so there may be missing information from this README file or the Python files in this repo. Use with caution!**
