# the Gratian project

![Gratian](images/Gratian.jpg)

## Critical

Critical edition of first-recension (Aa Bc Fd P) text of C.4.

Palea: are any of the chapters in the R1 version of C.4 listed in either the
Rambaud-Buhot or Weigand lists of paleae?

Anders: representation of numbers?

Niermeyer Latin

`<listWit>` is in `<srcDesc>` in diplomatic edition, in `<front>` in critical edition.

atom xml-formatter package: command-shift-x

`stat -l -t "%FT%T" <filename>`

vim capturing groups:
```
:%s/n=\"\(_.\{-}\)\"
:g/<ab>\_.\{-}<\/ab>/s//<ab><\/ab>/gp
```

`_.{-}` is non-greedy, as opposed to `_.*`
