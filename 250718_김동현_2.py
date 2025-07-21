# 제품 납품시 납품 상자에 적재하는 최적화 알고리즘
# 우유를 업체에 납품할 때 입고 받은 우유를 납품 상자에 옮겨 담아야 할 때
# 납품 상자를 최소한으로 사용하도록 하는 최적화 알고리즘.
# 1리터 우유는 납품 상자 한개에 최대 40개 적재가 가능.
# 1리터 휘핑크림은 최대 40개가 가능하지만 작업 편의상 한 상자에 36개를 넣는 것이 편함.
# 납품 갯수가 꼭 40개를 가득 채워야 하는 상황이 아니라면 36개씩 적재하도록 함.
# 업체에서 나온 발주 수량을 입력 후에 납품 상자를 사용할 최적의 갯수를 출력해줌.



import math

# 납품 상자 용량 기준
BOX_SIZES = {
    "1L 우유": 40,
    "1L 휘핑크림": 36,  # 기본 36, 최대 40 허용
    "1L 멸균우유": 40,
    "200ml 우유": 120
}

# 발주 수량 입력
orders = {}
print("📋 품목별 발주 수량을 입력하세요:")
for product in BOX_SIZES:
    while True:
        try:
            qty = int(input(f"{product}: ").strip())
            orders[product] = qty
            break
        except ValueError:
            print("❗ 숫자를 입력해주세요.")

# 휘핑크림 최적 분배 (그리디 + 구성 출력)
def greedy_cream_detail(qty):
    best_config = None
    min_boxes = math.inf

    for count_40 in range(qty // 40 + 1):
        remain = qty - count_40 * 40
        if remain < 0:
            continue
        if remain % 36 == 0:
            count_36 = remain // 36
            total = count_36 + count_40
            if total < min_boxes:
                min_boxes = total
                best_config = (count_36, count_40)

    if best_config:
        count_36, count_40 = best_config
        # 출력 구성 만들기
        sizes = ["36"] * count_36 + ["40"] * count_40
        return min_boxes, " + ".join(sizes)

    # 36으로 나누기 불가 → 모두 40 기준
    num_boxes = math.ceil(qty / 40)
    sizes = []
    remaining = qty
    for _ in range(num_boxes - 1):
        sizes.append("40")
        remaining -= 40
    sizes.append(str(remaining))  # 마지막 박스
    return num_boxes, " + ".join(sizes)

# 일반 품목 납품 계산
def greedy_basic(qty, box_size):
    num_boxes = math.ceil(qty / box_size)
    return num_boxes, None

# 결과 출력
print("\n납품 상자 계산 결과:")
for product, qty in orders.items():
    if product == "1L 휘핑크림":
        num_boxes, config = greedy_cream_detail(qty)
        print(f"🔸 {product}: {qty}개 → {num_boxes} 상자 필요")
        print(f"   구성: {config}")
    else:
        box_size = BOX_SIZES[product]
        num_boxes, _ = greedy_basic(qty, box_size)
        print(f"{product}: {qty}개 → {num_boxes} 상자 필요")
