import os
import re
import json


def clean_tweets(*args):
        results = {"N": {"success": 0, "fail":0}, "NEU":{"success": 0, "fail":0}, "NONE":{"success": 0, "fail":0}, "P":{"success": 0, "fail":0}}
        Sucios = args[0]
        for emocion in os.listdir(Sucios):
            for tweet in os.listdir(Sucios+emocion):
                texto = ""
                with open(Sucios+emocion+"/"+tweet, encoding='utf8', mode='r') as f: #leemos en utf8 para que no de problemas
                    texto = f.read()
                with open("D:/PyCharm/Ejercicios/CleanTweets/"+emocion+"/"+tweet, encoding='utf8', mode="w") as clean:
                    comas = [",", ".", ";"]
                    lower = str(texto).lower() #poner a minusculas
                    lower = remove_emoji(lower) #quitar emojis
                    lower = ''.join([i for i in lower if not i.isdigit()]) #comprobar que no tiene numeros
                    lower = re.sub(r'\W+', ' ', lower) #quitar simbolos (deja los valores de un [a-zA-z0-9]
                    clean.write(lower)
                    iterator = 0
                    with open(args[1], encoding='utf8' ,mode="r") as lexico:
                        data = lexico.read().split() #leemos y separamos los datos de léxico para tenerlo dividido por comas
                        dataLexico = data[0::2] #tomar solo la primera columna de datos
                        state = data[1::2] #tomar solo la segunda columna de datos
                        aux = None
                        contador = 0
                        for word in lower.split():
                            if word in dataLexico:
                                aux = not None
                                index = dataLexico.index(word)
                                if state[index] == "negative":
                                    contador -= 1
                                else:
                                    contador += 1
                    if emocion == "N":
                        if contador < 0 and aux is not None:
                            results["N"].update({"success": results["N"].get("success") + 1})
                        else:
                            results["N"].update({"fail": results["N"].get("fail") + 1})
                    elif emocion == "NEU":
                        if contador == 0 and aux is not None:
                            results["NEU"].update({"success": results["NEU"].get("success") + 1})
                        else:
                            results["NEU"].update({"fail": results["NEU"].get("fail") + 1})
                    elif emocion == "NONE":
                        if aux is None:
                            results["NONE"].update({"success": results["NONE"].get("success") + 1})
                        else:
                            results["NONE"].update({"fail": results["NONE"].get("fail") + 1})
                    elif emocion == "P":
                        if contador > 0 and aux is not None:
                            results["P"].update({"success": results["P"].get("success") + 1})
                        else:
                            results["P"].update({"fail": results["P"].get("fail") + 1})
        print(results)
        out = open(args[2], encoding='utf8', mode="w")
        json.dump(results, out, ensure_ascii=False)
        out.close()
def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)
clean_tweets("D:/PyCharm/Ejercicios/CorpusTrainTASS/", "D:\PyCharm\Ejercicios\lexico", "C:/Users/PC/Desktop/testPython/tweetsJSON.json")