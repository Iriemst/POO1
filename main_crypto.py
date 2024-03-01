from crypto import Crypto

if __name__=="__main__":
    bitcoin=Crypto("Bitcoin",57000)
    bitcoin.stopLoss(55000,60000)
    bitcoin.imprimir()
