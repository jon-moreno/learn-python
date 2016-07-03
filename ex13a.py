from sys import argv

user_in = raw_input("Write something.")

argv.extend(user_in)

#argv = raw_input("Give me some arguments ")

print argv