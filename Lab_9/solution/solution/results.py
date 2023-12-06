import typing
import pycamunda.variable
import worker
from worker import printStory

def results(survivors: pycamunda.variable.Variable, 
            legion: pycamunda.variable.Variable,
            defendants: pycamunda.variable.Variable,
            capitalAttack: pycamunda.variable.Variable)-> typing.Dict:

    printStory(survivors.value, legion.value, defendants.value, capitalAttack.value)
    return {}


if __name__ == '__main__':
    import pycamunda.processdef

    url = 'http://localhost:8080/engine-rest'
    worker_id = '3'
    
    worker = worker.Worker(url=url, worker_id=worker_id)
    worker.subscribe(
        topic='Results',
        func=results,
        variables=['survivors', 'legion', 'defendants','capitalAttack']
    )

    worker.run()
