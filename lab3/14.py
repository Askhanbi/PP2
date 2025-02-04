# Functions 1    Task 3

def foo(head,legs):
    if head > legs or legs % 2 != 0 or head == 0:
        print("No solution")
    else:
        x = int((legs - 2 * head) / 2)
        y = int(head - x)
        print(x, y)

HEADS = int(input("Count head: "))
LEGS = int (input("Count legs: "))
foo(HEADS, LEGS)
