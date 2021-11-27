```Trying:
    decode('... --- ...')
Expecting:
    'SOS'
ok
Trying:
    decode('/')# doctest: +ELLIPSIS
Expecting:
    Traceback (most recent call last):
    ...
    KeyError: '/'
ok
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
1 items had no tests:
    test_doc_morse
2 items passed all tests:
   2 tests in test_doc_morse.decode
   2 tests in test_doc_morse.encode
4 tests in 3 items.
4 passed and 0 failed.
Test passed.
PS C:\Users\Владислав\PycharmProjects\pythonProject>  python -m doctest -v -o NORMALIZE_WHITESPACE test_doc_morse.py
Trying:
    decode('... --- ...')
Expecting:
    'SOS'
ok
Trying:
    decode('/')# doctest: +ELLIPSIS
Expecting:
    Traceback (most recent call last):
    ...
    KeyError: '/'
ok
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
1 items had no tests:
    test_doc_morse
2 items passed all tests:
   2 tests in test_doc_morse.decode
   2 tests in test_doc_morse.encode
4 tests in 3 items.
4 passed and 0 failed.
Test passed.
```
