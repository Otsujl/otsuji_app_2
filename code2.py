# code2.py
# 簡単なリスト処理とファイル書き込みの例

def write_fruits(filename):
    """果物リストをファイルに書き込む"""
    fruits = ["apple", "banana", "orange", "grape"]

    with open(filename, "w") as f:
        for fruit in fruits:
            f.write(fruit + "\n")

def main():
    print("=== code2.py 実行 ===")
    filename = "fruits.txt"
    write_fruits(filename)
    print(f"{filename} に果物リストを書き込みました！")

if __name__ == "__main__":
    main()
