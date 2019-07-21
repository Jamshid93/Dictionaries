phone=input("Phone: ")
digits_mapping = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
output = ""
for charater in phone:
    output += digits_mapping.get(charater, "!") + " "
print(output)