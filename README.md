# dot-dict

A dictionary that's recursively navigable with dots, not brackets.

### Installation with Poetry
```bash
git clone https://github.com/kirisakow/dot-dict.git

cd dot-dict

poetry install
```
```bash
cd your-project

poetry add --editable ../rel/path/to/dot-dict/

poetry install
```

### Usage examples:
```py
from dot_dict.dot_dict import DotDict

d = {'key1': 'value1',
     'key2': 'value2',
     'key3': {'key3a': 'value3a'},
     'key4': {'key4a': [{'key4aa': 'value4aa',
                         'key4ab': 'value4ab',
                         'key4ac': 'value4ac'}],
              'key4b': 'value4b'}}

dd = DotDict(d)
print(dd.key4.key4a[0].key4aa)  # value4aa

dd.key4.key4a[0].key4aa = 'newval'
print(dd.key4.key4a[0].key4aa)  # newval

print(dd.key4.key4a[0].key4aaa) # AttributeError: attribute .key4aaa not found

DotDict({}) # OK
DotDict()   # AttributeError: DotDict must be instantiated with a dictionary, not a NoneType.
```
Source: https://stackoverflow.com/questions/22161876/python-getattr-and-setattr-with-self-dict/75561249#75561249