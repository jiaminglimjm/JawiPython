# https://projecteuler.net/problem=1
جواڤن = 0

اونتوق ن دالم جولت(1000):
    جک ن % 3 == 0:
        جواڤن += ن
    جک ن % 5 == 0:
        جواڤن += ن
    جک ن % 15 == 0:
        جواڤن -= ن

چيتق(جواڤن)
