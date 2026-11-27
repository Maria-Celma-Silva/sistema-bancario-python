# Sistema-Bancario-Python

Projeto prático desenvolvido para exercitar lógica de programação e conceitos de Programação Orientada a Objetos (POO) com Python.
Sobre o projeto
O Banco Python é uma aplicação de terminal que permite cadastrar clientes, abrir contas e realizar operações bancárias simuladas. O projeto foi organizado em classes para separar os dados dos clientes, as regras das contas e o gerenciamento do banco.

# Funcionalidades
- Cadastro de clientes com nome e CPF.
- Abertura de contas vinculadas a clientes cadastrados.
- Depósitos com validação de valores.
- Saques com validação de saldo, limite por operação e quantidade diária.
- Consulta de extrato e saldo.
- Listagem de contas cadastradas.
- Verificação de senha para operações da conta.
- Armazenamento de hash da senha com salt, sem guardar a senha original.
  
# Como executar
1. Instale o Python 3.10 ou superior.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto.
4. Execute:
python sistema_bancario.py
No Windows, também pode ser necessário usar:
py sistema_bancario.py

# Como utilizar
1. Escolha 1 para cadastrar um cliente.
2. Escolha 2 para abrir uma conta e definir uma senha.
3. Use as opções 3, 4 e 5 para depositar, sacar e consultar o extrato. Essas operações solicitam o número da conta e a senha.
4. Escolha 6 para listar as contas cadastradas.
5. Escolha 0 para encerrar o programa.
   
# Regras de negócio demonstradas
- Não é permitido depositar ou sacar valores menores ou iguais a zero.
- Cada saque é limitado a R$ 500,00.
- Cada conta pode realizar até três saques por dia.
- Não é permitido sacar mais do que o saldo disponível.
- O cliente precisa estar cadastrado antes de abrir uma conta.
  
# Limitações e melhorias futuras
Esta é uma aplicação educacional: os dados ficam apenas na memória e são apagados quando o programa é encerrado. O CPF é validado pelo tamanho, mas não pelo cálculo dos dígitos verificadores. A verificação de senha é uma demonstração de boas práticas, não uma solução de segurança bancária pronta para produção.

# Possíveis evoluções:
- Persistir clientes, contas e movimentações em um banco de dados.
- Implementar validação completa de CPF.
- Criar testes automatizados.
- Adicionar transferências entre contas.
- Criar uma interface web ou gráfica.

Objetivo de aprendizagem
Praticar a construção de uma aplicação em Python, organizar o código em classes, aplicar regras de negócio e utilizar Git e GitHub para documentar e compartilhar a evolução do projeto.
