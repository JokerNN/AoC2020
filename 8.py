from console import ConsoleExecutor, ProgramStatus

inp = ''
with open('./inp8.txt') as f:
    inp = f.read()

# inp = '''nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6'''

program = inp.split('\n')

ce = ConsoleExecutor(program=program)

ran_lines = set()
while ce.pos not in ran_lines:
    ran_lines.add(ce.pos)
    ce.run_next()

print('Part 1.', ce.accum)

for l_idx in range(len(program)):
    if not program[l_idx].startswith('jmp') and not program[l_idx].startswith('nop'):
        continue
    # print('Checking line', l_idx)
    new_program = inp.split('\n')
    if new_program[l_idx].startswith('jmp'):
        new_program[l_idx] = new_program[l_idx].replace('jmp', 'nop')
    else:
        new_program[l_idx] = new_program[l_idx].replace('nop', 'jmp')

    ran_lines = set()
    ce = ConsoleExecutor(program=new_program)
    while ce.pos not in ran_lines and ce.status != ProgramStatus.EXIT_NORMALLY:
        ran_lines.add(ce.pos)
        ce.run_next()

    if ce.status == ProgramStatus.EXIT_NORMALLY:
        print('Part 2.', ce.accum)
        break

