CRM MARGÔ APP V1.11.2 — HOTFIX HISTÓRICO / FORMATOS MISTOS

CAUSA COMPROVADA:
Versões antigas do registro de conversas gravavam data_hora com toLocaleString(pt-BR),
por exemplo:
13/08/2026, 09:08:00

A v6.2 atual grava:
13/08/2026 10:23

A V1.11.1 aceitava apenas o segundo padrão, por isso mensagens novas eram ordenadas
enquanto mensagens antigas ficavam fora da ordenação.

CORREÇÃO:
- aceita dd/mm/aaaa, HH:mm:ss
- aceita dd/mm/aaaa HH:mm:ss
- aceita dd/mm/aaaa HH:mm
- aceita yyyy-mm-dd HH:mm:ss
- aceita ISO
- remove NBSP/espaços anormais
- se a data ainda não puder ser interpretada, usa o timestamp do conversa_id CONV_<13 dígitos>
- preserva scroll para última mensagem

NÃO ALTERADO:
- card ATENÇÃO
- nome_contato
- áudio
- Cérebro
- n8n
- Motor de Continuidade
