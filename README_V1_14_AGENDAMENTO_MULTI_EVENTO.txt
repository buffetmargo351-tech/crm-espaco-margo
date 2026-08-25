CRM APP V1.14 — AGENDAMENTO MULTI-EVENTO

ESCOPO
- Adaptar consultoria.html para distinguir CASAMENTO x CORPORATIVO.
- Preservar integralmente as travas atuais de casamento.
- Permitir agendamento corporativo com regras próprias.

CORPORATIVO
Obrigatórios:
- data_evento
- quantidade_pessoas

Opcional:
- nome_empresa

Comportamento da tela:
- usa a mesma agenda de consultorias;
- exibe Data do evento, Quantidade de pessoas e Nome da empresa;
- oculta Nome do noivo, Email da noiva, Como conheceu o Margô e Encantamentos;
- mantém Observações;
- botão passa a ser Confirmar Visita;
- payload envia tipo_evento=CORPORATIVO, data_evento, quantidade_pessoas e nome_empresa.

CASAMENTO
- tela e validações existentes preservadas;
- nome do noivo continua obrigatório;
- origem continua obrigatória;
- encantamento continua obrigatório;
- nenhum novo bloqueio introduzido.

BACKEND
- compatível com v25.1_API_REGISTRAR_VISITA_MULTI_EVENTO.
- não publicar frontend antes da troca controlada v25 -> v25.1.

CACHE
- service-worker: crm-margo-pwa-v14-multi-evento-20260825.

STATUS
- branch isolada; produção/main ainda não alterados.
