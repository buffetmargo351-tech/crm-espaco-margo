CHAT 2 — AGENDAMENTO MULTI-EVENTO V25.1

STATUS
- Bateria READ ONLY aprovada em 25/08/2026.
- Nenhuma escrita real foi feita no teste.
- Nenhuma vaga foi ocupada.
- Nenhum WhatsApp foi enviado.

REGRA UNIVERSAL
- data_evento: obrigatório para CORPORATIVO
- quantidade_pessoas: obrigatório para CORPORATIVO
- nome_empresa: opcional para CORPORATIVO
- mesma agenda_consultorias para todos os tipos de evento
- casal_id permanece como chave central

CORPORATIVO — TELA DE AGENDAMENTO
- detectar tipo_evento=CORPORATIVO
- mostrar data_evento e quantidade_pessoas
- permitir preencher/editar nome_empresa opcional
- esconder nome do noivo, email da noiva, origem e encantamentos
- manter observacoes_gerais
- exigir apenas data_evento + quantidade_pessoas + horario selecionado
- enviar payload para v25.1 com tipo_evento, data_evento, quantidade_pessoas e nome_empresa

CASAMENTO
- preservar fluxo atual sem nova trava
- manter campos/validações existentes enquanto a migração para campos universais é gradual

CONFIRMAÇÃO CORPORATIVA
- sem Milene
- sem referência a casamento
- registrar saída como CRM_AGENDAMENTO_CORPORATIVO

SEGURANÇA
- branch isolada: chat2/agendamento-multi-evento-v25-1
- não fazer merge/publicação antes de teste controlado do frontend + backend
