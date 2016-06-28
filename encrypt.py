import uuid
import hashlib

def genSalt():
	outSalt = uuid.uuid4().hex
	return outSalt

def encryptPassword(inSalt, inPassword):
	algorithm= 'sha256'
	h = hashlib.new(algorithm)
	h.update(inSalt + inPassword)
	outHash = h.hexdigest()

	outPassword = "$".join([algorithm, inSalt, outHash])
	return outPassword