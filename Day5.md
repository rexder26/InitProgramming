# 📌 Day-5: Linux Core Utilities.

## Linux Commands can be combined and make a powerfull scripts. BASH programming language helps to make athe scripts on linux.

> ## 1) Simple Cryptography by [**tr**] command
    tr means text replace, this command used to replace some letters with another word, like the ROT encodes.
```bash
    cat yourtext.txt | tr 'A-Za-z' 'B-Zb-z'
```
> ## 2) Finding a specific text from a folder.
    grep can help us here.
    grep have an option called recursive( -r )
```bash
    ls path | grep -r "TEXT"
```
> ## 3) Changing a filename with a sequenced textx.
```bash
    for i in *; mv $i 00i%
```

