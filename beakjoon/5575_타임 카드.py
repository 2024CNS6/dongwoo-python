for i in range(3):
    s_h, s_m, s_s, e_h, e_m, e_s = map(int, input().split())
    w_h=e_h-s_h
    w_m=e_m-s_m
    w_s=e_s-s_s
    if w_s<0:
        w_s=60+w_s
        w_m-=1
    if w_m<0:
        w_m=60+w_m
        w_h-=1
    print(w_h,w_m,w_s)