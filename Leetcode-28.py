if __name__ == "__main__":
    haystack = input()
    needle = input()
    n = len(needle)
    for i in range(len(haystack)):
        if haystack[i:n] == needle:
            print(i)
        else: n+=1
    print(-1)