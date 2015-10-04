import sys
sys.setrecursionlimit(300000)


def ackermann(m, n):
    """
    The Ackermann function can be defined using this recurrence:
    A(m,n) =
            {
                n+1 if m = 0
                A(m-1,1) if m > 0 and n=0
                A(m-1, A(m,n-1)) if m > 0 and n > 0
            }
    where m and n are non-negative integers
    Can most machines handle this recurrence once m and n grow even a little? IDK.
    (My experience indicates: no)
    """
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ackermann(m-1, 1)
    elif m > 0 and n > 0:
        return ackermann(m-1, ackermann(m, n-1))

if __name__ == '__main__':
    ret = ackermann(2, 3)
    print ret
    # Warning! This crashes.
    ret = ackermann(4, 1)
    print ret
