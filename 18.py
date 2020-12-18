with open('inputs/inp18.txt') as f:
    inp = f.read()

# inp = '''
# 2 * 3 + (4 * 5)
# 5 + (8 * 3 + 9 + 3 * 4 * 3)
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
# '''

class WrongExpressionException(Exception):
    pass


def eval_exp(exp):
    if type(exp) is not list:
        return int(exp)

    idx1 = 0
    mutations = []
    while idx1 < len(exp):
        char1 = exp[idx1]
        if char1 == '(':
            c = 1
            idx2 = idx1 + 1
            while idx2 < len(exp):
                char2 = exp[idx2]
                if char2 == '(':
                    c += 1
                elif char2 == ')':
                    c -= 1
                if c == 0:
                    eval_res = eval_exp(exp[idx1 + 1: idx2])
                    mutations.append((idx1, idx2, eval_res))
                    idx1 = idx2
                    break

                idx2 += 1
        idx1 += 1

    for beg, end, res in reversed(mutations):
        exp = [*exp[:beg], res, *exp[end + 1:]]


    if len(exp) == 2:
        raise WrongExpressionException

    if len(exp) == 3:
        if exp[1] == '+':
            return eval_exp(exp[0]) + eval_exp(exp[2])
        if exp[1] == '*':
            return eval_exp(exp[0]) * eval_exp(exp[2])


    if exp[-2] == '+':
        return eval_exp(exp[:-2]) + eval_exp(exp[-1])
    if exp[-2] == '*':
        return eval_exp(exp[:-2]) * eval_exp(exp[-1])

    
s = 0
for sent in inp.strip().split('\n'):
    exp = list(sent.replace(' ', ''))
    s += eval_exp(exp)


print('Part 1.', s)



def eval_exp2(exp):
    if type(exp) is not list:
        return int(exp)

    if len(exp) == 1:
        return int(exp[0])

    idx1 = 0
    mutations = []
    while idx1 < len(exp):
        char1 = exp[idx1]
        if char1 == '(':
            c = 1
            idx2 = idx1 + 1
            while idx2 < len(exp):
                char2 = exp[idx2]
                if char2 == '(':
                    c += 1
                elif char2 == ')':
                    c -= 1
                if c == 0:
                    eval_res = eval_exp2(exp[idx1 + 1: idx2])
                    mutations.append((idx1, idx2, eval_res))
                    idx1 = idx2
                    break

                idx2 += 1
        idx1 += 1

    for beg, end, res in reversed(mutations):
        exp = [*exp[:beg], res, *exp[end + 1:]]


    if len(exp) == 2:
        raise WrongExpressionException

    if len(exp) == 3:
        if exp[1] == '+':
            return eval_exp2(exp[0]) + eval_exp2(exp[2])
        if exp[1] == '*':
            return eval_exp2(exp[0]) * eval_exp2(exp[2])

    for idx in range(len(exp)):
        op = exp[idx]
        if op == '*':
            return eval_exp2(exp[:idx]) * eval_exp2(exp[idx + 1:])

        
    return eval(''.join(str(op) for op in exp))

# inp = '''
# 1 + (2 * 3) + (4 * (5 + 6))
# 2 * 3 + (4 * 5)
# 5 + (8 * 3 + 9 + 3 * 4 * 3)
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
# '''
  
s = 0
for sent in inp.strip().split('\n'):
    exp = list(sent.replace(' ', ''))
    s += eval_exp2(exp)


print('Part 2.', s)