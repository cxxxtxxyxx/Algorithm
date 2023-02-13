import copy
def solution(new_id):
    answer = new_id.lower()
    length = len(answer)
    ban = "~!@#$%^&*()=+[{]}:?,<>/"
    while True:
        cnt = 0
        length = len(answer)
        for i in range(length):
            if answer[i] in ban:
                answer = copy.deepcopy(answer[:i]) + copy.deepcopy(answer[i+1:])

                cnt += 1
                break
        if cnt == 0:
            break
    


    while answer.find('..') != -1:
        start = answer.find('..')
        flag = False

        cnt = 0
        end = start
        for i in range(answer.find('..'), len(answer)):
            if answer[i] != '.':
                end = i
                answer = copy.deepcopy(answer[:start] + '.' + answer[end:])
                flag = True
                cnt = 0
                break
            if answer[i] == '.':
                cnt += 1
        
        if cnt != 0:
            end = len(answer) - 1
            answer = copy.deepcopy(answer[:start]) + '.'

    
    if answer.find('.') == 0:
        answer = copy.deepcopy(answer[1:])

    if answer.find('.') == len(answer) - 1:
        answer = copy.deepcopy(answer[:len(answer)])

    
    if answer == '':
        answer += 'a'

    if len(answer) >= 16:
        answer = copy.deepcopy(answer[:15])
    
    if answer[len(answer) - 1] == '.':
        answer = copy.deepcopy(answer[:len(answer) - 1])

    if len(answer) <= 2:
        tmp = answer[-1]
        while len(answer) != 3:
            answer += tmp



        
        

    return answer

"""
규칙 x => 입력 유사 아이디 + 규칙 맞는 아이디 추천

아이디 길이 3자 이상 15자 이하
아이디는 알파벳 소문자, 숫자, 빼기, 밑줄(_) 마침표(.) 만 사용 가능
마침표는 처음과 끝에 사용할 수 없으며 연속으로 사용 불기

1단계: 모든 대문자 => 소문자로 치환
2단계: 해당에서 대응되는 문자 뺴고 모두 제거
3단계: 마침표 2번 이상 => 하나로 치환
4단계: 마침표가 처음이나 끝 => 제거
5단계: 빈 문자열 => new id에 a를 대입
6단계: 길이 16자 이상 => 첫 15개 문자 제외 나머지 문자 모두 제거
        - 만약 제거 후 마침표가 끝에 위치한다면 끝에 위치한 마침표 제거
7단계: newid 2자 이하라면 new id의 마지막 문자를 길이가 3이 될 때 가지 계속 붙임
"""

# result = "bat.y.abcdefghi"
print(solution("...!@BaT#*..y.abcdefghijklm"))

# result = "z--"
print(solution("z-+.^."))

# result = "aaa"
print(solution("=.="))

# result = "123_.def"
print(solution("123_.def"))

# result = "abcdefghijklmn"
print(solution("abcdefghijklmn.p"))