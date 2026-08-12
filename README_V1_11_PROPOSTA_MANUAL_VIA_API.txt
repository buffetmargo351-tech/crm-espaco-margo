CRM MARGÔ APP V1.11 — PROPOSTA MANUAL VIA API

BASE:
CRM_MARGO_APP_V1_10_ALERTA_CONFIAVEL_E_RETORNO_IMEDIATO

PROBLEMA CORRIGIDO:
Ao assumir atendimento manual e gerar/enviar Proposta Digital, o CRM usava
um link https://wa.me/... e abria o WhatsApp instalado no aparelho.
Isso fazia o envio sair do WhatsApp administrativo/pessoal, legado da operação antiga.

NOVA REGRA:
- geração da proposta continua em /crm/gerar-proposta;
- envio manual da proposta passa a usar /crm/enviar-whatsapp;
- portanto sai pelo número oficial da API Meta/WhatsApp;
- depois do envio confirmado, a mensagem aparece no chat do CRM;
- o histórico é registrado em /crm/conversas;
- falha no registro do histórico não repete um envio já confirmado;
- proposta ativa/reenvio manual também usa a API e não abre wa.me.

NÃO ALTERADO:
- v32.4 gerador/cálculo da proposta;
- Cérebro Milene;
- v21 executor de revisões;
- envio automático da Milene;
- lógica de cálculo;
- agenda;
- mídia;
- alertas da Home;
- typing.

TESTE RECOMENDADO:
1. assumir um atendimento;
2. abrir Gerar Proposta Digital;
3. gerar proposta;
4. confirmar que NÃO abre WhatsApp pessoal;
5. confirmar que mensagem aparece no WhatsApp do casal pelo número da API;
6. confirmar que a saída aparece no histórico do CRM.
