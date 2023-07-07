# Task 2
# The sys module.
# The “sys.path” list is initialized from the PYTHONPATH environment variable. Is it possible to change it from within Python? If so, does it affect where Python looks for module files? Run some interactive tests to find it out.

import sys 
print(sys.path)

sys.path.append('c:\\Users\\Asus\\Desktop\\beetroot\\homework\\hw_9\\hw9_task2_module') # додаєм
print(sys.path)

import hw9_task2_module
sys.path.remove('c:\\Users\\Asus\\Desktop\\beetroot\\homework\\hw_9\\hw9_task2_module')  # видаляєм
print(sys.path)


