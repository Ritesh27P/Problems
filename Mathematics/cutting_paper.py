# Mary has an  piece of paper that she wants to cut into  pieces according to the following rules:

# She can only cut one piece of paper at a time, meaning she cannot fold the paper or layer already-cut pieces on top of one another.
# Each cut is a straight line from one side of the paper to the other side of the paper. For example, the diagram below depicts the three 
# possible ways to cut a  piece of paper:


def solve(n, m):
    # Write your code here
    return (n-1) + ((m-1)*n)