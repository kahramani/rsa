import logger
import constants


logger = logger.build_logger('deciphering')


def decipher_with_private_keys(cipher_text, multiplicative_inverse, multiplication_of_key_primes):
    """
    :param cipher_text:
    :param multiplicative_inverse:
    :param multiplication_of_key_primes:
    :return:
    """
    deciphered_items = list()
    for i in range(0, len(cipher_text)):
        cipher_item = cipher_text[i]
        deciphered_item = pow(cipher_item, multiplicative_inverse, multiplication_of_key_primes)
        deciphered_items.append(deciphered_item)

    return deciphered_items


def calculate_modular_inverse(alg, n, m):
    """
    :param alg: algorithm  type
    :param n: multiplicative
    :param m: modulo
    :return: modular multiplicative inverse by algorithm
    """
    if alg == constants.algorithm_brute_force:
        return modular_inverse_via_brute_force(n, m)
    elif alg == constants.algorithm_totient:
        return modular_inverse_via_totient(n, m)
    else:
        return -1


def modular_inverse_via_brute_force(n, m):
    """
    :param n:
    :param m:
    :return: modular multiplicative inverse calculated by brute force algorithm
    """
    inverse = 0
    for i in range(1, m):
        if (n*i) % m == 1:
            inverse = i
            break

    return inverse


def modular_inverse_via_totient(n, m):
    """
    :param n:
    :param m:
    :return: modular multiplicative inverse calculated by Extended Euclidean algorithm
    """
    inverse = 0
    g, x, y = extended_greatest_common_divisor(n, m)
    if g != 1:
        raise Exception('Modular inverse does not exist!')
    else:
        inverse = x % m

    return inverse


def extended_greatest_common_divisor(a, b):
    """
    :param a:
    :param b:
    :return: greatest common divisor of a and b
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_greatest_common_divisor(b % a, a)
        return g, x - (b // a) * y, y
