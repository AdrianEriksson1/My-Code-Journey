A = [5, 1, 3, 2, 4] # Program to sort an list/array, Make it!
def sorting(list):
    for i in range(0, len(list) - 1):
        for u in range(i + 1, len(list)):
            if list[u] < list[i]:
                list[i], list[u] = list[u], list[i]
    print(list)           
sorting(A)
