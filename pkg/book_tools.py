import json


def read_books(file_name: str) -> list:
    """讀取 file_name 指定的 JSON 檔案，回傳書籍資料串列。"""
    # JSON 陣列會轉為 list，陣列中的物件會轉為 dict。
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_books(books: list, file_name: str) -> None:
    """將書籍資料 books 寫入 file_name 指定的 JSON 檔案；無回傳值。"""
    # 保留中文並縮排，讓匯出的 JSON 容易閱讀。
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def search_books(books: list, keyword: str) -> list:
    """從 books 中查詢書名包含 keyword 的書籍，回傳符合條件的串列。"""
    # 比對時統一轉成小寫，再用列表推導式找出符合的書籍。
    keyword = keyword.lower()
    return [book for book in books if keyword in book['title'].lower()]


def show_books(books: list) -> None:
    """顯示書籍資料 books；books 為空時顯示提示，無回傳值。"""
    if not books:
        print('目前沒有書籍資料。')
        return

    print('編號  書籍編號  書名  作者  價格  狀態')
    # 從 1 開始編號，並用條件表達式決定借閱狀態。
    for number, book in enumerate(books, 1):
        status = '已借出' if book['borrowed'] else '可借閱'
        print(f'{number:>4}  {book["id"]}  {book["title"]}  '
              f'{book["author"]}  {book["price"]:>7,}  {status}')
