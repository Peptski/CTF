import hashlib
import uuid

poss = b"991975facbb047e8a9402c94286afa81"

def find(ans):
    while 1:
        bitstring = uuid.uuid4().hex
        md5 = hashlib.md5(bytes(bitstring, 'utf-8')).hexdigest()
        sha1 = hashlib.sha1(bytes(md5, 'utf-8')).hexdigest()
        print(sha1[-4:])
        if sha1[-4:] == ans:
            return bitstring


print(find("222f"))