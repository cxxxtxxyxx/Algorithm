import sys

input = sys.stdin.readline

START = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
QUESTION = '"재귀함수가 뭔가요?"'
STORY_1 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
STORY_2 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
STORY_3 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
CONDITION = '"재귀함수는 자기 자신을 호출하는 함수라네"'
END = "라고 답변하였지."
SEPARATOR = "____"

n = int(input().strip())

def recursive(recur_count):
    if recur_count == n:
        print(SEPARATOR * recur_count + QUESTION)
        print(SEPARATOR * recur_count + CONDITION)
        print(SEPARATOR * recur_count + END)
        return
    
    print(SEPARATOR * recur_count + QUESTION)
    print(SEPARATOR * recur_count + STORY_1)
    print(SEPARATOR * recur_count +  STORY_2)
    print(SEPARATOR * recur_count +  STORY_3)
    recursive(recur_count + 1)
    print(SEPARATOR * recur_count + END)
    

print(START)
recursive(0)