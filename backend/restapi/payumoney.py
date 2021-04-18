import hashlib


class PayuMoney:
    def generateHash(data):
        posted = {}
        for i in data:
            posted[i] = data[i]
        
        hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
        hash_string=''
        hashVarsSeq=hashSequence.split('|')
        for i in hashVarsSeq:
            try:
                hash_string+=str(posted[i])
            except Exception:
                hash_string+=''
            hash_string+='|'
        hash_string+=data['salt']
        hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()

        return hash