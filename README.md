# PwnedPy
![PyPI - License](https://img.shields.io/pypi/l/PwnedPy.svg)
A Python Wrapper for the Have I Been Pwned API

### Installation
```
pip3 install PwnedPy
```
### Initialisation
```
import PwnedPy
```
or
```
import PwnedPy as pp
```
### Functions

| Function | Optional Values | Required Values | Example | Output |
|----------|-----------------|--------|---------|-----------|
| getAllBreaches | domain | None | breaches = PwnedPy.getAllBreaches(domain="adobe.com")| JSON |
| getBreaches | Truncated and Unverified | account | breaches = pp.getBreaches("navanchauhan@gmail.com", Truncated=True, Unverified=True) | JSON |
| getBreachesByDomain | Truncated and Unverified | account and domain | breaches = PwnedPy.getBreachesByDomain("navanchauhan@gmail.com", domain="dubsmash.com") | JSON |
| getPastes | None | account | breaches = pp.getPastes("navanchauhan@gmail.com") | JSON |
