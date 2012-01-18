Hackercup solver framework
==========================

A simple framework which can make writing solvers to Facebook Hackercup problems a bit easier.

How to use
----------

To add a solver for a problem you should:

*  Create a python file `problemname.py` somewhere in the `problems` directory with the following functions: `solver` and
`fetcher`. The fetcher should have one input argument: an iterator of input file strings, it should read as many strings
as required for one task for given problem, preformat it and return all the data needed. The solver gets the fetcher's
output as input argument and should return the answer as a string or any object that can be formatted to a string.
*  Create a text file `input_problemname.txt` in the `input` directory as taken from the Hackercup problem site.
*  Run `python runner.py problemname` (it is possible to enter `problemname` in the command prompt).
*  See the result at `output/output_problemname.txt`

Notes
-----

The `problemname` string in the text above is an identifier to a task and should match for a solver and a corresponding
input file.

A `fetcher` function should not read more strings than it is required: iterators are not reversible.
