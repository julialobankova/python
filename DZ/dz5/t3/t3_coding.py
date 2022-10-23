
def open_txt(fail_txt):
    with open(fail_txt) as file:
        text_import = file.read()
        return text_import

content = open_txt('1.txt')

seen = ""
for i in content:
    with open("2.txt","a", encoding="utf-8") as f:
        if i not in seen:
            f.write(f'{content.count(i)}{i}')
            seen += i




def decode(fail_txt):
    decoded_message = ""
    i = 0
    j = 0
    while (i <= len(fail_txt) - 1):
        run_count = int(fail_txt[i])
        run_word = fail_txt[i + 1]
        for j in range(run_count):
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2
    return decoded_message
    
content2  = open_txt('2.txt')
print(content2)
with open("3.txt","a", encoding="utf-8") as f:
    f.write(decode(content2))
print(decode(content2))







