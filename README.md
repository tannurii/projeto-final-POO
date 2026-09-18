# Sistema de Gestão de Zoológico

## Sobre o Projeto

O Sistema de Gestão de Zoológico é uma aplicação desenvolvida em Python utilizando os princípios de Programação Orientada a Objetos (POO). O objetivo do projeto é simular o gerenciamento operacional de um zoológico, permitindo o controle de animais, recintos, funcionários e rotinas diárias por meio de um sistema de cronograma.

O projeto foi estruturado com foco em modularidade, escalabilidade e organização do código, adotando conceitos como encapsulamento, composição e separação de responsabilidades entre classes.

## Estrutura Atual

O sistema possui uma arquitetura baseada nas seguintes entidades:

- TipoTarefa: enum responsável pela padronização das tarefas disponíveis.
- Tarefa: representa uma atividade agendada para execução.
- Cronograma: gerencia o armazenamento, consulta e persistência das tarefas.
- Tratador: responsável pela execução das atividades relacionadas aos animais e recintos.

## Sistema de Cronograma

O módulo de cronograma permite registrar atividades em horários específicos, garantindo que não existam conflitos de agenda. As informações são persistidas em arquivos JSON, possibilitando o armazenamento permanente dos dados cadastrados.

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

## Tecnologias Utilizadas

- Python 3
- Programação Orientada a Objetos (POO)
- Enum
- JSON para persistência de dados

## Próximas Implementações

As próximas etapas previstas para o desenvolvimento do projeto incluem:

- Implementação da classe Animal;
- Implementação da classe Recinto;
- Implementação de um sistema de controle de tempo;
- Automatização da execução das tarefas agendadas;
- Controle de saúde e alimentação dos animais;
- Geração de relatórios gerenciais.

## Objetivos de Aprendizado

Este projeto tem como finalidade aplicar conceitos de Programação Orientada a Objetos em um cenário prático, explorando modelagem de sistemas, persistência de dados, organização de código e boas práticas de desenvolvimento em Python.
