import csv
from unittest import result

with open("sales.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)

# 전체 매출
total = 0
for row in data:
    total += int(row["단가"]) * int(row["수량"])

# 메뉴별 판매량
qty_by_menu = {}
for row in data:
    x = row["메뉴"]
    y = row["수량"]
    qty_by_menu[x] = qty_by_menu.get(x, 0) + int(y)

# 카테고리별 매출
sales_by_category = {}
for row in data:
    x = row["카테고리"]
    y = row["수량"]
    z = row["단가"]
    sales_by_category[x] = sales_by_category.get(x, 0) + int(y) * int(z)

# 월별 매출
sales_by_month = {}
for row in data:
    k = row["날짜"][:7]
    result = int(row["수량"]) * int(row["단가"])
    sales_by_month[k] = sales_by_month.get(k,0)+result

# 분석결과
##가장 많이 팔린 메뉴(메뉴, 판매량)
best_menu = max(qty_by_menu, key=qty_by_menu.get)
best_menu_qty = qty_by_menu[best_menu]
##매출 1위 카테고리(카테고리, 매출)
num_one_category = max(sales_by_category, key=sales_by_category.get)
sales_num_one_category = sales_by_category[num_one_category]

# 리포트 파일 저장
with open("report01.txt","w", encoding="utf-8") as f:
    f.write("===== 파이빈 카페 매출 리포트 (2025.01 ~ 03) =====\n")

    f.write(f"\n[전체 매출] {total:,}원\n")

    f.write("[\n메뉴별 판매량]\n")
    for k,v in qty_by_menu.items():
        f.write(f"{k}: {v}잔\n")

    f.write("\n[카테고리별 매출]\n")
    for k,v in sales_by_category.items():
        f.write(f"{k}: {v:,}원\n")

    f.write("\n[월별 매출]\n")
    for k,v in sales_by_month.items():
        f.write(f"{k}: {v:,}원\n")

    f.write("\n[분석결과]\n")
    ##가장 많이 팔린 메뉴(메뉴, 판매량)
    f.write(f"가장 많이 팔린 메뉴: {best_menu} ({best_menu_qty}잔)\n")
    ##매출 1위 카테고리(카테고리, 매출)
    f.write(f"매출 1위 카테고리: {num_one_category} ({sales_num_one_category:,}원)\n")