import os, sys
import datetime
import time
from colorama import init
init()
from colorama import Fore, Back, Style

from learning_lib.parsers.findata_parsers.binance_realtime import BinanceRealtimeParser, concat
from learning_lib.parsers.news_parsers.coindesk_realtime import CoinDeskRealTimeParser
from learning_lib.models.lstm import LSTMModel
from learning_lib.models.nlp import NLPModel, RegressionHead
from learning_lib.models.merge_predictions import PredictionMerger
from learning_lib.utils.strategy_update import StrategyUpdater
from server import Server
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings("ignore")

IMPORT_FINDATA = False
IMPORT_NEWSDATA = False

#TODO: 
# Инициализация парсеров done
# Инициализация моделей done
# Поддержка сервера done
# Поток передачи данных с моделей на сервер

binance_parser = BinanceRealtimeParser()
coin_parser = CoinDeskRealTimeParser()
lstm_model = LSTMModel()
nlp_model = NLPModel(
    model_path="src/learning_lib/models/NLPmodels/NLP_model.pth",
    tokenizer_path="src/learning_lib/models/NLPmodels/tokenizer",
    valid_tickers_list_path="src/learning_lib/models/NLPassets/tokens_names.txt",
    tickers_order_path="src/learning_lib/models/NLPassets/tokens_order.txt"
)
merger = PredictionMerger()
updater = StrategyUpdater()
server = Server()

cols = ["open", "high", "low", "close", "baseVolume", "quoteVolume",
        "numTrades", "takerBuyBaseVolume", "takerBuyQuoteVolume"]

if __name__ == "__main__":
    with open("src/learning_lib/parsers/findata_parsers/tokens_names.txt") as f:
        tick = [line.strip() for line in f.readlines()]
    binance_parser.init(tick, EXPORT=True)
    coin_parser.init(EXPORT=True)

    if IMPORT_NEWSDATA:
        coin_parser._import("coindesk_news.json")
    else:
        print("importing data from coindesk_news.json" + Fore.YELLOW, "skip", Style.RESET_ALL)

    if IMPORT_FINDATA:
        binance_parser._import(None)
    else:
        print(f"importing data from src/data" + Fore.YELLOW, "skip", Style.RESET_ALL)
    
    server.start()

    num = 10

    try:
        findata = concat(binance_parser.request(None), tick)
    except Exception as e:
        print(f"parsing last {num} candles..", Fore.RED + "error")
        print(str(e) + Style.RESET_ALL)
    else:
        print(f"parsing last {num} candles..", Fore.GREEN + "done" + Style.RESET_ALL)

    coin_parser.start()
    binance_parser.start()

    time.sleep(1)
    сpred = np.array([.0 for i in range(120)], dtype=np.float32)
    merged = np.array([.0 for i in range(120)], dtype=np.float32)
    while True:
        x = False
        if coin_parser.done:
            x = True
            data = list(map(lambda x: x[2], list(coin_parser.fetch().values())))[0]
            cpred = nlp_model.predict(data)
            print(cpred)
        if binance_parser.done:
            x = True
            data = binance_parser.fetch()
            d = concat(data, tick)
            #print(d.info())
            #print([t + "_close" for t in tick])
            df = pd.DataFrame(columns=[t + "_close" for t in tick])
            for t in tick:
                df[t + "_close"] = d[t + "_close"]
            updater.update(merged, df.to_numpy()[0])
            findata = pd.concat([findata, d])
            findata = findata.iloc[1:]
            pred = lstm_model.predict(findata)
            #print(pred)
            merged = merger.merge(pred, cpred)
            print(merged)
        if not x:
            time.sleep(1)

"""
{
    "data": {
        "pnl": "$21",
        "sharp": "1.4",
        "profit_margin": "18.0",
        "max_drawdown": "10%",
        "turnover": "6.0"
    }
}
"""