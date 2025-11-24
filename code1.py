# code1.py
# シンプルな計算処理のチュートリアル用コード

def add_numbers(a, b):
    """2つの数値を足して返す"""
    return a + b

def main():
    print("=== code1.py 実行 ===")
    x = 10
    y = 20
    result = add_numbers(x, y)
    print(f"{x} + {y} = {result}")

if __name__ == "__main__":
    main()
