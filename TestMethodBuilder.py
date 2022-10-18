class TestMethodBuilder:
    def __init__(self, test_name, parameters, return_type, method_type) -> None:
        self.file = open("csFiles/result.cs", "a")
        self.test_name = test_name
        self.parameters = parameters
        self.return_type = return_type
        self.type = method_type
    

    def build(self):
        self.erase_file()
        self.add_test_method_annotation()
        self.add_test_signature()
        self.add_curly_braces()
        self.file.close()


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
