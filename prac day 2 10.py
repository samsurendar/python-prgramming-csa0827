def remove_common_words(sentence1, sentence2):
    words1 = sentence1.split()
    words2 = sentence2.split()

    set1 = set(words1)
    set2 = set(words2)

    common_words = set1.intersection(set2)

    words1_without_common = [word for word in words1 if word not in common_words]
    words2_without_common = [word for word in words2 if word not in common_words]

    sentence1_without_common = ' '.join(words1_without_common)
    sentence2_without_common = ' '.join(words2_without_common)

    return sentence1_without_common, sentence2_without_common

sentence1 = "2024 cm of andhara pradesh"
sentence2 = "pspk"

result1, result2 = remove_common_words(sentence1, sentence2)
print("2024 cm of andhara pradesh:", result1)
print("pspk:", result2)
