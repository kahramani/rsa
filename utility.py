from random import choice
import random
import sys
import string
import re
import math
import configparser
import constants
import logger


logger = logger.build_logger("utility")


def read_property_key(key, structure_type, section, file_name):
    """
    :param key:
    :param structure_type:
    :param section:
    :param file_name:
    :return: read key with desired type of structure from property file
    """
    try:
        config = configparser.RawConfigParser()
        config.optionxform = str
        config.read(file_name)
        if structure_type == constants.structure_type_int:
            return config.getint(section, key)
        elif structure_type == constants.structure_type_float:
            return config.getfloat(section, key)
        elif structure_type == constants.structure_type_boolean:
            return config.getboolean(section, key)
        else:
            return config.get(section, key)
    except configparser.Error:
        raise Exception("Failed to read key from file. File: \'" + file_name + "\', Section: \'" + section + "\', " +
                        "Key: \'" + key + "\', Type: \'" + structure_type + "\'")

    return key

# initialize first parameters - start
comma_delimiter = ","
hyphen_delimiter = "-"
log_enabled = read_property_key("log_enabled", constants.structure_type_boolean, constants.section_parameters,
                                constants.property_file)
random_text_test = read_property_key("random_text_test", constants.structure_type_boolean, constants.section_parameters,
                                     constants.property_file)
length_of_random_text = 0
if random_text_test:
    length_of_random_text = read_property_key("length_of_random_text", constants.structure_type_int,
                                              constants.section_parameters, constants.property_file)
private_key_primes_bit_length = read_property_key("private_key_primes_bit_length", constants.structure_type_int,
                                                  constants.section_key, constants.property_file)
# initialize first parameters - end


def validate_initial_parameters():
    """
    :return: validate initial parameters before run
    """
    validation_message = ""
    log_enable_regex_check = check_regex_match(str(log_enabled), constants.regex_pattern_boolean)
    if not log_enable_regex_check:
        validation_message = "Log enabled parameter can set only true or false. " + \
                             "Rearrange it from " + str(constants.property_file)
    return validation_message


def user_input(m, r):
    """
    :param m: direction message
    :param r: regex pattern to validate
    :return: user input text
    """
    text_input = input(m + " > ")
    while not check_regex_match(text_input, r):
        wrong_input = "\n" + constants.background_colorant_red + "You entered a wrong input." + \
                      constants.attribute_default + "\n" + m
        text_input = input(wrong_input + " > ")

    return text_input


def press_enter_to_continue():
    """
    :return:
    """
    input("Press Enter to continue...\n")


def text_to_ascii_response(text):
    """
    :param text:
    :return: a list which holds ascii responses of every char in text one-by-one
    """
    return [ord(c) for c in text]


def ascii_responses_to_text(ascii_responses):
    """
    :param ascii_responses:
    :return: a list which holds char responses of ascii values one-by-one
    """
    return [str(chr(n)) for n in ascii_responses]


def check_regex_match(text, regex_pattern):
    """
    :param text: text to check does pattern match
    :param regex_pattern: pattern to look up
    :return: does regex_pattern match on text or not
    """
    if regex_pattern == "":
        return True
    compiled_regex = re.compile(regex_pattern)
    match = compiled_regex.search(text)
    if match:
        return True
    else:
        return False


def is_prime(n):
    """
    :param n:
    :return: boolean which tells the given number is prime or not
    """
    if n >= 3:
        if (n & 1) != 0:
            for p in constants.low_primes:
                if n == p:
                    return True
                if n % p == 0:
                    return False
            return rabin_miller_primality_test(n)
    return False


def rabin_miller_primality_test(n):
    """
    :param n:
    :return: boolean which tells the given number is prime or not
    """
    s = n - 1
    t = 0
    while s % 2 == 0:
        s //= 2
        t += 1
    k = 0
    while k < 128:
        a = random.randrange(2, n - 1)
        v = pow(a, s, n)
        if v != 1:
            i = 0
            while v != (n - 1):
                if i == t - 1:
                    return False
                else:
                    i += 1
                    v = pow(v, 2, n)
        k += 2
    return True


def determine_power_prime_to_mask():
    """
    :return: a prime number which will be used to mask text while ciphering
    """
    bit_length = private_key_primes_bit_length // 2
    return generate_large_prime(bit_length)


def calculate_totient_of_primes(m, n):
    """
    :param m:
    :param n:
    :return: a number which is totient (phi function result) of given primes
    """
    if not is_prime(m) or not is_prime(n):
        raise ValueError("At least one of the numbers is not a prime number: " + str(m) + ", " + str(n))
    else:
        return (m-1)*(n-1)


def generate_random_text(l):
    """
    :param l: length of text
    :return: a random text which contains letters, digits and punctuations
    """
    random_text = ""
    chars = string.ascii_letters + string.digits + string.punctuation
    for n in range(l):
        random_text += choice(chars)

    return random_text


def generate_large_prime(k):
    """
    :param k:
    :return: k bit prime number which is generated
    """
    r = 100 * (math.log(k, 2) + 1)
    r_ = r
    while r > 0:
        n = random.randrange(2 ** (k - 1), 2 ** k)
        r -= 1
        if is_prime(n) is True:
            return n
    print("Large prime number could not generated after " + str(r_) + " tries. Try again.")
    sys.exit()
