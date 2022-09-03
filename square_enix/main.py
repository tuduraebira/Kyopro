import datetime
import sys


records = []
for s in sys.stdin:
    t, d = s.rstrip().split()
    t_list = t.split(':')
    tmp = t_list.pop().split('.')
    t_list += tmp
    #print(t_list)


    if len(t_list[0]) != 2 or len(t_list[1]) != 2 or len(t_list[2]) != 2 or len(t_list[3]) != 3:
        #print(-1)
        exit()

    if float(d) < 0 or float(d) >= 100:
        #print(-2)
        exit()

    records.append([t, d])

#print(records)

price = 0
dist_meter = 0
lowspeed_time_meter = 0
price_meter = 0

for i, l in enumerate(records):
    t, d = l[0], l[1]
    hh, mm, ss_fff = t.split(':')
    ss, fff = ss_fff.split('.')
    dist = float(d)

    # 距離メーター
    if dist > 0:
        pdist_meter = dist_meter
        dist_meter += dist

    # 低速走行時間メーター
    dt = datetime.datetime(year=2000, month=1, day=1, hour=int(hh), minute=int(mm), second=int(ss), microsecond=int(fff))
    if i != 0:
        phh, pmm, pss_fff = records[i - 1][0].split(':')
        pss, pfff = pss_fff.split('.')
        pdt = datetime.datetime(year=2000, month=1, day=1, hour=int(phh), minute=int(pmm), second=int(pss), microsecond=int(pfff))
        
        tsa = dt - pdt

        if (dist / 1000) / (tsa.total_seconds() / (60 * 60)) <= 10:
            lowspeed_time_meter += tsa.total_seconds()

    # 運賃メーター
    if dist_meter <= 1000:
        price = 400
    elif dist_meter <= 10000:
        if (dist_meter - 1000) % 400 != (pdist_meter - 1000) % 400:
            if 0 <= hh % 24 and hh % 24 < 6:
                price += 60
            elif 6 <= hh % 24 and (hh % 24 <= 9 and mm < 30):
                price += 52
            elif 20 <= hh % 24 and hh % 24 <= 24:
                price += 52
            else:
                price += 40
    else:
        if (dist_meter - 1000) % 350 != (pdist_meter - 1000) % 350:
            if 0 <= hh % 24 and hh % 24 < 6:
                price += 60
            elif 6 <= hh % 24 and (hh % 24 <= 9 and mm < 30):
                price += 52
            elif 20 <= hh % 24 and hh % 24 <= 24:
                price += 52
            else:
                price += 40

    if 0 <= hh % 24 and hh % 24 < 6:
        price += (lowspeed_time_meter // 45) * 60
    elif 6 <= hh % 24 and (hh % 24 <= 9 and mm < 30):
        price += (lowspeed_time_meter // 45) * 52
    elif 20 <= hh % 24 and hh % 24 <= 24:
        price += (lowspeed_time_meter // 45) * 52
    else:
        price += (lowspeed_time_meter // 45) * 40

print(price)
