import csv

with open("weather.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)


# 전체 관측
total = len(data)
# 비 온 날(건 수, 비율)
rainy_day = 0
for row in data:
    r = int(row["강수량"])
    if r > 0 :
        rainy_day +=  1
    else:
        continue
rainy_percent = (rainy_day / total) * 100


# 도시별 기온 정보
city_sum = {}
city_count = {}
hot_day = data[0]
hot_temp = int(data[0]["최고기온"])
for row in data:
    c = row["도시"]
    temp = int(row["최고기온"])
    # 도시 최고기온 합
    city_sum[c] = city_sum.get(c, 0) + temp
    city_count[c] = city_count.get(c, 0) + 1

    # 가장 더웠던 날
    if temp > hot_temp:
        hot_temp = temp
        hot_day = row
hot_city = hot_day["도시"]

# 도시별 평균 최고기온
city_avg_temp = {}
for c in city_sum:
    city_avg_temp[c] = city_sum[c] / city_count[c]


## 일교차가 가장 큰날
crazy_day = data[0]
crazy_temp = int(data[0]["최고기온"]) - int(data[0]["최저기온"])

for row in data:
    diff = int(row["최고기온"]) - int(row["최저기온"])
    if diff > crazy_temp:
        crazy_temp = diff
        crazy_day = row

crazy_city = crazy_day["도시"]
# 리포트 파일 저장
with open("report03.txt","w", encoding="utf-8") as f:
    f.write("=== 여름 날씨 분석 리포트 (2025.06 ~ 08) ===\n\n")

    f.write(f"[전체 관측] {total}건\n")
    f.write(f"[비 온 날] {rainy_day}건 ({rainy_percent:.1f}%)\n")

    f.write("\n[도시별 평균 최고기온]\n")
    for k,v in city_avg_temp.items():
        f.write(f"{k}: {v:.1f}℃\n")

    f.write("\n[분석결과]\n")
    f.write(f"가장 더웠던 날 : {hot_day["날짜"]} {hot_city} ({hot_temp}℃)\n")
    f.write(f"일교차가 가장 큰 날 : {crazy_day["날짜"]} {crazy_city} ({crazy_temp}℃)\n")

