# Jeffrey Romero
# GitHub: jeff-romero

# def permute1(s=[], j=0, n=0):
#     if j == n:
#         if s[0] != 'l' and s[3] != 'l' and s[4] == 'e':
#             permutation = ''.join(s)
#             results.append(permutation)
#     else:
#         for i in range(j, n):
#             s[j], s[i] = s[i], s[j]
#             permute1(s, j + 1, n)
#             s[j], s[i] = s[i], s[j]

def permute2(permutation, topermute, positions):
    if (len(permutation) == len(topermute)):
        for ele in permutation:
            print(ele, end=' ')
        print('\n')
    else:
        for i in range(0, len(topermute)):
            if (positions[i]):
                continue
            positions[i] = True
            permutation.append(topermute[i])

            permute2(permutation, topermute, positions)

            permutation.pop()
            positions[i] = False


# FOR TESTING
# permutation = []
# topermute = ['a', 'b', 'c']
# positions = [False] * len(topermute)

# print('Permuting:', topermute)
# permute2(permutation, topermute, positions)
