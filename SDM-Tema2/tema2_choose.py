import asyncio


def choose_path(choices):
    print('Introdu calea pe care vrei sa o urmezi. Poti sa alegi una din urmatoarele variante:')
    for i in range(len(choices)):
        print(str(i) + '. ' + choices[i])
    print('Valoare selectata de tine :')
    chosen = input()
    if (int(chosen) > len(choices)):
        print('Valoare introdusa nu este valida.')
        choose_path(choices)
    print('\n')
    return int(chosen)


@asyncio.coroutine
def StartState():
    choices = ['Sapi mai mult', 'Deschide usa']
    print('\nSapand in desert dupa o comoara, gasesti o usa.\n')
    input_value = choose_path(choices=choices)
    if (input_value == 0):
        yield from State2()
    else:
        yield from State1()


@asyncio.coroutine
def State1():
    choices = ['Mergi pe hol', 'Deschide usa', 'Coboara scara']
    print('Gasesti o camera cu o usa, un hol si o scara.')
    input_value = choose_path(choices)
    if (input_value == 0):
        yield from State3()
    if (input_value == 1):
        yield from State4()
    if (input_value == 2):
        yield from State5()


@asyncio.coroutine
def State2():
    choices = ['Deschide usa', 'Cobori pe trepte']
    result = 'Mai jos de usa sunt niste trepte.'
    print(result)
    input_value = choose_path(choices)
    if (input_value == 1):
        yield from State5()
    else:
        yield from State1()


@asyncio.coroutine
def State3():
    choices = ['Te intorci pe hol', 'Deschide usa', 'Stai in fotoliu']
    result = 'In camera este un fotoliu, o usa si o deschidere spre hol.'
    print(result)
    input_value = choose_path(choices)
    if input_value == 0:
        yield from State1()
    if (input_value == 1):
        yield from State4()
    if (input_value == 2):
        yield from EndState()


@asyncio.coroutine
def State4():
    choices = ['Deschide usa din stanga', 'Deschide usa din dreapta']
    result = 'In camera este un paianjen urias.Camera contine si doua usi.'
    print(result)
    input_value = choose_path(choices)
    if (input_value == 1):
        yield from State3()
    else:
        yield from State1()


@asyncio.coroutine
def State5():
    choices = ['Urci pe scara', 'Intri pe usa']
    result = 'Gaseseti o camera cu o usa si o scara.'
    print(result)
    input_value = choose_path(choices)
    if (input_value == 1):
        yield from State6()
    else:
        yield from State1()


@asyncio.coroutine
def State6():
    result = 'Camera contine lava. Trebuie sa te intorci.\nTe intorci.'
    print(result)
    yield from State5()


@asyncio.coroutine
def EndState():
    print('\nCand te-ai asezat pe fotoliu, comoara devine vizibila. Ai castigat!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(StartState())
