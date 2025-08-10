def password_maker(word):

    password = word.replace("a", "@")
    password = password.replace("e", "3")
    password = password.replace("i", "!")
    password = password.replace("o", "0")
    password = password.replace("s", "$")
    password = password.capitalize() 
    password += "195!"  
    return password


word = input("Enter a word to create a strong password: ")
strong_password = password_maker(word)
print(f"Your secure password is: {strong_password}")
