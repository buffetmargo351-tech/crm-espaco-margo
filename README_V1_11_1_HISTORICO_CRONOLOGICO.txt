CRM MARGÔ APP V1.11.1 — HOTFIX HISTÓRICO CRONOLÓGICO

BASE:
CRM_MARGO_APP_V1_11_PROPOSTA_MANUAL_VIA_API

PROBLEMA:
O atendimento.html renderizava as conversas exatamente na ordem devolvida
pela API /crm/conversas. Como a aba/endpoint pode devolver registros fora
da ordem temporal, mensagens recentes podiam aparecer acima de mensagens
antigas. O scroll no final então dava a impressão de que a conversa estava
cortada/truncada.

CORREÇÃO:
1. Ordena todas as conversas por data_hora antes de renderizar.
2. Suporta dd/mm/aaaa HH:mm, dd/mm/aaaa HH:mm:ss e ISO.
3. Em empate, preserva a ordem original da API.
4. No carregamento inicial/forçado, posiciona corretamente na última mensagem.
5. Ao abrir o painel de revisão, se o usuário já estava no final do chat,
   preserva o final após o redimensionamento.

NÃO ALTERADO:
- Card ATENÇÃO (continua pendente para versão consolidada)
- nome_contato nos cards (continua pendente)
- transcrição automática de áudio (continua pendente)
- proposta manual via API (preservada da V1.11)
- Cérebro Milene
- workflows n8n
- Motor de Continuidade
