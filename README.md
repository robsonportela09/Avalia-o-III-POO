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


**PRINTS DO SISTEMA FUNCIONANDO**


<img width="302" height="112" alt="Captura de tela 2026-06-05 122026" src="https://github.com/user-attachments/assets/52343699-aee4-4690-8fb1-f20b25e2ca29" />
<img width="398" height="56" alt="Captura de tela 2026-06-05 122004" src="https://github.com/user-attachments/assets/0cebbeeb-2119-43b5-9b43-8d35382c775a" />
<img width="412" height="312" alt="Captura de tela 2026-06-05 121900" src="https://github.com/user-attachments/assets/fa1764ae-22c5-4afa-84f9-0e806480a329" />
<img width="420" height="167" alt="Captura de tela 2026-06-05 121849" src="https://github.com/user-attachments/assets/6227c4b8-c4e0-46ea-a188-7fce4a9afd3c" />
<img width="362" height="147" alt="Captura de tela 2026-06-05 121800" src="https://github.com/user-attachments/assets/951690a3-b0d1-427b-8754-816682867312" />
<img width="342" height="166" alt="Captura de tela 2026-06-05 121715" src="https://github.com/user-attachments/assets/bf99cb0b-5c0a-4bb8-9f38-036015e2cca8" />
<img width="322" height="313" alt="Captura de tela 2026-06-05 121707" src="https://github.com/user-attachments/assets/c109bbcf-b4f3-42d9-a77c-ceb5962c3e05" />
<img width="355" height="142" alt="Captura de tela 2026-06-05 122036" src="https://github.com/user-attachments/assets/ab09b588-e217-4bb1-a11b-618add09f95a" />
