# Git
É um sistema de controle de versões de código (versionamento).



## Conceitos

**Versionamento de código:** processo de controle de versão baseado em numeração de históricos diferentes.

**Repositório:** pasta onde o projeto é armazenada. Todo repositório tem um arquivo rastreável .git. Esse arquivo é necessário para trabalhar com o versionamento do projeto. 

**Commit:** conjunto de alteração no código. O git consegue rastrear a mudanças (diff) provocado por cada versão do código. São alterações: 

- Criação, alteração ou exclusão de arquivos;
- Inserção ou exclusão de linhas.

**Branch:**  são a separação de código que permite que várias pessoas contribuam com o código. 

**Merge:**  é a união de duas branchs. Une as alterações realizadas por diferentes pessoas.

**Clone:** realizar uma cópia do repositório do github (remoto) para o repositório local (máquina).

**Pull:** atualizar o repositório local com as informações atualizadas no repositório do github (remoto).

**Push:** envio das alterações do repositório local para o repositório remoto.

**Fork:** é a cópia do repositório remoto de outra pessoa para seu repositório remoto. 

**Pull request:** solicitação de atualização do seu repositório local para o repositório remoto de outra pessoa para contribuir com o open source. A dona do repositório avalia e aceita ou não as alterações.



## Comandos do git
Essa seção foi elaborado a partir de aulas do curso de *Data Analytics* da WoMakersCode e do artigo [Git e Github - Guia rápido e Comandos básicos para iniciantes] (https://dev.to/womakerscode/git-e-github-guia-rapido-e-comandos-basicos-para-iniciantes-4ile). 

Eu listei os comandos iniciais abaixo e tentei adicionar na ordem utilizada durante o primeiro uso em um novo repositório.

- `git config —  list`: Mostra a lista de configurações do seu terminal

- `git status`: Verifica o status do repositório
    
- `git init`: Criar um repositório local Dentro do diretório que você deseja versionar, digite o comando `git init`
    
- `git remote add origin link_do_repositorio`: Liga o repositório local ao repositório remoto

- `git add`: Adicionar um arquivo no repositório
    
    `git add nome_do_arquivo`: adiciona apenas esse arquivo
    
    `git add *`: adiciona todos os arquivos da pasta

- `git commit`: Promove o rastreamento do arquivo  pelo git
    
    É necessário adicionar o comando e a mensagem para arquivos **NOVOS**: `git commit -m ‘seu comentário sobre seus arquivos’`
    
    Adicionar o comando e a mensagem para arquivos **ALTERADOS**: `git commit -am ‘digite a mensagem’`