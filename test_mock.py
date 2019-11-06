import unittest
from mock import patch
from budget import Budget


class MockTest(unittest.TestCase):

    @patch('budget_repo.BudgetRepo')
    def test_mock_repo(self, repo):
        repo.findAll.return_value = [Budget('2018-01', 1000)]
        self.assertEqual(1, len(repo.findAll()))


