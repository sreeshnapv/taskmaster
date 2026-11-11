def create_task(task_name, product_name, price):
    return {
        'task': task_name,
        'product': product_name,
        'price': price
    }
def show_task(task):
    print(f"Task: {task['task']} | Item: {task['product']} - {task['price']}")

tasks = []
tasks.append(create_task('Buy groceries', 'Milk', 30))
tasks.append(create_task('Electronics shopping', 'Earphones', 500))

for item in tasks:
    show_task(item)