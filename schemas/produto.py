from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto

from schemas import ComentarioSchema


class ProdutoSchema(BaseModel):
    """ Define como um novo aluno a ser inserido deve ser representado
    """
    nome: str = "fulano"
    matricula: Optional[int] = 0000
    mensalidade: float = 00.00



class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do aluno.
    """
    nome: str = "Teste"


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de alunos será retornada.
    """
    produtos:List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação do aluno seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for produto in produtos:
        result.append({
            "nome": produto.nome,
            "matricula": produto.matricula,
            "mensalidade": produto.mensalidade,
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    """ Define como um aluno será retornado: aluno + comentários.
    """
    id: int = 1
    nome: str = "fulano"
    matricula: Optional[int] = 0000
    mensalidade: float = 00.00
    total_cometarios: int = 1
    comentarios:List[ComentarioSchema]


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_produto(produto: Produto):
    """ Retorna uma representação do aluno seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "matricula": produto.matricula,
        "mensalidade": produto.valor,
        "total_cometarios": len(produto.comentarios),
        "comentarios": [{"texto": c.texto} for c in produto.comentarios]
    }
