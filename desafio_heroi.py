# 3️⃣ Escrevendo as classes de um Jogo

class Heroi:
    # O método __init__ é o construtor da classe.
    # Ele é chamado quando criamos um novo objeto (um novo herói).
    def __init__(self, nome, idade, tipo):
        # 'self' se refere à instância do objeto.
        # Estamos atribuindo os valores recebidos aos atributos do objeto.
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    # Método para o herói realizar um ataque
    def atacar(self):
        # Inicializamos a variável de ataque
        ataque = ""

        # Usamos uma estrutura de decisão (if/elif/else) para
        # determinar o ataque com base no tipo do herói.
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            # Uma boa prática é ter um caso padrão
            ataque = "um ataque indefinido"

        # Exibimos a mensagem final, conforme solicitado no desafio.
        # Usamos uma f-string para facilitar a formatação.
        print(f"o {self.tipo} atacou usando {ataque}")

# --- FIM DA CLASSE ---

# --- INÍCIO DO TESTE ---
# Agora, vamos criar os objetos (heróis) e testar o método atacar.

# 1. Criando um herói do tipo Mago
heroi_mago = Heroi(nome="Merlin", idade=150, tipo="mago")

# 2. Criando um herói do tipo Guerreiro
heroi_guerreiro = Heroi(nome="Aragorn", idade=35, tipo="guerreiro")

# 3. Criando um herói do tipo Monge
heroi_monge = Heroi(nome="Aang", idade=112, tipo="monge")

# 4. Criando um herói do tipo Ninja
heroi_ninja = Heroi(nome="Naruto", idade=17, tipo="ninja")


# Chamando o método atacar() para cada um dos heróis
heroi_mago.atacar()
heroi_guerreiro.atacar()
heroi_monge.atacar()
heroi_ninja.atacar()