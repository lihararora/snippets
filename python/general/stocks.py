import sys,requests,argparse

parser = argparse.ArgumentParser()
parser.add_argument('--symbols', nargs='*')
parser.add_argument('--threshold', type=int, default=5)
args = parser.parse_args()

def get_percent_change(symbols):
    percent_change = {}
    symbols_string = ",".join(symbols)
    r = requests.get("https://api.iextrading.com/1.0/stock/market/batch?symbols="+symbols_string+"&types=quote&displayPercent=true")
    for symbol,quote in r.json().items():
        percent_change[symbol] = quote['quote'].get('changePercent', None)
    return percent_change

def losers(changes, threshold):
    losers = {}
    for symbol, percent in changes.items():
        if percent < -1*threshold:
            losers[symbol] = round(percent, 2)
    return losers

def winners(changes, threshold):
    winners = {}
    for symbol, percent in changes.items():
        if percent > threshold:
            winners[symbol] = round(percent, 2)
    return winners

changes = get_percent_change(args.symbols)
l = losers(changes, args.threshold)
print "Losers: "+str(l)
w = winners(changes, args.threshold)
print "Winner: "+str(w)
