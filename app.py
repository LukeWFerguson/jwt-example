import jwt
import datetime
import time

from datetime import timezone

# Creating a JWT with expiration 3 seconds in the future.
encoded_jwt = jwt.encode(
    payload=
    {
        "user": "Luke",
        "is_awesome": True,
        "exp": datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(seconds=3)
    },
    key="42",  # This would be held on either side of the Web Component and would only be passed through it.
    algorithm="HS256"
)

#  Prints out a compliant JSON Web Token.
print(encoded_jwt)

#  Show that you HAVE to have the right key to use.
try:
    decoded_jwt = jwt.decode(jwt=encoded_jwt, key="43", algorithms="HS256")
except jwt.InvalidSignatureError:
    print("Signature verification failed.")

#  Decode and print out the value of the JSON Web Token.
decoded_jwt = jwt.decode(jwt=encoded_jwt, key="42", algorithms="HS256")
print(decoded_jwt)

# Wait till expired (four seconds).
time.sleep(4)

#  Show that you HAVE to be within the expiry window.
try:
    decoded_jwt = jwt.decode(jwt=encoded_jwt, key="42", algorithms="HS256")
except jwt.ExpiredSignatureError:
    print("Signature has expired.")
