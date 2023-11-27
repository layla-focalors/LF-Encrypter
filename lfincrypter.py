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

def CustomGetENV(cust:str):
    import os
    return os.environ[f'{cust}']

def CustomEncrypt(hash_text : str, env_name):
    import hashlib, os
    hash_text += os.environ[f'{env_name}']
    print(hash_text)
    byte_data = hash_text.encode("UTF-8")
    hash_object = hashlib.sha256(byte_data)
    return hash_object.hexdigest()

def Encrypt(hash_text : str):
    import hashlib, os
    hash_text += os.environ['LF-ENC']
    byte_data = hash_text.encode("UTF-8")
    hash_object = hashlib.sha256(byte_data)
    return hash_object.hexdigest()

def EncyptChecker(hash : str, userText : str):
    import hashlib, os
    userText += os.environ['LF-ENC']
    byte_data = userText.encode("UTF-8")
    hash_object = hashlib.sha256(byte_data)
    hash2 = hash_object.hexdigest()
    if hash == hash2:
        return True
    else:
        return False
