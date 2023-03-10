masiv = [int(x) for x in input().split()]
print(masiv)
print(min(masiv))
resul = [i for i, j in enumerate(masiv) if j == min(masiv)]
print(resul)
print(*filter(lambda x : x > 0, masiv))
print(*filter(lambda x : x < 0, masiv))
