def primeSum(N):
    sum = 0  # cummulative sum
    for i in range(2, N+1):
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            sum += i
    return sum


if __name__ == "__main__":
    T = int(input())
    lys = []  # empty list

    for i in range(T):
        new = int(input())
        lys.append(new) # add new item to list
    
    for i in range(len(lys)):
        print(primeSum(lys[i]))  # Runs function and prints the sum of each list item



