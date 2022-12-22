# Write a function to calculate the value of  𝑒  (mathematical constant) using the following formula. 
# The input of this function n is the upper bound of k. i.e., if n=4, then use k=0,1,2,3,4 to approximate.

# 𝑒=∑𝑘=0∞1𝑛!
# $$ e = \sum_{k=0}^{\infty} \frac{1}{n!} $$
 
# >>> print(q1(10))
# 2.7182815255731922
# >>> print(q1(4))
# 2.6666666666666665

def factorial(k):
    return 1 if k==0 else k*factorial(k-1)
def q1(n):
    aa = 0
    for i in range(n+1):
        aa += 1/factorial(i)
    return aa

print(q1(10))
print(q1(4))