n = int(input("Enter the number of clients\n"))
client_dict = {}
while n > 0:
    name = input()
    email = input()
    passport = input()
    detail = [name, email]
    client_dict[passport] = detail
    n -= 1

tosearch = input("Enter the passport number of the client to be searched\n")

if tosearch in client_dict:
    print(f"{client_dict[tosearch][0]}--{client_dict[tosearch][1]}--{tosearch}")
else:
    print("Client not found")

