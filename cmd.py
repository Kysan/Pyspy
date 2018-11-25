

def exec_command_and_get_output():
    try:
        process = subprocess.Popen(args=comando,stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell= True)
        output = (process.communicate())
        out2 = outt[0]
        out3 = out2.split('\r\n')
        for item in (out3):     #très très chiant
            debuged = item.replace("\x82", "?")
            debuged = item.replace("\xc6", "?")
            debuged = item.replace("\xa3", "?")
            debuged = item.replace("\xa1", "?")
            debuged = item.replace("\xa2", "?")
            debuged = item.replace("\x87", "?")
            debuged = item.replace("\x93", "?")
            debuged = item.replace("\xa0", "?")
            debuged = item.replace("\x88", "?")
            debuged = item.replace("\x83", "?")
            debuged = item.replace("\xc7", "?")
            debuged = item.replace("\xb8", "?")
            debuged = item.replace("\xad", "?")
            debuged = item.replace("\xef", "?")
            debuged = item.replace("\xa7", "?")
            debuged = item.replace("\xf5", "?")
            debuged = item.replace("\xf0", "?")
            debuged = item.replace("\xfc", "?")
            debuged = item.replace("\xa6", "?")
            return item
    except:
        return "probleme dans l'analyse de la réponse"