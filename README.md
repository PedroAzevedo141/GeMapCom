# GeMapCom: Uma Ferramenta para Mapeamento Comparativo e Visualização de Dados Genômicos

Uma ferramenta que auxilia e facilita pesquisadores da área a realizá comparações, de diversos modos, entre genomas e de ter os melhores tipos de visualização dos resultados obtidos pela ferramenta.

-----

### Instalação da ferramenta no Linux Mint

A ferramenta está desenvolvida na linguagem python, versão 3.0, e utiliza diversas bibliotecas externas. Para que a ferramenta rode em seu Linux é necessário ter instalado o python e suas respectivas bibliotecas, mostrado abaixo;

 - Primeiro passo, instale o Python 3.0:

       sudo apt-get install python3

 - Segundo passo, instalar o gerenciador de pacotes do python 3.0:

       sudo apt-get install python3-pip

 - Terceiro passo, instalar o PyQt5, biblioteca responsável pela personalização das interfaces:

       pip3 install pyqt5

 - Quarto passo, instalar o BioPython, biblioteca responsável pela manipulação dos arquivos que contém as sequencias:

       pip3 install biopython

 - Quinto passo, instalar o MatPlot, biblioteca responsável por métodos de visualização de certo tipos de dados:

       pip3 install matplot

 - Sexto passo, instalar o Pandas, biblioteca responsável pela manipulação de certos tipos de dados:

       pip3 install pandas

 - Sétimo passo, instalar o BLAST, software licenciada pela NCBi, para realização de comparações genomicas de alta capacidade:

       sudo apt install ncbi-blast+

-------

### Execução da ferramenta

Percorra pelo terminal até a pasta na qual está situado a ferramenta, então execute o seguinte comando:

    $ python3 GeMapCom.py

-------

### Desenvolvedores

 - Romuere Rodrigues Veloso e Silva
 - Pedro Azevedo Abrantes de Oliveira
 - Francisco das Chagas dos Anjos Carvalho Júnior

-------
