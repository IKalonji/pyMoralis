import { Request, Response, NextFunction } from 'express';
import axios, { AxiosResponse } from 'axios';
// In a node environment
import Moralis from 'moralis/node';

Moralis.initialize("APP ID")
Moralis.serverURL = "SERVER URL"

const login = async (req: Request, res: Response, next: NextFunction) => {
    res.sendFile(__dirname +'/login.html')
    // return res.status(200).json({message: "Navigate to localhost to login"});
}

const logout = async (req: Request, res: Response, next: NextFunction) => {
    await Moralis.User.logOut();
    console.log("logged out");
    return res.status(200).json({
        message: "Loggged out"
    });
}

const transferNative = async (req: Request, res: Response, next: NextFunction) => {
    const options: Moralis.TransferOptions = {type: "native", amount: Moralis.Units.ETH(req.body.amount), receiver: req.body.receiver}
    const transaction = await Moralis.transfer(options)
    return res.status(200).json({
        result: transaction
    })
}

const transferERC20 = async (req: Request, res: Response, next: NextFunction) => {
    const options: Moralis.TransferOptions = {type: "erc20", amount: Moralis.Units.ETH(req.body.amount), receiver: req.body.receiver, contractAddress: req.body.contractAddress}
    const transaction = await Moralis.transfer(options)
    return res.status(200).json({
        result: transaction
    })
}

const transferERC721 = async (req: Request, res: Response, next: NextFunction) => {
    const options: Moralis.TransferOptions = {type: "erc721", receiver: req.body.receiver, contractAddress: req.body.contractAddress, tokenId: req.body.tokenId}
    const transaction = await Moralis.transfer(options)
    return res.status(200).json({
        result: transaction
    })
}

const transferERC1155 = async (req: Request, res: Response, next: NextFunction) => {
    const options: Moralis.TransferOptions = {type: "erc20", receiver: req.body.receiver, contractAddress: req.body.contractAddress, tokenId: req.body.tokenId, amount: req.body.amount}
    const transaction = await Moralis.transfer(options)
    return res.status(200).json({
        result: transaction
    })
}

const runContractFunction = async (req: Request, res: Response, next: NextFunction) => {
    const options = {chain: req.body.chain, address: req.body.address, function_name: req.body.functionName, abi: req.body.abi, params: {owner: req.body.owner, spender: req.body.spender}}
    const transaction = await Moralis.Web3API.native.runContractFunction(options)
    return res.status(200).json({
        result: transaction
    })
}

const getContractEvents = async (req: Request, res: Response, next: NextFunction) => {
    let chain: any = req.body.chain
    const options = {chain: chain, address: req.body.address, topic: req.body.topic, abi: req.body.ABI}
    const transaction = await Moralis.Web3API.native.getContractEvents(options)
    return res.status(200).json({
        result: transaction
    })
}

const resolveDomain = async (req: Request, res: Response, next: NextFunction) => {
    let currency: any = req.params.currency
    let domain: any = req.params.domain
    const options = {currency: currency, domain:domain}
    const transaction = await Moralis.Web3API.resolve.resolveDomain(options)
    return res.status(200).json(
        {
            result: transaction
        }
    )
}






export default {
    login,
    logout, 
    transferNative,
    transferERC20,
    transferERC721,
    transferERC1155,
    runContractFunction,
    getContractEvents,
    resolveDomain
}
