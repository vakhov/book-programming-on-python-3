#!/usr/bin/env python3

import collections
import sys

ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)

User = collections.namedtuple('User', 'username forename middlename surname id')


def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] + fields[SURNAME]).replace('-', '').replace("'", ''))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = '{0}{1}'.format(original_name, count)
        count += 1
    usernames.add(username)
    return username


def process_line(line, usernames):
    fields = line.split(':')
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])
    return user


def print_users(users):
    namewidt = 32
    usernamewidt = 9

    print("{0:<{nw}} {1:^6} {2:{uw}}".format('Name', 'ID', 'Username', nw=namewidt, uw=usernamewidt))
    print("{0:-<{nw}} {0:-<6} {0:-<{uw}}".format('', nw=namewidt, uw=usernamewidt))
    for key in sorted(users):
        user = users[key]
        initial = ''
        if user.middlename:
            initial = ' ' + user.middlename[0]
        name = '{0.surname}, {0.forename}{1}'.format(user, initial)
        print("{0:.<{nw}} ({1.id:4}) {1.username:{uw}}".format(name, user, nw=namewidt, uw=usernamewidt))


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print('usage: {0} file1 [file2 [... fileN]]'.format(sys.argv[0]))
        sys.exit()
    usernames = set()
    users = {}

    for filename in sys.argv[1:]:
        for line in open(filename, encoding='utf-8'):
            line = line.rstrip()
            if line:
                user = process_line(line, usernames)
                users[(user.surname.lower(), user.forename.lower(), user.id)] = user
    print_users(users)


if __name__ == '__main__':
    main()
