import collections
from collections import Counter
import mapping as mapping
from numpy import iterable
cnt = collections.Counter([iterable or mapping])

y = "f"
while y == "f":
    z = 0
    x = input("Enter a text: ").replace(",", "").lower()
    x = x.replace("/", "")
    x = x.replace("+", "")
    x = x.replace(".", "")
    x = x.replace("%", "")
    x = x.replace("]", "")
    x = x.replace("(", "")
    x = x.replace(")", "")
    x = x.replace("]", "")
    x = ''.join((x for x in x if not x.isdigit()))
    x = x.split()
    x = [i for i in x if len(i) > 3 and len(i) < 100]

    choose = input("Choose a,b,c: ").lower()
    if choose == "a":
        counter = Counter(x).most_common(5)
        print(counter)
    elif choose == "b":
        print(sorted(set(x)))
    elif choose == "c":
        while z != 5:
            wrd = max(x, key=len)
            print(wrd)
            x.remove(wrd)
            z += 1

    y = input("Press 'f' to continue or another button to exit: ")
