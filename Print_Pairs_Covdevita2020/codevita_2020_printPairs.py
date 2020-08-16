ones = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}
def say_number(i):
    if i == 0:
        return 'zero'
    return _say_number_pos(i)
def _say_number_pos(i):
    if i < 20:
        return ones[i]
    if i < 100:
        return _join(tens[i // 10], ones[i % 10])
    if i < 1000:
        return _divide(i, 100, 'hundred')
    for illions_number, illions_name in illions.items():
        if i < 1000**(illions_number + 1):
            break
    return _divide(i, 1000**illions_number, illions_name)

def _divide(dividend, divisor, magnitude):
    return _join(
        _say_number_pos(dividend // divisor),
        magnitude,
        _say_number_pos(dividend % divisor),
    )

def _join(*args):
    return ' '.join(filter(bool, args))
    
    
c=say_number(9)
print(c)