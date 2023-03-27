while 1:
	try:
    		N, S = map(int, input().split())
    #문제 조건에 텍스트 파일로부터 데이터를 읽어온다고 했기에
    #파일이 마지막에 도달했을 때 발생하는 EOFError를 처리해줘야함
	except EOFError:
    		break
	else:
    		print(S // (N + 1))