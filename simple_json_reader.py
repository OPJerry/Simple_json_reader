import json
from rich import print

def verify_json(file_path):
    """
    Verify if the specified JSON file contains a valid AWS IAM Role Policy.

    Parameters:
    file_path (str): Path to the JSON file containing the IAM Role Policy.

    Returns:
    bool: True if the IAM Role Policy is valid, otherwise False.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
        if 'PolicyDocument' in data:
            pd = data['PolicyDocument']
            if 'Statement' in pd and pd['Statement']:
                first_statement = pd['Statement'][0]
                if 'Action' in first_statement:
                    actions = first_statement['Action']
                    if all('iam' in action for action in actions):
                        return True
        else:
            return False

def verify_resource(file_path):
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
    check = verify_json(path)
    if check == True:
        print('Data format is defined as AWS::IAM::Role Policy')
        print(verify_resource(path))
    else:
        raise ValueError('the data format is incorrect for the script to run')
    
    

if __name__ == '__main__':
    main()