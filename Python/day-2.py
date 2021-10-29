#문자열을 입력받아 해당 문자열을 출력 및 길이 출력하라

input_str = input("문자를 입력하시오.\n")

print("입력한 문자 : ",input_str,"\n" ,"길이 : ",len(input_str))

"문자 입력".format()

# format : {}에 값을 대입함
print("{}".format(10))
print("{}{}{}".format(10,'test',20))

print("입력받은 문자 : {}\n문자열의 길이는 : {}".format(input_str,len(input_str)))

# 정수 자릿수 지정하기
num_1 = 52
print("{:d}".format(num_1))       
print("{:5d}".format(num_1))      
print("{:5d}".format(num_1*-1)) 
print("{:05d}".format(num_1))    
print("{:05d}".format(num_1*-1))

#부호 붙이기(빈공간으로 작성 시 부호는 마이너스만 표시됨.)
print("{:+d}".format(num_1))
print("{:+d}".format(num_1*-1))
print("{:d}".format(num_1))
print("{:d}".format(num_1*-1))

#조합하기
print("{:+5d}".format(num_1))
print("{:+5d}".format(num_1*-1))
print("{:=+5d}".format(num_1))
print("{:=+5d}".format(num_1*-1))
print("{:+05d}".format(num_1))
print("{:+05d}".format(num_1*-1))


#부동 소수점 출력 {:f}

num_f = 52.273
print("{:f}".format(num_f))
print("{:15f}".format(num_f))#전체 표현하는  자리수가 15자리
print("{:+15f}".format(num_f))
print("{:015f}".format(num_f))

#소수점 미만 표현 자리수 지정
print("{:15.3f}".format(num_f)) #전체 표현 자리수는 15, 소수점 미만 3자리.

#의미없는 소수점 미만 제거 확인
print("{:g}".format(10.0))# 10을 출력 {:g}는 의미없는 소수점 제거하는 함수

#upper(), lower(), strip()

str_a = ' Hello World !! '
print(str_a.upper()) #전 문자 대문자
print(str_a.lower()) #전 문자 소문자
print('/',str_a.strip(),'/') #양쪽 공백 제거
print('/',str_a.lstrip(),'/') #왼쪽 공백 제거
print('/',str_a.rstrip(),'/') #오른쪽 공백 제거;

#소문자 바꿔서 공백 제거 받는 게 문자열이면 계속해서 문자열 함수 붙여쓰는 것 가능
str_a.strip().lower().upper()

#문자열 구성 파악하기 is함수명()
print("Translate".isalnum())
print("10".isdigit())
print("import".isidentifier())

# find(), rfind() : 찾고자하는 문자열의 위치 반환
input_str = "asdf hellohello python" # 처음 나오는 hello를 추출해서 출력
start_p = input_str.find("hello") #처음 hello가  나오는 index 반환
end_p = input_str.rfind("hello") #뒤에서부터 검색해서 처음 나오는 index 반환

print("시작 위치 : {}, 마지막 위치 : {}, {}".format(start_p, end_p,
                                           input_str[start_p:end_p]))

#마지막 위치의 hello부터 뒤에 있는 문자 모두 출력
print(input_str[end_p:])

#키보드에서  공백 포함 문자열을 입력받아 처음 공백이 나오는 위치까지의 문자만 출력

str_o = input("공백 포함해서 작성하시오\n")
str_g = str_o.find(" ")
print(str_o[:str_g].upper())

# 문자열 자르기  문자열.split()

# a_str = "10 20 30 40 test abcd"
# print(a_str.split())

# b_str = "10,20,30,40,test,abcd"
# print(b_str.split(","))

#키보드로부터 데이터를 입력받아 공백으로 데이터를 분리하고
#2번째 입력된 자료를 출력하세요.
#abcd test c 10 30 => b를 출력하시오.
split_tr = input("단어를 작성하시오\n")
split_t= split_tr.split()
print(split_tr,'\t 2번째 입력 자료 : ', split_t[1])

(',' in "10,20,30,40,test")

# and, or, not, ==,!=,>,<,<=,>=
a = 10; b = 20
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)

#and
print(a == 10 and b== 20)
print(a != 10 and b== 20)
print(a == 10 and b!= 20)
print(a != 10 and b!= 20)

#or
print(a == 10 or b== 20)
print(a != 10 or b== 20)
print(a == 10 or b!= 20)
print(a != 10 or b!= 20)

#not

print(not(a != 10 or b!= 20))

#if 조건식 :
#    들여쓰기
if True:
    print("if 문장 실행")
    
if False:
    print("if false 실행") #실행되지 않음
    
# 정수를 입력받아 10보다 작으면 입력된 값 출력
input_s = input("숫자를 입력하시오")
if input_s.isdecimal():
    input_s = int(input_s)
    if input_s <10:
        print(input_s)



#숫자를 입력받아 실수로 변환한 후
#0보다 크면 양수, 0보다 작으면 음수, 0이면 'zero'를 출려하세요.
input_e = input("숫자 입력")
if input_e.isdecimal:
    input_e = float(input_e)
if input_e> 0:
    print("양수")
if input_e<0:
    print("음수")
if not input_e:
    print("zero")

#날짜 시간 관련 함수를 사용하기 위해서 datetime 모듈 가져오기
import datetime

now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

# 정수 입력 받아 짝수인지 확인
input_p = input("정수 입력\n")
last_p = input_p[-1] # 마지막 글자를 가져온다.
last_l = int(last_p)
if last_l == 0 or last_l == 2 or last_l == 4\
  or last_l == 6 or last_l == 8:
    print("짝수입니다.")
if last_l == 1 or last_l == 3 or last_l == 5\
  or last_l == 7 or last_l == 9:
    print("홀수입니다.")
    
#int로 형변화 후 2로 나눈 나머지 값이 0이면 짝수, 1이면 홀수
input_p1 = int(input("숫자적기"))
if not input_p1%2:
    print("짝수입니다.")
if input_p1%2:
    print("홀수입니다.") 
    
#in 연산자를 활용하여 처리
if last_p in "02468":
    print("짝수입니다.")
if last_p in "13579":
    print("홀수입니다.")

# 1. 두 개의 숫자를 입력받아 작은 수 부터 출력
# 2. 작은 수와 큰 수가 3의 배수인지 확인

input_q = input("숫자 작성\n")
input_k1 = input_q.split()
input_1 = int(input_k1[0])
input_2 = int(input_k1[1])
if input_1>input_2:
    print("작은 수 : {}, 큰 수 : {}".format(input_2,input_1))
else:
    print("작은 수 : {}, 큰 수 : {}".format(input_1,input_2))
if input_1%3 == 0:
    print("{}은(는) 3의 배수입니다.".format(input_1))
else:
    print("{}은(는) 3의 배수가 아닙니다.".format(input_1))
if input_2%3 == 0:
    print("{}은(는) 3의 배수입니다.".format(input_2))
else:
    print("{}은(는) 3의 배수가 아닙니다.".format(input_2))

#정수를 입력받아 90 이상이면 'A', 80 이상이면 'B', 70이상이면 'C' 그 외 'D'
#elif는 위의 if 문이 만족하지 않았을 때 elif 조건을 확인하는 함수이다.
input_number = int(input("점수 입력"))

if input_number>=90:
    print("A")
elif input_number>=80:
    print("B")
elif input_number>=70:
    print("C")
else:
    print("D")


# 날짜함수에서 월을 추출해서 현재 월이 봄인지, 가을인지 출력
# 1~3월은 봄, 4~6여름 7~9은 가을 10~12월은 겨울이라고 출력
#if~elif~...else 사용
# import datetime

now = datetime.datetime.now()#<= 년 월 일 시 분 초 전부
# #now = datetime.date.today() <= 년 월 일 만
# now = int(input("달을 입력하시오.\n"))


if 0< now.month <=3:
    print("현재는 봄입니다.")
elif 3<now.month<=6:
    print("현재는 여름입니다.")
elif 6<now.month<=9:
    print("현재는 가을입니다.")
elif 9<now.month<=12:
    print("현재는 겨울입니다.")
else:
    print("잘못된 입력입니다.")

# if 0< now <=3:
#     print("현재는 봄입니다.")
# elif 3<now<=6:
#     print("현재는 여름입니다.")
# elif 6<now<=9:
#     print("현재는 가을입니다.")
# elif 9<now<=12:
#     print("현재는 겨울입니다.")
# else:
#     print("잘못된 입력입니다.")

# 숫자 부호 숫자를 입력받아 게산하는 프로그램 작성
# 10+20, 10-20, 부호는 +,-,*,/ 를 입력하세요.
input_t = input("계산식을  작성하시오.\n")

num_1 = int(input_t.split()[0])
util = input_t.split()[1]
num_2 = int(input_t.split()[2])

if util == '+':
    print("{} {} {} = {}".format(num_1,util,num_2,num_1+num_2))
elif util == '-':
    print("{} {} {} = {}".format(num_1,util,num_2,num_1-num_2))
elif util == '*':
    print("{} {} {} = {}".format(num_1,util,num_2,num_1*num_2))
elif util == '/':
    print("{} {} {} = {}".format(num_1,util,num_2,int(num_1/num_2)))
else :
    print("잘못된 부호입니다.")

# list 여러개의 데이터 집합 변수명 = [,,...,]
# +, *, len() 리스트의 갯수
# list.append(요소), list.insert(위치, 요소), list.extend(리스트) 리스트 연결
a_list = [1,2,3]
b_list = ['a','b','c']
print(a_list+b_list)
print(a_list*3)

c_list = a_list+b_list
print("a_list 갯수 : {}, b_list 갯수 : {}, c_list 갯수 : {}".format(len(a_list),len(b_list),len(c_list)))

a_list.append(b_list)
print(a_list)
# a_list의 'a'를 출력
print(a_list[3][0])

a_list.insert(1,c_list) #a_list의 1 인데스 위치에 c_lisst 추가
a_list

# a_list = [1, 2, 3], b_list = ["test", "abcd"]
#a_list에 b_list를 추가하세요.

a_list = [1,2,3]; b_list = ["test", "abcd"]
a_list.extend(b_list)
print(a_list)

#a_list에 b_list를 append로 추가하세요.

a_list.append(b_list)
print(a_list)

#추가된 a_list에서 "abcd"를 출력 하세요.-> index를 이용하여.

print(a_list[5][1])

#b_list에서 "test" 앞에 "name"을 추가하세요.

b_list.insert(0,"name")
print(b_list)

#a_list의 두 번째 요소를 'change'로 변경하세요.

a_list[1] = "change"
print(a_list)

대입 연산자
a = 10 좌측 변수에 우측의 값을 입력
비교 연산자
a == b a와 b의 값을 비교 true or false로 반환

문자 또는 문자열
a = '10 test' <- 문자=> a[0] : 1, a[1] : 0, a[-1] : t a[3:5] : te (3위치는 포함. 5는 포함 안함.)
                
num = 10 숫자

리스트[]
a_list = [1,2,'test', [1, 'a', 'b']]
a_list[0] : 1 a_list[-1] = [1,'a','b'], a_list[-1][1] = 'a'

a_list[2:4] = 'test', [1,'a','b']

a_list.append(요소), a_list.insert(위치, 요소)
a_list[1] = 'abcd' : 1의 값이 'abcd'로 변경됨.
a_list.extend(리스트) : 리스트 병합


