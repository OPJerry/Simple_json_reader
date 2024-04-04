import json
from rich import print

def verify_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        if 'Statement' in data['PolicyDocument']:
            for statement in data['PolicyDocument']['Statement']:
                if 'Resource' in statement and statement['Resource'] == '*':
                    return False
    return True
            

def main():
    path = r'C:\Users\Jerry\Desktop\Projekty\Simple_json_reader\example.json'
    print(verify_json(path))
    

if __name__ == '__main__':
    main()