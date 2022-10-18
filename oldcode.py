from ClassHelper import ClassHelper
from MethodsHelper import MethodsHelper
                

file = open('csFiles/exampleRepository.cs', 'r')
interfaces_to_mock = []
methods = []
class_name = ""
parameters = {}
methods_return_type = {}
lines = file.readlines()

for line in lines:
    if "class" in line:
        class_name = ClassHelper.get_class_name(line)
        if "Repository" in class_name:
            interfaces_to_mock.append("ISession")
    
    if "public" in line:
            line_after_public = line.split("public", 1)
            if  class_name not in line_after_public[1]:        
                #getting methods
                method_name = MethodsHelper.clean_method_name(line_after_public[1])
                methods.append(method_name)

                #getting parameters
                parameter_list = MethodsHelper.get_parameters_list(line)
                parameters[method_name] = parameter_list

                #getting return types
                return_type = MethodsHelper.get_return_type(line)
                methods_return_type[method_name] = return_type

                #getting returns to mock
                initial_method_index = lines.index(line)
                print(initial_method_index)

        

print(lines)