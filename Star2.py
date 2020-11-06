# Loops

for i in range(int(input())):
    print(i * i)

# Write a function

def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
year = int(input())
print(is_leap(year))

# Print Function

for i in range(1, int(input()) + 1):
    print(i, end='')

# List Comprehensions

x, y, z, n = [int(input()) for _ in range(4)]
listOfAnswers = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(listOfAnswers)

# Find the Runner-Up Score!

n = int(input())
arr = list(map(int, input().split()))
print(max([x for x in arr if x != max(arr)]))

# Nested Lists

def secondLowestGrade(classList):
    secondLowestScore = sorted(set(_[1] for _ in classList))[1]
    result = sorted([_[0] for _ in classList if _[1] == secondLowestScore])
    return result


numberOfStudents = int(input())
classList = []
for i in range(numberOfStudents):
    classList.append([str(input()), float(input())])
print('\n'.join(secondLowestGrade(classList)))

def readScores(listOfStudents):
    line = list(input().split())
    avScore = sum(map(float, line[1:])) / 3
    name = line[0]
    listOfStudents[name] = avScore

# Finding the percentage

n = int(input())
listOfStudents = dict()
for i in range(n):
    readScores(listOfStudents)
print('%.2f' % listOfStudents[input()])