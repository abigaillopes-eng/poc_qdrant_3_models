# POC: três modelos de embeddings em uma única collection Qdrant

## Hipótese
Uma collection pode armazenar vetores densos de dimensões diferentes **desde que cada espaço vetorial tenha um nome próprio** (named vector) e uma configuração fixa. O retrieval consulta um named vector por vez, usando uma query produzida pelo mesmo modelo.

## Modelos reais
- `intfloat/multilingual-e5-small`: 384 dimensões
- `intfloat/multilingual-e5-base`: 768 dimensões
- `intfloat/multilingual-e5-large`: 1024 dimensões

> O modelo large pode exigir bastante memória. Para uma máquina pequena, execute primeiro apenas small/base ou altere a configuração.

## Execução
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
docker compose up -d
python -m src.run_poc
pytest -q
```

## Cenários demonstrados
1. Criação de uma collection com três named vectors de dimensões diferentes.
2. Ingestão única dos documentos/payloads, calculando três representações por chunk.
3. Retrieval independente por modelo.
4. Fusão de rankings com Reciprocal Rank Fusion, sem comparar scores brutos entre espaços incompatíveis.
5. Avaliação simples com perguntas e documentos esperados.

## Conclusão operacional
A solução evita refazer parsing e chunking. Contudo, ao introduzir um novo modelo depois, ainda é necessário gerar seus embeddings a partir do texto persistido. Além disso, o schema do named vector precisa existir na collection; se ele não existir, crie uma nova collection com o schema completo e migre/copie os pontos usando o payload existente.
