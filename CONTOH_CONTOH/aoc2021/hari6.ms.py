اينڤوت = [1,2,1,1,1,1,1,1,2,1,3,1,1,1,1,3,1,1,1,5,1,1,1,4,5,1,1,1,3,4,1,1,1,1,1,1,1,5,1, 4,1,1,1,1,1,1,1,5,1,3,1,3,1,1,1,5,1,1,1,1,1,5,4,1,2,4,4,1, 1,1,1,1,5,1,1,1,1,1,5,4,3,1,1,1,1,1,1,1,5,1,3,1,4,1,1,3,1, 1,1,1,1,1,2,1,4,1,3,1,1,1,1,1,5,1,1,1,2,1,1,1,1,2,1,1,1,1, 4,1,3,1,1,1,1,1,1,1,1,5,1,1,4,1,1,1,1,1,3,1,3,3,1,1,1,2,1, 1,1,1,1,1,1,1,1,5,1,1,1,1,5,1,1,1,1,2,1,1,1,4,1,1,1,2,3,1, 1,1,1,1,1,1,1,2,1,1,1,2,3,1,2,1,1,5,4,1,1,2,1,1,1,3,1,4,1, 1,1,1,3,1,2,5,1,1,1,5,1,1,1,1,1,4,1,1,4,1,1,1,2,2,2,2,4,3, 1,1,3,1,1,1,1,1,1,2,2,1,1,4,2,1,4,1,1,1,1,1,5,1,1,4,2,1,1, 2,5,4,2,1,1,1,1,4,2,3,5,2,1,5,1,3,1,1,5,1,1,4,5,1,1,1,1,4
]

#اينڤوت = [3,4,3,1,2]
'''
اونتوق شي دالم اينڤوت:
    چيتق(شي ,end=' ')
'''

'''
اونتوق _ دالم جولت(80):
    چيتق(_ ,len(اينڤوت))
    اونتوق ي ,ن دالم مڠڠکاکن(اينڤوت):
        جک ن == 0:
            اينڤوت[ي] = 7
            اينڤوت.append(9)
        اينڤوت[ي] -= 1

چيتق(len(اينڤوت))
'''

ڤڠيرا = {شي  :اينڤوت.count(شي) اونتوق شي دالم جولت(0 ,9)}

اونتوق _ دالم جولت(256):
    چيتق(_ ,(ڤڠيرا))
    کوسوڠ = ڤڠيرا[0]
    اونتوق شي دالم جولت(0 ,8):
        ڤڠيرا[شي] = ڤڠيرا[شي+1]
    ڤڠيرا[6] += کوسوڠ
    ڤڠيرا[8] = کوسوڠ

چيتق(ڤڠيرا,تمبه(ڤڠيرا.values()))


# 390923
# 1749945484935























    #
