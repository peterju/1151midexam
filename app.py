from pkg.book_tools import read_books, search_books, show_books, write_books


def input_text(prompt: str) -> str:
    """讀取非空白文字；prompt 為提示文字，回傳去除前後空白的內容。"""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print('不可空白，請重新輸入。')


def add_book(books: list) -> None:
    """讀取書籍資料並新增至 books；無回傳值。"""
    while True:
        book_id = input_text('請輸入書籍編號：')
        duplicate = False
        for book in books:
            if book['id'] == book_id:
                duplicate = True
                break
        if duplicate:
            print('書籍編號已存在，請重新輸入。')
        else:
            break

    title = input_text('請輸入書名：')
    author = input_text('請輸入作者：')
    while True:
        try:
            price = int(input('請輸入價格：').strip())
            if price > 0:
                break
        except ValueError:
            pass
        print('價格須為大於 0 的整數，請重新輸入。')

    books.append({
        'id': book_id,
        'title': title,
        'author': author,
        'price': price,
        'borrowed': False,
    })
    print('新增成功。')


def change_status(books: list) -> None:
    """依書籍編號切換 books 中的借閱狀態；無回傳值。"""
    book_id = input('請輸入書籍編號：').strip()
    for book in books:
        if book['id'] == book_id:
            book['borrowed'] = not book['borrowed']
            status = '已借出' if book['borrowed'] else '可借閱'
            print(f'「{book["title"]}」的狀態已變更為：{status}')
            return
    print('查無此書籍編號。')


def show_statistics(books: list) -> None:
    """顯示 books 最後三筆書籍與全部資料的統計；無回傳值。"""
    if not books:
        print('目前沒有書籍資料。')
        return

    print('\n--- 最後 3 筆書籍 ---')
    show_books(books[-3:])
    borrowed_count = 0
    total_price = 0
    for book in books:
        if book['borrowed']:
            borrowed_count += 1
        total_price += book['price']

    count = len(books)
    print('\n--- 書籍統計 ---')
    print(f'書籍總數：{count}')
    print(f'可借閱：{count - borrowed_count}')
    print(f'已借出：{borrowed_count}')
    print(f'價格合計：{total_price:,} 元')
    print(f'平均價格：{total_price / count:,.2f} 元')


def main() -> None:
    """讀取書籍資料並顯示主選單；無參數及回傳值。"""
    try:
        books = read_books('books.json')
    except FileNotFoundError:
        print('找不到 books.json，程式結束。')
        return
    except ValueError:
        print('books.json 格式錯誤，程式結束。')
        return
    except OSError:
        print('無法讀取 books.json，程式結束。')
        return

    while True:
        print('\n--- 簡易書籍管理系統 ---')
        print('1. 顯示全部書籍')
        print('2. 新增書籍')
        print('3. 查詢書籍')
        print('4. 變更借閱狀態')
        print('5. 顯示最後 3 筆書籍與統計')
        print('6. 匯出書籍資料')
        print('7. 離開系統')
        print('------------------------')
        choice = input('請選擇功能：').strip()

        if choice == '1':
            print('\n--- 全部書籍 ---')
            show_books(books)
        elif choice == '2':
            add_book(books)
        elif choice == '3':
            keyword = input_text('請輸入書名關鍵字：')
            results = search_books(books, keyword)
            if results:
                print('\n--- 查詢結果 ---')
                show_books(results)
            else:
                print('查無符合的書籍。')
        elif choice == '4':
            change_status(books)
        elif choice == '5':
            show_statistics(books)
        elif choice == '6':
            try:
                write_books(books, 'output.json')
            except OSError:
                print('無法匯出書籍資料。')
            else:
                print(f'已匯出 {len(books)} 筆書籍資料至 output.json。')
        elif choice == '7':
            print('系統已退出。')
            break
        else:
            print('選項錯誤，請重新選擇。')


main()
