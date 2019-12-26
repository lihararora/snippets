import argparse
import requests
import ConfigParser
from datetime import date
from dateutil.relativedelta import relativedelta

parser = argparse.ArgumentParser(description='Get stock data')
parser.add_argument('type', help='Type of info requested')
parser.add_argument('stocks', help='Stock tickers')
parser.add_argument('--lookback', help='Number of years to look back', type=int, default=24)
args = vars(parser.parse_args())

configParser = ConfigParser.RawConfigParser()
configFilePath = r'config.ini'
configParser.read(configFilePath)

ALPHA_API_KEY = configParser.get('API_KEYS', 'ALPHA')
IEX_API_KEY_SANDBOX = configParser.get('API_KEYS', 'IEX_SANDBOX')
IEX_API_KEY_PROD = configParser.get('API_KEYS', 'IEX_PROD')

HIGH_KEY = "2. high"
LOW_KEY = "3. low"
DIVIDEND_KEY = "7. dividend amount"

stocks = args['stocks'].split(',')
print stocks

def get_dividend_high_low(stock,lookback):
    #Return dividend info and "lookback" high and low for a given "stock"
    data = {}
    complete_data = {}
    r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol="+stock+"&apikey="+ALPHA_API_KEY)
    result_data = r.json()
    time_series = result_data.get("Monthly Adjusted Time Series", None)
    if time_series is None:
        return
    ordered_keys = time_series.keys()
    ordered_keys.sort(reverse=True)
    all_time_high = float(time_series[ordered_keys[0]][HIGH_KEY])
    all_time_low = float(time_series[ordered_keys[0]][LOW_KEY])
    lookback_high = float(time_series[ordered_keys[0]][HIGH_KEY])
    lookback_low = float(time_series[ordered_keys[0]][LOW_KEY])
    lookback_date = str(date.today() - relativedelta(months=lookback))
    one_year_lookback_date = str(date.today() - relativedelta(months=12))
    dividends = dict()
    for k in ordered_keys:
        d = float(time_series[k][DIVIDEND_KEY])
        high = float(time_series[k][HIGH_KEY])
        low = float(time_series[k][LOW_KEY])
        if high > all_time_high:
            all_time_high = high
        if low < all_time_low:
            all_time_low = low
        if k > lookback_date and high > lookback_high:
            lookback_high = high
        if k > lookback_date and low < lookback_low:
            lookback_low = low
        if k > one_year_lookback_date and d > 0:
            dividends[k] = d
    data["all_time_high"] = all_time_high
    data["all_time_low"] = all_time_low
    data["lookback_high"] = lookback_high
    data["lookback_low"] = lookback_low
    data['dividends'] = dividends
    complete_data[stock] = data
    return complete_data

def get_stats(stock):
    data = {}
    complete_data = {}
    r = requests.get("https://sandbox.iexapis.com/stable/stock/"+stock+"/stats?token="+IEX_API_KEY_SANDBOX)
    #r = requests.get("https://cloud.iexapis.com/stable/stock/"+stock+"/stats?token="+IEX_API_KEY_PROD)
    result_data = r.json()
    if not isinstance(result_data,dict):
        return complete_data
    next_dividend_date = result_data.get("nextDividendDate", None)
    pe_ratio = result_data.get("peRatio", None)
    next_earnings_date = result_data.get("nextEarningsDate", None)
    five_day_change = result_data.get("day5ChangePercent", None)
    shares_outstanding = result_data.get("sharesOutstanding", None)
    dividend_yield = result_data.get("dividendYield", None)
    employees = result_data.get("employees", None)
    market_cap = result_data.get("marketcap", None)
    data["next_dividend_date"] = next_dividend_date
    data["pe_ratio"] = pe_ratio
    data["next_earnings_date"] = next_earnings_date
    data["five_day_change"] = five_day_change
    data["shares_outstanding"] = shares_outstanding
    data["dividend_yield"] = dividend_yield
    data["employees"] = employees
    data["market_cap"] = market_cap
    complete_data[stock] = data
    return complete_data

def get_stocktwits(stock):
    trusted_sources = ["AnalystRatingsNetwork","newsfilter","MarketBeatInsiderTrades","risenhoover","livetraderalerts"]
    data = {}
    complete_data = {}
    r = requests.get("https://api.stocktwits.com/api/2/streams/symbol/"+stock+".json")
    result_data = r.json()
    messages = result_data.get("messages", None)
    for m in messages:
        user = m.get("user", None)
        if user["username"] in trusted_sources:
            data[user["username"]] = m["body"]
    complete_data[stock] = data
    return complete_data



if args['type'] == 'dividend':
    for stock in stocks:
        data = get_dividend_high_low(stock,args['lookback'])
        print data

if args['type'] == 'stats':
    for stock in stocks:
        data = get_stats(stock)
        print data

if args['type'] == 'stocktwits':
    for stock in stocks:
        data = get_stocktwits(stock)
        print data
