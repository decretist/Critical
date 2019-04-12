## Notes

vim regular expression to remove all text inside anonymous block
tags (non-greedy).
```
:g/<ab>\_.\{-}<\/ab>/s//<ab><\/ab>/gp
```
