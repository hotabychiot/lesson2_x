
def is_prime(func):
    def wrapper(*args, **kwargs):
        original = func(*args, **kwargs)
        mod_original = abs(original)
        if mod_original <= 2:
            print('Простое')
            return original

        for i in range(2, int(mod_original ** 0.5) + 1):
            if mod_original % i == 0:
                print('Составное')
                return original
        print('Простое')
        return original
    return wrapper

@is_prime
def  sum_three(one, two, three):
    return one+two+three

if __name__ == '__main__':
    result = sum_three(2, 3, 6)
    print(result)