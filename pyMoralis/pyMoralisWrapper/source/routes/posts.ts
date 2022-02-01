/** source/routes/posts.ts */
import express from 'express';
import controller from '../controllers/posts';
const router = express.Router();

//pyMoralisWrapper endpoints
// router.get('/connect-server', controller.connectServer)
router.get('/login', controller.login)
router.get('/logout', controller.logout)
router.post('/transfer-native', controller.transferNative)
router.post('/transfer-ERC20', controller.transferERC20)
router.post('/transfer-ERC721', controller.transferERC721)
router.post('/transfer-ERC1155', controller.transferERC1155)
router.post('/run-contract-function', controller.runContractFunction)
router.post('contract-events', controller.getContractEvents)
router.get('/resolve-domain', controller.resolveDomain)

export = router;