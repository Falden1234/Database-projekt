import hashlib, bcrypt
#Demonstrer forskellen på bcrypt og SHA-1 hashing
password = input("Skriv password der skal Hashes:\n>")
print("\nSHA-1:\n")


setpass = bytes(password, 'utf-8')
hash_object = hashlib.sha1(setpass)
guess_pw = hash_object.hexdigest()
print(guess_pw)
