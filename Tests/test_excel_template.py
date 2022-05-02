import pytest
from prolog_code_generator import excel_template
import os 

class TestExcelTemplate:
        FILE_PATH = "Tests/test_data.csv"
        
        @pytest.fixture
        def absolute_path(self):
            return os.path.abspath(self.FILE_PATH)

        def test_get_template(self,absolute_path):
            
            test_list  = excel_template.get_template(absolute_path,delimiter=',')
            assert test_list == [
                ["name","Aarg1","aarg2","arg3"],
                ["NAME1","ARG1","ARG2","arg3"],
                ["NAME2","ARG4","ARG5","arg6"]
                ]

            
 
