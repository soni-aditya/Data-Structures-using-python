'''
You are given data structure of a person and his busy time. You need to return all the possible time slots and person who is busy in that.

e.g.
Person name Start time End time
A 10 50
B 30 70
C 40 80
D 10 20

Output:
10-20 -> A, D
20-30 -> A (Note: this time slot was not given in input. You need to find it out.)
30-50 -> A, B, C
50-70 -> B,C
70-80 -> C
'''
from collections import defaultdict

from collections import defaultdict

def write_schedule(inputs):
    # Create a dictionary to store time slots and the associated participants
    time_slots = defaultdict(lambda: [set(), set()])

    # Populate the time_slots dictionary with participants and their start/end times
    for participant, [start_time, end_time] in inputs.items():
        time_slots[start_time][0].add(participant)
        time_slots[end_time][1].add(participant)

    current_participants, sorted_times = set(), sorted(time_slots)

    # Iterate through the sorted time slots
    for time1, time2 in zip(sorted_times[:-1], sorted_times[1:]):
        # Calculate the participants available during this time slot
        current_participants = (current_participants | time_slots[time1][0]) - time_slots[time1][1]

        # Print the time slot and the participants available during that time
        print('{}-{} {}'.format(time1, time2, ' '.join(current_participants)))

    print()
 


inputs={'Matt':[3,8],'julia':[7,10], 'me':[3,6]}
write_schedule(inputs)
inputs2 = {'A':[10,50],'B':[30,70],'C':[40,80],'D':[10,20]}
write_schedule(inputs2)