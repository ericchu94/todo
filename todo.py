#!/usr/bin/env python
import argparse
import os


TODOTXT = os.path.expanduser('~/todo.txt')


def add_task(task):
    with open(TODOTXT, mode='a', encoding='utf-8') as f:
        print(task, file=f)


def add_func(args):
    task = ' '.join(args.task)
    add_task(task)


def list_tasks():
    with open(TODOTXT, mode='r', encoding='utf-8') as f:
        for i, task in enumerate(f):
            print(i, task.strip())


def list_func(args):
    list_tasks()


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_add = subparsers.add_parser('add', aliases=['a'])
    parser_add.add_argument('task', nargs=argparse.REMAINDER)
    parser_add.set_defaults(func=add_func)

    parser_list = subparsers.add_parser('list', aliases=['l'])
    parser_list.set_defaults(func=list_func)
    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
