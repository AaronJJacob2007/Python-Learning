def emoji_converter(message):
     words=message.split(' ')
     emojis={
        ":)":"😀",
        ":(":"🙁"
     }
     op=""
     for word in words:
        op+=emojis.get(word,word)+" "
     return(op)


message=input(">")
print(emoji_converter(message))