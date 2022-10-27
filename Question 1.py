### <span style="color:red">Question 1:</span> (5 pts)
Following `hw1_1`, input an integer n>2.
Print a hollow diamond of size n.   
This diamond has double `*` boundary.

<span style="color:green"> <b>Examples:</b></span>
```
>>> hollow_diamond(7)
      *
     ***
    ** **
   **   **
  **     **
 **       **
**         **
 **       **
  **     **
   **   **
    ** **
     ***
      *

>>> hollow_diamond(3)
  *
 ***
** **
 ***
  *
```


"""Solution"""

def hollow_diamond(n):
    for i in range(2*n-1):
        i = i if i<n else 2*n-2-i
        if i == 0:
            print(" "*(n-1)+"*"+" "*(n-1))
        elif i == 1:
            print(" "*(n-2)+"***"+" "*(n-2))
        else:
            print(" "*(n-1-i)+"**"+ " "*(2*i-3)+"**"+" "*(n-1-i))
