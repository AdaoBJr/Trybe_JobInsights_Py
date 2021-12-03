from src.sorting import sort_by

# Esse teste deve se chamar test_sort_by_criteria e garantir que # a função funciona segundo esta especificação:

# A função sort_by recebe dois parâmetros:
# jobs uma lista de dicionários com os detalhes de cada emprego;
# criteria uma string com uma chave para ser usada como critério de ordenação.
# O parâmetro criteria deve ter um destes
# valores: min_salary, max_salary, date_posted


def test_sort_by_criteria():
    assert sort_by(
        [{"title_job": "Senior Software Engineer", "company": "Google"}],
        "min_salary",
    ) is None
