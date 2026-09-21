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

Responsável pelo cadastro e gerenciamento das espécies catalogadas. Cada espécie possui um identificador único (UUID), permitindo sua associação futura com os animais cadastrados.

---

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

O sistema utiliza arquivos JSON para armazenamento das informa
