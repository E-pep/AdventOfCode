import hashlib

def lowestNumber(input):
    counter = 0
    md5_hash_check = False
    while md5_hash_check is False:
        text = input + str(counter)
        hash_object = hashlib.md5(text.encode())
        md5_hash = hash_object.hexdigest()
        # For part 1
        # if md5_hash.startswith("00000"):
        # For part 2
        if md5_hash.startswith("000000"):
            md5_hash_check = True
        else:
            md5_hash_check = False
            counter = counter + 1

    print("lowest number: " + str(counter))

if __name__ == "__main__":
    # Testing the hash encode
    text = "abcdef609043"
    hash_object = hashlib.md5(text.encode())
    md5_hash = hash_object.hexdigest()
    print(md5_hash)

    # function to find number
    lowestNumber("bgvyzdsv")