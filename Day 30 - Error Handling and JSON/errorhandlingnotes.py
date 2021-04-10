
# Goal: Open a file called "a_file.txt" and read its content.

try:
    file = open("a_file.txt")    # <---- try to open this file. If that fails (it doesn't exist, then do except block
    a_dictionary = {"key": "value"}
    print(a_dictionary["asdsf"])
except FileNotFoundError: #<--- add the type of error to except block so it isn't overly broad.
    file = open("a_file.txt", "w") #<--- and open in write mode, which will make the file.
    file.write("something")

except KeyError as error_message:  # <--- get ahold of message.
    print(f"The key {error_message} does not exist.")


else:        #<---- if everything in try succeeded with no exceptions, skip except block.
    content = file.read()
    print(content)

finally:
    file.close()  #<-- will close file, regardless of success (else block) or failure (except block)
    print("File was closed")

# "TRY this. If there are EXCEPTions, do this, ELSE if there are no exceptions, do this. FINALLY, do this regardless.
# Finally is not often used, but it can be helpful for cleanup.