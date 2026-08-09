CRM MARGÔ APP V1.8 — ENVIO ROBUSTO + DIAGNÓSTICO

1. Mensagem manual é enviada ao WhatsApp ANTES de qualquer tentativa de descartar revisão antiga.
2. Falha ao limpar revisão nunca bloqueia envio manual.
3. Em erro, o App mostra:
   - REVISÃO HTTP <status>: <corpo>
   - WHATSAPP HTTP <status>: <corpo>
   Isso permite localizar exatamente a falha.
4. Legado visual:
   NOVO com ultimo_status_milene=RESPONDIDO ou data_ultima_resposta_ia preenchida
   deixa de aparecer como "Novo casal".
5. Mantém pendência única, polling 30s e alarme 5min.

Workflows recomendados:
- v21.11_API_REVISAO_ROBUSTA_SEM_TRAVA_ULTIMA_REVISAO_ID
- v6.2_API_REGISTRAR_CONVERSA_DIALOGO_E_STATUS_ATENDIMENTO
