while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except EOFError:
        print("EOFerror")
        break
    except ValueError:
        print("ValueError")
        break