import numpy as np
corpus = open("alice.txt")
words_corpus = []
for l in corpus:
    for w in l.split(" "):
        words_corpus.append(" "+w+" ")
first_char = {}
counts = {}
for w in words_corpus:
    for i in range(len(w)-1):
        if w[i] not in counts:
            counts[w[i]] = 0
        counts[w[i]]=counts[w[i]]+1
        if(w[i] in first_char):
            if(w[i+1] in first_char[w[i]]):
                first_char[w[i]][w[i+1]]= first_char[w[i]][w[i+1]] +1
            else:
                first_char[w[i]][w[i+1]] = 1
        else :
            first_char[w[i]] = {}
            first_char[w[i]][w[i+1]]=1
for c1 in first_char:
    for c2 in first_char[c1]:
        first_char[c1][c2] = first_char[c1][c2]/counts[c1]
#generating random words

for i in range(10):

    word = ""
    generated_char = np.random.choice(a=list(first_char[' '].keys()),p=[first_char[' '][c] for c in first_char[' ']])

    while(generated_char!=' '):

        word += generated_char
        generated_char =  np.random.choice(a=list(first_char[generated_char].keys()),p=[first_char[generated_char][c] for c in first_char[generated_char]])
    print(word)

#generating ten fairly low info content words
i = 0
while i != 10:
    total_prob = 1
    word = ""
    generated_char = np.random.choice(a=list(first_char[' '].keys()),p=[first_char[' '][c] for c in first_char[' ']])
    last_generated = ' '
    while(generated_char!=' '):
        total_prob = total_prob * first_char[last_generated][generated_char]
        word += generated_char
        last_generated = generated_char
        generated_char =  np.random.choice(a=list(first_char[generated_char].keys()),p=[first_char[generated_char][c] for c in first_char[generated_char]])
    if(total_prob >= 0.0001 and len(word)>=5):
        print(word)
        i=i+1








