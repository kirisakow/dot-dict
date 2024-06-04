class DotDict(dict):
    """A dictionary that's recursively navigable with dots, not brackets.

Usage examples:

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
DotDict({}) # AttributeError: DotDict must be instantiated with a non-empty dictionary.
DotDict()   # AttributeError: DotDict must be instantiated with a non-empty dictionary.

Source: https://stackoverflow.com/questions/22161876/python-getattr-and-setattr-with-self-dict/75561249#75561249
"""

    def __init__(self, data: dict = None):
        if data is None or not isinstance(data, dict):
            raise AttributeError(f"{type(self).__name__} must be instantiated with a dictionary, not a {type(data).__name__}.")
        for key, value in data.items():
            if isinstance(value, list):
                self[key] = [DotDict(item) for item in value]
            elif isinstance(value, dict):
                self[key] = DotDict(value)
            else:
                self[key] = value

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as exc:
            raise AttributeError(f"attribute .{key} not found") from exc
