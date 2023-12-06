import random
import typing
import pycamunda.variable
import worker


def capital(survivors: pycamunda.variable.Variable,
          capital: pycamunda.variable.Variable, 
          legionS: pycamunda.variable.Variable, 
          capitalS: pycamunda.variable.Variable)-> typing.Dict[str, str]:
    legS = survivors.value * legionS.value * random.uniform(0, 1)
    capS = capital.value * capitalS.value * random.uniform(0, 1)
    res = legS - capS
    survivors = res / legionS.value
    return {'survivors': int(survivors)}

if __name__ == '__main__':
    import pycamunda.processdef

    url = 'http://localhost:8080/engine-rest'
    worker_id = '2'

    worker = worker.Worker(url=url, worker_id=worker_id)
    worker.subscribe(
        topic='Capital',
        func=capital,
        variables=['survivors',"capital","legionS","capitalS"]
    )

    worker.run()
