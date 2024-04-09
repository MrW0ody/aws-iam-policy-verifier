from main import PolicyVerifier


class TestPolicyVerifier:
    policy_verifier = PolicyVerifier()

    def test_verify_iam_policy_one_asterix(self):
        file = 'files/one_asterix_file.json'
        assert self.policy_verifier.verify_iam_policy(file) == False

    def test_verify_iam_policy_two_asterix(self):
        file = 'files/two_asterix_file.json'
        assert self.policy_verifier.verify_iam_policy(file) == True

    def test_verify_iam_policy_zero_asterix(self):
        file = 'files/zero_asterix_file.json'
        assert self.policy_verifier.verify_iam_policy(file) == True

    def test_verify_iam_policy_without_statement(self):
        file = 'files/file_without_statement.json'
        assert self.policy_verifier.verify_iam_policy(file) == f'Error Statement is empty'

    def test_verify_iam_policy_with_no_existing_file(self):
        file = 'files/non_existent_file.json'
        assert self.policy_verifier.verify_iam_policy(file) == f'File {file} not found.'

    def test_verify_iam_policy_with_no_json_file(self):
        file = 'files/file.txt'
        assert self.policy_verifier.verify_iam_policy(file) == f'File {file} is not a JSON file'

    def test_verify_iam_policy_empty_file(self):
        file = 'files/empty_file.json'
        assert self.policy_verifier.verify_iam_policy(file) == 'Error File is empty'
