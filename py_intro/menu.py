import time
import random

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
while True:
    print(lunch)
    item = input("음식을 추가해주세요: ")
    if (item == 'q'):
        break
    else:
        lunch.append(item)
print(lunch)
set_lunch = set(lunch)
while True:
    print(set_lunch)
    item = input("음식을 삭제해주세요: ")
    if item == 'q':
        break
    else: 
        set_lunch = set_lunch - set([item])

print(set_lunch,"중에서 선택합니다.")
for i in range (1,6):
    print(i)
    time.sleep(1)
print(random.choice(list(set_lunch)))
 