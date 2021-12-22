from src.sorting import sort_by

sort_criteria = [
    {
        "min_salary": 7000,
        "max_salary": 11000,
        "date_posted": "2021-12-22",
    },
    {
        "min_salary": 4000,
        "max_salary": 6000,
        "date_posted": "2021-11-22",
    },
    {
        "min_salary": 1000,
        "max_salary": 3000,
        "date_posted": "2021-10-22",
    },
]

sort_min_salary = [sort_criteria[2], sort_criteria[1], sort_criteria[0]]
sort_max_salary = [sort_criteria[0], sort_criteria[1], sort_criteria[2]]


def test_sort_by_criteria():
    sort_by(sort_criteria, "min_salary")
    assert sort_criteria == sort_min_salary

    sort_by(sort_criteria, "max_salary")
    assert sort_criteria == sort_max_salary

# deve se chamar test_sort_by_criteria e garantir que a função funciona segundo
# esta especificação:

# A função sort_by recebe dois parâmetros:
# jobs uma lista de conhecimento com os detalhes de cada emprego;
# criteria uma string com uma chave para ser usada como critério de ordenação.
# O parámetro criteriaDEVE ter hum destes Valores: min_salary, max_salary,
# date_posted
# A ordenação para min_salarydeve ser crescente, mas para max_salaryou
# date_posteddevem ser decrescentes.
# Os empregos que não apresentarem um valor válido no campo escolhido para
# ordenação devem aparecer no final da lista.
