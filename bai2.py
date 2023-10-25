
h = int(input("Nhập chiều cao của tam giác (h): ")

# Lặp qua các hàng của tam giác
for i in range(h):
    # In ra khoảng trống trước dấu '*'
    for j in range(h - i - 1):
        print("  ", end="")

    # In ra dấu '*' cho hàng hiện tại
    for j in range(2 * i + 1):
        print("* ", end="")

    # Xuống dòng để bắt đầu hàng mới
    print()

