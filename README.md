# todo
A command line todo app

## usage
```
$ todo add Buy groceries today @personal
1 Buy groceries today p3 @personal

$ todo add Buy eggs today @personal parent:1
1 Buy groceries today p3 @personal
  2 Buy eggs today p3 @personal

$ todo add Buy milk today @personal parent:1
1 Buy groceries today p3 @personal
  2 Buy eggs today p3 @personal
  3 Buy milk today p3 @personal

$ todo add Check email daily 9 am @work p1
1 Check email 9 am p1 @work
2 Buy groceries today p3 @personal
  3 Buy eggs today p3 @personal
  4 Buy milk today p3 @personal

$ todo add Submit report friday @work p1
1 Check email 9 am p1 @work
2 Submit report friday p1 @work
3 Buy groceries today p3 @personal
  4 Buy eggs today p3 @personal
  5 Buy milk today p3 @personal

$ todo list
1 Check email 9 am p1 @work
2 Submit report friday p1 @work
3 Buy groceries today p3 @personal
  4 Buy eggs today p3 @personal
  5 Buy milk today p3 @personal

$ todo list today @personal
1 Buy groceries today p3 @personal
  2 Buy eggs today p3 @personal
  3 Buy milk today p3 @personal

$ todo list @work
1 Check email 9 am p1 @work
2 Submit report friday p1 @work

$ todo complete 1
1 Check email tomorrow 9 am p1 @work
2 Submit report friday p1 @work
```
