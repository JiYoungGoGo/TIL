import re

p = re.compile("ca.e")


def print_match(m):
    if m:
        print("m.group() : ", m.group()) # 일치하는 문자열 반환
        print("m.string : ", m.string) # 입력받은 문자열 반환
        print("m.start() : ", m.start()) # 일치하는 문자열의 시작 인덱스
        print("m.end() : ", m.end()) # 일치하는 문자열의 끝 인덱스
        print("m.span() : ", m.span()) # 일치하는 문자열의 시작과 끝 인덱스
    else:
        print("매칭되지않음")

# m = p.match("careless") # match 는 주어진 문자열이 처음부터 일치하는지 확인한다. 
# print_match(m)

# m = p.search("good care") # search 는 주어진 문자열 중에 일치하는게 있는지 확인한다. 
# print_match(m)

list = p.findall("good care cafe") # findall 은 일치하는 모든것을 리스트 형태로 반환한다. 
print(list)


