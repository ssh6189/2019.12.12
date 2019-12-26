from collections import Counter

print("알파벳으로 된 단어나 문장을 입력하시오.")
sentence = str(input())
counter = Counter(sentence)
print(max(sentence, key=counter.get))
