# ProtoBase Client

**ProtoBase Client** is a simple and efficient Python package designed to interact with the ProtoBase authentication API. It provides easy-to-use functions for user sign-up and sign-in via email or username, abstracting away the complexity of API calls and streamlining the authentication process in Python applications.

---

## Features

- **Email-based authentication**: Easily sign up and sign in users using their email and password.
- **Username-based authentication**: Allow users to sign up and sign in using a username and password.
- **Simple integration**: Quickly integrate authentication features into any Python application with minimal code.
- **Seamless API interaction**: The package handles all the HTTP request/response management, making authentication tasks straightforward.

---
## Api Token

Get Your Api-Token from the [Official Website](https://protobase.pythonanywhere.com/)

## Installation

To install the package, simply use `pip`:

```bash
pip install protobase-client
```

---

## Usage

Here’s how you can use the **ProtoBase Client** in your Python application:

### 1. Import the package

```python
from protobase_client import ProtoBaseClient
```

### 2. Create an instance of the client

```python
client = ProtoBaseClient()
```

### 3. Sign up with email

To sign up a user with their email and password:

```python
signup_response = client.signup_email("username", "password", "email@example.com", "api_token")
print(signup_response)
```

### 4. Sign in with email

To sign in a user with their email and password:

```python
signin_response = client.signin_email("username", "password", "email@example.com", "api_token")
print(signin_response)
```

### 5. Sign up with username

To sign up a user with just a username and password:

```python
signup_response = client.signup_username("username", "password", "api_token")
print(signup_response)
```

### 6. Sign in with username

To sign in a user with their username and password:

```python
signin_response = client.signin_username("username", "password", "api_token")
print(signin_response)
```

---

## Example

```python
from protobase_client import ProtoBaseClient

# Initialize client
client = ProtoBaseClient()

# Sign up using email
response = client.signup_email("john_doe", "securepassword123", "john.doe@example.com", "api_token")
print(response)

# Sign in using email
signin_response = client.signin_email("john_doe", "securepassword123", "john.doe@example.com", "api_token")
print(signin_response)
```

---

## Contributing

We welcome contributions to the ProtoBase Client! If you would like to improve or add features, feel free to fork the repository, create a branch, and submit a pull request.

Please ensure that you follow the contribution guidelines:
- Write clear and descriptive commit messages.
- Add tests for new features or bug fixes.
- Follow Python coding standards (PEP 8).

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- Thanks to the ProtoBase API for providing the authentication backend.
- Inspired by the desire to simplify authentication workflows in Python.

---

## Contact

For support or inquiries, you can reach out to [k.akashkumar@gmail.com](mailto:k.akashkumar@gmail.com).

---

### Customizing the GitHub Documentation

- **Badges**: You can add badges like build status, license, and PyPI version by using shields.io or similar services.
- **Screenshots**: If the package includes a GUI or more visual outputs, add screenshots to illustrate the usage.
- **Links to Documentation**: If your package is further documented elsewhere (like ReadTheDocs), include those links.

---

### Example of a Badge Section

![PyPI](https://img.shields.io/pypi/v/protobase-client)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

