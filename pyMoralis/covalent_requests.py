import requests

url_covalent = "https://api.covalenthq.com/v1/"
PARAMS = {'key': "API KEY"}

def get_address_balance(address, chainId):
    return requests.get(url=f"{chainId}/address/{address}/balances_v2/", params=PARAMS).json()

def get_portfolio_value(address, chainId):
    return requests.get(url=f"{chainId}/address/{address}/portfolio_v2/", params=PARAMS).json()

def get_address_transactions(address, chainId):
    return requests.get(url=f"{chainId}/address/{address}/transactions_v2/", params=PARAMS).json()

def get_transaction_by_hash(tx_hash, chainId):
    return requests.get(url=f"{chainId}/transaction_v2/{tx_hash}/", params=PARAMS).json()

def get_ERC20_transfers(address, chainId):
    return requests.get(url=f"{chainId}/address/{address}/transfers/", params=PARAMS).json()

def get_block_latest(chainId):
    return requests.get(url=f"{chainId}/block_v2/latest/", params=PARAMS).json()

def get_block_height(chainId, start, end):
    return requests.get(url=f"{chainId}/block_v2/{start}/{end}/", params=PARAMS).json()

def get_token_holders(chainId, address):
    return requests.get(url=f"{chainId}/tokens/{address}/token_holders/", params=PARAMS).json()

def get_token_holding_changes(chainId, address):
    return requests.get(url=f"{chainId}/tokens/{address}/token_holders_changes/", params=PARAMS).json()

def get_NFT_ids(chainId, contract_address):
    return requests.get(url=f"{chainId}/tokens/{contract_address}/nft_token_ids/", params=PARAMS).json()

def get_NFT_transactions(chainId, contract_address, tokenId):
    return requests.get(url=f"{chainId}/tokens/{contract_address}/nft_transactions/{tokenId}/", params=PARAMS).json()

def get_NFT_metadata(chainId, contract_address, tokenId):
    return requests.get(url=f"{chainId}/tokens/{contract_address}/nft_metadata/{tokenId}/", params=PARAMS).json()

def get_NFT_market_data(chainId):
    return requests.get(url=f"{chainId}/nft_market/", params=PARAMS).json()

def get_NFT_collection_data(chainId, collection_address):
    return requests.get(url=f"{chainId}/nft_market/collection/{collection_address}/", params=PARAMS).json()

def get_all_contract_metadata(chainId):
    return requests.get(url=f"{chainId}/tokens/tokenlists/all/", params=PARAMS).json()

def get_all_chains():
    return requests.get(url=f"chains/", params=PARAMS).json()

def get_all_chain_status():
    return requests.get(url=f"chains/status/", params=PARAMS).json()

def get_token_price_history(chainId, contract_address):
    return requests.get(url=f"pricing/historical_by_addresses_v2/{chainId}/USD/{contract_address}/", params=PARAMS).json()

def get_token_price_by_ticker(ticker):
    return requests.get(url=f"pricing/historical/USD/{ticker}/", params=PARAMS).json()

def get_spot_price():
    return requests.get(url=f"pricing/tickers", params=PARAMS).json()

def get_volatility():
    return requests.get(url=f"pricing/volatility", params=PARAMS).json()

    


