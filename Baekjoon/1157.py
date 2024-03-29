ord_s = input().upper()
set_s = list(set(ord_s))
cnt_s = [ord_s.count(i) for i in set_s]

if cnt_s.count(max(cnt_s)) >= 2:
    print('?')
else:
    print(set_s[cnt_s.index(max(cnt_s))])