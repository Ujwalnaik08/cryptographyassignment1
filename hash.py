import hashlib

def compute(msg):
    hash_obj = hashlib.sha256()
    hash_obj.update(msg.encode('utf-8'))
    hash_value = hash_obj.hexdigest()
    return hash_value

msg = "Hello World!"

original_hash = compute(msg)
print(original_hash)

received_hash = compute(msg)
print("Received Hash:",received_hash)

if received_hash == original_hash:
    print("The received message is not compromised")
else:
    print("Alert!!The received message is compromised")

another_msg = "AI is the future"

changed_hash = compute(another_msg)
print("Another message:",changed_hash)

if changed_hash == original_hash:
    print("The received message is not compromised")
else:
    print("Alert!!The received message is compromised")