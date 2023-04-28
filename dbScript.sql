
CREATE TABLE tblExchange
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exchangeDate VARCHAR(30),
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    adjClose REAL,
)

INSERT INTO exchangeRates (exchangeDate,open, high, low, close, adjClose) VALUES('2023-04-21',1.1046,1.1067,1.0996,1.1030,1.1030)
INSERT INTO exchangeRates (exchangeDate,open, high, low, close, adjClose) VALUES('2023-04-24',1.0978,1.1094,1.0969,1.0978,1.0978)
INSERT INTO exchangeRates (exchangeDate,open, high, low, close, adjClose) VALUES('2023-04-25',1.1059,1.1068,1.0969,1.1059,1.1059)
INSERT INTO exchangeRates (exchangeDate,open, high, low, close, adjClose) VALUES('2023-04-26',1.0992,1.1034,1.0969,1.0992,1.0992)
INSERT INTO exchangeRates (exchangeDate,open, high, low, close, adjClose) VALUES('2023-04-27',1.0971,1.0993,1.0940,1.0971,1.0971)