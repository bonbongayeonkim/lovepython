import bookcardfunc as cf

# bookcard = [['353535','데스티니', '한길출판사','2005년'],
# ['245232','삼국지','길벗출판사','2013년'],
# ['198959','나의연인','한국출판사','2019년']]

bookcard = []
bookcard = cf.dataload(bookcard)

while True:
    menu = input('''
--------------------------------------------
1.저장 2.수정 3.삭제 4.리스트 5. 검색 6.종료(Q)    
---------------------------------------------   
>>>''')
    if menu == '1':
       cf.save(bookcard)

    elif menu == '2':
       cf.update(bookcard)

    elif menu =='3':
       cf.delete(bookcard)

    elif menu =='4':
        cf.cardlist(bookcard)

    elif menu =='5':
        cf.search(bookcard)
        
    elif menu in ('6'):  
        print('프로그램종료')
        break
    else:
        print('메뉴선택을 잘못하셨습니다.')
        
cf.datasave(bookcard)

        

       


