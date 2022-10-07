"""Crie um programa que leia nome, Sexo e idade de váriastemp
pessoas, guardando os dados de cada
pessoa em um
dicionário a todos os
dicionários em uma
lista. No final, mostra:
A) Quantas pessoas foram cadastradas
B) A média de idade do
grupo. C) Uma lista com todas
as mulheres.
D) Uma lista com todas
as pessoas com idade acima da média.
"""
dict = {}
lista = []

dict['nome'] = str(input('Nome: '))
dict['sexo'] = str(input('Sexo: ')).upper()[0]
dict['idade'] = str(input('Idade: '))
