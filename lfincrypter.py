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

def CustomEncryptChecker(hash : str, userText : str, env_name : str):
    import hashlib, os
    userText += os.environ[f'{env_name}']
    byte_data = userText.encode("UTF-8")
    hash_object = hashlib.sha256(byte_data)
    hash2 = hash_object.hexdigest()
    if hash == hash2:
        return True
    else:
        return False

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

def Set_database(database : str):
    import os
    os.environ['LF-database'] = database
    return None

def SetUp_database(database_address : str, userid : str, userpw : str, database : str, table : str):
    import os
    os.environ['LF-Daddress'] = database_address
    os.environ['LF-Did'] = userid
    os.environ['LF-Dpw'] = userpw
    os.environ['LF-database'] = database
    os.environ['LF-Dtable'] = table
    return None

def GetDB_LoginInfomation(isprint : bool):
    if(isprint):
        import datetime, os
        output = f"""
        Now time : {datetime.datetime.now()}
        your database login lofomation is ...
        database_address : {os.environ['LF-Daddress']}
        database_ID : {os.environ['LF-Did']}
        database_PW : {len(os.environ['LF-Dpw']) * '*'}
        database_Table : {os.environ['LF-Dtable']}
        """
        print(output)
    return output

# sliceing, type = list ["'key' : 'value'"]
def Insert_table(section : list):
    for i in section:
        key = i.split(":")[0]
        valuem = i.split(":")[1]
        print(i.split(":"))
        print(key)
        print(valuem)
    return None