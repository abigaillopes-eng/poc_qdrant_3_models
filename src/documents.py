DOCUMENTS = [
    {
        "id": 1,
        "title": "Política de trabalho remoto",
        "department": "RH",
        "text": "A empresa permite trabalho remoto até três dias por semana. A solicitação deve ser aprovada pela liderança e registrada no portal de RH.",
    },
    {
        "id": 2,
        "title": "Prazo de implantação",
        "department": "Projetos",
        "text": "O prazo estimado para implantação e go-live da solução é de até 30 dias após a conclusão do levantamento inicial.",
    },
    {
        "id": 3,
        "title": "Entregáveis de analytics",
        "department": "Dados",
        "text": "A solução entrega dashboard executivo, dashboard operacional, histórico de eventos, indicadores de desempenho e relatórios gerenciais.",
    },
    {
        "id": 4,
        "title": "Gestão da base de conhecimento",
        "department": "Conhecimento",
        "text": "A gestão da base inclui indexação, estruturação, atualização, correção, curadoria contínua e monitoramento da qualidade dos documentos.",
    },
    {
        "id": 5,
        "title": "Integrações",
        "department": "Tecnologia",
        "text": "A plataforma pode ser integrada ao Microsoft Teams, portal corporativo, APIs internas e interfaces white-label.",
    },
    {
        "id": 6,
        "title": "Segurança e privacidade",
        "department": "Segurança",
        "text": "Dados pessoais devem seguir controles de acesso, rastreabilidade, minimização e requisitos da LGPD.",
    },
]

GOLDEN_QUERIES = [
    {"query": "Qual o prazo para o go-live?", "expected_id": 2},
    {"query": "Quais dashboards e relatórios são entregues?", "expected_id": 3},
    {"query": "Como é feita a manutenção da base de conhecimento?", "expected_id": 4},
    {"query": "A plataforma integra com Teams e APIs?", "expected_id": 5},
    {"query": "Quantos dias de trabalho remoto são permitidos?", "expected_id": 1},
]
