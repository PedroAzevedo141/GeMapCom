# 🧬 GeMapCom — Ferramenta para Mapeamento Comparativo de Genomas

Ferramenta desktop para comparação, alinhamento e visualização de dados genômicos, desenvolvida em Python com PySide6.

## ✨ Funcionalidades

- **Alinhamento Global** — Algoritmo de Needleman-Wunsch via Biopython
- **Alinhamento Local** — Algoritmo de Smith-Waterman via Biopython  
- **BLAST+** — Interface completa para NCBI BLAST (blastn, blastp, blastx, tblastx, tblastn, psiblast)
- **Visualização Interativa** — Kablammo integrado para visualização dinâmica de resultados BLAST em XML
- **Filtros de Resultados** — Filtragem por identidade, E-value e RAG
- **Conversão de Formatos** — GenBank → FASTA e FASTQ → FASTA
- **Busca no NCBI** — Consulta de sequências por ID via Entrez (nucleotide, protein, PubMed, etc.)
- **Exportação** — Salvar resultados em TXT e imagens (PNG/JPG)

## 🔬 Ferramentas e Alternativas Pesquisadas

| Ferramenta | Uso no GeMapCom | Alternativas Modernas |
|:---|:---|:---|
| BLAST+ | Alinhamento de sequências | MMseqs2 (100-400x mais rápido), DIAMOND (proteínas) |
| Kablammo | Visualização BLAST XML | D-GENIES, SequenceServer |
| Needleman-Wunsch | Alinhamento global | Bio.Align.PairwiseAligner (Biopython) |
| Smith-Waterman | Alinhamento local | Bio.Align.PairwiseAligner (Biopython) |

> O BLAST+ foi mantido por ser o padrão-ouro para comparações individuais. Os algoritmos de alinhamento foram migrados para a API moderna do Biopython (`Bio.Align.PairwiseAligner`), que é otimizada em C.

## 📋 Pré-requisitos

- Python 3.9+
- NCBI BLAST+ instalado no sistema

## 🚀 Instalação

### Linux (Ubuntu/Debian/Mint)

```bash
# Instalar Python e BLAST+
sudo apt update
sudo apt install python3 python3-pip python3-venv ncbi-blast+

# Clonar o repositório
git clone https://github.com/PedroAzevedo141/GeMapCom.git
cd GeMapCom

# Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### Windows

```powershell
# Instalar Python 3.9+ de https://python.org
# Instalar BLAST+ de https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/

# Clonar o repositório
git clone https://github.com/PedroAzevedo141/GeMapCom.git
cd GeMapCom

# Criar e ativar ambiente virtual
python -m venv venv
.\venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt
```

## ▶️ Executando

```bash
python GeMapCom.py
```

## 📁 Estrutura do Projeto

```
GeMapCom/
├── GeMapCom.py              # Aplicação principal
├── Algoritmos/              # Algoritmos de alinhamento (Biopython)
│   ├── algorithm_needleman_wunsch.py
│   └── algorithm_smith_waterman.py
├── src/blast/               # Módulo BLAST+
│   ├── __init__.py          # Lógica principal do BLAST
│   ├── filtros.py           # Filtros de resultados
│   ├── result.py            # Exibição de resultados
│   ├── searchAlign.py       # Busca NCBI Entrez
│   └── graphKablammo.py     # Visualização Kablammo
├── Telas/                   # Interfaces gráficas (PySide6)
├── Plotar/                  # Geração de imagens de resultados
├── images/                  # Assets visuais
├── css/                     # Estilos Kablammo
├── js/                      # JavaScript Kablammo
└── requirements.txt         # Dependências Python
```

## 🛠️ Tecnologias

- **Python 3.9+** — Linguagem principal
- **PySide6** — Interface gráfica (Qt6)
- **Biopython** — Bioinformática (alinhamentos, parsing, Entrez)
- **NCBI BLAST+** — Comparação de sequências
- **Kablammo** — Visualização interativa de resultados BLAST
- **Matplotlib** — Geração de imagens de alinhamento
- **Pandas** — Manipulação de dados tabulares (filtros)

## 👨💻 Desenvolvedores

- Romuere Rodrigues Veloso e Silva
- Pedro Azevedo Abrantes de Oliveira
- Francisco das Chagas dos Anjos Carvalho Júnior

## 📄 Licença

Este projeto está licenciado sob a licença MIT — veja o arquivo [LICENSE](LICENSE) para detalhes.
