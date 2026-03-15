import json
import os 
from typing import Any, Dict

def read_json_file(file_path: str) -> Dict[str, Any]:
    with open (file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def get_expected_response(filename: str) -> Dict[str, Any]:
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, 'test', 'data', 'ecpected_responses', filename)
    return read_json_file(file_path)