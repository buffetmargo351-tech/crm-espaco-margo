CRM MARGÔ APP V1.5 — PENDÊNCIA ÚNICA

Mudança principal:
- 1 casal = 1 pendência no app.
- Home mostra somente a revisão mais recente do casal.
- Atendimento abre sempre a revisão mais recente retornada pelo backend.
- Não obedece uma ultima_revisao_id antiga que possa prender a interface numa mensagem anterior.

Mantido da V1.4:
- polling 30s;
- alarme imediato + repetição a cada 5 minutos;
- botões simplificados;
- envio detecta edição do texto;
- demais telas/recursos preservados.

Backend recomendado em conjunto:
v21.8_API_REVISAO_PENDENCIA_UNICA_DIGITACAO_DINAMICA
