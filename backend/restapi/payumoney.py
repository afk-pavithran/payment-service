import hashlib


class PayuMoney:
    def generateHash(data):
        # req = data
    
        hashString = f"{data['key']}|{data['txnid']}|{data['amount']}|{data['productinfo']}|{data['firstname']}|{data['email']}|||||||||||{data['salt']}"
        hash_String = hashString.encode('utf-8')
        hash = hashlib.sha512(hash_String).hexdigest().lower()
        return hash