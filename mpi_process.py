import sys
from logger import log
from mpi_instance import MPIInstance, RING


if __name__ == '__main__':
    unavailables = [int(u) for u in sys.argv[1: ]]
    mpi = MPIInstance()

    if mpi.rank == 0:
        log(f'{mpi.rank} is starting an election.')
        data = {
            'sender': mpi.rank,
            'tag': 'election',
            'rank': [0],
            'unavailables': unavailables}
        mpi.send(data)

    while True:
        data = mpi.receive()

        if data['tag'] == 'end':
            data['sender'] = mpi.rank
            mpi.send(data)
            break

        if mpi.rank in data['unavailables']:
            log(f'{mpi.rank} is unavalaible.')
            mpi.send(data)
            continue

        if data['tag'] == 'election':
            if mpi.rank == 0:
                data = {
                    'sender': mpi.rank,
                    'tag': 'confirmation',
                    'elected': max(data['rank']),
                    'unavailables': data['unavailables'],
                }
                mpi.send(data)

            else:
                data['sender'] = mpi.rank
                data['rank'].append(mpi.rank)
                mpi.send(data)

        elif data['tag'] == 'confirmation':
            if mpi.rank == 0:
                data = {
                    'sender': mpi.rank,
                    'tag': 'end',
                    'unavailables': data['unavailables']
                }
                mpi.send(data)

            else:
                if data['elected'] == mpi.rank:
                    log(f'I was elected! My rank is {mpi.rank}.')
                    mpi.elected = True
                else:
                    mpi.elected = False

                data['sender'] = mpi.rank
                mpi.send(data)

        elif data['tag'] == 'action':
            if mpi.elected:
                log(f'{mpi.rank} is executing task.')
