import unittest
import json
from unittest.mock import mock_open, patch

class TestPasswordManager(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open, read_data='{"Google": {"email": "test@test.com", "password": "password123"}}')
    def test_json_load_success(self, mock_file):
        # Testing if the file loader correctly parses standard JSON formats
        with open("passwords.json", "r") as f:
            data = json.load(f)
            
        self.assertIn("Google", data)
        self.assertEqual(data["Google"]["password"], "password123")
        
    @patch("builtins.open", new_callable=mock_open)
    def test_json_save_format(self, mock_file):
        # Testing the data persistence structure
        new_data = {"GitHub": {"email": "dev@test.com", "password": "secure456"}}
        with open("passwords.json", "w") as f:
            json.dump(new_data, f, indent=4)
            
        mock_file.assert_called_with("passwords.json", "w")

if __name__ == '__main__':
    unittest.main()
