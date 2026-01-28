# 1
s = "python string manipulation"
words = s.split()
camel = words[0]
for w in words[1:]:
    camel += w.capitalize()
print(camel)


# 2
s = "python is easy and python is powerful"
freq = {}
for word in s.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)


# 3
s = "Hello World Python"
caps = ""
for ch in s:
    if ch.isupper():
        caps += ch
print(caps)


# 4
s = "aaabbcddd"
result = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1
result += s[-1] + str(count)
print(result)


# 5
s1 = "listen"
s2 = "silent"
print(sorted(s1) == sorted(s2))
