def mirror_sum_1(a:list, b:list) -> list:
    return [a[i] + b[len(a)-i-1] for i in range(len(a))];

def mirror_sum_2(a:list, b:list) -> list:
    return [u + v for u,v in zip(a,reversed(b))];

#ДОБАВЛЕНИЕ ИНФОРМАЦИ
Содержание отчета
1. Цель работы.
2. Назначения GitHub.
3. Созданный аккаунт на GitHub с календарем активностей