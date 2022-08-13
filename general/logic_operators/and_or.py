"""
AND gives you the first value if it is FALSE, otherwise it gives the second value
OR  gives you the first value if it is TRUE,  otherwise it gives the second value
"""
name = ""
surname = "Smith"

greeting = name or f"Mr. {surname}"
print(greeting)
# output:
# Mr. Smith
