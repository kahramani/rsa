import sys
import constants
import utility
import ciphering
import deciphering
import logger
import time

"""
For test purposes. You can also use this file as main file to check all application
"""
logger = logger.build_logger("tester")


def main():
    validation_message = utility.validate_initial_parameters()
    if validation_message != "":
        print(validation_message)
        sys.exit()

    print(constants.terminal_delimiter)
    print("\n" + constants.foreground_colorant_yellow + "The application started" + constants.attribute_default)
    private_key_primes_holder = list()
    generated_key_found = False
    t1 = time.process_time()
    print("\nPublic keys are generating...")
    while generated_key_found is False:
        private_key_primes_holder.append(utility.generate_large_prime(utility.private_key_primes_bit_length))
        private_key_primes_holder.append(utility.generate_large_prime(utility.private_key_primes_bit_length))
        if private_key_primes_holder[0] == private_key_primes_holder[1]:
            private_key_primes_holder = list()
            print("\n" + str(utility.private_key_primes_bit_length) + " bit prime number generation produce the same" +
                  " prime numbers for pair. So, public keys are generating again...")
        else:
            generated_key_found = True
    print("\nGenerating two " + str(utility.private_key_primes_bit_length) + " bit prime numbers" + " took " +
          str(time.process_time()-t1) + " ms.")
    t = time.process_time()
    multiplication_of_key_primes = private_key_primes_holder[0] * private_key_primes_holder[1]
    print("\nMultiplication of key primes took " + str(time.process_time() - t) + " ms.")
    t = time.process_time()
    totient_of_key_primes = utility.calculate_totient_of_primes(private_key_primes_holder[0],
                                                                private_key_primes_holder[1])
    print("\nCalculating totient of key primes took " + str(time.process_time() - t) + " ms.")
    t = time.process_time()
    power_prime_to_mask = utility.determine_power_prime_to_mask()
    print("\nDetermining power prime to mask took " + str(time.process_time() - t) + " ms.")
    t = time.process_time()
    if utility.log_enabled:
        print("\nprivate_key_primes: " + str(private_key_primes_holder[0]) + ", " + str(private_key_primes_holder[1]))
        print("totient_of_key_primes: " + str(totient_of_key_primes))
        print("power_prime_to_mask: " + str(power_prime_to_mask))

    print("\nPublic keys are generated. It took " + str(time.process_time()-t) + " ms in total. \n" +
          "power to mask: " + str(power_prime_to_mask) + " \n" +
          "key primes multiplication: " + str(multiplication_of_key_primes) + " \n" +
          constants.foreground_colorant_green +
          "These keys will be used to cipher the message you text.\n" + constants.attribute_default)

    input_text = ""
    if not utility.random_text_test:
        input_text = utility.user_input("Please enter text to cipher", "")
        print("input text: " + str(input_text) + "\n")
    else:
        input_text = utility.generate_random_text(utility.length_of_random_text)
        print("generated input text: " + str(input_text) + "\n")
        utility.press_enter_to_continue()

    print("Ciphering part of the application is starting...\n")

    ascii_response_of_text = utility.text_to_ascii_response(input_text)

    if utility.log_enabled:
        print("ascii_response_of_text: " + str(ascii_response_of_text) + "\n")

    cipher_text = ciphering.cipher_with_public_keys(ascii_response_of_text,
                                                    multiplication_of_key_primes, power_prime_to_mask)

    print("Ciphering part of the application is over. You just sent this cipher text: \n" + str(cipher_text) + " \n" +
          constants.foreground_colorant_green +
          "It can't be deciphered by anybody except the one who generated the public key vector." +
          constants.attribute_default + "\n")

    decipher_as_receiver(cipher_text, private_key_primes_holder, power_prime_to_mask, multiplication_of_key_primes)

    print("\n" + constants.foreground_colorant_yellow + "The application ended" + constants.attribute_default)
    print(constants.terminal_delimiter)


def decipher_as_receiver(cipher_text, private_key_primes_holder, power_prime_to_mask, multiplication_of_key_primes):
    t = time.process_time()
    print("\nAs a " + constants.bold_attribute + "RECEIVER" + constants.attribute_default +
          " who generated public keys, you own the private key primes. \n" +
          constants.foreground_colorant_green +
          "So, you can easily decipher the cipher text with using multiplicative inverse which is acquirable from " +
          "private key primes and public power prime to mask." + constants.attribute_default + "\n")

    print("Deciphering part is about to start...\n")
    totient_of_key_primes = utility.calculate_totient_of_primes(private_key_primes_holder[0],
                                                                private_key_primes_holder[1])

    multiplicative_inverse = deciphering.calculate_modular_inverse(constants.algorithm_totient,
                                                                   power_prime_to_mask, totient_of_key_primes)

    if utility.log_enabled:
        print("totient_of_key_primes: " + str(totient_of_key_primes) + "\n")
        print("multiplicative_inverse: " + str(multiplicative_inverse) + "\n")
        print("\nDetermining totient and multiplicative inverse took " + str(time.process_time() - t) + " ms.")

    deciphered_vector = deciphering.decipher_with_private_keys(cipher_text, multiplicative_inverse,
                                                               multiplication_of_key_primes)

    if utility.log_enabled:
        print("deciphered_vector: " + str(deciphered_vector) + "\n")

    deciphered_text_vector = utility.ascii_responses_to_text(deciphered_vector)

    deciphered_text = ""
    for i in range(0, len(deciphered_text_vector)):
        deciphered_text += deciphered_text_vector[i]

    print("Finished to decipher the text in " + str(time.process_time()-t) + " ms as a receiver.\n\n" +
          "Original text: " +
          str(deciphered_text))

    return True


if __name__ == "__main__":
    main()
