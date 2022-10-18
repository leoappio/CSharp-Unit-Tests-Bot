from asyncore import write
from enumType import Type


class TestMethodBuilder:
    def __init__(self, test_name, parameters, return_type, method_type, object_variable_name, original_method_name, class_name, mock_session) -> None:
        self.file = open("csFiles/result.cs", "a")
        self.test_name = test_name
        self.parameters = parameters
        self.return_type = return_type
        self.type = method_type
        self.object_variable_name = object_variable_name
        self.original_method_name = original_method_name
        self.class_name = class_name
        self.mock_session = mock_session
        self.parameters_name_string = self.build_parameters_name_string()
        self.tab = "    "
    

    def build(self):
        self.erase_file()
        self.add_test_method_annotation()
        self.add_test_signature()
        self.add_curly_braces()
        self.add_arrange_comment()
        self.add_substitutes_lines()
        self.add_blank_line()
        self.add_parameters_lines()
        self.add_blank_line()
        self.add_expected_result()
        self.add_blank_line()
        self.add_mock_session_line()
        self.add_blank_line()
        self.add_act_comment()
        self.add_method_call_line()
        self.add_blank_line()
        self.add_assert_comment()
        self.add_asserts_lines()
        self.close_curly_braces()
        self.file.close()
    

    def build_parameters_name_string(self):
        parameters_string =""
        for parameter in self.parameters:
            parameter_splitted = parameter.split(" ")
            if len(parameters_string) == 0:
                parameters_string = parameter_splitted[1]
            else:
                parameters_string += ", "+parameter_splitted[1]
        
        return parameters_string


    def erase_file(self):
        file = open('csFiles/result.cs', 'r+')
        file.truncate(0)
        file.close()


    def add_test_method_annotation(self):
        self.file.write('[TestMethod]\n')
    

    def add_test_signature(self):
        self.file.write(f'public void {self.test_name}()\n')
    

    def add_curly_braces(self):
        self.file.write("{\n")
    

    def close_curly_braces(self):
        self.file.write("}\n")
    
    
    def add_arrange_comment(self):
        self.file.write(f"{self.tab}//Arrange\n")
    

    def add_substitutes_lines(self):
        if self.type == Type.REPOSITORY:
            self.file.write(f"{self.tab}var session = Substitute.For<ISession>();\n")
            self.file.write(f"{self.tab}var {self.object_variable_name} = new {self.class_name[0]}(session);\n")

    

    def add_parameters_lines(self):
        for parameter in self.parameters:
            type, name = parameter.split(" ")
            self.write_variable_mock(type, name)
    

    def get_mock_default_value(self, line):
        values = {"string":"\"AAA\"", "double": 1111, "int": 1111, "bool": "true"}

        for key,value in values.items():
            if key in line:
                return value

    
    def write_variable_mock(self, variable_type, variable_name):
        value = self.get_mock_default_value(variable_type)
        if "IEnumerable" in variable_type or "IList" in variable_type:
            if value is None:
                type_list = variable_type.replace("IEnumerable", "", 1)
                type_list = type_list.replace("IList", "", 1)
                type_list = type_list.replace("<","")
                type_list = type_list.replace(">","")
                value = f"new {type_list}()"
            
            type = variable_type.replace("IEnumerable", "List", 1)
            type = type.replace("IList", "List", 1)
            self.file.write(f"{self.tab}var {variable_name} = new {type}\n")
            self.file.write(f"{self.tab}""{""\n")
            self.file.write(f"{self.tab}{self.tab}{value}\n")
            self.file.write(f"{self.tab}""};""\n")
        else:
            if value is not None:
                self.file.write(f"{self.tab}var {variable_name} = {value};\n")
            else:
                self.file.write(f"{self.tab}var {variable_name} = new {variable_type}();\n")


    def add_expected_result(self):
        self.write_variable_mock(self.return_type, "expectedResult")
    

    def add_mock_session_line(self):
        self.file.write(f"{self.tab}{self.mock_session[0]}")
        for line in self.mock_session[1:len(self.mock_session)]:
            self.file.write(f"{line[4:len(line)]}")
    

    def add_act_comment(self):
        self.file.write(f"{self.tab}//Act\n")
    

    def add_method_call_line(self):
        self.file.write(f"{self.tab} var result = {self.object_variable_name}.{self.original_method_name}({self.parameters_name_string});\n")
    

    def add_blank_line(self):
        self.file.write("\n")


    def add_assert_comment(self):
        self.file.write(f"{self.tab}//Assert\n")
    

    def add_asserts_lines(self):
        self.file.write(f"{self.tab}using (new AssertionScope())\n")
        self.file.write(f"{self.tab}""{""\n")
        self.file.write(f"{self.tab}{self.tab}_ = result.Should().BeEquivalentTo(expectedResult);\n")
        self.file.write(f"{self.tab}""}""\n")
