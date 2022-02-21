import time, sys
indent = 0 # How many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 0.1 seconds

        if indentIncreasing:
            # Increase the number of spaces:
            indent += 1
            if indent == 5:
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent -= 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()