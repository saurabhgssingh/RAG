import re
def split_text(text:str):
    split_text = re.split('\n',text)
    return [i for i in split_text if i!=""]
