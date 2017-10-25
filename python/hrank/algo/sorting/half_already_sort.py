



def mysort(A, p, n):
    result = []
    i = 0
    j = p

    while i < p and j < n:
        if A[i] < A[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(A[j])
            j += 1

    while i < p:
        result.append(A[i])
        i += 1

    while j < n:
        result.append(A[j])
        j += 1
    return result




def main():
    A = [3,4,7,9,13,1,5,6,8]
    B = mysort(A, 5, len(A))
    

    A = [3,1,2,3,4,5,6]
    B = mysort(A, 1, len(A))
    
    A = [1,2,3,4,5,6,2]
    B = mysort(A, 6, len(A))

    print B


if __name__ == '__main__':
    main()

