# Built Function ex2

string = input()

cnt = 0
cnt1 = 0

for i in string:
    if i.isupper():
        cnt += 1
    if i.islower():
        cnt1 += 1

print(cnt)
print(cnt1)