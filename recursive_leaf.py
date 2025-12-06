############################ Part A
from turtle import *

def draw_leaf_straight(recursion_level, length):
    def branch(length, depth):
        """One branch only"""
        if depth == 0:
            return 
        else:
            forward(length)
            branch(length/2, depth-1)  # forward
            backward(length*1/3)
            left(45)
            branch(length/(5/2), depth-1)  # left side 
            right(90)
            branch(length/(5/2), depth-1)  # right side 
            left(45)
            backward(length*2/3)
    

    branch(length, recursion_level)
    
clearscreen()
speed(0)
tracer(0)
left(90)  # Make it vertical
width(0.1)
draw_leaf_straight(6, 120)
update()
done()

########################################Part B
def strB(n, base=10):
    if n == 0:
        return '0'
    
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Recursive case
    if n < base:
        return digits[n]
    else:
        return strB(n // base, base) + digits[n % base]

def testif(condition):
    return bool(condition)

def test_strB():

    result = strB(123, 10)
    assert testif(result == "123"), f"Failed: base 10 test, expected '123', got '{result}'"
    
    result = strB(123, 16)
    assert testif(result == "7B"), f"Failed: base 16 test, expected '7B', got '{result}'"
    
    result = strB(10, 2)
    assert testif(result == "1010"), f"Failed: base 2 test, expected '1010', got '{result}'"
    
    result = strB(0, 10)
    assert testif(result == "0"), f"Failed: zero test, expected '0', got '{result}'"
    
    print("All test_strB tests passed!")

test_strB()
print(strB(7,2))
print(strB(523,6))
print(strB(322,7))

###################### Part C
cnk_dict = {}

cnk_dict[(0, 0)] = 1
for i in range(100):
    cnk_dict[(i, 0)] = 1
    cnk_dict[(i, i)] = 1

def Cnk_m(n, k):
    if (n, k) not in cnk_dict:
        cnk_dict[(n, k)] = Cnk_m(n-1, k-1) + Cnk_m(n-1, k)
    
    return cnk_dict[(n, k)]

def testif(condition):
    return bool(condition)

def test_Cnk_m():
    print("Testing binomial coefficients:\n")
    
    assert testif(Cnk_m(5, 2) == 10), "Failed: C(5, 2)"
    print("PASS: C(5, 2) = 10")
    
    assert testif(Cnk_m(10, 3) == 120), "Failed: C(10, 3)"
    print("PASS: C(10, 3) = 120")
    
    assert testif(Cnk_m(6, 0) == 1), "Failed: C(6, 0)"
    print("PASS: C(6, 0) = 1")
    
    assert testif(Cnk_m(7, 3) == 35), "Failed: C(7, 3)"
    print("PASS: C(7, 3) = 35")
    
    print("\nAll tests passed!")

def run_Cnk():
    print("Computing binomial coefficients with memoization:")
    
    test_cases = [
        (5, 2),
        (10, 3),
        (20, 10),
        (30, 15),
        (50, 25)
    ]
    
    for n, k in test_cases:
        result = Cnk_m(n, k)
        print(f"C({n:2d}, {k:2d}) = {result:,}")


if __name__ == "__main__":
    test_Cnk_m()
    run_Cnk()


## Part D

def make_pairs(seq1, seq2, acc=None):
    if acc is None:
        acc = []
    
    if len(seq1) == 0 or len(seq2) == 0:
        return acc
    
    return make_pairs(seq1[1:], seq2[1:], acc + [(seq1[0], seq2[0])])


def testif(condition):
    return bool(condition)


# Unit tests
def test_make_pairs():
    print("Testing make_pairs function:\n")
    
    result = make_pairs([1,2,3], [4,5,6])
    assert testif(result == [(1, 4), (2, 5), (3, 6)]), \
        f"Test 1 Failed: Expected [(1, 4), (2, 5), (3, 6)], Got {result}"
    print("PASS: Test 1 - Equal length lists")
    
    result = make_pairs([1,2,3], [4,5])
    assert testif(result == [(1, 4), (2, 5)]), \
        f"Test 2 Failed: Expected [(1, 4), (2, 5)], Got {result}"
    print("PASS: Test 2 - First list longer, stops at shorter")
    
    result = make_pairs([1,2,3], [4,5,6,7,8,9])
    assert testif(result == [(1, 4), (2, 5), (3, 6)]), \
        f"Test 3 Failed: Expected [(1, 4), (2, 5), (3, 6)], Got {result}"
    print("PASS: Test 3 - Second list longer, stops at shorter")
    
    result = make_pairs([], [4,5,6,7,8,9])
    assert testif(result == []), \
        f"Test 4 Failed: Expected [], Got {result}"
    print("PASS: Test 4 - Empty first list")
    
    result = make_pairs([1,2,3], [])
    assert testif(result == []), \
        f"Test 5 Failed: Expected [], Got {result}"
    print("PASS: Test 5 - Empty second list")
    
    print("\nAll 5 tests passed!")

test_make_pairs()


