from functools import partial

def main():
    print("lambdas with late binding:")
    ns = range(5)
    lambda_with_late_binding = []
    for n in ns:
        lambda_with_late_binding.append(lambda: print(f"{n=}"))
    for fun in lambda_with_late_binding:
        fun()
    
    print("\nlambda with early binding (default arg):")
    lambda_with_early_binding = []
    for n in ns:
        lambda_with_early_binding.append(lambda n=n: print(f"{n=}"))
    for fun in lambda_with_early_binding:
        fun()

    print("\nearly binding with partial:")
    def show_n(n):
        print(f"{n=}")

    lambda_with_partial = []
    for n in ns:
        lambda_with_partial.append(partial(show_n, n=n))
    for fun in lambda_with_partial:
        fun()

    print("\nearly binding using a closure:")
    def get_fun(n):
        return lambda: print(f"{n=}")
    early_binding_with_closure = []
    for n in ns:
        early_binding_with_closure.append(get_fun(n))
    for fun in early_binding_with_closure:
        fun()                           

if __name__ == "__main__":
    main()
