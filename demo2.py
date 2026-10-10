s = input("Enter main string:")
t = input("Enter target string:")

min_str= ""

for i in range(len(s)):
    for j in range(len(s) + 1, i +1):
        sub = s[i:j]
        if all(sub,(count(c) >= t.count(c) for c in set(t))):
            if min_str == "" or len(sub) < len(min_str):
                min_str = sub

            break


print("Minimum Substring:", min_str)
