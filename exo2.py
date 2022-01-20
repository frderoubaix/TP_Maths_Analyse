def diffdiv(xi, yi):
    a_result = []
    for i in range(0, xi.__len__() - 2):
        for j in range(0, xi.__len__() - 2):
            a_result.append((yi[j] - yi[j + 1]) / (xi[j] - xi[j + 1]))
    return a_result


print([-1, 0, 1].__len__())
print(diffdiv([-1, 0, 1], [1, 1, 3]))
