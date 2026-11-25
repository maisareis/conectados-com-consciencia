# Conectados com Consciência

Campanha de conscientização em segurança digital, com edições mensais pensadas para o ambiente corporativo e para o dia a dia pessoal. Aqui está todo o material que produzi: boletins, infográficos, quadrinho, roteiro de apresentação, plano de lançamento e um estudo de caso real.

> **Sobre este repositório:** a campanha foi planejada para uma empresa, mas não chegou a ser lançada. Em vez de deixar o material parado, organizei tudo aqui como portfólio e como arquivo, para que qualquer pessoa possa reaproveitar.

## Objetivo

Mostrar segurança digital sem jargão, para quem não é da área. A ideia é que cada pessoa leia em poucos minutos, entenda o risco e saia com uma ação prática. Quem protege a própria conta em casa também protege a empresa.

## Como cada edição é montada

Todas as edições seguem o mesmo formato, o que facilita produzir e manter a campanha:

1. **Tema do mês**, com o contexto do risco
2. **Dica rápida**, com ações práticas
3. **Você sabia?**, com um fato que gera curiosidade
4. **Desafio rápido**, com uma pergunta de múltipla escolha e a resposta explicada
5. **Link útil**, com uma fonte confiável (em geral, as cartilhas do CERT.br)
6. **Frase do mês**, para fixar a ideia

## Edições

| # | Tema | Arquivos |
|---|------|----------|
| 1 | Senhas seguras | [PDF](edicoes/pdf/edicao-01-agosto-senhas.pdf) · [PDF colorido](edicoes/pdf-colorido/edicao-01-agosto-senhas.pdf) · [Word](edicoes/word/edicao-01-agosto-senhas.docx) |
| 2 | Phishing | [PDF](edicoes/pdf/edicao-02-setembro-phishing.pdf) · [PDF colorido](edicoes/pdf-colorido/edicao-02-setembro-phishing.pdf) · [Word](edicoes/word/edicao-02-setembro-phishing.docx) |
| 3 | Privacidade digital | [PDF](edicoes/pdf/edicao-03-outubro-privacidade.pdf) · [PDF colorido](edicoes/pdf-colorido/edicao-03-outubro-privacidade.pdf) · [Word](edicoes/word/edicao-03-outubro-privacidade.docx) |
| 4 | Golpes em mensagens (WhatsApp e SMS) | [PDF](edicoes/pdf/edicao-04-novembro-golpes-mensagens.pdf) · [PDF colorido](edicoes/pdf-colorido/edicao-04-novembro-golpes-mensagens.pdf) · [Word](edicoes/word/edicao-04-novembro-golpes-mensagens.docx) |
| 5 | Riscos do Wi-Fi aberto | [PDF](edicoes/pdf/edicao-05-dezembro-wifi-aberto.pdf) · [PDF colorido](edicoes/pdf-colorido/edicao-05-dezembro-wifi-aberto.pdf) · [Word](edicoes/word/edicao-05-dezembro-wifi-aberto.docx) |
| 6 | Segurança no celular | [Word](edicoes/word/edicao-06-janeiro-celular.docx) |
| 7 | Deepfakes e desinformação | [Word](edicoes/word/edicao-07-fevereiro-deepfakes-desinformacao.docx) |
| 8 | Golpes financeiros online | [Word](edicoes/word/edicao-08-marco-golpes-financeiros.docx) |
| 9 | Redes sociais: pessoal e profissional | [Word](edicoes/word/edicao-09-abril-redes-sociais.docx) |
| 10 | Engenharia social | [Word](edicoes/word/edicao-10-maio-engenharia-social.docx) |
| 11 | Atualizações de sistema | [Word](edicoes/word/edicao-11-junho-atualizacoes.docx) |
| 12 | Vazamento de dados | [Word](edicoes/word/edicao-12-julho-vazamento-de-dados.docx) |
| 13 | Backups | [Word](edicoes/word/edicao-13-agosto-backups.docx) |

**Edições especiais** ([`edicoes/especiais/`](edicoes/especiais/)): PDF perigoso, como funciona um ataque com PDF malicioso (visão geral, sem instruções operacionais) e credenciais salvas no navegador.

## O que tem em cada pasta

| Pasta | Conteúdo |
|-------|----------|
| [`edicoes/`](edicoes/) | Boletins em Word (1 a 13) e em PDF simples e colorido (1 a 5), mais as edições especiais |
| [`infograficos/`](infograficos/) | Infográficos e checklist em HTML, informativos de senhas (versão geral e técnica) e quadrinho |
| [`apresentacao/`](apresentacao/) | Roteiro de apresentação da campanha (com tempo por slide), slides em PPTX e PDF |
| [`plano-agosto-senhas/`](plano-agosto-senhas/) | Plano semanal de um mês de campanha, com informativos geral e técnico sobre senhas |
| [`casos/cisco-2022/`](casos/cisco-2022/) | Estudo de caso do incidente da Cisco em 2022: senha vazada e MFA burlado |
| [`ameacas/`](ameacas/) | Mapa dos tipos de ameaças cibernéticas |
| [`referencias/`](referencias/) | Fontes externas usadas (os links, não os arquivos) |

## Como rodar um mês de campanha

O [plano semanal](plano-agosto-senhas/plano-semanal-agosto.pdf) mostra um mês completo sobre senhas:

- **Semana 1:** boletim do mês e um quadrinho leve, para quem não vai ler o texto inteiro
- **Semana 2:** informativo geral explicando como senhas são quebradas
- **Semana 3:** versão técnica para quem é de TI (funções de hash, tipos de ataque)
- **Semana 4:** caso real para fixar o aprendizado (Cisco 2022)

Dá para repetir a mesma estrutura em qualquer um dos outros temas.

## Estudo de caso: Cisco 2022

Uma conta pessoal comprometida, uma senha reaproveitada e um MFA contornado foram o ponto de partida do incidente. A pasta [`casos/cisco-2022/`](casos/cisco-2022/) resume o caso em linguagem acessível. Para o relato técnico completo, use a fonte original da Cisco Talos: <https://blog.talosintelligence.com/recent-cyber-attack/>.

## Avisos

- Este material é educativo e foi escrito em linguagem acessível. Ele simplifica propositalmente alguns conceitos técnicos.
- As estatísticas citadas vêm das fontes indicadas em cada material. Confira a fonte original antes de reutilizar um número.
- As metas do roteiro de apresentação (conscientização, redução de incidentes) são **propostas**. A campanha não foi lançada, então nada disso foi medido.
- Os e-mails de exemplo nos infográficos são fictícios.

## O que eu aprendi

- Um formato fixo por edição reduz muito o esforço de produzir todo mês.
- Duas versões do mesmo tema (geral e técnica) atendem públicos diferentes sem precisar de duas campanhas.
- Um caso real dá peso ao risco: as pessoas lembram da história, não da lista de dicas.
- Se fosse lançar, eu definiria as métricas antes (taxa de abertura, resultado dos desafios, simulação de phishing) para poder medir de verdade.

## Autoria e licença

Criado por **Maisa Reis Araujo** ([@maisareis](https://github.com/maisareis)).

Licença [CC BY-NC-SA 4.0](LICENSE.md): você pode usar, adaptar e compartilhar, desde que dê o crédito, não use para fins comerciais e mantenha a mesma licença.
