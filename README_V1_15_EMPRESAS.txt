CRM APP V1.15 — EMPRESAS

OBJETIVO
Criar a fila visual EMPRESAS para leads corporativos, sem mistura com oportunidades de casamento.

IDENTIFICACAO
- tipo_evento = CORPORATIVO; ou
- origem = META_CORPORATIVO.

PRECEDENCIA
1. AGENDADOS: qualquer evento com visita agendada.
2. EMPRESAS: corporativo ativo sem visita agendada.
3. ATENCAO: humano nao corporativo sem visita.
4. OPORTUNIDADES/AGENDAR/RESGATAR: somente nao corporativos.
5. ENCERRADOS: arquivo de perdas.

VISIBILIDADE
EMPRESAS e fila compartilhada entre usuarios autenticados; consultora_responsavel continua sendo responsabilidade, nao filtro de visibilidade da fila.

ATENDIMENTO CORPORATIVO
- nome da empresa no cabecalho quando disponivel;
- data_evento e quantidade_pessoas no lugar dos campos de casamento;
- rota permanece HUMANO;
- controles de devolver para Milene e Atenção ficam indisponiveis;
- Consultar Data de casamento fica oculto;
- Agendar continua disponivel.

ARQUIVOS
- home.html
- oportunidades.html
- atendimento.html
- service-worker.js
