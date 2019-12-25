## Introduction

This is my solution to a supposed Google interview question. The
initial question posed was to calculate the number of rectangles
given a set of points where a rectangle is defined of consisting
only of verticle and horizontal lines. The follow up question
was to calcuate the number of rectangles when rectangles are not
restricted to just verticle and horizontal lines. I thought the
more general second question, with the added challenge of reporting
the vertices of the rectangles, would be an interesting challenge.
This is my solution to that problem.

## Solution

I chose to implement the solution in python. The rectangles.py
file contains the entire solution. I wrote the runtime.py script
to emperically determine the runtime complexity of the solution.
If you run that script you will see that the runtime is ultimately
O(N^4), however, it is in fact slightly more efficient.

Do you have a better solution? If so send me a link by adding
an issue to this repository.
