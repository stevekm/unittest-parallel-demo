# Python `unittest` parallel test execution demo

The standard library `unittest` framework in Python lacks the ability to execute tests in parallel.

To get around this limitation, we use the included script `print_tests.py` to print the list of tests to stdout, then pipe that to `xargs` for parallel execution with `python -m unittest`.

Note that since each test cases is being executed individually, this could have implications for any complex setup or teardown directives used in your tests, or the initialization or usage of shared resources between tests. Your mileage may vary.

When used successfully, this technique can drastically reduce test execution time.

## Why?

There are alternative testing frameworks in Python that already support parallel execution, among other features.

One of the primary advantages to the methods shown here is that `unittest` is in the Python standard library and is available by default on all systems with Python installed. Thus external dependencies (and by extension, dependency management systems) are not needed in order to use it. Most systems that have `bash` installed will likely have `xargs` available either already or with an easy installation.

# Usage

Using the `tests` dir as input, the script lists all tests found in the directory

```
$ ./print_tests.py tests/
tests.test_bar.TestBar.test_bar_1
tests.test_bar.TestBar.test_bar_2
tests.test_bar.TestBar.test_bar_3
tests.test_bar.TestBar.test_bar_4
tests.test_bar.TestBar.test_bar_5
tests.test_bar.TestBar.test_bar_6
tests.test_baz.TestBaz.test_baz_1
tests.test_baz.TestBaz.test_baz_2
tests.test_baz.TestBaz.test_baz_3
tests.test_baz.TestBaz.test_baz_4
tests.test_baz.TestBaz.test_baz_5
tests.test_baz.TestBaz.test_baz_6
tests.test_foo.TestFoo.test_foo_1
tests.test_foo.TestFoo.test_foo_2
tests.test_foo.TestFoo.test_foo_3
tests.test_foo.TestFoo.test_foo_4
tests.test_foo.TestFoo.test_foo_5
tests.test_foo.TestFoo.test_foo_6
```

You can optionally supply only a single test file

```
$ ./print_tests.py tests/test_foo.py
tests.test_foo.TestFoo.test_foo_1
tests.test_foo.TestFoo.test_foo_2
tests.test_foo.TestFoo.test_foo_3
tests.test_foo.TestFoo.test_foo_4
tests.test_foo.TestFoo.test_foo_5
tests.test_foo.TestFoo.test_foo_6
```

Note that if you ran all tests using the "normal" method, which executes sequentially, it will take a long time

```
$ python -m unittest discover tests/

>>> starting test: TestBaz.test_baz_1

>>> stopping test: TestBaz.test_baz_1 (0:00:05.004537)
.

...
...
...

----------------------------------------------------------------------
Ran 18 tests in 90.041s

OK
```

However the `print_tests.py` script is designed to be piped to `xargs` for parallel execution as shown

```
$ time ./print_tests.py tests/ | xargs -n 1 -P 8 python3 -m unittest

>>> starting test: TestBar.test_bar_1

>>> starting test: TestBar.test_bar_2

>>> starting test: TestBar.test_bar_5

>>> starting test: TestBar.test_bar_3

>>> starting test: TestBar.test_bar_4

>>> starting test: TestBar.test_bar_6

>>> starting test: TestBaz.test_baz_2

>>> starting test: TestBaz.test_baz_1

...
...
...

>>> stopping test: TestFoo.test_foo_5 (0:00:05.005108)
.
----------------------------------------------------------------------
Ran 1 test in 5.006s

OK

>>> stopping test: TestFoo.test_foo_6 (0:00:05.002082)
.
----------------------------------------------------------------------
Ran 1 test in 5.002s

OK

real	0m15.575s
user	0m1.963s
sys	0m0.604s
```

(you can omit the `time` usage if you dont need it)

As you can see, execution of all demo test cases dropped from 90s to 15s thanks to running 8 tests at once in parallel. This technique can be expanded upon to suite other testing needs.
