# Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not. Use the prior prime number exercise as a starting point. For example, a GET request for number 31 is given as: http://127.0.0.1:5000/prime_number/31. The response must be in the format of {"Number":31, "isPrime":true}.

from flask import Flask,request

app= Flask(__name__)

def check_if_prime(n):
    if n <2:
        return False
    if n == 2 :
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
@app.route('/prime_number/<int:number>')
def handle_request(number):
    result = check_if_prime(number)
    return {
        "Number": number,
        "isPrime": result
    }

if __name__ == '__main__':
    app.run(port=5000)