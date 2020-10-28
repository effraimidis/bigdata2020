def subset(arr):
    arr.sort(reverse=True)
    print(arr)
    i = len(arr) // 2
    j = 0
    B = arr[-i:]
    A = []
    A.append(arr[0])

    while i + j < len(arr) - 1:
        # print(A)
        # print(B)
        if sum(A) > sum(B):
            if len(arr) - 1 - (i + j) > 1:
                i += 1
                B.append(arr[-i])
            elif len(arr) - 1 - (i + j) == 1:
                if sum(A) > sum(B) + arr[-i-1]:
                    i += 1
                    B.append(arr[-i])
                else:
                    j += 1
                    A.append(arr[j])
        else:
            j += 1
            A.append(arr[j])

    print(A)
    print(B)


def subset1(arr):
    from itertools import permutations
    A = list(permutations(arr))
    matA = set()
    for i in range(len(arr) // 2):
        for a in A:
            if sum(a[:i+1]) > sum(a[i+1:]):
                matA.add((a[:i + 1], a[i + 1:]))
                # print(a)

    # print(matA)
    matA = list(matA)
    min = len(arr)
    for a in matA:
        if min > len(a[0]):
            min = len(a[0])
    max = 0
    idx = -1
    for i, a in enumerate(matA):
        if min == len(a[0]):
            if max < sum(a[0]):
                max = sum(a[0])
                idx = i

    print(matA[idx])

subset([3,7,5,6,2,2])
subset1([3,7,5,6,2,2])