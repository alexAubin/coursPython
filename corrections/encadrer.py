def centrer(mot, N=20):
    L = (N - len(mot))/2
    space_left = " " * int(L)
    space_right = " " * int(L+0.5)
    return space_left + mot + space_right


def encadrer(mot, N=20, c="#"):
    if N == -1:
        return c * (len(mot) + 4) + "\n" \
             + c + " " + mot + " " + c + "\n" \
             + c * (len(mot) + 4)
    else:
        return c * (N + 4) + "\n" \
             + c + " " + centrer(mot, N) + " " + c + "\n" \
             + c * (N + 4)

print(encadrer("pikach",30))
print(encadrer("pikachu",30))
print(encadrer("pikachut",-1, c="="))
