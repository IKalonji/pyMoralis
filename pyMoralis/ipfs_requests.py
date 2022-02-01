from urllib import response
import requests

ipfs_url = "https://api.nft.storage/upload"

header = {"Authorization": "API KEY"}

def uploadIPFS(file):
    _response = requests.post(ipfs_url, headers=header, files=file)
    return _response.json()

