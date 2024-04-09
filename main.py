import json
import os


class PolicyVerifier:
    @staticmethod
    def verify_iam_policy(json_file: str) -> bool | str:
        try:
            if os.path.splitext(json_file)[1].lower() == '.json':
                with open(json_file, 'r') as f:
                    file_content = f.read()
                    if not file_content.strip():
                        raise ValueError(f'File is empty')

                    data = json.loads(file_content)

                    statement = data.get('PolicyDocument', {}).get('Statement', [])
                    if not statement:
                        raise ValueError(f'Statement is empty')

                    for item in statement:
                        resource = item.get('Resource', '')
                        if resource == '*':
                            return False

                    return True
            else:
                return f'File {json_file} is not a JSON file'
        except FileNotFoundError:
            return f'File {json_file} not found.'
        except Exception as e:
            return f'Error {e}'


if __name__ == '__main__':
    # Examples
    policy_verifier = PolicyVerifier()
    file = 'files/one_asterix_file.json'
    print(f'One asterix : {policy_verifier.verify_iam_policy(json_file=file)}')

    file2 = 'files/two_asterix_file.json'
    print(f'Two asterix : {policy_verifier.verify_iam_policy(json_file=file2)}')

    file3 = 'files/zero_asterix_file.json'
    print(f'Zero asterix : {policy_verifier.verify_iam_policy(json_file=file3)}')

    file4 = 'files/resource_not_asterix_file.json'
    print(f'Resource field with text not asterix: {policy_verifier.verify_iam_policy(json_file=file4)}')

    file5 = 'files/file_without_statement.json'
    print(f'File without statement: {policy_verifier.verify_iam_policy(json_file=file5)}')

    file6 = 'files/non_existent_file.json'
    print(f'File not found: {policy_verifier.verify_iam_policy(json_file=file6)}')

    file7 = 'files/file.txt'
    print(f'Not json type file: {policy_verifier.verify_iam_policy(json_file=file7)}')

    file8 = 'files/empty_file.json'
    print(f'Empty file: {policy_verifier.verify_iam_policy(json_file=file8)}')
