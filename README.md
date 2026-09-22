# Sistema de Gestão de Zoológico

## Sobre o Projeto

O Sistema de Gestão de Zoológico é uma aplicação desenvolvida em Python com foco na aplicação prática dos conceitos de Programação Orientada a Objetos (POO). O projeto tem como objetivo simular o gerenciamento operacional de um zoológico, permitindo o controle de espécies, animais, recintos, funcionários e rotinas diárias por meio de um sistema de cronograma.

O desenvolvimento segue princípios de modularidade, organização e escalabilidade, buscando aproximar a estrutura do sistema de soluções utilizadas em ambientes profissionais.

---

## Estrutura Atual

Atualmente, o sistema é composto pelos seguintes módulos:

### TipoTarefa

Enum responsável por padronizar os tipos de tarefas disponíveis no sistema.

### Tarefa

Representa uma atividade agendada para execução em um horário específico.

### Cronograma

Gerencia o armazenamento, consulta e persistência das tarefas cadastradas no sistema.

### Tratador

Responsável pela execução das atividades relacionadas aos animais e recintos do zoológico.

### Especie

Cada espécie cadastrada armazena as seguintes informações:

- Identificador único (UUID);
- Nome da espécie;
- Tipo de tratamento necessário;
- Tipo de alimentação;
- Necessidade de banho de sol.

### Animal

Responsável pelo cadastro e gerenciamento dos animais do zoológico.

Cada animal é associado a uma espécie previamente cadastrada através de um identificador único (UUID), evitando duplicação de informações e permitindo consultas centralizadas ao banco de espécies.

As informações armazenadas para cada animal incluem:

- Identificador único (UUID);
- Espécie associada;
- Apelido (opcional);
- Idade;
- Sexo;
- Estado de saciedade.

## Sistema de Animais

O sistema de animais foi estruturado utilizando herança para representar diferentes grupos zoológicos.

A classe base `Animal` concentra toda a lógica de cadastro, associação com espécies e persistência dos dados.

A partir dela foram criadas as seguintes subclasses:

```text
Animal
│
├── Mamiferos
├── Aves
├── Repteis
├── Peixes
└── Anfibios
## O sistema realiza automaticamente o cadastro de uma nova espécie caso ela não esteja presente no banco de dados durante o processo de registro de um animal.

## Sistema de Espécies

O módulo de espécies foi criado para separar as características de uma espécie dos dados individuais de cada animal.

Cada espécie cadastrada armazena as seguintes informações:

- Identificador único (UUID);
- Nome da espécie;
- Tipo de tratamento necessário;
- Necessidade de banho de sol.

As espécies podem ser consultadas tanto pelo nome quanto pelo identificador único, reduzindo duplicidade de informações e facilitando a modelagem dos animais.

As informações são persistidas em arquivos JSON para armazenamento permanente.

---

## Sistema de Cronograma

O módulo de cronograma permite registrar atividades em horários específicos, garantindo que não ocorram conflitos de agenda.

Cada tarefa contém:

- Horário de execução;
- Tipo da tarefa;
- Animal associado à atividade, quando aplicável;
- Recinto associado à atividade, quando aplicável.

Os tipos de tarefa atualmente suportados são:

- Tratar animal;
- Alimentar animal;
- Limpar recinto;
- Realizar banho de sol.

---

## Persistência de Dados

Arquivos atualmente utilizados:

- `cronograma.json`
- `especies.json`
- `mamiferos.json`
- `aves.json`
- `repteis.json`
- `peixes.json`
- `anfibios.json`

```
