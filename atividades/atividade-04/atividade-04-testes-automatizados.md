# Atividade 4: Testes Automatizados do LocalEats

## 1. Identificação

- Unidade curricular: Qualidade de Software
- Projeto: LocalEats
- Turma: ADS MANHÃ
- Modalidade: Individual
- Integrante: Pedro Vital
- Sistema: [LocalEats](https://local-eats-unisenac.vercel.app/)
- Data da execução: 10/11/2026
- Repositório Git: [QA-TB4](https://github.com/pedrov1tal/QA-TB4).
- Diretório da atividade: [atividades/atividade-04](https://github.com/pedrov1tal/QA-TB4/tree/main/atividades/atividade-04).
- Diretório no workspace: `atividades/atividade-04/`.

## 2. Integrante e responsabilidades

| ID | Integrante responsável | Tipo | Comportamento verificado | Arquivo e função de teste |
|---|---|---|---|---|
| TU01 | Pedro Vital | Unitário | Pedido no mínimo de R$ 30,00 é aceito | `tests/test_regras_localeats.py::test_pedido_no_limite_minimo_e_aceito` |
| TU02 | Pedro Vital | Unitário | Pedido abaixo de R$ 30,00 não é aceito | `tests/test_regras_localeats.py::test_pedido_abaixo_do_minimo_nao_e_aceito` |
| TU03 | Pedro Vital | Unitário | Valor negativo gera `ValueError` | `tests/test_regras_localeats.py::test_pedido_negativo_gera_value_error` |
| TF01 | Pedro Vital | Funcional | Seleciona “Italiana” e confere os restaurantes filtrados | `tests/test_localeats.py::test_filtrar_restaurantes_da_categoria_italiana` |

## 3. Testes unitários

### Regra de Pedro Vital

- Regra escolhida: valor mínimo do pedido.
- Função implementada: `pedido_atingiu_valor_minimo(valor_pedido)`.
- Arquivo da implementação: `src/regras_localeats.py`.
- Regra: retorna `True` para valores de R$ 30,00 ou mais, `False` abaixo desse valor e lança `ValueError` para valores negativos.
- Testes: `test_pedido_no_limite_minimo_e_aceito`, `test_pedido_abaixo_do_minimo_nao_e_aceito` e `test_pedido_negativo_gera_value_error`.

## 4. Aplicação do TDD

### TDD de Pedro Vital

- Regra escolhida: valor mínimo do pedido.
- Primeiro teste escrito: `test_pedido_no_limite_minimo_e_aceito`.
- Por que o teste falhou inicialmente: na primeira execução, a coleta falhou com `ModuleNotFoundError`, pois o módulo e a função ainda não haviam sido implementados.
- Implementação mínima realizada: rejeitar valor negativo com `ValueError` e retornar se o valor é maior ou igual a 30.
- Segundo teste escrito: `test_pedido_abaixo_do_minimo_nao_e_aceito`.
- Melhoria/refatoração: o caso negativo foi coberto com `pytest.raises`; a função manteve uma condição direta para o limite.

## 5. Teste funcional com Playwright

- Sistema: [LocalEats](https://local-eats-unisenac.vercel.app/).
- ID: `TF01`.
- Fluxo: filtrar restaurantes pela categoria “Italiana”. O HTML público apresenta o botão `Italiana` (`.filter-btn`) e os cards usam `.rest-card` e `.card-meta`.
- Interação: clicar no botão “Italiana”.
- Assertions: título da página; botão selecionado com classe `active`; existência de cards; culinária de todos os cards exibidos contém “Italiana”.
- Não usa `time.sleep`; espera locators e condições do Playwright.
- Arquivo e função: `tests/test_localeats.py::test_filtrar_restaurantes_da_categoria_italiana`.
- Estado inicial: a aplicação redireciona visitantes sem sessão para o login. O teste prepara `userId` e `userName` no `localStorage` isolado do navegador; não cria uma conta nem grava dados de usuário.
- Evidência: [screenshot do filtro](evidencias/filtro-categoria-italiana.png).
- Resultado final: consultar o relatório de execução abaixo.

## 6. Resultado da execução

- Comando executado no PowerShell: `& 'C:\Users\Administrador\AppData\Local\Python\pythoncore-3.14-64\python.exe' -m pytest -v -p no:cacheprovider | Tee-Object -FilePath 'relatorio-pytest.txt'`. O Python instalado não está no PATH deste computador; `-p no:cacheprovider` evita o cache de pytest neste ambiente.
- Relatório: [relatorio-pytest.txt](relatorio-pytest.txt).
- Total: 4. Aprovados: 4. Reprovados: 0.

## 7. Explicação individual

### Explicação do teste de Pedro Vital

- Teste escolhido: `test_filtrar_restaurantes_da_categoria_italiana`.
- Comportamento verificado: ao selecionar a categoria “Italiana”, a interface marca o filtro como ativo e mostra apenas restaurantes italianos.
- Estado inicial: sessão local de demonstração no navegador isolado e página inicial do LocalEats carregada antes de escolher uma categoria.
- Resultado esperado: pelo menos um card visível e todos os cards resultantes indicam a culinária “Italiana”.
- O que faria o teste falhar: título incorreto, botão que não fica ativo, nenhum restaurante exibido ou card de culinária diferente.

## 8. Uso de inteligência artificial

- Ferramenta utilizada: ChatGPT, como apoio.
- Como foi utilizada: apoio na organização dos arquivos e na revisão de ideias para os testes e assertions.
- Sugestão alterada: ajustar seletores genéricos após conferir os identificadores, classes e textos existentes na interface pública do LocalEats.
- Motivo: os locators precisam corresponder à página real.
- Verificação: revisar os arquivos, executar os testes unitários e funcionais com pytest/Playwright e consultar o relatório gerado.

## 9. Diferenciais opcionais implementados

- Terceiro teste unitário: `test_pedido_negativo_gera_value_error`.
- `pytest.raises` para verificar `ValueError`: `test_pedido_negativo_gera_value_error`.
- Screenshot capturado pelo Playwright: [filtro-categoria-italiana.png](evidencias/filtro-categoria-italiana.png).
