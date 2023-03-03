import bookcard as nc
import pickle

bookclip = None

with open ('01_basic/bookclip.pickle','rb') as f:
    bookclip = pickle.load(f)
while True:
    menu = input('''
-------------------------------------------------------------------------
1.Bookclip생성 2.Bookclip추가 3.삭제 4.내용보기 5.전체목록보기 6.종료  
--------------------------------------------------------------------------   
>>>''')
    if menu == '1': 
        if bookclip == None:
            bookclip = nc.Bookclip(input('일련번호를 입력하세요>>>'))
        else:
            print('생성된 Bookclip이 존재합니다. ') 
    elif menu == '2':
        if bookclip ==None:
            print('Bookclip 생성후 추가 가능합니다') 
        else:
            number = input('number>>>')
            name = input('name>>>')
            publisher = input('publisher>>>')
            year = input('year>>>')
            bookcard = nc.Bookcard(number,name,publisher,year)
            bookclip.add_bookcard(bookcard)

    elif menu == '3':
        if bookclip == None:
            print('bookclip 생성한 후 가능합니다.')
        else:
            print(list(bookclip.bookcard.keys()))
            page = int(input('page number >>> '))
            bookcard = bookclip.remove_bookcard(page)
            print(bookcard, '-> 삭제')

    elif menu == '4':
        if bookclip == None:
            print('bookclip 생성한 후 가능합니다.')
        else:
            print(list(bookclip.bookcard.keys()))
            page = int(input('page number >>> '))
            bookcard = bookclip.bookcard[page]
            print(bookcard)
    elif menu == '5':
        if bookclip == None:
            print('bookcards 생성한 후 가능합니다.')
        else:
            key = input('정렬 키(입력값:number,name,publisher,year) >>>')
            sort = bool(input('오름차순(enter),내림차순(1) >>>'))
            # print(sort,type(sort))
            if key in ('number','name','publisher','year'):
                bookclip.list_bookcard(key,sort)
            else:
                bookclip.list_bookcard(reverse=sort)

    elif menu == '6':
        print('프로그램 종료')
        break

with open ('01_basic/bookclip.pickle','wb') as f:
    pickle.dump(bookclip,f)
