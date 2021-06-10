import math
import re
from collections import Counter

WORD = re.compile(r"\w+")


def get_cosine(text1, text2):
    words = WORD.findall(text1)
    vec1 = Counter(words)
    words = WORD.findall(text2)
    vec2 = Counter(words)
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator



# text1 = "DSP Bond Fund - IDCW"
# text2 = "DSP Bond Fund - Growth"

# cosine = get_cosine(text1, text2)

# print("Cosine:", cosine)