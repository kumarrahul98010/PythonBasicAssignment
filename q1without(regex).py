def check_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return "Galat IP"
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            return "Galat IP"
    first, second = int(parts[0]), int(parts[1])
    if first == 10 or (first == 172 and 16 <= second <= 31) or (first == 192 and second == 168):
        return "Private"
    return "Public"

def check_email(email):
    special_chars = "~! $%^&*_=+}{'?-."
    if email.endswith("@gmail.com"):
        local_part = email.split('@')[0]
        if any(char in special_chars for char in local_part):
            return "Invalid mail"
        if not local_part.isalnum():
            return "Invalid mail"
        return "Valid Gmail address."
    return "Invalid mail"

def main():
    print(check_ip(input("Apna IP daaliye: ")))
    print(check_email(input("Apna Email daaliye: ")))

main()
