import json
from pydantic import BaseModel, field_validator
from rich import print

class Statement(BaseModel):
    Sid: str
    Effect: str
    Action: list
    Resource: str

    @field_validator('Resource')
    def check_resource(cls, value):
        required_content = '*'
        if value == required_content:
            return False
        return True

class PolicyDocument(BaseModel):
    Version: str
    Statement: list[Statement]

class Resource(BaseModel):
    PolicyName: str
    PolicyDocument: PolicyDocument

def get_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def main():
    file_path = r'XXX'
    data = get_data_from_file(file_path)

    pydantic_item = Resource(**data)  
    print(pydantic_item)


if __name__ == '__main__':
    main()
