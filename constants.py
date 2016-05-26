"""
initialize constants which are going to use
"""
property_file = "config\\rsa.properties"
log_file = "logs\\rsa.log"
regex_pattern_english_alphabet = "[a-zA-Z]+$"
regex_pattern_digit = "\d+$"
regex_pattern_range = "\d+-\d+$"
regex_pattern_boolean = "(?i)true$|false$"
regex_pattern_decipher_side_choice = "(?i)^(r|a)$"
foreground_colorant_black = "\033[30m"
foreground_colorant_red = "\033[31m"
foreground_colorant_green = "\033[32m"
foreground_colorant_yellow = "\033[33m"
foreground_colorant_blue = "\033[34m"
background_colorant_black = "\033[40m"
background_colorant_red = "\033[41m"
background_colorant_green = "\033[42m"
background_colorant_yellow = "\033[43m"
background_colorant_blue = "\033[44m"
background_colorant_white = "\033[47m"
bold_attribute = "\033[1m"
attribute_default = "\033[0m"
terminal_delimiter = "\n*******************"
section_key = "KeySection"
section_parameters = "ParametersSection"
algorithm_brute_force = "BruteForce"
algorithm_totient = "Totient"
algorithm_back_tracking = "BackTracking"
structure_type_string = "String"
structure_type_boolean = "Boolean"
structure_type_int = "Int"
structure_type_float = "Float"
low_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
              101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
              181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269,
              271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367,
              373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
              463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
              577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661,
              673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773,
              787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883,
              887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
