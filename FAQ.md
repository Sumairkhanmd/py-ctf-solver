
## Has already opted in to app XXXX
The account has already successfully opted into the application.

## "txgroup had 0 in fees, which is less than the minimum"
Make sure you are setting the fee correctly or using the suggested parameters with the transaction. If you are using fee pooling make sure to set the suggested fee high enough to cover all transactions. See: https://developer.algorand.org/docs/get-details/transactions/#pooled-transaction-fees

## "check failed on ApprovalProgram: program version must be \\u003e= 2 
This error occurs when you use the compile endpoint but you have not set the version of TEAL you are using. If using TEAL, the version is specified with #pragma version 9.

## logic eval error: unavailable App XXXX
An application that the smart contract interacts with is currently not in the application array.
Make sure the calling application loads the foreign apps array. See: https://developer.algorand.org/docs/get-details/dapps/smart-contracts/apps/#reference-arrays 

## logic eval error: invalid Applications index 2
This error occurs when a smart contract tries to access the second element in the foreign application array but it down not exist. Make sure you have loaded your foreign apps array properly. See: https://developer.algorand.org/docs/get-details/dapps/smart-contracts/apps/#reference-arrays

## logic eval error: assert failed pc=41. Details: pc=41, opcodes=pushbytes 0x616363657373 // \\"access\\"; app_global_get_ex; assert"}\n'
This error occurs when a smart contract is trying to access a global variable in another contract that is not in the foreign apps array. Make sure you have loaded your foreign apps array properly. See: https://developer.algorand.org/docs/get-details/dapps/smart-contracts/apps/#reference-arrays

## invalid : tx references exceed MaxAppTotalTxnReferences = 8'
You have more than 8 references in your reference arrays. Add up all references in foreign apps, accounts, assets, boxes arrays and make sure they are less than or equal to 8. More references can be used by grouping additional transactions.

## logic eval error: invalid ApplicationArgs index 0. Details: pc=50, opcodes===; assert; txna ApplicationArgs 0"}\n'
This error occurs when a smart contract attempts to read an application argument and the application argument was not passed in with the call to the smart contact. Make sure you are passing in the correct arguments. See: https://developer.algorand.org/docs/get-details/dapps/smart-contracts/frontend/apps/#call-with-arguments

## logic eval error: invalid Box reference 
This error occurs when a smart contract tries to read or write a box that has not been passed in with the boxes array. Make sure your box array is set correctly. See: https://developer.algorand.org/docs/get-details/dapps/smart-contracts/apps/state/#box-array for more details.


## logic eval error: fee too small
Fee was set to low, most likely to a contract issuing an inner transaction that was not paid for. In this particular case, set the fee higher in the outer application transaction or add funds to the contract to cover the cost of the inner transaction.
