def gkatn(a):
    for i in range(2, a):
        if a%i==0:
           return 0
    return 1
      

wjdtn=int(input("정수를 입력하시오. : "))
a=gkatn(wjdtn)

if a==0:
    print(wjdtn,"는 소수가 아닙니다.", sep="") #wjdtn와 문자열을 띄어쓰기 없이 출력하기 위해, sep=""을 넣어줬다.(+는 안 되니까)
else:
    print(wjdtn,"는 소수입니다.", sep="") #wjdtn와 문자열을 띄어쓰기 없이 출력하기 위해, sep=""을 넣어줬다.(+는 안 되니까)
