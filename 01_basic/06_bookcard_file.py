import json

# bookcard = [['353535','데스티니', '한길출판사','2005년'],
# ['245232','삼국지','길벗출판사','2013년'],
# ['198959','나의연인','한국출판사','2019년']]

bookcard = []

with open('01_basic/bookcard.data','r') as f:
      bookcard = json.load(f)
      
while True:
    menu = input('''
--------------------------------------------
1.저장 2.수정 3.삭제 4.리스트 5. 검색 6.종료(E)    
---------------------------------------------   
>>>''')
    if menu == '1':
        while True:
            number = input('일련번호를 입력하세요>>>')
            check = 0
            for item in bookcard:
                if item['number'] == number:
                    check = 1
            if check ==0:
                break
            print('중복되는 일련번호가 있습니다.')

        name = input('책이름을 입력하세요>>>')
        publisher = input('출판사를 입력하세요>>>')
        year = input('출간년을 입력하세요>>>')
        bookcard.append({'number':number,'name':name,'publisher':publisher,'year':year})
        print(bookcard)


    elif menu == '2':
        number = input('수정할 데이터 일련번호')
        idx = -1
        for i, item in enumerate(bookcard):
            if item['number'] == number:
                idx = i

                while True:
                    update = input('수정할정보 - name, publisher,year,exit(종료)>>>')
                    if update in ('name','publisher','year'):
                       bookcard[idx][update] = input(f'{update}수정내용>>>')
                    elif update == 'exit':
                       break
                print(bookcard[idx])
                break
        if idx == -1:
            print('등록되지 않은 데이터입니다.')

    elif menu == '3':
        number = input('삭제할 이름 입력 >>>')
        delok = 0
        for i, item in enumerate(bookcard):
            if item['number'] == number :
                print(item, 'delete!')
                del bookcard[i]
                delok = 1
                break
            if delok == 0:
                print('등록되지 않은 데이터입니다.')

    elif menu == '4':
        for item in bookcard:
            print(f'''
   --------------------------------
   일련번호 :{item['number']}
   책 이 름 :{item['name']}
   출 판 사 :{item['publisher']}
   출 간 일 :{item['year']}''')

    elif menu == '5':
        number = input('검색할일련번호>>>')
        idx = -1
        for i, item in enumerate(bookcard):
            if item['number'] == number:
                idx = i
                print(item[i])
                break
        if idx == -1:
            print('등록되지 않은 데이터 입니다.')

    elif menu in ('6'):
        print('프로그램종료')
        break
    else:
        print('메뉴선택을 잘못하셨습니다.')

with open('01_basic/bookcard.data','w') as f:
    json.dump(bookcard,f, indent=2)
    

