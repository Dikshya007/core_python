"""
The while loop is also called a loop, but it is considered more dangerous than a for loop because it can lead to infinite loops if the condition never becomes false.
Therefore, Python recommends using it less frequently and ensuring the condition in the loop is correctly managed to avoid such issues.
"""

i=1
while i<10:
    print(i)
    i += 1