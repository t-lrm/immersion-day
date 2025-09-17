from moulinette import *
import warmup
import serious_encodings
import hard

c_encode = Test("caesar_encode", warmup.caesar_encode)
c_encode.add(["bac", 2], "dce")
c_encode.add(["bowser fait du zele!", 7], "ivdzly mhpa kb glsl!")
c_encode.add(["koopa", -3], "hllmx")
c_encode.add(["mario aime beaucoup les champignons", 9817], "bpgxd pxbt qtpjrdje ath rwpbexvcdch")
c_encode.add(["", 0], "")
c_encode.run()

c_decode = Test("caesar_decode", warmup.caesar_decode)
c_decode.add(["dce", 2], "bac")
c_decode.add(["ivdzly mhpa kb glsl!", 7], "bowser fait du zele!")
c_decode.add(["hllmx", -3], "koopa")
c_decode.add(["bpgxd pxbt qtpjrdje ath rwpbexvcdch", 9817], "mario aime beaucoup les champignons")
c_decode.add(["", 0], "")
c_decode.run()

s_encode = Test("substitution_encode", warmup.substitution_encode)
s_encode.add(["bowser travaille dur pour rendre la vie difficile a mario.", "fqhowjlzabxsekdcgpmnuyrvti"], "qdrmwp npfyfassw oup cdup pwkopw sf yaw oajjahasw f efpad.")
s_encode.add(["le resultat est illisible!", "azertyuiopqsdfghjklmwxcvbn"], "st ktlwsmam tlm ossolozst!")
s_encode.add(["", "azertyuiopqsdfghjklmwxcvbn"], "")
s_encode.run()

s_decode = Test("substitution_decode", warmup.substitution_decode)
s_decode.add(["qdrmwp npfyfassw oup cdup pwkopw sf yaw oajjahasw f efpad.", "fqhowjlzabxsekdcgpmnuyrvti"], "bowser travaille dur pour rendre la vie difficile a mario.")
s_decode.add(["st ktlwsmam tlm ossolozst!", "azertyuiopqsdfghjklmwxcvbn"], "le resultat est illisible!")
s_decode.add(["", "azertyuiopqsdfghjklmwxcvbn"], "")
s_decode.run()

v_encode = Test("vigenere_encode", warmup.vigenere_encode)
v_encode.add(["bonjour les amis", "vigenere"], "wwtnbyi gmy nqzw")
v_encode.add(["bowser aime bien ces petits exercices", "toad"], "ucwvxf dbae uweq qev dewbhs xleuvwchl")
v_encode.add(["", "vigenere"], "")
v_encode.run()

v_decode = Test("vigenere_decode", warmup.vigenere_decode)
v_decode.add(["wwtnbyi gmy nqzw", "vigenere"], "bonjour les amis")
v_decode.add(["ucwvxf dbae uweq qev dewbhs xleuvwchl", "toad"], "bowser aime bien ces petits exercices")
v_decode.add(["", "vigenere"], "")
v_decode.run()

x_encode = Test("xor_encode", warmup.xor_encode)
xor_encoded = "".join(chr(c) for c in [30, 66, 8, 14, 24, 31, 23, 21, 6, 76, 80, 20, 20, 12, 1, 83, 75])
x_encode.add(["n'importe$ quoi#.", "peach"], xor_encoded)
x_encode.add(["", "peach"], "")
x_encode.add([xor_encoded, "peach"], "n'importe$ quoi#.")
x_encode.run()


def caesar_test(messages):
    res = serious_encodings.caesar_doors(messages)
    if res is None:
        return None
    return [door.message for door in res]


c_doors = Test("caesar_doors", caesar_test)
c_doors.add([["sauter", "faire un double saut", "s'accroupir"]], ["ygazkx", "zucly oh xiovfy muon", "d'lnnczfatc"])
c_doors.add([["joe", "seme", "phare", "champ"]], ['mrh', 'wiqi', 'umfwj', 'hmfru'])
c_doors.run()

t_encode = Test("transposition_encode", serious_encodings.transposition_encode)
t_encode.add(["donkey", [2, 1, 3, 0]], "koyden")
t_encode.add(["donkey", [0, 1, 2, 3]], "deoynk")
t_encode.add(["donkey", [0, 1, 2, 3, 4, 5]], "donkey")
t_encode.add(["Cette phrase sera toute chamboulée.", [1, 4, 2, 5, 0, 6, 3]], "eethéChetbtaa upsum.erreots cl  oae")
t_encode.add(["", [1, 4, 2, 5, 0, 6, 3]], "")
t_encode.run()

t_decode = Test("transposition_decode", serious_encodings.transposition_decode)
t_decode.add(["koyden", [2, 1, 3, 0]], "donkey")
t_decode.add(["deoynk", [0, 1, 2, 3]], "donkey")
t_decode.add(["donkey", [0, 1, 2, 3, 4, 5]], "donkey")
t_decode.add(["eethéChetbtaa upsum.erreots cl  oae", [1, 4, 2, 5, 0, 6, 3]], "Cette phrase sera toute chamboulée.")
t_decode.add(["", [1, 4, 2, 5, 0, 6, 3]], "")
t_decode.run()

h_encode = Test("hill_encode", serious_encodings.hill_encode)
h_encode.add(["mario est un nigaud", [[3, 5], [6, 17]]], "kunebhysqlvdevcuwcut")
h_encode.add(["bowser est le plus fort", [[57, 9], [8, 83]]], "bamgrnvwbfgftrstcqebppqh")
h_encode.add(["mario", [[3, 8], [87, 65]]], "kelxsj")
h_encode.run()

h_decode = Test("hill_decode", serious_encodings.hill_decode)
h_decode.add(["kunebhysqlvdevcuwcut", [[3, 5], [6, 17]]], "marioxestxunxnigaudx")
h_decode.add(["bamgrnvwbfgftrstcqebppqh", [[57, 9], [8, 83]]], "bowserxestxlexplusxfortx")
h_decode.add(["kelxsj", [[3, 8], [87, 65]]], "mariox")
h_decode.run()

test_gcd = Test("gcd", hard.gcd)
test_gcd.add([0, 0], 0)
test_gcd.add([0, 1], 1)
test_gcd.add([12, 18], 6)
test_gcd.add([17, 23], 1)
test_gcd.add([-100, 100], 100)
test_gcd.run()

test_egcd = Test("egcd", hard.egcd)
test_egcd.add([0, 1], (1, 0, 1))
test_egcd.add([12, 18], (6, -1, 1))
test_egcd.add([17, 23], (1, -4, 3))
test_egcd.add([-100, 100], (100, -1, 0))
test_egcd.run()

key_gen = Test("generate_key", hard.generate_key)
key_gen.add([17, 23], (391, 3, 235))
key_gen.add([101, 103], (10403, 7, 8743))
key_gen.add([10007, 10009], (100160063, 5, 60084029))
key_gen.run()

r_encode = Test("rsa_encode", hard.rsa_encode)
r_encode.add(["mario", (391, 3)], [37, 79, 45, 265, 304])
r_encode.add(["bowser", (10403, 7)], [4378, 6252, 5199, 2228, 6464, 3176])
r_encode.add(["mario", (100160063, 5)], [61749910, 73734902, 23413728, 42487624, 23690967])
r_encode.run()

r_decode = Test("rsa_decode", hard.rsa_decode)
r_decode.add([[37, 79, 45, 265, 304], (391, 235)], "mario")
r_decode.add([[4378, 6252, 5199, 2228, 6464, 3176], (10403, 8743)], "bowser")
r_decode.add([[61749910, 73734902, 23413728, 42487624, 23690967], (100160063, 60084029)], "mario")
r_decode.run()


