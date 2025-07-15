import requests
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import os


class F1DataProcessor:

    def __init__(self, cache_dir: str = "f1_cache"):

        self.base_url = "http://ergast.com/api/f1"
        self.cache_dir = cache_dir
        self.cache_duration = 3600
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent' : 'F1DataProcessor/1.0'
        })
        
        
        # Create cache directory if it doesn't exist

        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)