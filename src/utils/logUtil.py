import sys

def printProgress(limmit : int, index : int) -> None:
    limmit -= 1
    n = (100*index) / limmit
    n = '{:.2f}'.format(n)
    sys.stdout.write('\r')
    sys.stdout.write("PROGRESSO >> {}% (registro = {})".format(n, index))
    sys.stdout.flush()

    if limmit == index:
        print("\nFINALIZADO!")