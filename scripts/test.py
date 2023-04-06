import subprocess

# Call a shell script named 'myscript.sh' with argument 'arg1'

result = subprocess.run(['sh','/c/Users/mirac/OneDrive/Masaüstü/djangoms/django-start/scripts/test.sh'], stdout=subprocess.PIPE)