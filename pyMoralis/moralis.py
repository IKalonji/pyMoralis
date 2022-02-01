import os
import moralis_requests
import covalent_requests
import ipfs_requests
import subprocess
import threading

# os.chdir("/".join(os.path.dirname(__file__).split("\\"))+"/pyMoralisWrapper")
# os.system('npm run dev')


class Moralis():

    def __init__(self):
        run_command = "npm run dev"
        os.chdir("/".join(os.path.dirname(__file__).split("\\"))+"/pyMoralisWrapper")
        subprocess.Popen(run_command, shell=True)   
        print("Moralis server started")

    def login(self):
        return moralis_requests.login()

    def logout(self):
        return moralis_requests.logout()

    def transfer_native(self, amount, receiver):
        return moralis_requests.transfer_native(amount, receiver)

    def transfer_ERC20(self, amount, receiver, contractAddress):
        return moralis_requests.transfer_ERC20(amount, receiver, contractAddress)

    def transfer_ERC721(self, receiver, contractAddress, tokenId):
        return moralis_requests.transfer_ERC721(receiver,contractAddress, tokenId)

    def transfer_ERC1155(self, amount, receiver, contractAddress, tokenId):
        return moralis_requests.transfer_ERC1155(amount, receiver, contractAddress, tokenId)

    def run_contract_function(self, chain, address, functionName, abi, owner, spender):
        return moralis_requests.run_contract_function(chain, address, functionName, abi, owner, spender)

    def contract_events(self, chain, address, topic, abi):
        return moralis_requests.contract_events(chain, address, topic, abi)

    def resolve_domain(self, currency, domain):
        return moralis_requests.run_contract_function(currency, domain)


class Covalent():

    def get_address_balance(self, address, chainId):
        return covalent_requests.get_address_balance(address, chainId)

    def get_portfolio_value(self, address, chainId):
        return covalent_requests.get_portfolio_value(address, chainId)

    def get_address_transactions(self, address, chainId):
        return covalent_requests.get_address_transactions(address, chainId)

    def get_transaction_by_hash(self, tx_hash, chainId):
        return covalent_requests.get_transaction_by_hash(tx_hash, chainId)

    def get_ERC20_transfers(self, address, chainId):
        return covalent_requests.get_ERC20_transfers(address, chainId)
    
    def get_block_latest(self, chainId):
        return covalent_requests.get_block_latest(chainId)

    def get_block_height(self, chainId, start, end):
        return covalent_requests.get_block_height(chainId, start, end)

    def get_token_holders(self, chainId, address):
        return covalent_requests.get_token_holders(chainId, address)

    def get_token_holding_changes(self, chainId, address):
        return covalent_requests.get_token_holding_changes(chainId, address)

    def get_NFT_ids(self, chainId, contract_address):
        return covalent_requests.get_NFT_ids(chainId, contract_address)

    def get_NFT_transactions(self, chainId, contract_address, tokenId):
        return covalent_requests.get_NFT_transactions(chainId, contract_address, tokenId)

    def get_NFT_metadata(self, chainId, contract_address, tokenId):
        return covalent_requests.get_NFT_metadata(chainId, contract_address, tokenId)

    def get_NFT_market_data(self, chainId):
        return covalent_requests.get_NFT_market_data(chainId)

    def get_NFT_collection_data(self, chainId, collection_address):
        return covalent_requests.get_NFT_collection_data(chainId, collection_address)

    def get_all_contract_metadata(self, chainId):
        return covalent_requests.get_all_contract_metadata(chainId)

    def get_all_chains(self):
        return covalent_requests.get_all_chains()
        
    def get_all_chain_status(self):
        return covalent_requests.get_all_chain_status()

    def get_token_price_history(self, chainId, contract_address):
        return covalent_requests. get_token_price_history(chainId, contract_address)

    def get_token_price_by_ticker(self, ticker):
        return covalent_requests.get_token_price_by_ticker(ticker)

    def get_spot_price(self):
        return covalent_requests.get_spot_price()

    def get_volatility(self):
        return covalent_requests.get_volatility()


class IPFS():

    def upload_file(self, file):
        return ipfs_requests.uploadIPFS(file)
        