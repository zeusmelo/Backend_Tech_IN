# Backend_Tech_IN
#### Refs:
https://www.youtube.com/watch?v=-Pi5AmOfL2s&t=2s <br>
https://fastapidozero.dunossauro.com/
## Ferramentas utilizadas 🛠
### Pyenv:
Permite a utilização de diversas versões do python <br>
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
### Poetry:
para gerenciar os pacotes e ambiente virtual <br> 
poetry install | *na mesma pasta que* o pyproject.toml <br>
poetry shell | entrar no ambiente virtual
### FAST-API (FRAMEWORK)
poetry add **fastapi**
## Opcionais 🛠:
### PIPX:
instala aplicações python no ambiente geral do computador, cria ambiente virtual. <br>
pip install pipx <br>
### IGNR:
Apenas para criar gitgnore.
### GH:
Para criar e gerenciar repositorio no GITHUB.

## Para facilitar Desenvolvimento: 🖥 
poetry add --group dev pytest pytest-cov taskipy ruff
### Ruff:
Formatador (analise estática) https://docs.astral.sh/ruff/
### Pytest:
para testar a aplicação
### Taskipy:
gerencia tasks (Windows substituir ; por &&)
