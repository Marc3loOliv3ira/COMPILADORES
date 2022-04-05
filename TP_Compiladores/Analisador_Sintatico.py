# Analisador Sintatico Por Descida Recursiva
import os

from tabulate import tabulate
from Analisador_Lexico import vetorTokens
from Analisador_Lexico import token_vet
from Analisador_Lexico import namefile


# Lista de Tokens
def getValues(token):
    if token == 'EOF':
        return -1
    elif token == 'ID':
        return 0
    elif token == 'PROGRAM':
        return 1
    elif token == 'BEGIN':
        return 2
    elif token == 'END':
        return 3
    elif token == 'VAR':
        return 4
    elif token == 'BOOLEAN':
        return 5
    elif token == 'INTEGER':
        return 6
    elif token == 'STRING':
        return 7
    elif token == 'REAL':
        return 8
    elif token == 'TRUE':
        return 9
    elif token == 'FALSE':
        return 10
    elif token == 'IF':
        return 11
    elif token == 'THEN':
        return 12
    elif token == 'WHILE':
        return 13
    elif token == 'PRINT':
        return 14
    elif token == 'READ':
        return 15
    elif token == 'TWOPOINT':
        return 16
    elif token == 'ASSIGN':
        return 17
    elif token == 'LBRACKET':
        return 18
    elif token == 'RBRACKET':
        return 19
    elif token == 'COMMA':
        return 20
    elif token == 'PCOMMA':
        return 21
    elif token == 'ATTR':
        return 22
    elif token == 'EQ':
        return 23
    elif token == 'NE':
        return 24
    elif token == 'LT':
        return 25
    elif token == 'LE':
        return 26
    elif token == 'GT':
        return 27
    elif token == 'GE':
        return 28
    elif token == 'PLUS':
        return 29
    elif token == 'MINUS':
        return 30
    elif token == 'MULT':
        return 31
    elif token == 'DIV':
        return 32
    elif token == 'STRING_LITERAL':
        return 33
    elif token == 'INTEGER_CONST':
        return 34
    elif token == 'REAL_CONST':
        return 35
    elif token == 'DO':
        return 36
    elif token == 'ERRO LEXICO':
        return 36


tokenNames = {getValues('EOF'): 'EOF', getValues('ID'): 'ID', getValues('PROGRAM'): 'PROGRAM',
              getValues('BEGIN'): 'BEGIN', getValues('END'): 'END', getValues('VAR'): 'VAR',
              getValues('BOOLEAN'): 'BOOLEAN', getValues('INTEGER'): 'INTEGER', getValues('STRING'): 'STRING',
              getValues('REAL'): 'REAL', getValues('TRUE'): 'TRUE', getValues('FALSE'): 'FALSE', getValues('IF'): 'IF',
              getValues('THEN'): 'THEN', getValues('WHILE'): 'WHILE', getValues('PRINT'): 'PRINT',
              getValues('READ'): 'READ', getValues('TWOPOINT'): 'TWOPOINT', getValues('ASSIGN'): 'ASSIGN',
              getValues('LBRACKET'): 'LBRACKET', getValues('RBRACKET'): 'RBRACKET', getValues('COMMA'): 'COMMA',
              getValues('PCOMMA'): 'PCOMMA', getValues('ATTR'): 'ATTR', getValues('EQ'): 'EQ', getValues('NE'): 'NE',
              getValues('LT'): 'LT', getValues('LE'): 'LE', getValues('GT'): 'GT', getValues('GE'): 'GE',
              getValues('PLUS'): 'PLUS', getValues('MINUS'): 'MINUS', getValues('MULT'): 'MULT',
              getValues('DIV'): 'DIV', getValues('STRING_LITERAL'): 'STRING_LITERAL',
              getValues('INTEGER_CONST'): 'INTEGER_CONST', getValues('REAL_CONST'): 'REAL_CONST', getValues('DO'): 'DO',
              getValues('ERRO LEXICO'): 'ERRO LEXICO'}

i = 0
j = 0
k = 0
SymbleT = []
variavel = []
tipo = []
linha = []
tok = getValues(vetorTokens[i])
First = []


def printa_Erro(Erro):
    if tokenNames[tok] == Erro:
        saida.write(f'Houve um  {tokenNames[tok]} : ERRO_SINTATICO  na linha {token_vet[i][2]}\n')


def match(token):
    global i, tok
    if tokenNames[tok] == token:
        saida.write(f'{tokenNames[tok]} Reconhecido na entrada\n')
        # print(f'{tokenNames[tok]} Reconhecido na entrada')
        if i < len(vetorTokens) - 1:
            i = i + 1
            tok = getValues(vetorTokens[i])
    else:
        saida.write(f'ERRO_SINTATICO Token {tokenNames[tok]} não esperado na linha {token_vet[i][2]}\n')
        if len(First) == 0:
            saida.write(f'TOKEN ESPERADO : {token}')
        else:
            for l in First:
                saida.write(f'TOKEN ESPERADO : {l}')

        Saidas_Gerais_E_S()
        erros.write(f'ERRO_SINTATICO Token {tokenNames[tok]} não esperado na linha {token_vet[i][2]}\n')
        if len(First) == 0:
            erros.write(f'TOKEN ESPERADO : {token}')
        else:
            for l in First:
                erros.write(f'TOKEN ESPERADO : {l}')
        erros.write('\n#################################################################################\n')
        exit()


def Program():
    if tokenNames[tok] == 'PROGRAM':
        match('PROGRAM')
        match('ID')
        match('PCOMMA')
        Bloco()
    elif tokenNames[tok] == 'EOF':
        match('EOF')
    elif tokenNames[tok] == 'ERRO LEXICO':
        printa_Erro('ERRO LEXICO')
    else:
        First.append('PROGRAM')
        match(' ')


def Bloco():
    if tokenNames[tok] == 'VAR':
        DeclaracaoSeq()
        SymbleTable()
    match('BEGIN')
    ComandoSeq()
    match('END')


def DeclaracaoSeq():
    if tokenNames[tok] == 'VAR':
        Declaracao()
        DeclaracaoSeq()


def Declaracao():
    if tokenNames[tok] == 'VAR':
        match('VAR')
        VarList()
        match('TWOPOINT')
        Type()
        match('PCOMMA')
    elif tokenNames[tok] == 'ERRO LEXICO':
        printa_Erro('ERRO LEXICO')
    else:
        First.append('VAR')
        match(' ')


def VarList():
    if tokenNames[tok] == 'ID':
        Table()
        match('ID')
        VarList2()
    elif tokenNames[tok] == 'ERRO LEXICO':
        printa_Erro('ERRO LEXICO')
    else:
        First.append('ID')
        match(' ')


def VarList2():
    if tokenNames[tok] == 'COMMA':
        match('COMMA')
        Table()
        match('ID')
        VarList2()
    elif tokenNames[tok] == 'ERRO LEXICO':
        printa_Erro('ERRO LEXICO')


def Type():
    global j
    if tokenNames[tok] == 'BOOLEAN':
        match('BOOLEAN')
        for n in range(j):
            tipo.append('BOOLEAN')
        j = 0
    elif tokenNames[tok] == 'INTEGER':
        match('INTEGER')
        for n in range(j):
            tipo.append('INTEGER')
        j = 0
    elif tokenNames[tok] == 'REAL':
        match('REAL')
        for n in range(j):
            tipo.append('REAL')
        j = 0
    elif tokenNames[tok] == 'STRING':
        match('STRING')
        for n in range(j):
            tipo.append('STRING')
        j = 0
    elif tokenNames[tok] == 'ERRO LEXICO':
        printa_Erro('ERRO LEXICO')
    else:
        First.append('BOOLEAN ,INTEGER, REAL ,STRING')
        match(' ')


def ComandoSeq():
    if tokenNames[tok] == 'ID' or tokenNames[tok] == 'IF' or tokenNames[tok] == 'WHILE' or \
            tokenNames[tok] == 'PRINT' or tokenNames[tok] == 'READ':
        Comando()
        ComandoSeq()


def Comando():
    global compara
    compara = " "
    if tokenNames[tok] == 'ID':
        if token_vet[i][1] not in variavel:
            saidaSemantico.write(
                f'ERRO SEMANTICO : A variavel {token_vet[i][1]} na linha {token_vet[i][2]} não foi declarada  \n')
        else:
            qval = variavel.index(token_vet[i][1])
            compara = tipo[qval]
        match('ID')
        match('ATTR')
        Expr()
        match('PCOMMA')
    elif tokenNames[tok] == 'IF':
        match('IF')
        Expr()
        match('THEN')
        ComandoSeq()
        match('END')
    elif tokenNames[tok] == 'WHILE':
        match('WHILE')
        Expr()
        match('DO')
        ComandoSeq()
        match('END')
    elif tokenNames[tok] == 'PRINT':
        match('PRINT')
        Expr()
    elif tokenNames[tok] == 'READ':
        match('READ')
        if token_vet[i][1] not in variavel:
            saidaSemantico.write(
                f'ERRO SEMANTICO : A variavel {token_vet[i][1]} na linha {token_vet[i][2]} não foi declarada  \n')
        match('ID')
    elif tokenNames[tok] == 'ERRO LEXICO':
        printa_Erro('ERRO LEXICO')
    else:
        First.append('ID, IF, WHILE, PRINT, READ')
        match(' ')


def Expr():
    if tokenNames[tok] == 'ID' or tokenNames[tok] == 'INTEGER_CONST' or tokenNames[tok] == 'REAL_CONST' or \
            tokenNames[tok] == 'TRUE' or tokenNames[tok] == 'FALSE' or tokenNames[tok] == 'STRING_LITERAL' or \
            tokenNames[tok] == 'LBRACKET':
        Rel()
        ExprOpc()
    else:
        First.append('ID , INTEGER_CONST , REAL_CONST , STRING_LITERAL , TRUE , FASE , LBRACKET')
        match(' ')


def Rel():
    if tokenNames[tok] == 'ID' or tokenNames[tok] == 'INTEGER_CONST' or tokenNames[tok] == 'REAL_CONST' or \
            tokenNames[tok] == 'TRUE' or tokenNames[tok] == 'FALSE' or tokenNames[tok] == 'STRING_LITERAL' or \
            tokenNames[tok] == 'LBRACKET':
        Adicao()
        RelOpc()
    else:
        First.append('ID , INTEGER_CONST , REAL_CONST , STRING_LITERAL , TRUE , FASE , LBRACKET')
        match(' ')


def ExprOpc():
    if tokenNames[tok] == 'EQ' or tokenNames[tok] == 'NE':
        OpIgual()
        Rel()
        ExprOpc()


def OpIgual():
    if tokenNames[tok] == 'EQ':
        match('EQ')
    elif tokenNames[tok] == 'NE':
        match('NE')
    elif tokenNames[tok] == 'ERRO LEXICO':
        printa_Erro('ERRO LEXICO')
    else:
        First.append('EQ,NE')
        match(' ')


def Adicao():
    if tokenNames[tok] == 'ID' or tokenNames[tok] == 'INTEGER_CONST' or tokenNames[tok] == 'REAL_CONST' or \
            tokenNames[tok] == 'TRUE' or tokenNames[tok] == 'FALSE' or tokenNames[tok] == 'STRING_LITERAL' or \
            tokenNames[tok] == 'LBRACKET':
        Termo()
        AdicaoOpc()
    else:
        First.append('ID , INTEGER_CONST , REAL_CONST , STRING_LITERAL , TRUE , FASE , LBRACKET')
        match(' ')


def AdicaoOpc():
    if tokenNames[tok] == 'PLUS' or tokenNames[tok] == 'MINUS':
        OpAdicao()
        Termo()
        AdicaoOpc()


def OpAdicao():
    if tokenNames[tok] == 'PLUS':
        match('PLUS')
    if tokenNames[tok] == 'MINUS':
        match('MINUS')
    elif tokenNames[tok] == 'ERRO LEXICO':
        printa_Erro('ERRO LEXICO')
    else:
        First.append('PLUS,MINUS')
        match(' ')


def Termo():
    if tokenNames[tok] == 'ID' or tokenNames[tok] == 'INTEGER_CONST' or tokenNames[tok] == 'REAL_CONST' or \
            tokenNames[tok] == 'TRUE' or tokenNames[tok] == 'FALSE' or tokenNames[tok] == 'STRING_LITERAL' or \
            tokenNames[tok] == 'LBRACKET':
        Fator()
        TermoOpc()
    else:
        First.append('ID , INTEGER_CONST , REAL_CONST , STRING_LITERAL , TRUE , FASE , LBRACKET')
        match(' ')


def TermoOpc():
    if tokenNames[tok] == 'MULT' or tokenNames[tok] == 'DIV':
        OpMult()
        Fator()
        TermoOpc()


def Fator():
    compara1 = " "
    if tokenNames[tok] == 'ID':
        if token_vet[i][1] not in variavel:
            saidaSemantico.write(f'A variavel {token_vet[i][1]} na linha {token_vet[i][2]} não foi declarada  \n')
        else:
            qval1 = variavel.index(token_vet[i][1])
            compara1 = tipo[qval1]
            if compara == "BOOLEAN" and (compara1 == "STRING_LITERAL" or compara1 == "STRING" or compara1 == "REAL"):
                saidaSemantico.write(
                    f'Erro de compatibilidade na linha : {token_vet[i][2]} : {compara} com {compara1} \n')
            elif compara == "STRING" and (compara1 == "REAL" or compara == "BOOLEAN" or compara1 == "INTEGER"):
                saidaSemantico.write(
                    f'Erro de compatibilidade na linha : {token_vet[i][2]} : {compara} com {compara1} \n')
            elif compara == "REAL" and (compara1 == "STRING" or compara == "BOOLEAN" or compara1 == "STRING_LITERAL"):
                saidaSemantico.write(
                    f'Erro de compatibilidade na linha : {token_vet[i][2]} : {compara} com {compara1} \n')
            elif compara == "INTEGER" and (compara1 == "STRING" or compara1 == "STRING_LITERAL"):
                saidaSemantico.write(
                    f'Erro de compatibilidade na linha : {token_vet[i][2]} : {compara} com {compara1} \n')
        match('ID')
    elif tokenNames[tok] == 'INTEGER_CONST':
        if compara == "STRING" or compara == "STRING_LITERAL":
            saidaSemantico.write(f'Erro de compatibilidade na linha {token_vet[i][2]}: {compara} com INTEGER_CONST\n')
        match('INTEGER_CONST')

    elif tokenNames[tok] == 'REAL_CONST':
        if compara == "STRING" or compara == "STRING_LITERAL":
            saidaSemantico.write(f'Erro de compatibilidade na linha {token_vet[i][2]}: {compara} com REAL_CONST\n')
        match('REAL_CONST')

    elif tokenNames[tok] == 'TRUE':
        if compara == "STRING" or compara == "STRING_LITERAL":
            saidaSemantico.write(f'Erro de compatibilidade na linha {token_vet[i][2]}: {compara} com TRUE\n')
        elif compara == "REAL":
            saidaSemantico.write(f'Erro de compatibilidade na linha {token_vet[i][2]}: {compara} com TRUE\n')
        match('TRUE')

    elif tokenNames[tok] == 'FALSE':
        if compara == "STRING" or compara == "STRING_LITERAL":
            saidaSemantico.write(f'Erro de compatibilidade na linha {token_vet[i][2]}: {compara} com FALSE\n')
        elif compara == "REAL":
            saidaSemantico.write(f'Erro de compatibilidade na linha {token_vet[i][2]}: {compara} com FALSE\n')
        match('FALSE')

    elif tokenNames[tok] == 'STRING_LITERAL':
        if compara == "REAL" or compara == "INTEGER" or compara == "BOOLEAN":
            saidaSemantico.write(f'Erro de compatibilidade na linha {token_vet[i][2]}: {compara} com STRING_LITERAL\n')
        match('STRING_LITERAL')
    elif tokenNames[tok] == 'LBRACKT':
        match('LBRACKET')
        Expr()
        match('RBRACKET')
    elif tokenNames[tok] == 'ERRO LEXICO':
        printa_Erro('ERRO LEXICO')

    else:
        First.append('ID , INTEGER_CONST , REAL_CONST , STRING_LITERAL , TRUE , FASE , LBRACKET')
        match(' ')


def RelOpc():
    if tokenNames[tok] == 'LT' or tokenNames[tok] == 'LE' or tokenNames[tok] == 'GT' or tokenNames[tok] == 'GE':
        OpRel()
        Adicao()
        RelOpc()


def OpRel():
    if tokenNames[tok] == 'LT':
        match('LT')
    elif tokenNames[tok] == 'LE':
        match('LE')
    elif tokenNames[tok] == 'GT':
        match('GT')
    elif tokenNames[tok] == 'GE':
        match('GE')
    elif ' ':
        First.append('LT , LE, GT, GE')
        match(' ')


def OpMult():
    if tokenNames[tok] == 'MULT':
        match('MULT')
    elif tokenNames[tok] == 'DIV':
        match('DIV')
    elif ' ':
        First.append('MULT,DIV')
        match(' ')


def Table():
    global j, k
    if token_vet[i][0] == 'ID':
        if token_vet[i][1] not in variavel:
            variavel.append(token_vet[i][1])
            linha.append(token_vet[i][2])
            j += 1
            k += 1
        else:
            saidaSemantico.write(
                f'ERRO SEMANTICO: variavel {token_vet[i][1]} ja foi declarada na linha {token_vet[i][2]}\n')
            saidaSemantico.write(f'A variavel {token_vet[i][1]} foi redeclarada para continuar a analise Semantica\n')
            ind = variavel.index(token_vet[i][1])
            variavel.pop(ind)
            linha.pop(ind)
            tipo.pop(ind)
            k -= 1
            variavel.append(token_vet[i][1])
            linha.append(token_vet[i][2])
            j += 1
            k += 1


def SymbleTable():
    for v in range(k):
        SymbleT.append([variavel[v], tipo[v], linha[v]])


def Saidas_Gerais():
    ha = 0;
    arquivoLex = open('Saida_Lexico/' + 'saida_' + namefile + '.txt', "r")
    arquivoSin = open('Saida_Sintatico/' + 'saida' + namefile + '.txt', "r")
    arquivoSem = open('Saida_Semantico/' + 'saida' + namefile + '.txt', "r")
    arquivoTab = open('Saida_Tabela/' + 'saida' + namefile + '.txt', "r")
    erros.write('\n#################################################################################\n')
    erros.write('\n                             ANALISADOR LEXICO \n')
    erros.write('\n                           ##########################                            \n')
    for linha in arquivoLex:
        erros.write(linha)
    erros.write('\n#################################################################################\n')

    erros.write('\n                             ANALISADOR SINTATICO \n')
    erros.write('\n                           ##########################                            \n')
    for linha in arquivoSin:
        erros.write(linha)
    erros.write('\n#################################################################################\n')

    erros.write(' \n                            ANALISADOR SEMANTICO \n')
    erros.write('\n                           ##########################                            \n')
    for linha in arquivoSem:
        ha = 1
        erros.write(linha)
    if ha == 0:
        erros.write(' \n                Fim da Analise semantica : Sem ERROS \n')
    erros.write('\n#################################################################################\n')

    erros.write(' \n                               TABELA DE SIMBOLOS \n')
    erros.write('\n                           ##########################                            \n')
    for linha in arquivoTab:
        erros.write(linha)
    erros.write('\n#################################################################################\n')

    arquivoLex.close()
    arquivoSin.close()
    arquivoSem.close()
    arquivoTab.close()


def Saidas_Gerais_E_S():
    ha = 0;
    arquivoLex = open('Saida_Lexico/' + 'saida_' + namefile + '.txt', "r")
    arquivoSem = open('Saida_Semantico/' + 'saida' + namefile + '.txt', "r")
    arquivoTab = open('Saida_Tabela/' + 'saida' + namefile + '.txt', "r")
    erros.write('\n#################################################################################\n')
    erros.write('\n                             ANALISADOR LEXICO \n')
    erros.write('\n                           ##########################                            \n')
    for linha in arquivoLex:
        erros.write(linha)
    erros.write('\n#################################################################################\n')

    erros.write(' \n                            ANALISADOR SEMANTICO \n')
    erros.write('\n                           ##########################                            \n')
    for linha in arquivoSem:
        ha = 1
        erros.write(linha)
    if ha == 0:
        erros.write(' \n                Fim da Analise semantica : Sem ERROS \n')
    erros.write('\n#################################################################################\n')

    erros.write(' \n                               TABELA DE SIMBOLOS \n')
    erros.write('\n                           ##########################                            \n')
    for linha in arquivoTab:
        erros.write(linha)
    erros.write('\n#################################################################################\n')
    erros.write('\n                             ANALISADOR SINTATICO \n')
    erros.write('\n                           ##########################                            \n')

    arquivoLex.close()
    arquivoSem.close()
    arquivoTab.close()


saida = open('Saida_Sintatico/' + 'saida' + namefile + '.txt', "w")
saidaTabela = open('Saida_Tabela/' + 'saida' + namefile + '.txt', "w")
saidaSemantico = open('Saida_Semantico/' + 'saida' + namefile + '.txt', "w")
erros = open('Arquivos_Gerais/' + 'Analises' + namefile + '.txt', "w")
Program()
saidaTabela.write(tabulate(SymbleT, headers=['VARIAVEL', 'TIPO', 'LINHA']))
saida.close()
saidaTabela.close()
saidaSemantico.close()
Saidas_Gerais()
