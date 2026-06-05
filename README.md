# Avalia-o-III-POO
Sistema Fast Delivery

Sistema baseado em terminal através de um MENU projetado para o gerenciamento de entregas urbanas da empresa FastDelivery Express, automatizando o controle de clientes, entregadores e o cálculo personalizado de fretes de pedidos.

## Tecnologias Utilizadas
* Python 3
* Git
* GitHub

## Estrutura de Pastas
fast_delivery/
│
├── main.py
* **modelos/**
│ ├── pessoa.py
│ ├── cliente.py
│ ├── entregador.py
│ ├── pedido.py
│ └── entrega.py

* **interfaces/**
│ └── calculo_frete_interface.py

* **services/**
│ ├── pedido_service.py
│ ├── cliente_service.py
│ └── entrega_service.py

* **util/**
│ ├── validador.py
│ ├── menu.py
│ └── formatador.py
└── README.md

## Conceitos de POO Aplicados
1. **Herança**: A classe `Pessoa` é a superclasse reaproveitada por `Cliente` e `Entregador`.
2. **Interface**: Através do módulo `abc`, a `CalculoFreteInterface` obriga por assimmdizer a padronização dos cálculos.
3. **Polimorfismo**: Usado em `calcular_frete()` que dependendo da instância ele tem um comportamento diferente: de entrega Comum, Expressa ou Premium.
4. **Encapsulamento**: Atributos definidos de forma privada (`__`) protegidos e expostos controladamente através de decoradores `@property`.

## Como Executar o Projeto
No terminal execute o comando:
**python main.py**
