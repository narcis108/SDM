import asyncio
from random import randint


@asyncio.coroutine
def StartState():
    print('Sapand in desert dupa o comoara, gasesti o usa.')
    input_value = randint(0, 1)
    if (input_value == 0):
        result = yield from State2()
    else:
        result = yield from State1(input_value)
    print(result)


@asyncio.coroutine
def State1(transition_value):
    if transition_value == 1:
        outputValue = '\nActiune : Deschide usa  ---> '
    if transition_value == 2:
        outputValue = '\nActiune : Deschide usa din stanga ---> '
    if transition_value == 3:
        outputValue = '\nActiune : Urci pe scara ---> '
    if transition_value ==4:
        outputValue = '\nActiune : Deschide usa  ---> '
    if transition_value == 0:
        outputValue = '\nActiune : Te intorci pe hol ---> '
    input_value = randint(0, 2)
    if (input_value == 0):
        result = yield from State3(input_value)
    if (input_value == 1):
        result = yield from State4()
    else:
        result = yield from State5(input_value)
    result = 'Gasesti o camera cu o usa, un hol si o scara.' + result
    return outputValue + result


@asyncio.coroutine
def State2():
    outputValue = '\nActiune : Sapa mai mult ---> '
    input_value = randint(1, 2)
    if (input_value == 1):
        result = yield from State5(input_value)
    else:
        result = yield from State1(4)
    result = 'Mai jos de usa sunt niste trepte' + result
    return outputValue + result


@asyncio.coroutine
def State3(transition_value):
    if (transition_value == 0):
        outputValue = '\nActiune : Mergi pe hol ----> '
    else:
        outputValue = '\nActiune : Deschide usa din dreapta ---> '
    input_value = randint(0, 2)
    if (input_value == 0):
        result = yield from State1(input_value)
    if (input_value == 1):
        result = yield from State4()
    if (input_value == 2):
        result = yield from EndState()
    result = 'In camera este un fotoliu, o usa si o deschidere spre hol.' + result
    return outputValue + result


@asyncio.coroutine
def State4():
    outputValue = '\nActiune : Deschide usa ---> '
    input_value = randint(1, 2)
    if (input_value == 1):
        result = yield from State3(input_value)
    else:
        result = yield from State1(input_value)
    result = 'In camera este un paianjen urias.Camera contine si doua usi.' + result
    return outputValue + result


@asyncio.coroutine
def State5(transition_value):
    if (transition_value == 2):
        outputValue = '\nActiune : Cobori pe scara ---> '
    if (transition_value == 1) :
        outputValue = '\nActiune : Cobori pe trepte ---> '
    if (transition_value == 0) :
        outputValue = '\nActiune : Te intorci ---> '
    input_value = randint(1,2)
    if(input_value == 1):
        result = yield from State6()
    else :
        result = yield from State1(3)
    result = 'Gaseseti o camera cu o usa si o scara.' + result
    return outputValue + result


@asyncio.coroutine
def State6():
    outputValue = '\nActiune : Intri pe usa --->'
    result = yield from State5(0)
    result = 'Camera contine lava. Trebuie sa te intorci.' + result
    return outputValue + result

@asyncio.coroutine
def EndState():
    return '\nCand te-ai asezat pe fotoliu, comoara devine vizibila. Ai castigat!'


if __name__ == '__main__':
    print('Simulare tema de casa')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(StartState())
