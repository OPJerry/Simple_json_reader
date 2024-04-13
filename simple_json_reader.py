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
        pd = data['PolicyDocument']
        if_statement = pd['Statement']
        unpak_list = if_statement[0]
        iam = unpak_list['Action']
        check_aim = any('iam' in _ for _ in iam)
        if check_aim:
            print('jest')
        else:
            print('nie jest')
        if 'Statement' in data['PolicyDocument']:
            for statement in data['PolicyDocument']['Statement']:
                if 'Resource' in statement and statement['Resource'] == '*':
                    return False
    return True
            

def main():
    path = r'C:\Users\jerem\Desktop\Projekty git\json\Simple_json_reader\example.json'
    print(verify_json(path))
    

if __name__ == '__main__':
    main()