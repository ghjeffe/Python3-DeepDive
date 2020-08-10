import sys
import types
import os.path

print('Running importer.py')

def import_(module_name, module_file, module_path):
    if module_name in sys.modules:
        return sys.modules[module_name]

    module_name = 'module1'
    module_file = 'module1_source.py'
    module_path = '.'
    
    module_rel_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)
    
    with open(module_rel_file_path, 'r') as code_file:
        source_code = code_file.read()
    
    #create module object
    mod = types.ModuleType(module_name)
    mod.__file__ = module_abs_file_path
    
    #set a ref in sys.modules
    sys.modules[module_name] = mod
    
    #compile source code
    code = compile(source_code, filename=module_abs_file_path, mode='exec')
    
    #execute compiled source code
    exec(code, mod.__dict__)
    
    return sys.modules[module_name]
