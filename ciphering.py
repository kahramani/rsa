import logger


logger = logger.build_logger('ciphering')


def cipher_with_public_keys(ascii_responses, multiplication_of_key_primes, power_prime_to_mask):
    """
    :param ascii_response:
    :param multiplication_of_key_primes:
    :param power_prime_to_mask:
    :return:
    """
    ciphered_items = list()
    for i in range(0, len(ascii_responses)):
        ascii_response = ascii_responses[i]
        ciphered_item = pow(ascii_response, power_prime_to_mask, multiplication_of_key_primes)
        ciphered_items.append(ciphered_item)

    return ciphered_items
