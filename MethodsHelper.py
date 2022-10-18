
class MethodsHelper:
    def get_parameters_list(line):
        after_name = line.split("(")
        cleaned_parameters = after_name[1].replace(")","")
        parameters_with_space = cleaned_parameters.split(",")
        parameters = []
        for parameter in parameters_with_space:
            parameter = parameter.strip()
            parameter = parameter.replace('\n', "")
            parameters.append(parameter)
        
        return parameters


    def clean_method_name(line):
        space_split = line.split(" ", 2)
        method_name = space_split[2].split("(", 1)[0]
        return method_name
    

    def get_return_type(line):
        after_public = line.split("public", 1)
        return after_public[1].strip().split(" ")[0]
    

    def get_mocked_session_query(lines, start_index):
        session_code_block = []
        for i in range(start_index, len(lines)):
            session_code_block.append(lines[i])
            if ";" in lines[i]:
                break
        
        return MethodsHelper.replace_mock_session_code(session_code_block)
    

    def replace_mock_session_code(session_code):
        mocked_code = []
        first_line = session_code[0].split("=")
        mocked_code.append(f"_ ={first_line[1].lower()}")

        for line in session_code:
            if "Session" not in line:
                if ";" in line:
                    line = line.replace(";",".ReturnsForAnyArgs(expectedResult);")
                mocked_code.append(line)
        
        return mocked_code
    

    def get_test_method_name(method_name, return_type):
        test_name = ""
        upper_counter = 0
        last_test_name_part = "ShouldReturn"+return_type
        for index, character in enumerate(method_name):
            if character.isupper():
                upper_counter += 1
            
            if upper_counter == 2:
                first_part_name = method_name[0:index]
                final_part_name = method_name[index:len(method_name)]
                if first_part_name[index-1] == 't':
                    test_name = first_part_name + "ting" + final_part_name + last_test_name_part
                else:
                    test_name = first_part_name + "ing" + final_part_name + last_test_name_part
                
                return test_name        
            