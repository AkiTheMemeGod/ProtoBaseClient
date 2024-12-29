# ProtoBase Client

A Python client for the ProtoBase authentication API that supports email and username sign-up/sign-in.

## Installation

```bash
pip install protobase-client
```
## Usage

```python
from protobase_client import ProtoBaseClient

client = ProtoBaseClient()

# Sign up with email
signup_response = client.signup_email("username", "password", "email@example.com")
print(signup_response)

# Sign in with email
signin_response = client.signin_email("username", "password", "email@example.com")
print(signin_response)

# Sign up with username
signup_response = client.signup_username("username", "password")
print(signup_response)

# Sign in with username
signin_response = client.signin_username("username", "password")
print(signin_response)

```