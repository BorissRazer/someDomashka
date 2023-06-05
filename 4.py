some = [1,2,5,6,7,8]
is_uniq = 0
for i in range(len(some)):
    counter = 0
    for j in range(i+1, len(some)):
        if some[i] == some[j]:
            counter += 1
    if counter > 0:
        print("число", some[i], "не уникально и встречается ", counter+1, "раз")
        is_uniq = 1
if is_uniq == 0:
    print("список уникален")
else:
    print("ряд не уникален")