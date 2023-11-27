def salt(text : str):
    import os
    try:
        os.environ['LF-ENC'] = str(text)
        print(f"salt setted as {text}")
    except:
        print("salt setting fail")
    return None

def CustomSalt(text: str, env_name: str):
    import os
    try:
        os.environ[f'{env_name}'] = str(text)
        print(f"salt setted as {text}, {env_name}")
    except:
        print("salt setting fail")
    return None

def GetENV():
    import os
    return os.environ['LF-ENC']

def GetEncrypt(text):
    
    return 9

