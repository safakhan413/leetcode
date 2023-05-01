input =  ["Binance,XRP/USDT,100000",
    "Binance,XRP/BTC,30000",
    "Binance,XRP/ETH,7000",
    "Huobi,XRP/USDT,200000",
    "Huobi,XRP/BTC,18000",
    "Upbit,XRP/KRW,250000",
    "Upbit,XRP/BTC,1500",
    "Upbit,XRP/ETH,100",
    "Bittrue,XRP/USD,20000",
    "Bittrue,XRP/BCH,5000",
    "Bittrue,XRP/BCH,6000",
    "Bittrue,XRP/ETH,15000",
    "Bittrue,XRP/LTC,9000"]

def maxKValues(input, k):
    ''''
    Algo:
    Output: The top k exchange currency pairs  based on tradevolumes
    Input: trade volume of different exchanges as input along with a parameter ‘k’ to find the top k currency pairs per exchange based on the trade volume.
    Steps:
    0. Split the strings in each s.t. numerical portion is tradevolume and the rest is treated as key
    1. create a dictionary with keys being e.g.Binance,XRP/USDT
    2. initialize a list when you coem across a key and tehn keep appending to that list

    
    '''
    a = dict()
    # j = []
    for i in input:
        x = i.split(',')
        print(x)
        # for a.keys()
        # for a[x[0]]
        # a[x[0]] = j.append((x[1], x[2]))
        # print(x)
    

    # for i in x:


    #     a[x[0]] = j.append((x[1], x[2]))
    #     # a[x[0]+x[1]] = x[2]
    # print(a)

    # find top value per exchange
    # print(max(a))

    



        # print(i.split(','))





maxKValues(input, 2)