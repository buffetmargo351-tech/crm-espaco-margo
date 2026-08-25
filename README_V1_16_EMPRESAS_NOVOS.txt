V1.16 — EMPRESAS CAPTURA LEADS CORPORATIVOS AINDA EM NOVO

Correção técnica sobre V1.15:
- /crm/casais é a fonte dos registros NOVO ainda sem resposta;
- EMPRESAS agora combina corporativos vindos de /crm/casais com /crm/oportunidades;
- corporativos NOVO continuam excluídos de NOVOS CASAIS;
- somente registros corporativos do endpoint /crm/casais são adicionados à tela Oportunidades, evitando alterar filas de casamento;
- precedência permanece AGENDADOS > EMPRESAS > ATENÇÃO > OPORTUNIDADES;
- fila EMPRESAS continua compartilhada entre usuários autenticados;
- cache PWA atualizado para V1.16.

Motivo:
o fluxo corporativo correto nasce como status_casal=NOVO e modo_atendimento_ia=HUMANO. Como a V1.15 montava EMPRESAS apenas com /crm/oportunidades, um lead corporativo recém-chegado poderia ficar invisível até mudar de status.
