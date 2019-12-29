
"""
Taxi simulator
==============

Driving a taxi from the console::

    >>> from taxi_sim import taxi_process
    >>> taxi = taxi_process(ident=13, trips=2, start_time=0)
    >>> next(taxi)
    Event(time=0, proc=13, action='leave garage')
    >>> taxi.send(_.time + 7)
    Event(time=7, proc=13, action='pick up passenger')
    >>> taxi.send(_.time + 23)
    Event(time=30, proc=13, action='drop off passenger')
    >>> taxi.send(_.time + 5)
    Event(time=35, proc=13, action='pick up passenger')
    >>> taxi.send(_.time + 48)
    Event(time=83, proc=13, action='drop off passenger')
    >>> taxi.send(_.time + 1)
    Event(time=84, proc=13, action='going home')
    >>> taxi.send(_.time + 10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

Sample run with two cars, random seed 10. This is a valid doctest::

    >>> main(num_taxis=2, seed=10)
    taxi: 0  Event(time=0, proc=0, action='leave garage')
    taxi: 0  Event(time=5, proc=0, action='pick up passenger')
    taxi: 1     Event(time=5, proc=1, action='leave garage')
    taxi: 1     Event(time=10, proc=1, action='pick up passenger')
    taxi: 1     Event(time=15, proc=1, action='drop off passenger')
    taxi: 0  Event(time=17, proc=0, action='drop off passenger')
    taxi: 1     Event(time=24, proc=1, action='pick up passenger')
    taxi: 0  Event(time=26, proc=0, action='pick up passenger')
    taxi: 0  Event(time=30, proc=0, action='drop off passenger')
    taxi: 0  Event(time=34, proc=0, action='going home')
    taxi: 1     Event(time=46, proc=1, action='drop off passenger')
    taxi: 1     Event(time=48, proc=1, action='pick up passenger')
    taxi: 1     Event(time=110, proc=1, action='drop off passenger')
    taxi: 1     Event(time=139, proc=1, action='pick up passenger')
    taxi: 1     Event(time=140, proc=1, action='drop off passenger')
    taxi: 1     Event(time=150, proc=1, action='going home')
    *** end of events ***

See longer sample run at the end of this module.

"""

import random
import collections
import queue
import argparse

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5

Event = collections.namedtuple('Event', 'time proc action')


# BEGIN TAXI_PROCESS
def taxi_process(ident, trips, start_time=0):  # <1> 택시 ID, 운행할 횟수, 택시가 차고를 나오는 시간
    """Yield to simulator issuing event at each state change"""
    time = yield Event(start_time, ident, 'leave garage')  # <2> 처음 생성된 이벤트는 리브, 그리고 suspend한 다음에 나중에 손님을 태웠다는 센드를 받으면 time을 받는다
    for i in range(trips):  # <3> 운행할 횟수 동안
        time = yield Event(time, ident, 'pick up passenger')  # <4> 이전에 받은 타임을 가지고 픽업을 했다는 이벤트를 생성 그다음 코루틴을 suspend한 다음에 손님을 내렸다는 센드를 받으면 time을 받는다. 
        time = yield Event(time, ident, 'drop off passenger')  # <5> 이전에 받은 타임을 가지고 내렸다는 이벤트를 생성 그 다음 코루틴을 suspend한 다음에 손님을 태우면 time을 받는다.

    yield Event(time, ident, 'going home')  # <6> ( 운행할 횟수를 다 채우면;) 이전에 받은 타임을 가지고 곧 집가는 시간이라고 해서 출력 ; 이때는 a = yield b가 아닌 것을 주목; 이 구문이 실행된 뒤에 send를 보내면 StopIteration을 뱉는다.
    # end of taxi process # <7>
# END TAXI_PROCESS


# BEGIN TAXI_SIMULATOR
class Simulator:

    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):  # <1>
        """Schedule and display events until time is up"""
        # schedule the first event for each cab
        for _, proc in sorted(self.procs.items()):  # <2>
            first_event = next(proc)  # <3> first_event에 출발시간 이벤트 바인딩; 그리고 proc은 코루틴 실행된 상태로 있음
            self.events.put(first_event)  # <4> 우선순위큐에(시간이 키) 보관

        # main loop of the simulation
        sim_time = 0  # <5> 시계 0
        while sim_time < end_time:  # <6> 시뮬레이션 제한시간 초과하면 중단
            if self.events.empty():  # <7>
                print('*** end of events ***')
                break # 큐가 비었으면; 모든 택시들이 제한시간내에 집갔으면 중단

            current_event = self.events.get()  # <8> time이 가장 작은 이벤트를 받는다; pop연산임
            sim_time, proc_id, previous_action = current_event  # <9> 그 이벤트에서 시간, 택시번호, 최근에 택시의 활동을 받는다
            print('taxi:', proc_id, proc_id * '   ', current_event)  # <10>
            active_proc = self.procs[proc_id]  # <11> 현재 활성화된 택시에 관한 코루틴을 받는다
            next_time = sim_time + compute_duration(previous_action)  # <12> 픽업하는데/내리는데/집가는데 걸리는 시간을 계산(지수분포)
            try:
                next_event = active_proc.send(next_time)  # <13> 택시 코루틴에 다음의 행동까지 걸린 시간을 보낸다
            except StopIteration:
                del self.procs[proc_id]  # <14> 스탑이터레이션; 즉 집가는 것까지 yield를 한 closed한 상태의 코루틴 삭제
            else:
                self.events.put(next_event)  # <15> 예외가 발생하지 않으면 next_event 추가
        else:  # <16> 예외가 발생하지 않고(큐가 비어있는 경우가 발생하지 않고) 시뮬레이션 시간이 초과됐을 때
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize())) # 남아있는 이벤트 갯수
# END TAXI_SIMULATOR


def compute_duration(previous_action):
    """Compute action duration using exponential distribution"""
    if previous_action in ['leave garage', 'drop off passenger']:
        # new state is prowling
        interval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
        # new state is trip
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unknown previous_action: %s' % previous_action)
    return int(random.expovariate(1/interval)) + 1


def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS,
         seed=None):
    """Initialize random generator, build procs and run simulation"""
    if seed is not None:
        random.seed(seed)  # get reproducible results

    taxis = {i: taxi_process(i, (i+1)*2, i*DEPARTURE_INTERVAL)
             for i in range(num_taxis)} # 택시별 출발시간 초기화 ; 각 딕셔너리 원소는 코루틴(제너레이터)이기 때문에 언제나 send를 기다리고 있다. 
    sim = Simulator(taxis)
    sim.run(end_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        description='Taxi fleet simulator.')
    parser.add_argument('-e', '--end-time', type=int,
                        default=DEFAULT_END_TIME,
                        help='simulation end time; default = %s'
                        % DEFAULT_END_TIME)
    parser.add_argument('-t', '--taxis', type=int,
                        default=DEFAULT_NUMBER_OF_TAXIS,
                        help='number of taxis running; default = %s'
                        % DEFAULT_NUMBER_OF_TAXIS)
    parser.add_argument('-s', '--seed', type=int, default=None,
                        help='random generator seed (for testing)')
    args = parser.parse_args()
    main(args.end_time, args.taxis, args.seed)


"""

Sample run from the command line, seed=3, maximum elapsed time=120::

# BEGIN TAXI_SAMPLE_RUN
$ python3 taxi_sim.py -s 3 -e 120
taxi: 0  Event(time=0, proc=0, action='leave garage')
taxi: 0  Event(time=2, proc=0, action='pick up passenger')
taxi: 1     Event(time=5, proc=1, action='leave garage')
taxi: 1     Event(time=8, proc=1, action='pick up passenger')
taxi: 2        Event(time=10, proc=2, action='leave garage')
taxi: 2        Event(time=15, proc=2, action='pick up passenger')
taxi: 2        Event(time=17, proc=2, action='drop off passenger')
taxi: 0  Event(time=18, proc=0, action='drop off passenger')
taxi: 2        Event(time=18, proc=2, action='pick up passenger')
taxi: 2        Event(time=25, proc=2, action='drop off passenger')
taxi: 1     Event(time=27, proc=1, action='drop off passenger')
taxi: 2        Event(time=27, proc=2, action='pick up passenger')
taxi: 0  Event(time=28, proc=0, action='pick up passenger')
taxi: 2        Event(time=40, proc=2, action='drop off passenger')
taxi: 2        Event(time=44, proc=2, action='pick up passenger')
taxi: 1     Event(time=55, proc=1, action='pick up passenger')
taxi: 1     Event(time=59, proc=1, action='drop off passenger')
taxi: 0  Event(time=65, proc=0, action='drop off passenger')
taxi: 1     Event(time=65, proc=1, action='pick up passenger')
taxi: 2        Event(time=65, proc=2, action='drop off passenger')
taxi: 2        Event(time=72, proc=2, action='pick up passenger')
taxi: 0  Event(time=76, proc=0, action='going home')
taxi: 1     Event(time=80, proc=1, action='drop off passenger')
taxi: 1     Event(time=88, proc=1, action='pick up passenger')
taxi: 2        Event(time=95, proc=2, action='drop off passenger')
taxi: 2        Event(time=97, proc=2, action='pick up passenger')
taxi: 2        Event(time=98, proc=2, action='drop off passenger')
taxi: 1     Event(time=106, proc=1, action='drop off passenger')
taxi: 2        Event(time=109, proc=2, action='going home')
taxi: 1     Event(time=110, proc=1, action='going home')
*** end of events ***
# END TAXI_SAMPLE_RUN

"""
