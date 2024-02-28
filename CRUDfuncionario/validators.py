import re
from django.core.exceptions import ValidationError
def valida_cnpj(cnpj):
        #Função para validar o cnpj, será aplicada em trabalhos futuros
    cnpj = ''.join(re.findall('\\d', str(cnpj)))

    if (len(cnpj) != 14):
            return False

    inteiros = list(map(int, cnpj))
    novo = inteiros[:12]

    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    while len(novo) < 14:
        r = sum([x*y for (x, y) in zip(novo, prod)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)
        prod.insert(0, 6)

    if novo == inteiros:
        return True

    return False
        
def valida_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
        # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

        # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito1 = 0 if resto == 10 else resto

        # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito2 = 0 if resto == 10 else resto

        # Verifica se os dígitos verificadores são iguais aos dois últimos dígitos do CPF
    return cpf[-2:] == f"{digito1}{digito2}"
def valida_texto(text):
    if not text.isalpha():
        raise ValidationError(
            _("A string deve conter apenas letras"),
            code="invalid_text",
            )