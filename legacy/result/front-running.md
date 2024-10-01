# Test Result

## User Input:

```
Is front running possible in TON?
```

## Normal GPT-4:

Front running is possible in any blockchain network, including TON (Telegram Open Network). Front running refers to the practice of a trader or insider taking advantage of advance knowledge of a large trade or transaction in order to profit from it. In decentralized systems like TON, front running can occur when a user with access to certain information about pending transactions exploits that information for their own gain.

While front running is technically possible in TON, the network's design features, such as transparency, immutability, and decentralization, can make it more difficult for bad actors to engage in such practices. Additionally, TON's smart contract functionalities and consensus mechanisms may have built-in protections against front running. However, it is still important for users to be cautious and aware of potential front running risks when using the network.

## TonGPT:

In TON, front running is effectively prevented due to its deterministic transaction ordering system. This architecture ensures that the order of transactions is predetermined and cannot be altered once they enter the transaction pool. Consequently, no participant can manipulate transaction order for profit, which distinguishes TON from blockchains like Ethereum, where validators can change transaction orders within a block, creating opportunities for maximum extractable value (MEV).

Additionally, the absence of a market-based mechanism for determining transaction fees in TON means that transaction commissions are fixed, making the incentive for front running less appealing. Overall, the combination of fixed fees and deterministic transaction ordering makes front running non-trivial in the TON ecosystem.
