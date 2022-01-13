

import getopt, sys

cmd_args = sys.argv[1:]


#print (cmd_args)


short_options = "ha:v"
long_options = ["help", "auto", "verbose"]


try:
    arguments, values = getopt.getopt(cmd_args, short_options, long_options)
except getopt.error as err:
    print (str(err))
    sys.exit(2)
for current_argument, current_value in arguments:
    if current_argument in ("-v", "--verbose"):
        print ("Enabling verbose mode")
    elif current_argument in ("-h", "--help"):
        print("""/
| |__   ___| |_ __  
| '_ \ / _ \  | '_ \ 
| | | |  __/  | |_) |
|_| |_|\___|_| .__/ 
              |_|    
              """)
        print ("a --auto -xrandr auto set to mirror display \n rr -right secondary monitor to right")
    elif current_argument in ("-o", "--output"):
        print (("Enabling special output mode (%s)") % (current_value))