
import unittest
import os
import subprocess
from unittest.mock import patch

class TestFormatter(unittest.TestCase):

    def setUp(self):
        self.test_input_file = 'test_clippings.txt'
        with open(self.test_input_file, 'w', encoding='utf-8') as f:
            f.write("""
私たちはなぜ税金を納めるのか―租税の経済思想史―（新潮選書） (諸富 徹)
- Your Highlight on Location 67-70 | Added on Wednesday, July 12, 2023 12:02:51 AM

「国」というものは「税」なしには生きていけないのである。しかしながら、国家は自ら税収を生み出すことができない。となると、外から調達しなければならない。つまり、権力によって個人の私有財産に介入し、強制的に課税し徴収せざるを得ない。
==========
私たちはなぜ税金を納めるのか―租税の経済思想史―（新潮選書） (諸富 徹)
- Your Highlight on Location 224-224 | Added on Friday, July 14, 2023 12:00:09 AM

は、「国家は、『共同の困難』が生み出す財政需要から創成された」
==========
日清・日露戦争をどう見るか　近代日本と朝鮮半島・中国 (ＮＨＫ出版新書) (原 朗)
- Your Highlight on page 80 | Location 1165-1177 | Added on Sunday, August 6, 2023 11:23:02 PM

どんな戦争でもそうですが、日露戦争のときも、日清戦争と同じように、政府とメディアは日本の勝利を宣伝し、国民もそれに熱狂しました。開戦前からロシアと戦え、と絶叫する意見が高ま <You have reached the clipping limit for this item>
==========
日清・日露戦争をどう見るか　近代日本と朝鮮半島・中国 (ＮＨＫ出版新書) (原 朗)
- Your Highlight on page 89 | Location 1338-1352 | Added on Sunday, August 6, 2023 11:31:12 PM

 
==========
日清・日露戦争をどう見るか　近代日本と朝鮮半島・中国 (ＮＨＫ出版新書) (原 朗)
- Your Highlight on page 94 | Location 1407-1413 | Added on Sunday, August 6, 2023 11:34:32 PM

<You have reached the clipping limit for this item>
""")

    def tearDown(self):
        os.remove(self.test_input_file)

    def test_default_output(self):
        command = ['python3', 'formatter.py', '--input', self.test_input_file]
        result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
        output = result.stdout
        self.assertIn('# 私たちはなぜ税金を納めるのか―租税の経済思想史―（新潮選書） (諸富 徹)', output)
        self.assertIn('# 日清・日露戦争をどう見るか', output)
        self.assertIn('> 「国」というものは「税」なしには生きていけないのである。しかしながら、国家は自ら税収を生み出すことができない。となると、外から調達しなければならない。つまり、権力によって個人の私有財産に介入し、強制的に課税し徴収せざるを得ない。', output)

    def test_titles_output(self):
        command = ['python3', 'formatter.py', '--input', self.test_input_file, '--titles']
        result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
        output = result.stdout
        self.assertIn('1. 日清・日露戦争をどう見るか', output)
        self.assertIn('2. 私たちはなぜ税金を納めるのか―租税の経済思想史―（新潮選書） (諸富 徹)', output)

    def test_book_output(self):
        command = ['python3', 'formatter.py', '--input', self.test_input_file, '--book', '1']
        result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
        output = result.stdout
        self.assertIn('# 日清・日露戦争をどう見るか', output)
        self.assertNotIn('# 私たちはなぜ税金を納めるのか―租税の経済思想史―（新潮選書） (諸富 徹)', output)

    def test_empty_highlight(self):
        command = ['python3', 'formatter.py', '--input', self.test_input_file]
        result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
        output = result.stdout
        self.assertNotIn('Location 1338-1352', output)

if __name__ == '__main__':
    unittest.main()
