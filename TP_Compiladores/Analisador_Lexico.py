from tokens import tokens
from tabulate import tabulate

# ----------------------------------------------------------------------------------------------------------------------
# Observações : Nesse codigo foi usada a tabela ascii para verificar os argumentos passados pelo arquivo
# ----------------------------------------------------------------------------------------------------------------------
namefile = input('Informe o nome do arquivo : ')
try:
    arquivo = open('Arquivos_Entrada/' + namefile, "r")  # Ler arquivo de entrada
except:
    print("Este arquivo não foi encontrado ou não pode ser aberto")
    exit()
token_vet = []
vetorTokens = []
buffer = []
state = 0
line_count = 1
erros_lexicos = open('Erros_Lexicos/' + 'saida_' + namefile + '.txt', "w")

for line in arquivo:
    line = line.rstrip('\n')
    word_count = 0
    while word_count < len(line):
        word = line[word_count]
        if state == 0:
            if word.isalpha():
                state = 1
                buffer.append(word)
            elif word.isnumeric():
                state = 2
                buffer.append(word)
            elif word == ':':
                state = 5
                buffer.append(word)
            elif word == '"':
                state = 6
                buffer.append(word)
            elif word == '=':
                state = 7
                buffer.append(word)
            elif word == '!':
                state = 8
                buffer.append(word)
            elif word == '<':
                state = 9
                buffer.append(word)
            elif word == '>':
                state = 10
                buffer.append(word)
            elif word == ' ' or word == '\t':
                pass
            else:
                buffer.append(word)
                lexeme = ''.join(buffer)
                token_vet.append([tokens[lexeme], lexeme, line_count])
                vetorTokens.append(tokens[lexeme])
                buffer = []  # Limpa o buffer

        elif state == 1:
            if 65 <= ord(word) <= 90 or 97 <= ord(word) <= 122 or 48 <= ord(word) <= 57 or word == '_':
                buffer.append(word)
            else:
                word_count -= 1
                state = 0
                lexeme = ''.join(buffer)
                # Caso exista cria o token reservado, se não cria um token ID
                token_vet.append([tokens[lexeme] if lexeme in tokens else "ID", lexeme, line_count])
                vetorTokens.append(tokens[lexeme] if lexeme in tokens else 'ID')
                buffer = []

        elif state == 2:
            if 48 <= ord(word) <= 57:
                buffer.append(word)
            elif word == '.':
                state = 3
                buffer.append(word)
            else:
                word_count -= 1
                state = 0
                lexeme = ''.join(buffer)
                token_vet.append(["INTEGER_CONST", lexeme, line_count])
                vetorTokens.append('INTEGER_CONST')
                buffer = []

        elif state == 3:
            if word.isnumeric():
                state = 4
                buffer.append(word)
            else:
                token_vet.append(["ERRO LEXICO", lexeme, line_count])
                vetorTokens.append('ERRO LEXICO')
                erros_lexicos.write(f'ERRO LEXICO na linha {line_count}')

        elif state == 4:
            if 48 <= ord(word) <= 57:
                buffer.append(word)
            else:
                word_count -= 1
                state = 0
                lexeme = ''.join(buffer)
                token_vet.append(["REAL_CONST", lexeme, line_count])
                vetorTokens.append('REAL_CONST')
                buffer = []

        elif state == 5:
            if word == '=':
                state = 0
                buffer.append(word)
            else:
                word_count -= 1
                state = 0
            lexeme = ''.join(buffer)
            token_vet.append([tokens[lexeme], lexeme, line_count])
            vetorTokens.append(tokens[lexeme])
            buffer = []

        elif state == 6:
            if word.isalpha() or word.isnumeric() or word == '_' or word == '?' or word == '#' or word == ' ' or word == ',':
                buffer.append(word)
            elif word == '"':
                state = 0
                buffer.append(word)
                lexeme = ''.join(buffer)
                token_vet.append(["STRING_LITERAL", lexeme, line_count])
                vetorTokens.append("STRING_LITERAL")
                buffer = []
            else:
                buffer.append(word)
                lexeme = ''.join(buffer)
                token_vet.append(['ERRO LEXICO', lexeme, line_count])
                vetorTokens.append('ERRO LEXICO')
                erros_lexicos.write(f'ERRO LEXICO na linha {line_count}')

        elif state == 7:
            if word == '=':
                state = 0
                buffer.append(word)
                lexeme = ''.join(buffer)
                token_vet.append([tokens[lexeme], lexeme, line_count])
                vetorTokens.append(tokens[lexeme])
                buffer = []
            else:
                token_vet.append(["ERRO LEXICO", lexeme, line_count])
                vetorTokens.append('ERRO LEXICO')
                erros_lexicos.write(f'ERRO LEXICO na linha {line_count}')
        elif state == 8:
            if word == '=':
                state = 0
                buffer.append(word)
                lexeme = ''.join(buffer)
                token_vet.append([tokens[lexeme], lexeme, line_count])
                vetorTokens.append(tokens[lexeme])
                buffer = []
            else:
                token_vet.append(["ERRO LEXICO", lexeme, line_count])
                erros_lexicos.write(f'ERRO LEXICO na linha {line_count}')
        elif state == 9:
            if word == '=':
                state = 0
                buffer.append(word)
            else:
                word_count -= 1
                state = 0
            lexeme = ''.join(buffer)
            token_vet.append([tokens[lexeme], lexeme, line_count])
            vetorTokens.append(tokens[lexeme])
            buffer = []
        elif state == 10:
            if word == '=':
                state = 0
                buffer.append(word)
            else:
                word_count -= 1
                state = 0
            lexeme = ''.join(buffer)
            token_vet.append([tokens[lexeme], lexeme, line_count])
            vetorTokens.append(tokens[lexeme])
            buffer = []
        word_count += 1
    line_count += 1
lexeme = ''.join(buffer)
token_vet.append([tokens[lexeme] if lexeme in tokens else "ID", lexeme, line_count])
vetorTokens.append(tokens[lexeme] if lexeme in tokens else 'ID')
buffer = []
token_vet.append(['EOF', '', line_count])
saida = open('Saida_Lexico/' + 'saida_' + namefile + '.txt', "w")
erros_Lexicos = open('Saida_Lexico/' + 'saida_' + namefile + '.txt', "w")
saida.write(tabulate(token_vet, headers=['TOKEN', 'LEXEMA', 'LINHA']))
saida.close()
arquivo.close()
