import unittest
import csv
import tempfile
from pathlib import Path
from csv_cleaner import remove_duplicates, remove_empty_rows, validate_row, validate_rows, read_csv, save_csv, backup_csv

class TestCSVFunctions(unittest.TestCase):

    def test_remove_duplicates(self):
        rows = [
            ["Alex", "20", "Moscow"],
            ["Bob", "25", "Kazan"],
            ["Alex", "20", "Moscow"]
        ]

        result = remove_duplicates(rows)

        expected = [
            ["Alex", "20", "Moscow"],
            ["Bob", "25", "Kazan"]
        ]

        self.assertEqual(result, expected)

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_no_duplicates(self):
        rows = [["Alex"], ["Bob"], ["Charlie"]]
        self.assertEqual(remove_duplicates(rows), rows)

    def test_all_duplicates(self):
        rows = [["Alex"], ["Alex"], ["Alex"]]
        self.assertEqual(remove_duplicates(rows), [["Alex"]])

    def test_remove_empty_rows(self):
        rows = [
            ["Alex", "20", "Moscow"],
            ["", "", ""],
            ["Bob", "25", "Kazan"]
        ]

        expected = [
            ["Alex", "20", "Moscow"],
            ["Bob", "25", "Kazan"]
        ]

        self.assertEqual(remove_empty_rows(rows), expected)

    def test_whitespace_rows(self):
        rows = [
            ["   ", " ", ""],
            ["Alex", "20", "Moscow"]
        ]

        expected = [
            ["Alex", "20", "Moscow"]
        ]

        self.assertEqual(remove_empty_rows(rows), expected)

    def test_no_empty_rows(self):
        rows = [["Alex", "20", "Moscow"], ["Bob", "25", "Kazan"]]

        self.assertEqual(remove_empty_rows(rows), rows)

    def test_valid_row(self):
        row = ["Alex", "20", "Moscow"]
        self.assertTrue(validate_row(row))

    def test_empty_name(self):
        row = ["", "20", "Moscow"]
        self.assertFalse(validate_row(row))

    def test_invalid_age(self):
        row = ["Alex", "abc", "Moscow"]
        self.assertFalse(validate_row(row))

    def test_negative_age(self):
        row = ["Alex", "-5", "Moscow"]
        self.assertFalse(validate_row(row))

    def test_missing_city(self):
        row = ["Alex", "20", ""]
        self.assertFalse(validate_row(row))

    def test_wrong_number_of_columns(self):
        row = ["Alex", "20"]
        self.assertFalse(validate_row(row))

    def test_validate_rows(self):
        rows = [
            ["Alex", "20", "Moscow"],
            ["Bob", "abc", "Kazan"],
            ["Charlie", "19", "Perm"]
        ]

        valid, invalid = validate_rows(rows)

        self.assertEqual(len(valid), 2)
        self.assertEqual(len(invalid), 1)
        self.assertEqual(invalid[0], ["Bob", "abc", "Kazan"])


    def test_validate_rows_empty(self):
        valid, invalid = validate_rows([])

        self.assertEqual(valid, [])
        self.assertEqual(invalid, [])

    def test_read_csv(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "test.csv"
            file_path.write_text(
                "name,age,city\nAlex,20,Moscow\n",
                encoding="utf-8"
            )

            result = read_csv(file_path)

            expected = [
                ["name", "age", "city"],
                ["Alex", "20", "Moscow"]
            ]

            self.assertEqual(result, expected)


    def test_read_missing_file(self):
        result = read_csv("file_that_does_not_exist.csv")
        self.assertIsNone(result)

    def test_save_csv(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "result.csv"

            rows = [
                ["name", "age", "city"],
                ["Alex", "20", "Moscow"]
            ]

            result = save_csv(rows, file_path)

            self.assertTrue(result)

            with open(file_path, "r", encoding="utf-8", newline="") as file:
                saved_rows = list(csv.reader(file))

            self.assertEqual(saved_rows, rows)


    def test_save_empty_csv(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "empty.csv"

            result = save_csv([], file_path)

            self.assertTrue(result)
            self.assertTrue(file_path.exists())
            self.assertEqual(file_path.read_text(encoding="utf-8"), "")

    def test_backup_csv(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "data.csv"
            source.write_text("name,age,city\nAlex,20,Moscow\n", encoding="utf-8")

            result = backup_csv(source)

            self.assertIsNotNone(result)
            self.assertTrue(result.exists())
            self.assertEqual(result.read_text(encoding="utf-8"), source.read_text(encoding="utf-8"))


    def test_backup_missing_file(self):
        result = backup_csv("missing_file.csv")

        self.assertIsNone(result)

    def test_whitespace_name(self):
        self.assertFalse(validate_row(["   ", "20", "Moscow"]))

    def test_whitespace_city(self):
        self.assertFalse(validate_row(["Alex", "20", "   "]))

    def test_zero_age(self):
        self.assertFalse(validate_row(["Alex", "0", "Moscow"]))

    def test_save_missing_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "missing" / "result.csv"

            result = save_csv([["Alex", "20", "Moscow"]], file_path)

            self.assertFalse(result)
            self.assertFalse(file_path.exists())
if __name__ == "__main__":
    unittest.main()