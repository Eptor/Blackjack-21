from esp import run_es as esp
from eng import run_en as eng

while True:
    leng = int(input('[1] Español\n[2] English\n> '))

    if leng == 1:
        esp()
    elif leng == 2:
        print('Still work in progress :(')
    else:
        print('Numero incorrecto // Wrong number')
