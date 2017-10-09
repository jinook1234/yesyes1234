Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle as t #turtle을 t로 치환
>>> t.shape("turtle") #t의 모양을 turtle로
>>> t.bgcolor("black") #배경화면 색깔을 검정으로
>>> t.color("yellow") #t의 색깔을 노랑색으로
>>> 
>>> n=36
>>> for x in range(n): #x문을 n만큼 반복
	t.right(n)
	for y in range(5): #y문을 5번만큼 반복
		t.fd(400) #t를 400만큼 전진
		t.right(180-n) #t를 180-n각도만큼 회전

		
#별모양을 그린후 36도 돌려서 계속 같은 도형이 반복되게 하는 그림입니다!.
