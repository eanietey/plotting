import numpy as np

def num_letters(num_rows, num_columns):
    return 2*(num_rows-2)+(num_columns*2)
        


assert num_letters(3, 4) == 10
assert num_letters(6, 7) == 22
assert num_letters(6, 4) == 16
assert num_letters(4, 4) == 12
assert num_letters(13, 4) == 30

print("done")

data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')

words = []
num_rows, num_columns = data.shape

for r in range(num_rows):
    for c in range(num_columns):
        if data[r,c] == "":
            continue
        words.append(str(data[r,c]))
print(words)

assert len(words) == num_letters(num_rows, num_columns)
