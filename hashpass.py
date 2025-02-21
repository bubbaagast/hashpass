import hashlib

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

password = input("Type the password to hash here : ")
hashed_password = hash_password(password)
print("Hashed password : ", hashed_password)
