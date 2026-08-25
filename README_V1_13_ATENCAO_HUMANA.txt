CRM MARGÔ — V1.13 | FILA ATENÇÃO HUMANA

- ATENÇÃO = modo_atendimento_ia HUMANO.
- HUMANO sai das filas normais de OPORTUNIDADES.
- Botão ATENÇÃO no rodapé entre AGENDAR e HISTÓRICO.
- Não cria novo status_casal.
- Precedência visual: AGENDADOS > ATENÇÃO.
- Se houver agenda_id ou CONSULTORIA_AGENDADA, aparece somente em AGENDADOS.
- Revisões pendentes da Milene continuam em fila separada.

TESTES
1. Oportunidade autônoma sem visita > ATENÇÃO: passa a HUMANO.
2. Home: OPORTUNIDADES -1 e ATENÇÃO +1.
3. Card ATENÇÃO abre a fila humana.
4. Agendar visita para casal em ATENÇÃO: fica somente em AGENDADOS.
5. Casal já agendado não pode ser movido para ATENÇÃO pelo botão.
6. DEVOLVER PARA MILENE retira da fila ATENÇÃO se não estiver agendado.
