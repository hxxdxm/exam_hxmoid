import csv

with open("loans.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
    
# 총 대출 건수
total = len(data)
# 평균 대출일수
total_days = 0
for row in data:
    total_days += int(row["대출일수"])
    avg_days = total_days / total

# 분야별 대출 건수
loans_by_genre = {}
for row in data:
    x = row["분야"]
    loans_by_genre[x] = loans_by_genre.get(x, 0) + 1

# 대출자 유형별
loans_by_user = {}
for row in data:
    k = row["대출자유형"]
    loans_by_user[k] = loans_by_user.get(k, 0) + 1

# 월별 대출 건수
loans_by_month = {}
for row in data:
    m = row["대출일"][:7]
    loans_by_month[m] = loans_by_month.get(m, 0) + 1

# 분석 결과
## 최다 대출 도서
qty_by_book = {}
for row in data:
    b = row["도서명"]
    qty_by_book[b] = qty_by_book.get(b, 0) + 1

best_book = max(qty_by_book, key=qty_by_book.get)
best_book_loan = qty_by_book[best_book]

## 인기 분야
best_genre = max(loans_by_genre, key=loans_by_genre.get)
best_user_loan = loans_by_genre[best_genre]

# 리포트 파일 저장
with open("report02.txt","w", encoding="utf-8") as f:
    f.write("=== 한빛도서관 대출 리포트 (2025.03 ~ 05) ===\n\n")

    f.write(f"[총 대출 건수] {total}건\n")
    f.write(f"[평균 대출일수] {avg_days:.1f}일\n")

    f.write("[\n분야별 대출 건수]\n")
    for k,v in loans_by_genre.items():
        f.write(f"{k}: {v}건\n")

    f.write("\n[대출자 유형별]\n")
    for k,v in loans_by_user.items():
        f.write(f"{k}: {v}건\n")

    f.write("\n[월별 대출 건수]\n")
    for k, v in loans_by_month.items():
        f.write(f"{k}: {v}건\n")

    f.write("\n[분석결과]\n")
    ##가장 많이 팔린 메뉴(메뉴, 판매량)
    f.write(f"최다 대출 도서: {best_book} ({best_book_loan}건)\n")
    #매출 1위 카테고리(카테고리, 매출)
    f.write(f"인기 분야 1위: {best_genre} ({best_user_loan}건)\n")