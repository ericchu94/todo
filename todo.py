#!/usr/bin/env python
import argparse
import os


TODOTXT = os.path.expanduser('~/todo.txt')


def add_task(task):
    with open(TODOTXT, mode='a', encoding='utf-8') as f:
        print(task, file=f)


def add(args):
    task = ' '.join(args.task)
    add_task(task)


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    parser_add = subparsers.add_parser('add', aliases=['a'])
    parser_add.add_argument('task', nargs=argparse.REMAINDER)
    parser_add.set_defaults(func=add)
    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
