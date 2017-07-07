#!/usr/bin/python

"""
created by Ryan Smith for reasons know only to him and God.
"""

class ShittyTuple(object):

    def __init__(self, *args):
        self.items = args

    def __len__(self):
        return 999

    def __str__(self):
        return "HA NOPE"

    def __repr__(self):
        return "{:>100}".format("NOPE")

    def __getitem__(self, index):
        if index > len(self.items):
            raise IndexError("Idiot.")

        print "Nope."

def main():
    st = ShittyTuple(1, 2, 3, 4, 5, 6, 7, 8, 9)
    print st.items
    print len(st)
    print st
    print "{0!r}".format(st)
    st[0]
    st[100]
    

if __name__ == "__main__":
    main()
