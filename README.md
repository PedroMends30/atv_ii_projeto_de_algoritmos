# Atividade II — Projetos de Algoritmos II
Soluções de dois problemas do HackerRank com foco na escolha correta de estruturas de dados para garantir eficiência.

**Alunos**: Pedro da Silva Mendes, Itallo F. C. do Nascimento
**Professor**: Dr. Denis Lima do Rosário — Fev/2026

## Jesse and Cookies

O problema exige combinar repetidamente os dois cookies menos doces até que todos atinjam uma doçura mínima k.
A ideia central é perceber que o gargalo não está na fórmula de combinação, mas no acesso contínuo aos menores elementos do conjunto. Ordenar a lista a cada passo funciona, porém é ineficiente.
A solução adequada utiliza um heap mínimo (min-heap), que permite remover e inserir elementos mantendo o acesso ao menor valor em tempo logarítmico.
Essência: trocar ordenações repetidas por uma estrutura que já mantém o menor elemento acessível.

## No Prefix Set

O problema consiste em verificar se alguma palavra do conjunto é prefixo de outra e, caso seja, identificar qual palavra causa a violação.
A estrutura natural para esse tipo de verificação é uma Trie (árvore de prefixos).
A ideia central é realizar a verificação durante a inserção das palavras na Trie. Enquanto cada palavra é inserida, é possível detectar imediatamente:

- Se ela é prefixo de alguma já inserida
- Ou se alguma já inserida é prefixo dela

Isso evita verificações posteriores e resolve o problema no próprio processo de construção da estrutura.

Essência: usar a Trie não apenas para armazenar, mas para validar o conjunto no momento da inserção.