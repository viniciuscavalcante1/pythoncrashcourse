def make_sandwich(*args):
    print(f"Seu sanduíche contém {", ".join(args)}")

make_sandwich('quejo', 'presunto')
make_sandwich('queijo')
make_sandwich('tomate', 'frango', 'requeijão')