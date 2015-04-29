import os
import sys
import binascii

def main(args):

    action, filename = args
    basename, _ = os.path.splitext(os.path.basename(filename))

    if action == "totext":
        txtfile = basename + '.txt'
        with open(txtfile, 'w') as i, open(filename, 'rb') as o:
            i.write(binascii.b2a_hex(o.read()))

    if action == "toexe":
        exefile = basename + '.exe'
        with open(filename, 'r') as i, open(exefile, 'wb') as o:
            o.write(binascii.a2b_hex(i.read()))

if __name__ == "__main__":

    #usage is chameleon.py <action> <filepath>
    #actions can be totext or toexe
    args = sys.argv[1:]
    main(args)
