import re
from collections import Counter
from nltk.corpus import stopwords

with open('random_paragraphs.txt', 'r') as file:
    text = file.read()

text = re.sub(r'[^\w\s]', '', text).lower()

stop_words = set(stopwords.words('english'))
words = text.split()
filtered_words = [word for word in words if word not in stop_words]

word_freq = Counter(filtered_words)

for word, freq in word_freq.items():
    print(f'{word}: {freq}')
