from MethodsHelper import MethodsHelper
from TestMethodBuilder import TestMethodBuilder
from enumType import Type            

class Main:
    def __init__(self) -> None:
        self.type = Type.REPOSITORY

        self.file = open('csFiles/method.cs', 'r')
        self.interfaces_to_mock = []
        self.method_name = ""
        self.test_method_name = ""
        self.parameters = []
        self.method_return_type = ""
        self.lines = self.file.readlines()
        self.mock_session = []
    
    def generate_test(self):
        for line in self.lines:
            if type == Type.REPOSITORY:
                self.interfaces_to_mock.append("ISession")
            
            if "public" in line:
                line_after_public = line.split("public", 1)
                self.method_name = MethodsHelper.clean_method_name(line_after_public[1])

                #getting parameters
                self.parameters = MethodsHelper.get_parameters_list(line)

                #getting return types
                self.method_return_type = MethodsHelper.get_return_type(line)

                #getting test method name
                if 'IEnumerable' in self.method_return_type:
                    self.test_method_name = MethodsHelper.get_test_method_name(self.method_name, "List")
                else:
                    self.test_method_name = MethodsHelper.get_test_method_name(self.method_name, self.method_return_type)
   
            if " = Session" in line:
                #getting returns to mock
                initial_session_index = self.lines.index(line)
                self.mock_session = MethodsHelper.get_mocked_session_query(self.lines, initial_session_index)
        
        builder = TestMethodBuilder(self.test_method_name, self.parameters, self.method_return_type, self.type)
        builder.build()
        self.file.close()


main = Main()
main.generate_test()