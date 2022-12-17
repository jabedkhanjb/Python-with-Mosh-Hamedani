def username(message):
    word = message.split(" ")
    emoji = {
        ":)": "Happy",
        ":(": "Sad"
    }
    output = ""
    for new in word:
        output += emoji.get(new, new) + " "
    return output

message = input("> ")
print(username(message))



