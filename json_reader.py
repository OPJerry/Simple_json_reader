import json
from pydantic import BaseModel, field_validator
from rich import print

class Statement(BaseModel):
    """
    Represents a statement - one of attribute in a PolicyDocument.

    Attributes:
    Sid (str):
    Effect (str):
    Action (list):
    Resource (str):

    Validators:
    check_resource: Validates the Resource attribute to ensure it is not '*'.
    """
    Sid: str
    Effect: str
    Action: list
    Resource: str

    @field_validator('Resource')
    def check_resource(cls, value):
        """
        Validator to check the Resource attribute.

        The Resource attribute should not be '*'. If it is, this method returns False.

        Parameters:
        value (str):

        Returns:
        bool: True if the Resource is valid, False otherwise.
        """
        required_content = '*'
        if value == required_content:
            return False
        return True

class PolicyDocument(BaseModel):
    """
    Represents a policy document.

    Attributes:
    Version (str):
    Statement (list[Statement]):
    """
    Version: str
    Statement: list[Statement]

class Resource(BaseModel):
    """
    Represents a Resource containing policy information.

    Attributes:
    PolicyName (str):
    PolicyDocument (PolicyDocument): The policy document containing statements.
    """
    PolicyName: str
    PolicyDocument: PolicyDocument

def get_data_from_file(file_path):
    """
    Load JSON data from a file.

    Parameters:
    file_path (str): The path to the JSON file.

    Returns:
    dict: The loaded JSON data as a dictionary.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def main():
    """
    Main function to load and print data from a JSON file using Pydantic.

    Modify the `file_path` variable to specify the path to the JSON file.

    Example:
    file_path = r'/path/to/your/file.json'

    Returns:
    Printed JSON file
    With marked Bool values of Resource accordingly to the conditions. 
    """
    file_path = r'XXX'
    data = get_data_from_file(file_path)

    pydantic_item = Resource(**data)  
    print(pydantic_item)


if __name__ == '__main__':
    main()
