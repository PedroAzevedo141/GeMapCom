# GeMapCom: Uma Ferramenta para Mapeamento Comparativo e Visualização de Dados Genômicos

Uma ferramenta que auxilia e facilita pesquisadores da área a realizá comparações, de diversos modos, entre genomas e de ter os melhores tipos de visualização dos resultados obtidos pela ferramenta.

-----

### Instalação da ferramenta no Linux Mint

A ferramenta está desenvolvida na linguagem python, versão 3.0, e utiliza diversas bibliotecas externas. Para que a ferramenta rode em seu Linux é necessário ter instalado o python e suas respectivas bibliotecas, mostrado abaixo;

 - Primeiro passo, instale o Python 3.0:

       sudo apt-get install python3

 - Segundo passo, instalar o gerenciador de pacotes do python 3.0:

       sudo apt-get install python3-pip

 - Instale o BLAST, software licenciada pela NCBi, para realização de comparações genomicas de alta capacidade:

       sudo apt install ncbi-blast+

-------

### Quickstart

Crie uma venv:

      python -m venv venv

Ative a venv:

      source venv/bin/activate

Instale as dependencias do projeto:

      pip3 install -r requirements.txt

-------

### Execução da ferramenta

Percorra pelo terminal até a pasta na qual está situado a ferramenta, então execute o seguinte comando:

      python3 GeMapCom.py

*Nota: Para qualquer auxílio com o funcionamento da ferramenta, é só acessar a pasta Manual, na qual contém o manual de uso da ferramenta.*

-------

### Desenvolvedores

 - Romuere Rodrigues Veloso e Silva
 - Pedro Azevedo Abrantes de Oliveira
 - Francisco das Chagas dos Anjos Carvalho Júnior

-------
