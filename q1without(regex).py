def check_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return "Galat IP"
    for part in parts:
        if not part.isdigit() or int(part) < 0 or int(part) > 255:
            return "Galat IP"
    first, second = int(parts[0]), int(parts[1])
    if first == 10 or (first == 172 and 16 <= second <= 31) or (first == 192 and second == 168):
        return "Private"
    return "Public"

def check_email(email):
    return "Sahi" if "@" in email and "." in email.split("@")[-1] else "Galat Mail_ID"

def main():
    print(check_ip(input("Apna IP daaliye: ")))
    print(check_email(input("Apna Email daaliye: ")))

main()