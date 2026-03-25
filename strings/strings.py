# Check the X string is in y or not
x = "s"
y = "abcsde"

found = False

for ch in y:
    if ch == x:
        found = True

print(found)

#check substring is part of main string or not
s = "abx"
t = "ahbgdc"
i = 0

for ch in t:
    if i == len(s):
        break
    if ch == s[i]:
        i += 1

print(i == len(s))