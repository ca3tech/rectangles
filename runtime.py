import math
import statistics as stats
import rectangles as r

def points(n : int):
    # Create a rectangular grid of n points
    nx = 2
    ny = int(n / nx)
    while ny > nx:
        nx += 1
        ny = int(n / nx)
    p = []
    for i in range(0, nx):
        for j in range(0, ny):
            p.append((i, j))
    return p

def print_graph(yxdict : dict, ymax : int):
    xmax = 0
    ys = range(1, ymax+1)
    for y in reversed(ys):
        s = "{:>2}-|".format(y)
        if y in yxdict:
            x = yxdict[y]
            s += "".join(["  " for i in range(1, x)])
            s += "* "
            if x > xmax:
                xmax = x
        print(s)
    xr = range(1, xmax+1)
    print("   |"+"".join(["--" for x in xr]))
    print("    "+"".join(["| " for x in xr]))
    xs = "    "
    for x in xr:
        l = " "
        if x % 5 == 0:
            l = x
        xs += "{:<2}".format(l)
    print(xs)

def main():
    npts = [4, 6, 9, 12, 16, 20, 25, 30, 36, 42]
    rtt = []
    slopes = []
    for n in npts:
        g = r.graph(points(n))
        g.get_rectangles()
        # Find the exponent of N
        e = int(math.log10(g.operations) / math.log10(n))
        # What is the multiplier of N^e
        m = g.operations / (n**e)
        rtt.append((n, e, m))
        slopes.append(m / n)
    mm = {}
    mmymax = 0
    # Print out N, runtime exponent of N, and the multiple of
    # the exponent of N calculated above
    print("n\texp\tmultiple")
    for t in rtt:
        print("\t".join([f"{_}" for _ in t]))
        y = round(t[2])
        mm[y] = t[0]
        if y > mmymax:
            mmymax = y
    # Print out a graph of the multiple value versus N to
    # determine if there is a relationship
    print()
    print("multiple by n")
    print_graph(mm, mmymax)
    # From the graph above it was clear that the multiple of N^e is a
    # linear function of N so here I calculate the mean slope for
    # informational purpose before printing the final runtime of
    # N^(e+1)
    avs = stats.mean(slopes)
    print()
    print(f"Runtime: O(N^{rtt[0][1]} * {avs:.2f}N) => O(N^{rtt[0][1]+1})")
    
if __name__ == "__main__":
    main()