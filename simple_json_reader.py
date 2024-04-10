import json
from rich import print

def verify_json(file_path):
    """
    Verify JSON file for specific conditions.

    Parameters:
    file_path (str): The path to the JSON file.

    Returns:
    bool: Return False if the key:'Resource' have value:'*', True otherwise.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
        if 'Statement' in data['PolicyDocument']:
            for statement in data['PolicyDocument']['Statement']:
                if 'Resource' in statement and statement['Resource'] == '*':
                    return False
    return True
            

def main():
    path = r'XXX'
    print(verify_json(path))
    

if __name__ == '__main__':
    main()