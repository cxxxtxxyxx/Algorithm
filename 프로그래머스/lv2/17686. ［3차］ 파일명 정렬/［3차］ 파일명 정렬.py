"""
    파일명 영문자 시작, 숫자 하나 이상 포함 => 파일명 = HEAD + NUMBER + TAIL
    Head -> 숫자가 아닌 문자로 이루어져 있음 (알파벳 + 특수문자) = 최소 한 글자 이상
    Number -> 1 ~ 5사이의 연속된 숫자로 이루어져 있으며 앞쪽에 0이 올 수 있다. 00000, 00001 등도 가능
    Tail -> Head, Number 제외 나머지 부분, 다시 숫자 나타날 수 있으며 아무 글자도 없을 수 있음
    1. Head 부분을 기준으로 사전 순으로 정렬 (대소 구분 x) -> 비교할떄만 lower() 사용
    2. Number 숫자 순으로 정렬 (앞쪽에 0 무시) -> int() 사용
    3. Head 부분 같고 number도 같을 경우 주어진 순서 유지
    
    입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
    
    입력: ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
    출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
"""

import re
def solution(files):
    
    
    # step 1: 파일 명을 Head, Number, Tail로 분리하기
    # step 1-1: 처음 숫자 나오기 전까지가 헤드
    # step 1-2: 첫 번째 숫자 ~ 두 번째 숫자가 아닌 문자가 나오기 전까지가 넘버
    # step 1-3: 나머지가 테일
    # head = []
    # number = []
    # tail = []
    # headRegex = re.compile("\d+")
    # numberRegex = re.compile("[^\d]+")
    split_file = []

    for file in files:
        head = ''
        number = ''
        tail = ''
        number_check = False
        for ch in file:
            if not ch.isdigit() and number == '':
                head += ch
            elif not ch.isdigit() and number != '':
                tail += ch
            elif ch.isdigit() and tail == '':
                number += ch
            elif ch.isdigit() and tail != '':
                tail += ch
        split_file.append([head, number, tail])
        # print(headRegex.findall(file), numberRegex.findall(file))
        # number.append(headRegex.findall(file)[0])
        # head.append(numberRegex.findall(file)[0])
        # if len(numberRegex.findall(file)) == 1:
        #     tail.append("")
        # else:
        #     tail_start = file.rfind(numberRegex.findall(file)[1])
        #     tail.append(file[tail_start:])
        # head_idx = file.find(headRegex.findall(file)[0])
        # head.append(file[:head_idx])
        # if len(headRegex.findall(file)[0]) + head_idx == len(file):
        # # if len(headRegex.findall(file)[0]) + head_idx == len(file):
        #     tail.append("")
        #     number.append(file[head_idx:])
        #     continue
        # tail_idx = file.find(numberRegex.findall(file[int(file.find(headRegex.findall(file)[0])):])[0])
        # tail.append(file[tail_idx:])
        # number.append(file[head_idx:tail_idx])

    # for idx in range(len(head)):
    #     split_file.append([head[idx], number[idx], tail[idx]])
        
    print(split_file)
    
    # step 2: 조건에 맞게 안정정렬하기 (sorted 이용)
    return list(map(lambda x: ''.join(x), sorted(split_file, key=lambda x: (x[0].lower(), int(x[1])))))