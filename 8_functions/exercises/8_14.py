def make_car(model, company, **kwargs):
    kwargs['model'] = model
    kwargs['company'] = company
    return kwargs

print(make_car('onix', 'chevrolet', color='black', year=2015))
