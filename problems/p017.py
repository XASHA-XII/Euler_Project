'''
https://projecteuler.net/problem=17
Number letter counts
'''


def main()->int:
    '''
    Returns the number of letters of the first 1000 postive integer numbers
    in their written English form.
    '''
    N = 10**3


    result=sum(len(digits_to_numerals(n)) for n in range(1,N+1))
    return result



def digits_to_numerals(n: int) -> str:
    NUMERALS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    MULTIPLES_OF_TEN = ["zero", "ten", "twenty", "thirty",
                        "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    HUNDRED = "hundred"
    THOUSAND = "thousand"
    AND = "and"

    numeral = str(n)
    if 0 <= n <= 19:
        return NUMERALS[n]
    elif 20 <= n <= 99:
        n_mod_10 = int(numeral[-1])
        return MULTIPLES_OF_TEN[int(numeral[-2])] + (NUMERALS[n_mod_10] if (int(numeral[-1]) != 0) else "")
    elif 100 <= n <= 999:
        n_mod_100 = int(str(n)[1:])
        return NUMERALS[int(numeral[-3])] + HUNDRED + (AND + digits_to_numerals(n_mod_100) if n_mod_100 != 0 else "")
    elif n==1000:
        return 'ONE'+THOUSAND
    else:
        raise ValueError("Implemented only for numbers smaller or equal 1000.")

    


if __name__=='__main__':
    result=main()
    print(result)