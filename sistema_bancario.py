numero = self.proximo_numero_conta
        self.contas[numero] = Conta(
            numero=numero,
            cliente=cliente,
            salt_senha=salt,
            hash_senha=senha_hash,
        )
        self.proximo_numero_conta += 1
        print(f"Conta criada com sucesso! Número da conta: {numero}")

    def autenticar_conta(self) -> Conta | None:
        try:
            numero = int(input("Número da conta: ").strip())
        except ValueError:
            print("Número de conta inválido.")
            return None

        conta = self.contas.get(numero)
        if conta is None:
            print("Conta não encontrada.")
            return None

        senha = input("Senha da conta: ")
        if not conta.conferir_senha(senha):
            print("Senha incorreta.")
            return None
        return conta

    def listar_contas(self) -> None:
        print("\n--- Contas cadastradas ---")
        if not self.contas:
            print("Nenhuma conta cadastrada.")
            return
        for conta in self.contas.values():
            print(
                f"Conta: {conta.numero} | Titular: {conta.cliente.nome} "
                f"| CPF: ***.***.***-{conta.cliente.cpf[-2:]}"
            )

    def executar_deposito(self) -> None:
        conta = self.autenticar_conta()
        if conta is None:
            return
        valor = ler_valor("Valor do depósito: R$ ")
        if valor is not None:
            conta.depositar(valor)

    def executar_saque(self) -> None:
        conta = self.autenticar_conta()
        if conta is None:
            return
        valor = ler_valor("Valor do saque: R$ ")
        if valor is not None:
            conta.sacar(valor)

    def executar_extrato(self) -> None:
        conta = self.autenticar_conta()
        if conta is not None:
            conta.exibir_extrato()


def exibir_menu() -> None:
    print("""
========== BANCO PYTHON ==========
[1] Cadastrar cliente
[2] Criar conta
[3] Depositar
[4] Sacar
[5] Consultar extrato
[6] Listar contas
[0] Sair
==================================
""")


def main() -> None:
    banco = Banco()
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            banco.cadastrar_cliente()
        elif opcao == "2":
            banco.criar_conta()
        elif opcao == "3":
            banco.executar_deposito()
        elif opcao == "4":
            banco.executar_saque()
        elif opcao == "5":
            banco.executar_extrato()
        elif opcao == "6":
            banco.listar_contas()
        elif opcao == "0":
            print("Obrigado por utilizar o Banco Python. Até mais!")
            break
        else:
            print("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    main()
