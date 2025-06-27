from dataclasses import dataclass
from models.profissao import Profissao

@dataclass
class Usuario:
    id: int
    nome : str
    foto : str
    data_nascimento : str
    link_profissional : str
    email : str
    senha : str
    cpf : str
    telefone : str
    profissao : Profissao
    status : str
    avaliacao : float