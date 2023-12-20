from functions import salary,hello_who

assert hello_who('Max') == 'Hello,Max', 'hello who error'
assert  hello_who('Leo') == 'Helo Leo', 'hello who error'
assert  hello_who('Nikita') == 'Helo Nikita', 'hello who error'
assert salary(2,1) == 4
assert salary(2,2) == 8