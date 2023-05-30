
class Task:

    def __init__(self, tag, start_time, duration) -> None:
        self.tag = tag
        self.start_time = start_time
        self.duration = duration

    @property
    def end_time(self):
        return self.start_time + self.duration

    def __repr__(self) -> str:
        return repr(self.tag)

#tasks: list of task objects
#start: starting available time
#end: last available time
#priority: function that takes in a Task object as parameter and determines it's priority
#returns: a list of the selected tasks tag
# The algorithm complexity is determined by the sorting, therefore O(n log(n))
def administrate_tasks(tasks: list, start: float, end: float, priority=None) -> list:

    if priority is None:
        priority = lambda task: task.start_time

    sorted_tasks = sorted(tasks, key = priority)

    selected_tasks_tag = []
    for task in sorted_tasks:

        # The task doesn't fit in the valid interval [start, end]
        if task.start_time < start or task.end_time > end:
            continue
        
        selected_tasks_tag.append(task.tag)
        start = task.end_time

    return selected_tasks_tag

