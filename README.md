# API Tester

A clean and simple command-line tool to test APIs quickly.

**Developed by Hamed Farifteh**

## Features
- Support GET, POST, PUT, DELETE
- Add custom headers
- Send JSON body
- Show status code, response time, and response
- Save response to file

## Installation
```bash
pip install requests
```

## Usage Examples

```bash
# Simple GET request
python api_tester.py get https://jsonplaceholder.typicode.com/posts/1

# POST request with JSON
python api_tester.py post https://jsonplaceholder.typicode.com/posts --json '{"title": "foo", "body": "bar"}'

# With custom header
python api_tester.py get https://api.github.com/user --header "Authorization: token YOUR_TOKEN"
```