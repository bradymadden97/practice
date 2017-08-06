# Arrays: Left Rotation
# Cracking the Coding Interview Challenge
# https://www.hackerrank.com/challenges/ctci-array-left-rotation

def array_left_rotation(a, n, k):
    # Initialize
    answer, rotations, count = [], k, 0
    
    # Begin new array from point in old array
    while rotations < len(a):
        answer.append(a[rotations])
        rotations += 1
        
    # Circle back to front of old array
    while count < k:
        answer.append(a[count])
        count += 1
    return answer


# -------------- Provided --------------

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
