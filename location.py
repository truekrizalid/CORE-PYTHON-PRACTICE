# set default values:
s0=v0=0; a=t=1
import getopt,sys
options,args = getopt.getopt(sys.argv[1:],'sss',
                 ['t=','s0=','v0=','a='])
print(options)
print(args)