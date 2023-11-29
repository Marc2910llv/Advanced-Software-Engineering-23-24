import typing
import pycamunda.variable
import worker
from worker import printStory

'''
Insert only the variables in input for the results function and assign their value accordly.
As before, 'variable_name: pycamunda.variable.Variable' is used to pass a variable to this function.
'''
def results(#insert variables here#)-> typing.Dict:
    
    survivors = #survivors number .value here#
    legion = #legion number .value here#
    defendants = #defendants number .value here#
    capitalAttacked = #capitalAttacked number .value here#

    printStory(survivors, legion, defendants, capitalAttacked)
    
    return {}


if __name__ == '__main__':
    import pycamunda.processdef

    url = 'http://localhost:8080/engine-rest'
    worker_id = '3'
    
    worker = worker.Worker(url=url, worker_id=worker_id)
    worker.subscribe(
        topic=#topic of the results here#,
        func=results,
        variables=[#list of variable names (strings) from the process here#]
    )

    worker.run()
