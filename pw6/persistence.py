import pickle
import os
import gzip

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR,"data.gz")

def save(manager):
    with gzip.open(DATA_FILE,'wb') as f:
        pickle.dump(manager,f)

def load():
    if not os.path.exists(DATA_FILE):
        return None
    with gzip.open(DATA_FILE,'rb') as f:
        return pickle.load(f)