import random
import typing
import pycamunda.variable
import worker

def fight(legion: pycamunda.variable.Variable,
          defendants: pycamunda.variable.Variable, 
          legionS: pycamunda.variable.Variable, 
          defendantsS: pycamunda.variable.Variable,
          capital: pycamunda.variable.Variable)-> typing.Dict[str, int]:
    legS = legion.value * legionS.value * random.uniform(0, 1)
    defS = defendants.value * defendantsS.value * random.uniform(0, 1)
    res = legS - defS
    survivors = res / legionS.value
    if capital.value / 2 > survivors:
        attack = 0
    else:
        attack = 1
        survivors = survivors * 1.33
    return {'survivors': int(survivors), 'capitalAttack': attack}

if __name__ == '__main__':
    import pycamunda.processdef

    url = 'http://localhost:8080/engine-rest'
    worker_id = '1'
    
    worker = worker.Worker(url=url, worker_id=worker_id)
    worker.subscribe(
        topic='TroopFight',
        func=fight,
        variables=['legion',"defendants","legionS","defendantsS",'capital']
    )

    worker.run()
