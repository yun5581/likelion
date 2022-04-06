# total_dictionary = {}

# while True:
#     Q = input('질문을 입력해주세요: ')
#     if Q == "q":
#         break
#     else:
#         total_dictionary[Q] = ""
# for i in total_dictionary:
#     print(i)
#     A = input("답변을 입력해주세요: ")
#     total_dictionary[i] = A
# print(total_dictionary)

total_list = []
while True:
    Q = input('질문을 입력해주세요: ')
    if Q == "q":
        break
    else:
        total_list.append({"질문" : Q, "답변" : ""})
for i in total_list:
    print(i["질문"])
    A = input("답변을 입력해주세요: ")
    i["답변"] = A
print(total_list)