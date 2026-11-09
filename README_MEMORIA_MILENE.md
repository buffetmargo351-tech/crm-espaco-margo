# Memória da Milene

Administradores do CRM acessam `memoria-milene.html` pelo menu. A tela usa a sessão já existente e valida usuário e permissão no servidor em cada operação.

Fluxo: editar orientação conversacional → ver prévia → salvar/publicar. Histórico permite restaurar uma versão como nova publicação. Preços/condições permanecem na planilha canônica; biblioteca factual e políticas sensíveis não são editáveis por esta tela.

API: `POST https://n8n.espacomargo.com.br/webhook/crm/milene-memoria`, operações `read`, `preview`, `publish`, `rollback`. A API exige autenticação e autorização administrativa; nenhuma credencial de infraestrutura é incluída na página. As execuções do endpoint e do validador de login não retêm payloads.

O backend usa versões imutáveis na aba `milene_memoria_versoes` do CRM e ponteiro publicado em `configuracoes`. Publicação usa comparação de versão e lote atômico. A biblioteca, a voz e a memória individual dos casais não são substituídas. Sessões de voz recebem a orientação em uma pausa segura, com versão e confirmação do provedor; teste humano durante a chamada continua necessário.

Validação da interface: Chrome headless, viewport 390×844, API e usuário sintéticos; leitura, prévia, publicação, restauração, categorias restritas e ausência de rolagem horizontal. Autenticação real sem credenciais retorna 403; CORS permite somente o CRM.

Rollback da interface: reverter o commit desta tela/menu/service worker. Não apagar as versões canônicas; elas preservam a auditoria. Rollback de conteúdo ocorre pelo histórico da própria tela.
