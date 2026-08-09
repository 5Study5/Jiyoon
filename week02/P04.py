def solution(word):
    answer = 0
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []

    def dfs(current):
        if len(current) > 5:
            return

        if current != '':
            words.append(current)

        for vowel in vowels:
            dfs(current + vowel)

    dfs('')
    
    answer = words.index(word) + 1
    return answer