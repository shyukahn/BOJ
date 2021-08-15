def fscore(score):
    if score <= 40:
        return 40
    else:
        return score
s1 = fscore(int(input()))
s2 = fscore(int(input()))
s3 = fscore(int(input()))
s4 = fscore(int(input()))
s5 = fscore(int(input()))
print((s1+s2+s3+s4+s5)//5)
