import logging

logging.basicConfig(
    filename="login.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class PasswordError(Exception):
    pass

try:

    password = input("Enter Password: ")

    if len(password) < 8:
        raise PasswordError("Password must contain at least 8 characters.")

    logging.info("Login Successful")

    print("Login Successful")

except PasswordError as e:
    logging.error(e)
    print(e)