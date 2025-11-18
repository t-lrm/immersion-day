import sujet_2.skeleton.warmup as warmup
import sujet_2.skeleton.serious_encodings as serious_encodings
import sujet_2.skeleton.hard as hard
from Moulinette.unit_test import *
from Moulinette.test_suite import TestSuite

test_caesar_encode = TestSuite(warmup.caesar_encode)
test_caesar_encode.add(AssertOutput(["bac", 2], "dce"))
test_caesar_encode.add(AssertOutput(["bowser fait du zele!", 7], "ivdzly mhpa kb glsl!"))
test_caesar_encode.add(AssertOutput(["koopa", -3], "hllmx"))
test_caesar_encode.add(AssertOutput(["mario aime beaucoup les champignons", 9817], "bpgxd pxbt qtpjrdje ath rwpbexvcdch"))
test_caesar_encode.add(AssertOutput(["", 0], ""))

test_caesar_decode = TestSuite(warmup.caesar_decode)
test_caesar_decode.add(AssertOutput(["bac", 2], "dce"))
test_caesar_decode.add(AssertOutput(["bowser fait du zele!", 7], "ivdzly mhpa kb glsl!"))
test_caesar_decode.add(AssertOutput(["koopa", -3], "hllmx"))
test_caesar_decode.add(AssertOutput(["mario aime beaucoup les champignons", 9817], "bpgxd pxbt qtpjrdje ath rwpbexvcdch"))
test_caesar_decode.add(AssertOutput(["", 0], ""))

test_substitution_encode = TestSuite(warmup.substitution_encode)
test_substitution_encode.add(AssertOutput(["bowser travaille dur pour rendre la vie difficile a mario.", "fqhowjlzabxsekdcgpmnuyrvti"], "qdrmwp npfyfassw oup cdup pwkopw sf yaw oajjahasw f efpad."))
test_substitution_encode.add(AssertOutput(["le resultat est illisible!", "azertyuiopqsdfghjklmwxcvbn"], "st ktlwsmam tlm ossolozst!"))
test_substitution_encode.add(AssertOutput(["", "azertyuiopqsdfghjklmwxcvbn"], ""))

test_substitution_decode = TestSuite(warmup.substitution_decode)
test_substitution_decode.add(AssertOutput(["qdrmwp npfyfassw oup cdup pwkopw sf yaw oajjahasw f efpad.", "fqhowjlzabxsekdcgpmnuyrvti"], "bowser travaille dur pour rendre la vie difficile a mario."))
test_substitution_decode.add(AssertOutput(["st ktlwsmam tlm ossolozst!", "azertyuiopqsdfghjklmwxcvbn"], "le resultat est illisible!"))
test_substitution_decode.add(AssertOutput(["", "azertyuiopqsdfghjklmwxcvbn"], ""))

test_vigenere_encode = TestSuite(warmup.vigenere_encode)
test_vigenere_encode.add(AssertOutput(["bonjour les amis", "vigenere"], "wwtnbyi gmy nqzw"))
test_vigenere_encode.add(AssertOutput(["bowser aime bien ces petits exercices", "toad"], "ucwvxf dbae uweq qev dewbhs xleuvwchl"))
test_vigenere_encode.add(AssertOutput(["", "vigenere"], ""))

test_vigenere_decode = TestSuite(warmup.vigenere_decode)
test_vigenere_decode.add(AssertOutput(["bonjour les amis", "vigenere"], "wwtnbyi gmy nqzw"))
test_vigenere_decode.add(AssertOutput(["bowser aime bien ces petits exercices", "toad"], "ucwvxf dbae uweq qev dewbhs xleuvwchl"))
test_vigenere_decode.add(AssertOutput(["", "vigenere"], ""))

test_xor_encode = TestSuite(warmup.xor_encode)
xor_encoded = "".join(chr(c) for c in [30, 66, 8, 14, 24, 31, 23, 21, 6, 76, 80, 20, 20, 12, 1, 83, 75])
test_xor_encode.add(AssertOutput(["n'importe$ quoi#.", "peach"], xor_encoded))
test_xor_encode.add(AssertOutput(["", "peach"], ""))
test_xor_encode.add(AssertOutput([xor_encoded, "peach"], "n'importe$ quoi#."))

def _caesar_door(messages): # Helper function
    res = serious_encodings.caesar_doors(messages)
    if res is None:
        return None
    return [door.message for door in res]

test_caesar_door = TestSuite(_caesar_door)
test_caesar_door.add(AssertOutput([["sauter", "faire un double saut", "s'accroupir"]], ["ygazkx", "zucly oh xiovfy muon", "d'lnnczfatc"]))
test_caesar_door.add(AssertOutput([["joe", "seme", "phare", "champ"]], ['mrh', 'wiqi', 'umfwj', 'hmfru']))

test_transposition_encode = TestSuite(serious_encodings.transposition_encode)
test_transposition_encode.add(AssertOutput(["donkey", [2, 1, 3, 0]], "koyden"))
test_transposition_encode.add(AssertOutput(["donkey", [0, 1, 2, 3]], "deoynk"))
test_transposition_encode.add(AssertOutput(["donkey", [0, 1, 2, 3, 4, 5]], "donkey"))
test_transposition_encode.add(AssertOutput(["Cette phrase sera toute chamboulée.", [1, 4, 2, 5, 0, 6, 3]], "eethéChetbtaa upsum.erreots cl  oae"))
test_transposition_encode.add(AssertOutput(["", [1, 4, 2, 5, 0, 6, 3]], ""))

test_transposition_decode = TestSuite(serious_encodings.transposition_decode)
test_transposition_decode.add(AssertOutput(["koyden", [2, 1, 3, 0]], "donkey"))
test_transposition_decode.add(AssertOutput(["deoynk", [0, 1, 2, 3]], "donkey"))
test_transposition_decode.add(AssertOutput(["donkey", [0, 1, 2, 3, 4, 5]], "donkey"))
test_transposition_decode.add(AssertOutput(["eethéChetbtaa upsum.erreots cl  oae", [1, 4, 2, 5, 0, 6, 3]], "Cette phrase sera toute chamboulée."))
test_transposition_decode.add(AssertOutput(["", [1, 4, 2, 5, 0, 6, 3]], ""))

test_hill_encode = TestSuite(serious_encodings.hill_encode)
test_hill_encode.add(AssertOutput(["mario est un nigaud", [[3, 5], [6, 17]]], "kunebhysqlvdevcuwcut"))
test_hill_encode.add(AssertOutput(["bowser est le plus fort", [[57, 9], [8, 83]]], "bamgrnvwbfgftrstcqebppqh"))
test_hill_encode.add(AssertOutput(["mario", [[3, 8], [87, 65]]], "kelxsj"))

test_hill_decode = TestSuite(serious_encodings.hill_decode)
test_hill_decode.add(AssertOutput(["kunebhysqlvdevcuwcut", [[3, 5], [6, 17]]], "marioxestxunxnigaudx"))
test_hill_decode.add(AssertOutput(["bamgrnvwbfgftrstcqebppqh", [[57, 9], [8, 83]]], "bowserxestxlexplusxfortx"))
test_hill_decode.add(AssertOutput(["kelxsj", [[3, 8], [87, 65]]], "mariox"))

test_gcd = TestSuite(hard.gcd)
test_gcd.add(AssertOutput([0, 0], 0))
test_gcd.add(AssertOutput([0, 1], 1))
test_gcd.add(AssertOutput([12, 18], 6))
test_gcd.add(AssertOutput([17, 23], 1))
test_gcd.add(AssertOutput([-100, 100], 100))

test_egcd = TestSuite(hard.egcd)
test_egcd.add(AssertOutput([0, 1], (1, 0, 1)))
test_egcd.add(AssertOutput([12, 18], (6, -1, 1)))
test_egcd.add(AssertOutput([17, 23], (1, -4, 3)))
test_egcd.add(AssertOutput([-100, 100], (100, -1, 0)))

test_generate_key = TestSuite(hard.generate_key)
test_generate_key.add(AssertOutput([17, 23], (391, 3, 235)))
test_generate_key.add(AssertOutput([101, 103], (10403, 7, 8743)))
test_generate_key.add(AssertOutput([10007, 10009], (100160063, 5, 60084029)))

test_rsa_encode = TestSuite(hard.rsa_encode)
test_rsa_encode.add(AssertOutput(["mario", (391, 3)], [37, 79, 45, 265, 304]))
test_rsa_encode.add(AssertOutput(["bowser", (10403, 7)], [4378, 6252, 5199, 2228, 6464, 3176]))
test_rsa_encode.add(AssertOutput(["mario", (100160063, 5)], [61749910, 73734902, 23413728, 42487624, 23690967]))

test_rsa_decode = TestSuite(hard.rsa_decode)
test_rsa_decode.add(AssertOutput([[37, 79, 45, 265, 304], (391, 235)], "mario"))
test_rsa_decode.add(AssertOutput([[4378, 6252, 5199, 2228, 6464, 3176], (10403, 8743)], "bowser"))
test_rsa_decode.add(AssertOutput([[61749910, 73734902, 23413728, 42487624, 23690967], (100160063, 60084029)], "mario"))