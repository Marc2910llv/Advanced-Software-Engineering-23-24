import random
import typing
import pycamunda.variable
import worker

'''
Implement the logic of the battle between the legion and the capital (as before but it should change the legion size variable).

To pass a variable to this function, you must use
'variable_name: pycamunda.variable.Variable'
where 'variable_name' is the name of the variable in the BPMN diagram and is used in the subscribe call.

To access the value of a variable, use 'variable_name.value'.

This function returns a dictionary str -> int, 
you should return the number of survivors of the legion.
'''
def capital(#variables here#)-> typing.Dict[str, str]:
    
    #battle logic here

    #return example {'survivors': survivors}

if __name__ == '__main__':
    import pycamunda.processdef

    url = 'http://localhost:8080/engine-rest'
    worker_id = '2'

    worker = worker.Worker(url=url, worker_id=worker_id)
    worker.subscribe(
        topic=#topic of the capital attack here#,
        func=capital,
        variables=[#list of variable names (strings) from the process here#]
        #those variables should match the ones in the BPMN diagram and the ones in input of the battle function
    )

    worker.run()
