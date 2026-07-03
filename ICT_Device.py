def check_device(username, device_type, encrypted, mfa_enabled):
    if encrypted.lower() == "yes" and mfa_enabled.lower() == "yes":
        result = "✔ Device Compliant"
    else:
        result = "✘ Device Not Compliant"

    device_info = {
        "username": username,
        "device_type": device_type,
        "encrypted": encrypted,
        "mfa_enabled": mfa_enabled,
        "result": result
    }

    return device_info


username = input("Enter username: ")
device_type = input("Enter device type: ")
encrypted = input("Device encrypted? Yes/No: ")
mfa_enabled = input("MFA enabled? Yes/No: ")

device = check_device(username, device_type, encrypted, mfa_enabled)

print("\n======== ICT Device Checker ========")
print(f"Username: {device['username']}")
print(f"Device Type: {device['device_type']}")
print(f"Encrypted: {device['encrypted']}")
print(f"MFA Enabled: {device['mfa_enabled']}")
print(f"Result: {device['result']}")