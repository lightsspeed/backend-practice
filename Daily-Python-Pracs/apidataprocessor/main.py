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

    def _get_cache_filename(self, endpoint: str, params: Dict = None) -> str:
        """Generate cache filename based on endpoint and parameters"""
        cache_key = endpoint
        if params:
            param_str = "_".join([f"{k}-{v}" for k, v in sorted(params.items())])
            cache_key += f"_{param_str}"
        return os.path.join(self.cache_dir, f"{cache_key.replace('/', '_')}.json")
    
    def _is_cache_valid(self, cache_file: str) -> bool:
        """Check if cache file exists and is still valid"""
        if not os.path.exists(cache_file):
            return False
        
        file_modified = os.path.getmtime(cache_file)
        return time.time() - file_modified < self.cache_duration
    
    def _load_from_cache(self, cache_file: str) -> Optional[Dict]:
        """Load data from cache file"""
        try:
            with open(cache_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Cache read error: {e}")
            return None
    
    def _save_to_cache(self, cache_file: str, data: Dict) -> None:
        """Save data to cache file"""
        try:
            with open(cache_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Cache write error: {e}")