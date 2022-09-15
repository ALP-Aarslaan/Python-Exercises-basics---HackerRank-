list1 = [[input(), float(input())] for _ in range(int(input()))]
# # for sublist in list1:
# #     sublist[1:] = sorted(sublist[1:], reverse=True)
# print(sublist)
l1 = []
l2 = []
i = 0
while i < len(list1):
    print(list1[i][1])
    l1.append(list1[i][1])
    i = i+1
l1.sort()
print(l1)
j = 0
while j < len(list1):
    print(list1[j][0])
    l2.append(list1[j][0])
    j = j + 1
l2.sort()
print(l2)
minNum = min(l1)
l1.remove(minNum)
print(l1)
secondMin = min(l1)
print(secondMin)
# l3 = []
# k = 0
# while k < len(list1):
#     if list1[k][1] == secondMin:
#         l3.append((list1[k][0]))
#     k = k+1 
# l3.sort(key=str.lower)
# h = 0
# while h < len(l3):
#     print(l3[h])
#     h = h+1
k = 0
while k < len(list1):
    if list1[k][1] == secondMin:
        print(list1[k][0])
    k = k+1
# list1 = [[input(), float(input())] for _ in range(int(input()))]
# for sublist in list1:
#     sublist[1:] = sorted(sublist[1:], reverse=True)

# l1 = []
# l2 = []
# i = 0
# while i < len(list1):
#     l1.append(list1[i][1])
#     i = i+1
# l1.sort()
# j = 0
# while j < len(list1):
#     l2.append(list1[j][0])
#     j = j + 1
# l2.sort()
# minNum = min(l1)
# l1.remove(minNum)
# secondMin = min(l1)
# k = 0
# while k < len(list1):
#     if list1[k][1] == secondMin:
#         print(list1[k][0])
#     k = k+1 