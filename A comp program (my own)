

pairs = [60, 13, 40, 10, 8, 6, 25, 3, 1, 18]

def find_fence(array):
    stack = sorted(array)
    total_pairs = 0
    able_pairs = [[] for _ in range(len(array) // 2)] # Makes empty "[]" for the pairs to go in
    u = 0

    for i in range(len(array) // 2):
        if len(stack) % 2 == 1: # To ensure that the highest possible values of the pairs, if it were odd then it would end up with a pair with low values and in the end, 1 left over value in the middle which could have been used intead
            stack.pop(0)
        if stack[0] * stack[-1] >= 100: 
            able_pairs[u].append(stack[0]) # Adds both the values to the first empty "[]"
            able_pairs[u].append(stack[-1]) # Adds both the values to the first empty "[]"
            stack.pop(0)
            stack.pop(-1)
            total_pairs += 1
            u += 1
        else:
            stack.pop(0)

    able_pairs = [sublist for sublist in able_pairs if sublist] # Removes any empty "[]" that are not used in the end (just for looks)
            

    print(f"Total pairs: {total_pairs}  \nPossible pairs: {able_pairs}")


find_fence(pairs)

