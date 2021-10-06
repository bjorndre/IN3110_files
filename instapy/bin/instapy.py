import argparse
import time as t

from numba.core.extending import type_callable
import filters as ins

def main():
    parser = argparse.ArgumentParser(description='Applies a filter to an image.')

    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Name of input file")

    parser_group = parser.add_mutually_exclusive_group(required=True)
    parser_group.add_argument('-se','--sepia', action='store_true', help="applies the sepia filter")
    parser_group.add_argument('-g','--gray', action='store_true', help="applies the gray filter")
    
    parser.add_argument('-le', '--level', action='store', type=float, \
        help='Level of sepia filter, does nothing unless -se is passed', default=1.0)

    parser.add_argument('-sc', '--scale', action='store', type=float, default=1.0, help="The scaling factor.")

    parser.add_argument('-i', '--implement', action='store', type=str, choices=['python', 'numpy', 'numba'], \
        default='python', help="The implementation to be used.")

    parser.add_argument('-r', '--runtime', action='store_true', help="Tracks average runtime")

    parser.add_argument('-o', '--out', action='store', type=str, help='Name of the output file', default=None)

    args = parser.parse_args()

    
    if args.gray == True:
        ins.grayscale_image(args.file, args.out, args.implement, args.scale)
    else:
        ins.sepia_image(args.file, args.out, args.implement, args.scale, args.level)
    
    if args.runtime == True:
        average_time = 0

        for i in range(3):
            start = t.time()
            if args.gray == True:
                ins.grayscale_image(args.file, args.out, args.implement, args.scale)
            else:
                ins.sepia_image(args.file, args.out, args.implement, args.scale, args.level)
            stop = t.time()
            average_time = average_time + (stop-start)
        
        average_time = average_time/3
        
        print(f"Average time over 3 runs: {average_time}")