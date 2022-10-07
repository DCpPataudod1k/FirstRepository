def mirror_sum_1(a:list, b:list) -> list:
    return [a[i] + b[len(a)-i-1] for i in range(len(a))];

def mirror_sum_2(a:list, b:list) -> list:
    return [u + v for u,v in zip(a,reversed(b))];