#Exceptions
#TypeError, ValueError, KeyError, SyntaxError

#try-except-finally-else

try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
except (ValueError, Exception) as e:
    print(e)
else:
    print("Success")
finally:
    print("Alway run")
    
print(1 or (1/0))

#modules
