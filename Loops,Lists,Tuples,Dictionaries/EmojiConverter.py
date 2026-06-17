msg=input(">")
words=msg.split(' ')
emojis={
    ":)":"😀",
    ":(":"🙁"
}
op=""
for word in words:
    op+=emojis.get(word,word)+" "
print(op)
    