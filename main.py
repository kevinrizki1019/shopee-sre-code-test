# Serve web url to one endpoint
# The program will readthe user address
# then save it to temporary database (on code)

from flask import Flask
from flask import request

app = Flask(__name__)

addressHits = {}

@app.route("/")
def main():
    visitorAddress = request.remote_addr
    if visitorAddress not in addressHits:
        addressHits[visitorAddress] = 1
    else:
        addressHits[visitorAddress] += 1 
    return "User Address: " + visitorAddress + "\nHits: " + str(addressHits[visitorAddress])