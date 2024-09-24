import json
import re

def load_json_data(file_path):
      with open(file_path, 'r') as file:
            content = file.read()
      #Split the json file content into json objects by using regex
      json_objects = re.findall(r'\{.*?\}(?=\s*\{|\s*$)', content, re.DOTALL)
      return [json.loads(obj) for obj in json_objects]