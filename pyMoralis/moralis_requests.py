from urllib import response
import requests
import webbrowser

moralis_url = "http://localhost:6060/"

def login():
    _response = requests.get(url = moralis_url+"login")
    webbrowser.open("http://localhost:6060/login")
    # return _response.json()

def logout():
    _response = requests.get(url = moralis_url+"logout")
    return _response.json()

def transfer_native(amount, receiver):
    _response = requests.post(url=moralis_url+'/transfer-native', json={amount:amount, receiver:receiver})
    return _response.json()

def transfer_ERC20(amount, receiver, contractAddress):
    _response = requests.post(url=moralis_url+'/transfer-ERC20', json={amount:amount, receiver:receiver, contractAddress:contractAddress})
    return _response.json()

def transfer_ERC721(receiver, contractAddress, tokenId):
    _response = requests.post(url=moralis_url+'/transfer-ERC721', json={receiver:receiver, contractAddress:contractAddress, tokenId:tokenId})
    return _response.json()

def transfer_ERC1155(amount, receiver, contractAddress, tokenId):
    _response = requests.post(url=moralis_url+'/transfer-ERC1155', json={amount:amount, receiver:receiver, contractAddress:contractAddress, tokenId:tokenId})
    return _response.json()

def run_contract_function(chain, address, functionName, abi, owner, spender):
    _response = requests.post(url=moralis_url+'/run-contract-function', json={chain:chain, address:address, functionName:functionName, abi:abi, owner:owner, spender:spender})
    return _response.json()

def contract_events(chain, address, topic, abi):
    _response = requests.post(url=moralis_url+'/contract-events', json={chain:chain, address:address, abi:abi, topic:topic})
    return _response.json()

def resolve_domain(currency, domain):
    _response = requests.get(url=moralis_url+'/resolve-domain', params={currency:currency, domain:domain})
    return _response.json()
