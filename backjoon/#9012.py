#9012

def is_vps(ps):
    stack = []
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:  # 스택이 비어 있는데 ')'를 만난 경우
                return "NO"
            stack.pop()
    if stack:  # 모든 문자를 처리한 후 스택에 여전히 요소가 남아 있는 경우
        return "NO"
    return "YES"

def main():
    T = int(input("Enter the number of test cases: "))
    results = []
    
    for _ in range(T):
        ps = input()
        results.append(is_vps(ps))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
