from xbot2_cli.main import Context

KEY_UP = '[A'
KEY_DOWN = '[B'
KEY_RIGHT = '[C'
KEY_LEFT = '[D'

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        self.impl = _GetchUnix()

    def __call__(self): 
        char = self.impl()
        if char == '\x03':
            raise KeyboardInterrupt
        elif char == '\x04':
            raise EOFError
        elif char == '\x1b':
            return self.impl() + self.impl()
        else:
            return char


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    
def tuning_tui(ctx: Context, args):
    # implement a minimal terminal ui for tuning
    # +/- to increase/decrease the value
    # q to quit
    
    # all params
    params = ctx.list_params(args)
    
    # param idx
    idx = params.index(args.name)
    
    # get the current value
    args.value = ctx.get_param(args)
    initial_value = args.value
    
    # set terminal to raw mode
    getch = _Getch()
    
    # step log10
    step_log10 = 0 
    step = 10**step_log10
    
    # print help
    def print_help():
        print("h: help")
        print("q: quit")
        print("a: increase step")
        print("z: decrease step")
        print("+/-: increase/decrease value")
    
    print_help()
    
    print('====================')
    
    # loop until q is pressed
    while True:
        
        print(f'[{args.name}] value = {args.value}  (step = {step})')
        
        try:
            ch = getch()
        except KeyboardInterrupt:
            break
        
        if ch == 'q':
            break
        if ch == 'i':
            args.value = initial_value
            print(f"Reset to initial value: {args.value}")
            ctx.set_param(args)
        elif ch == 'h':
            print_help()
        elif ch == '+':
            step_log10 += 1
            step = 10**step_log10
        elif ch == '-':
            step_log10 -= 1
            step = 10**step_log10
        elif ch == KEY_UP:
            args.value += step
            ctx.set_param(args)
        elif ch == KEY_DOWN:
            args.value -= step
            ctx.set_param(args)
        elif ch == KEY_RIGHT:
            idx = (idx + 1) % len(params)
            args.name = params[idx]
            args.value = ctx.get_param(args)
            initial_value = args.value
        elif ch == KEY_LEFT:
            idx = (idx - 1) % len(params)
            args.name = params[idx]
            args.value = ctx.get_param(args)
            initial_value = args.value
        else:
            print("Invalid key: {}".format(ch))
            
    