#!/usr/bin/env python3
"""
API Tester - Simple CLI Tool
Developed by Hamed Farifteh
"""

import requests
import json
import time
import argparse

def test_api(method, url, headers=None, json_data=None, save_response=False):
    headers = headers or {}
    
    print(f"\n{'='*60}")
    print(f"API Tester - {method.upper()} Request")
    print(f"{'='*60}")
    print(f"URL: {url}")
    
    if headers:
        print(f"Headers: {headers}")
    if json_data:
        print(f"Body: {json_data}")
    
    print(f"{'-'*60}")
    
    start_time = time.time()
    
    try:
        if method.lower() == 'get':
            response = requests.get(url, headers=headers, timeout=15)
        elif method.lower() == 'post':
            response = requests.post(url, headers=headers, json=json_data, timeout=15)
        elif method.lower() == 'put':
            response = requests.put(url, headers=headers, json=json_data, timeout=15)
        elif method.lower() == 'delete':
            response = requests.delete(url, headers=headers, timeout=15)
        else:
            print("Unsupported method!")
            return

        elapsed = time.time() - start_time
        
        print(f"Status Code : {response.status_code}")
        print(f"Response Time: {elapsed:.2f} seconds")
        print(f"Content-Type: {response.headers.get('Content-Type', 'N/A')}")
        
        print(f"{'-'*60}")
        print("Response Body:")
        
        try:
            # Try to pretty print JSON
            json_response = response.json()
            print(json.dumps(json_response, indent=2, ensure_ascii=False))
        except:
            # If not JSON, print raw text
            print(response.text[:2000])  # Limit output

        # Save response if requested
        if save_response:
            filename = f"response_{int(time.time())}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"\n✅ Response saved to: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(description="API Tester by Hamed Farifteh")
    parser.add_argument("method", choices=["get", "post", "put", "delete"], help="HTTP method")
    parser.add_argument("url", help="API endpoint URL")
    parser.add_argument("--header", action="append", help="Add header (format: 'Key: Value')")
    parser.add_argument("--json", help="JSON body for POST/PUT")
    parser.add_argument("--save", action="store_true", help="Save response to file")

    args = parser.parse_args()

    # Parse headers
    headers = {}
    if args.header:
        for h in args.header:
            if ":" in h:
                key, value = h.split(":", 1)
                headers[key.strip()] = value.strip()

    # Parse JSON body
    json_data = None
    if args.json:
        try:
            json_data = json.loads(args.json)
        except json.JSONDecodeError:
            print("Invalid JSON format!")
            return

    test_api(
        method=args.method,
        url=args.url,
        headers=headers,
        json_data=json_data,
        save_response=args.save
    )

if __name__ == "__main__":
    main()