```
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('SOSА') # doctest: +ELLIPSIS
Expecting:
    Traceback (most recent call last):
    ...
    KeyError: 'А'
ok
2 items had no tests:
    test_doc_morse
    test_doc_morse.decode
1 items passed all tests:
   2 tests in test_doc_morse.encode
2 tests in 3 items.
2 passed and 0 failed.
Test passed.
```
