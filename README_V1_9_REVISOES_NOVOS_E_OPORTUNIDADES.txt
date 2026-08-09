CRM MARGÔ APP V1.9

CORREÇÃO ÚNICA:
O filtro anti-fantasma da Home agora considera como casal válido:

- casal retornado por /crm/casais (NOVOS)
OU
- casal retornado por /crm/oportunidades (AGENDAR/RESGATAR)

Motivo:
o endpoint /crm/casais retorna apenas status NOVO.
Quando o casal virava EM_ATENDIMENTO, a versão anterior entendia
erroneamente que ele havia sido apagado e escondia sua revisão pendente.

NÃO ALTERADO:
- v17.7
- Cérebro V1.2.1
- v21.13
- v6.2
- lógica de envio
- lógica de três pontinhos
- polling
- alarmes

Não adiciona chamadas novas: reutiliza /crm/oportunidades, que a Home já consulta.
