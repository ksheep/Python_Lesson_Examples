# Exception Hierarchy
#
# BaseException
# +-- SystemExit
# +-- KeyboardInterrupt
# +-- GeneratorExit
# +-- Exception
#     +-- StopIteration
#     +-- StandardError
#     |   +-- BufferError
#     |   +-- ArithmeticError
#     |   |   +-- FloatingPointError
#     |   |   +-- OverflowError
#     |   |   +-- ZeroDivisionError
#     |   +-- AssertionError
#     |   +-- AttributeError
#     |   +-- EnvironmentError
#     |   |   +-- IOError
#     |   |   +-- OSError
#     |   +-- EOFError
#     |   +-- ImportError
#     |   +-- LookupError
#     |   |   +-- IndexError
#     |   |   +-- KeyError
#     |   +-- MemoryError
#     |   +-- NameError
#     |   |   +-- UnboundLocalError
#     |   +-- ReferenceError
#     |   +-- RuntimeError
#     |   |   +-- NotImplementedError
#     |   +-- SyntaxError
#     |   |   +-- IndentationError
#     |   |       +-- TabError
#     |   +-- SystemError
#     |   +-- TypeError
#     |   +-- ValueError
#     |       +-- UnicodeError
#     |           +-- UnicodeDecodeError
#     |           +-- UnicodeEncodeError
#     |           +-- UnicodeTranslateError
#     +-- Warning
#         +-- DeprecationWarning
#         +-- PendingDeprecationWarning
#         +-- RuntimeWarning
#         +-- SyntaxWarning
#         +-- UserWarning
#         +-- FutureWarning
#         +-- ImportWarning
#         +-- UnicodeWarning
#         +-- BytesWarning




#______________________Test Code_______________________


a = 10/0
b = a + c
 c = '2' + 2
d = [1, 2, 3, 4]

print d[3]
print d[6]

while True:
    try:
        x = int(raw_input("\nPlease enter a number: "))
        break
    except ValueError:
        print "That wasn't a valid number. Please try again."

#try:
#    raise NameError("This exception was raised")
#except:
#    print "A raised exception was caught!\n\n"
#    raise
#finally:
#    print "You have reached the end of the program\n\n"


#__________________Common Uses of Try______________________

# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except IOError:
#         pring "Cannon open", arg
#     else:
#         print arg, "has", len(f.readlines()), "lines"
#         f.close()


