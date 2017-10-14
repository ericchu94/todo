#!/usr/bin/env python
import argparse
import os
import re
import sys


TODOTXT = os.path.expanduser('~/todo.txt')
TODO_STATE = os.path.expanduser('~/.todo.state')


class Task:
    def __init__(self, raw, index=None):
        raw = raw.strip()
        self.raw = raw
        self.index = index
        self.task = raw
        self.tags = self._extract_tags()
        self.priority = self._extract_priority()


    def _extract(self, prefix, remainder):
        pattern = r'(?<!\S){}{}+(?!\S)'.format(prefix, remainder)
        matches = [match[1:] for match in re.findall(pattern, self.task, flags=re.IGNORECASE)]
        self.task = re.sub(pattern, '', self.task, flags=re.IGNORECASE).strip()
        return matches


    def _extract_tags(self):
        return self._extract('@', '\S')


    def _extract_priority(self):
        try:
            return self._extract('p', '\d')[0]
        except IndexError:
            return 3


    def __repr__(self):
        yaml = []
        yaml.append('task: {}'.format(self.task))
        if len(self.tags) > 0:
            yaml.append('tags:')
            for tag in self.tags:
                yaml.append('  - {}'.format(tag))
        yaml.append('priority: {}'.format(self.priority))
        return '\n'.join(yaml)


    def __str__(self):
        return self.raw


    def __lt__(self, other):
        return self.task < other.task


def add_task(task):
    with open(TODOTXT, mode='a', encoding='utf-8') as f:
        print(task, file=f)


def add_func(args):
    task = ' '.join(args.task)
    add_task(task)


def list_tasks():
    with open(TODOTXT, mode='r', encoding='utf-8') as f, \
         open(TODO_STATE, mode='w', encoding='utf-8') as state:
        tasks = sorted((Task(task, index) for index, task in enumerate(f)))
        id = 0
        for i, task in enumerate(tasks):
            if True:
                print(id, task)
                print(task.index, file=state)
                id += 1


def list_func(args):
    list_tasks()


def show_task(id):
    with open(TODO_STATE, mode='r', encoding='utf-8') as state:
        i = int(state.readlines()[id])
    with open(TODOTXT, mode='r', encoding='utf-8') as f:
        task = Task(f.readlines()[i])
        print(repr(task))


def show_func(args):
    show_task(args.id)


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_add = subparsers.add_parser('add', aliases=['a'])
    parser_add.add_argument('task', nargs=argparse.REMAINDER)
    parser_add.set_defaults(func=add_func)

    parser_list = subparsers.add_parser('list', aliases=['l'])
    parser_list.set_defaults(func=list_func)

    parser_show = subparsers.add_parser('show', aliases=['s'])
    parser_show.add_argument('id', type=int)
    parser_show.set_defaults(func=show_func)

    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
