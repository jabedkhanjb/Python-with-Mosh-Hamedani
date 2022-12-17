def squre(number):
    #print(number * number)
    return (number * number)

result = squre(3)
print(result)
    
def emojiconverter(message):
    word = message.split(" ")
    emoji = {
        ":)": "Happy",
        ":(": "Sad"
    }
    output = ""
    for new in word:
        output += emoji.get(new, new) + " "
    return output
message = input("Talk about your Emotions > ")
print(emojiconverter(message))