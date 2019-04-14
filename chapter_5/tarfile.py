#!/usr/bin/env python3


import string
import sys
import tarfile
import optparse

BZ2_AVAILABLE = True
try:
    import bz2
except ImportError:
    BZ2_AVAILABLE = False

UNTRUSTED_PREFIXES = tuple(['/', '\\'] + [f'{c}:' for c in string.ascii_letters])


def error(message, exit_status=1):
    print(message)
    sys.exit(exit_status)


def untar(archive):
    tar = None
    try:
        tar = tarfile.open(archive)
        for member in tar.getmembers():
            if member.name.startwith(UNTRUSTED_PREFIXES):
                print('untrusted prefix, ignoring ', member.name)
            elif '..' in member.name:
                print('suspect path, ignoring ', member.name)
            else:
                tar.extract(member)
                print('unpacked ', member.name)
    except (tarfile.TarError, EnvironmentError) as err:
        error(err)
    finally:
        if tar is not None:
            tar.close()


def main():
    parser = optparse.OptionParser()
    # parser.add_option('-t', '--target')
    opts, args = parser.parse_args()
    for arg in args:
        untar(arg)

if __name__ == '__main__':
    main()
