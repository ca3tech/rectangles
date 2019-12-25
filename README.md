## Introduction

This is my solution to a supposed Google interview question. The
initial question posed was to calculate the number of rectangles
given a set of points where a rectangle is defined as consisting
only of verticle and horizontal lines. The follow up question
was to calcuate the number of rectangles when rectangles are not
restricted to just verticle and horizontal lines. I thought the
more general second question, with the added challenge of reporting
the vertices of the rectangles, would be an interesting challenge.
This is my solution to that problem.

## Solution

I chose to implement the solution in python. The rectangles.py
file contains the entire solution. I won't try and describe the
solution here, but rather refer you to the file itself. As you
will see there are 3 functions defined:

* num_rectangles
    * This reports the number of rectangles that can be formed
      given the input set of points.
* get_rectangles
    * This returns the vertices of all rectangles that can
      be formed given the input set of points. Each item of
      the list returned is a list of tuples where each tuple
      is one of the input points.
* print_rectangles
    * This will print the rectangles returned by the
      get_rectangles function.

To emperically determine the runtime complexity of the solution
I wrote the runtime.py script. If you run that script you will
see that the runtime is ultimately O(N^4), however, it is in
fact slightly more efficient.

Do you have a better solution? If so send me a link by adding
an issue to this repository.
