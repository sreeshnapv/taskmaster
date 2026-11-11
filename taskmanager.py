tasks=[]
def add_task(task):
 tasks.append(task)
def show_tasks():
 for task in tasks:
  print(task)
add_task('buy groceries')
show_tasks()