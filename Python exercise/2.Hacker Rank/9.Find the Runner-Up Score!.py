score = int(input())
score_List = []
for x in range(score):
    score_List.append(input())

max_score = score_List[0]

for x in score_List:
    if max_score <= x:
        max_score = x

new_score_list = []

for y in score_List:
    if y == max_score:
        continue
    else:
        new_score_list.append(y)


second_max = new_score_list[0]
for z in new_score_list:
    if second_max <= z:
        second_max = z

print(second_max)
