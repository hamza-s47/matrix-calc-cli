import sys
from colorama import Fore, Back, Style, init
import utils.switch as method
from utils.tools import cli
from utils.help import help_commands, help_keys

args=sys.argv[1:]

if cli(args)[0] in ["--help", "-h"] and len(cli(args))==1:
    for x in help_keys:
        print(help_commands[x])
elif cli(args)[0] in help_keys and cli(args)[1] in ["--help", "-h"] and len(cli(args))==2:
    print(help_commands[cli(args)[0]])
elif (cli(args)[0] in ["d_type", "dimension", "length", "shape", "size", "summary"]) and (len(cli(args))==2):
    print(method.Inspect(cli(args)[0], cli(args)[1]))
elif cli(args)[0] in ["flatten", "ravel", "sort", "transpose"] and 2<=len(cli(args))<=3:
    if len(cli(args))==3:
        print(method.Manip(cli(args)[0], cli(args)[1], cli(args)[2]))
    else:
        print(method.Manip(cli(args)[0], cli(args)[1]))
elif cli(args)[0] in ["det", "inv", "magnitude", "rank","trace"] and len(cli(args))==2:
    print(method.Adv(cli(args)[0], cli(args)[1]))
elif cli(args)[0] in ["loadNpy", "saveNpy", "loadTxt", "saveTxt"] and 2<=len(cli(args))<=4:
    if len(cli(args))==3:
        print(method.FileSys(cli(args)[0], cli(args)[1], cli(args)[2]))
    elif len(cli(args))==4:
        print(method.FileSys(cli(args)[0], cli(args)[1], cli(args)[2], cli(args)[3]))
    else:
        print(method.FileSys(cli(args)[0], cli(args)[1]))
elif cli(args)[0] in ["add", "divide", "elementMul", "exp", "dot", "linear", "sqrt", "sin", "cos", "log", "scalarMul", "subtract"] and 2<=len(cli(args))<=3:
    if len(cli(args))==3:
        print(method.Arithmetic(cli(args)[0], cli(args)[1], cli(args)[2]))
    else:
        print(method.Arithmetic(cli(args)[0], cli(args)[1]))
elif cli(args)[0] in ["corr_coef", "cum_prod", "cum_sum", "max", "mean", "median", "min", "prod", "sum", "var", "std"] and 2<=len(cli(args))<=5:
    if len(cli(args))==3:
        print(method.Aggregate(cli(args)[0], cli(args)[1], cli(args)[2]))
    elif len(cli(args))==4:
        print(method.Aggregate(cli(args)[0], cli(args)[1], cli(args)[2], cli(args)[3]))
    elif len(cli(args))==5:
        print(method.Aggregate(cli(args)[0], cli(args)[1], cli(args)[2], cli(args)[3], cli(args)[4]))
    else:
        print(method.Aggregate(cli(args)[0], cli(args)[1]))
elif cli(args)[0] in ["ones", "constants", "eye", "linspace", "random", "arr_range", "zeros"] and 2<=len(cli(args))<=7:
    if len(cli(args))==3:
        print(method.Init(cli(args)[0], cli(args)[1], cli(args)[2]))
    elif len(cli(args))==4:
        print(method.Init(cli(args)[0], cli(args)[1], cli(args)[2], cli(args)[3]))
    elif len(cli(args))==5:
        print(method.Init(cli(args)[0], cli(args)[1], cli(args)[2], cli(args)[3], cli(args)[4]))
    elif len(cli(args))==6:
        print(method.Init(cli(args)[0], cli(args)[1], cli(args)[2], cli(args)[3], cli(args)[4], cli(args)[5]))
    elif len(cli(args))==7:
        print(method.Init(cli(args)[0], cli(args)[1], cli(args)[2], cli(args)[3], cli(args)[4], cli(args)[5], cli(args)[6]))
    else:
        print(method.Init(cli(args)[0], cli(args)[1]))
    
else:
    print(f"{Fore.RED+Style.BRIGHT}There's some mistake in typing command, use: \n{Fore.YELLOW+Style.BRIGHT}main.py --help{Style.RESET_ALL}")