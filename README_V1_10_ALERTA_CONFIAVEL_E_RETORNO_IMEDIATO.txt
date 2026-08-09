CRM MARGÔ APP V1.10

ALTERAÇÕES CONSOLIDADAS — SOMENTE HOME

1. RETORNO IMEDIATO
Ao voltar para a Home:
- recarrega NOVOS/OPORTUNIDADES;
- recarrega revisões imediatamente;
- não espera o próximo polling de 30 segundos.

2. ALARME SONORO CONFIÁVEL
Problema anterior:
- o primeiro toque apenas mudava uma variável booleana;
- o AudioContext era criado depois, fora do gesto do usuário;
- celulares/PWA podiam bloquear o som;
- a revisão era marcada como 'som tentado' mesmo sem áudio.

Nova lógica:
- primeiro toque cria/desbloqueia um AudioContext REAL;
- toca um bipe curto de confirmação;
- o mesmo AudioContext é reutilizado para alarmes;
- revisão só é marcada como avisada depois que o tom foi disparado;
- se o contexto for suspenso ao sair do App, novo toque pode reativá-lo;
- vibração é usada como apoio onde houver suporte.

3. ALARME
- nova revisão detectada: aviso imediato;
- pendência continua aberta: repete a cada 5 minutos;
- mantém throttle de 20 s contra duplicação.

NÃO ALTERADO:
- v17.7
- Cérebro V1.2.1
- v21.13
- v6.2
- envio WhatsApp
- três pontinhos
- regras comerciais
- polling de 30 segundos
